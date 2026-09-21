import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from lib.report_knowledge import load_dossiers, merge_dossiers, dossier_text, validate_dossiers, relocate_links, collection_index
from lib.legacy_information import search_information
from lib.forecast_learning import empty_state, append_records, validate_plan
from lib.forecast_contract import instant
from lib.learning_cycle import run_cycle
from test_learning_cycle import successful_stage

ROOT = Path(__file__).resolve().parents[1]
NOW = '2026-09-23T09:00:00+09:00'
URL = 'https://openai.com/index/test-announcement/'


def update_records(root):
    base = load_dossiers(root, NOW)['openai']['sections'][0]
    evidence = dict(type='evidence', id='E-new', visibility='public', url=URL,
                    published_at=NOW, retrieved_at=NOW, source_group='openai',
                    claim_type='observed_fact', summary='New enterprise product.', content_hash='sha256:' + 'a' * 64)
    update = dict(type='dossier_section', id='D-new', visibility='public', subject='openai',
                  section=base['id'], reviewed_at=NOW, body=base['body'] + f'\n\n確認した新しい企業向け製品。[発表]({URL})',
                  analysis='企業向け販売経路が増える。採用実績とは区別する。',
                  uncertainty='契約社数・利益は未開示。', evidence_ids=['E-new'], supersedes=None)
    return [evidence, update]


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for directory in ['config', 'prompts', 'schemas']:
            shutil.copytree(ROOT / directory, self.root / directory)

    def tearDown(self):
        self.temporary.cleanup()

    def test_empty_and_partial_days_keep_all_company_state(self):
        for name, quality in [('empty', 'complete'), ('partial', 'partial')]:
            def runner(stage, *args):
                if stage == 'collect':
                    return dict(quality=quality, records=[], gaps=['Coverage limited']), {}
                return successful_stage(stage, *args)
            manifest = run_cycle(self.root, NOW, name, runner)
            self.assertEqual(manifest['outcome'], quality)
            daily = (self.root / 'state/shadow/Intelligence/2026-09-23.md').read_text()
            for subject, dossier in load_dossiers(self.root, NOW).items():
                self.assertIn(dossier['title'], daily)
                static = (self.root / 'state/shadow/static_intelligence' / (subject + '.md')).read_text()
                for section in dossier['sections']:
                    self.assertTrue(relocate_links(section['body'], 'state/shadow/Intelligence') in daily, section['title'])
                    self.assertTrue(relocate_links(section['body'], 'state/shadow/static_intelligence') in static, section['title'])
            self.assertFalse((self.root / 'static_intelligence').exists())

    def test_update_replaces_only_reviewed_section_and_keeps_history(self):
        prior = empty_state()
        plan = dict(run_id='new', expected_revision='0', quality='complete', review_complete=True,
                    records=update_records(self.root))
        candidate = validate_plan(prior, plan, instant(NOW))
        dossiers = merge_dossiers(load_dossiers(self.root, NOW), candidate, NOW)
        validate_dossiers(dossiers)
        self.assertEqual(dossiers['openai']['sections'][0]['body'], plan['records'][1]['body'])
        self.assertEqual(dossiers['anthropic'], load_dossiers(self.root, NOW)['anthropic'])
        self.assertEqual(prior['records']['dossier_section'], {})
        self.assertEqual(candidate['records']['dossier_section']['D-new'], plan['records'][1])

    def test_accepted_section_is_rendered_and_survives_next_day(self):
        records = update_records(self.root)
        def runner(stage, *args):
            if stage == 'collect':
                return dict(quality='complete', records=[records[0]], gaps=[]), {}
            if stage in {'blue', 'arbiter'}:
                return dict(records=[records[1]], reason='Preserve company facts and add verified product'), {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, 'update', runner)
        self.assertEqual(manifest['outcome'], 'complete')
        self.assertTrue(manifest['dossier_hash'])
        later = '2026-09-24T09:00:00+09:00'
        manifest = run_cycle(self.root, later, 'carry', successful_stage)
        self.assertEqual(manifest['outcome'], 'complete')
        for target in ['Intelligence/2026-09-24.md', 'static_intelligence/openai.md']:
            body = (self.root / 'state/shadow' / target).read_text()
            self.assertIn('確認した新しい企業向け製品', body)
            self.assertIn('2026-09-23T09:00:00+09:00', body)

    def test_unknown_section_fails_before_committing_any_records(self):
        records = update_records(self.root)
        bad = {**records[1], 'section': 'section-99'}
        def runner(stage, *args):
            if stage == 'collect':
                return dict(quality='complete', records=[records[0]], gaps=[]), {}
            if stage in {'blue', 'arbiter'}:
                return dict(records=[bad], reason='Wrong target'), {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, 'bad-section', runner)
        self.assertEqual(manifest['outcome'], 'failed')
        self.assertEqual(list((self.root / 'state/shadow/data/forecast_ledger/transactions').glob('*.json')), [])

    def test_unreviewed_new_url_cannot_be_smuggled_into_section(self):
        records = update_records(self.root)
        bad = {**records[1], 'body': records[1]['body'] + ' [unsupported](https://evil.test/claim)'}
        state = append_records(empty_state(), [records[0], bad])
        with self.assertRaises(ValueError):
            merge_dossiers(load_dossiers(self.root, NOW), state, NOW)

    def test_future_and_unlinked_or_cross_subject_updates_are_rejected(self):
        records = update_records(self.root)
        for change in [dict(reviewed_at='2027-01-01T00:00:00Z'), dict(evidence_ids=[]),
                       dict(body='Unattributed information'), dict(subject='../private')]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_plan(empty_state(), dict(run_id='bad', expected_revision='0', quality='complete',
                              review_complete=True, records=[records[0], {**records[1], **change}]), instant(NOW))
        state = append_records(empty_state(), records)
        with self.assertRaises(ValueError):
            validate_plan(state, dict(run_id='cross', expected_revision='0', quality='complete', review_complete=True,
                          records=[{**records[1], 'id': 'D-cross', 'subject': 'anthropic', 'supersedes': 'D-new'}]), instant(NOW))

    def test_cannot_fork_section_history_or_update_unknown_section(self):
        records = update_records(self.root)
        state = append_records(empty_state(), records)
        with self.assertRaises(ValueError):
            validate_plan(state, dict(run_id='fork', expected_revision='0', quality='complete', review_complete=True,
                          records=[{**records[1], 'id': 'D-fork'}]), instant(NOW))
        bad = append_records(empty_state(), [records[0], {**records[1], 'section': 'missing'}])
        with self.assertRaises(ValueError):
            merge_dossiers(load_dossiers(self.root, NOW), bad, NOW)

    def test_future_baseline_is_not_retroactively_available(self):
        with self.assertRaises(ValueError):
            load_dossiers(self.root, '2026-09-21T00:00:00Z')

    def test_collection_index_preserves_sources_without_replacing_full_dossiers(self):
        dossiers = load_dossiers(self.root, NOW)
        original = json.dumps(dossiers, ensure_ascii=False)
        index = collection_index(dossiers)
        self.assertEqual(set(index), set(dossiers))
        self.assertIn('https://openai.com/index/accelerating-the-next-phase-ai/',
                      index['openai']['sections'][0]['source_urls'])
        self.assertLess(len(json.dumps(index, ensure_ascii=False)), len(original) / 2)
        self.assertEqual(json.dumps(dossiers, ensure_ascii=False), original)

    def test_shadow_links_use_the_same_snapshot_and_root_archives(self):
        text = '[company](openai.md) [archive](../archive/original.md)'
        self.assertEqual(relocate_links(text, 'state/shadow/Intelligence'),
                         '[company](../static_intelligence/openai.md) [archive](../../../archive/original.md)')

    def test_render_retry_uses_saved_baseline_even_if_config_changes(self):
        with patch('lib.learning_cycle.write_outputs', side_effect=OSError('disk unavailable')):
            failed = run_cycle(self.root, NOW, 'resume', successful_stage)
        self.assertEqual(failed['outcome'], 'failed')
        base_path = self.root / 'config/dossiers/openai.json'
        base_path.write_text('broken JSON')
        recovered = run_cycle(self.root, NOW, 'resume', lambda *args: self.fail('Model repeated'))
        self.assertEqual(recovered['outcome'], 'complete')

    def test_failed_collection_leaves_full_prior_state_as_marked_reference(self):
        def fail(*args):
            raise RuntimeError('provider unavailable')
        manifest = run_cycle(self.root, NOW, 'failure-reference', fail)
        self.assertEqual(manifest['outcome'], 'failed')
        text = (self.root / 'state/shadow/Intelligence/2026-09-23.md').read_text()
        self.assertIn('以前の確認済み情報を持ち越した参考資料', text)
        for dossier in load_dossiers(self.root, NOW).values():
            self.assertIn(dossier['title'], text)
        self.assertFalse((self.root / 'state/shadow/static_intelligence').exists())

    def test_legacy_search_preserves_bytes_ids_provenance_and_unknown_dates(self):
        path = self.root / 'Information/processed/2026-09-20.jsonl'
        path.parent.mkdir(parents=True)
        row = dict(evidence_id='EVD-20260920-0001', legacy_info_id='INFO-001',
                   source_url=URL, source_type='official', retrieved_at='2026-09-20T09:00:00+09:00',
                   source_title='OpenAI Agents', run_date='2026-09-20', content_hash='sha256:' + 'b'*64,
                   raw_path='Information/raw/2026-09-20/firecrawl.jsonl', summary_for_indexing='agents')
        path.write_text(json.dumps(row)+'\n')
        before = path.read_bytes()
        result = search_information(self.root, query='INFO-001', subject='openai', before='2026-09-21', limit=5)
        self.assertEqual(len(result['items']), 1)
        item = result['items'][0]
        self.assertEqual(item['legacy_info_id'], 'INFO-001')
        self.assertIsNone(item['published_at'])
        self.assertEqual(item['trust'], 'legacy_unverified')
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(search_information(self.root, before='2026-09-19')['items'], [])
        path.write_text(path.read_text()+'broken\n')
        self.assertEqual(len(search_information(self.root)['errors']), 1)


if __name__ == '__main__':
    unittest.main()
