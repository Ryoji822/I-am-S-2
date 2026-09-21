import json
import shutil
import sys
import tempfile
import unittest
import subprocess
import importlib.util
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lib.learning_cycle import run_cycle, model_config, current_context
from lib.forecast_learning import load_state, scorecard
from test_forecast_learning import initial_records, actual_records, LATER


ROOT = Path(__file__).resolve().parents[1]
NOW = "2026-09-22T09:00:00+09:00"


def successful_stage(stage, context, directory, policy):
    if stage == "collect":
        return {"quality": "complete", "records": [], "gaps": ["No new verified evidence"]}, {}
    if stage == "blue":
        return {"records": [], "reason": "No new evidence"}, {}
    if stage == "red":
        return {"accepted": True, "issues": [], "reason": "No unsupported update"}, {}
    return {"records": [], "reason": "Keep prior judgment"}, {}


class CycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "config", self.root / "config")
        shutil.copytree(ROOT / "prompts", self.root / "prompts")
        shutil.copytree(ROOT / "schemas", self.root / "schemas")

    def tearDown(self):
        self.temp.cleanup()

    def run_cycle(self, **kwargs):
        return run_cycle(self.root, NOW, stage_runner=successful_stage, **kwargs)

    def test_shadow_run_is_replayable_and_does_not_change_official_ledger(self):
        manifest = self.run_cycle(run_id="test-success")
        self.assertEqual(manifest["outcome"], "complete")
        self.assertEqual(load_state(self.root)["sequence"], 0)
        count = load_state(self.root / "state/shadow")["sequence"]
        again = self.run_cycle(run_id="test-success")
        self.assertEqual(manifest, again)
        self.assertEqual(count, load_state(self.root / "state/shadow")["sequence"])

    def test_failure_does_not_overwrite_an_existing_report(self):
        path = self.root / "Intelligence/2026-09-22.md"
        path.parent.mkdir()
        path.write_text("Existing official report")
        def fail(*args):
            raise RuntimeError("Secret provider response must not be logged")
        manifest = run_cycle(self.root, NOW, "test-failure", fail)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(path.read_text(), "Existing official report")
        self.assertNotIn("Secret provider", json.dumps(manifest))

    def test_red_rejection_keeps_ledger_unchanged(self):
        def reject(stage, *args):
            return ({"accepted": False, "issues": ["unverified"], "reason": "Missing source"}, {}) if stage == "red" else successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-reject", reject)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(manifest['validation_failure'], 'red review rejected proposal')
        self.assertEqual(load_state(self.root / "state/shadow")["sequence"], 0)

    def test_arbiter_cannot_add_a_new_unreviewed_judgment(self):
        def invented(stage, *args):
            if stage == "arbiter":
                return {"records": [{"type": "warning", "id": "invented"}], "reason": "New idea"}, {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-invented", invented)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(load_state(self.root / "state/shadow")["sequence"], 0)

    def test_model_has_no_write_shell_or_delegation_permission(self):
        config = model_config(self.root)
        permission = config["agent"]["learning"]["permission"]
        for action in ["bash", "edit", "task", "external_directory"]:
            self.assertEqual(permission[action], "deny")
        self.assertEqual(config["share"], "disabled")
        self.assertFalse(config['compaction']['auto'])

    def test_model_receives_valid_record_values_not_only_field_names(self):
        context = current_context(self.root, load_state(self.root), NOW)
        variants = context['record_schema']['items']['oneOf']
        evidence = next(row for row in variants if row['properties']['type']['const'] == 'evidence')
        self.assertEqual(set(evidence['properties']['claim_type']['enum']),
                         {'observed_fact', 'announced_plan', 'reported_claim', 'expert_opinion', 'analysis'})

    def test_historical_live_run_is_rejected(self):
        with self.assertRaises(ValueError):
            run_cycle(self.root, NOW, "../bad", successful_stage)

    def test_end_to_end_issuance_observation_resolution_and_review_queue(self):
        initial = initial_records()
        initial[-1] = {**initial[-1], "issued_at": NOW, "knowledge_cutoff": NOW}
        def issue(stage, *args):
            if stage == "collect":
                return {"quality": "complete", "records": [initial[1]], "gaps": []}, {}
            if stage in {"blue", "arbiter"}:
                return {"records": [initial[0], *initial[2:]], "reason": "Test issuance"}, {}
            return successful_stage(stage, *args)
        first = run_cycle(self.root, NOW, "issue", issue)
        self.assertEqual(first["outcome"], "complete")
        def observe(stage, *args):
            if stage == "collect":
                return {"quality": "complete", "records": actual_records(), "gaps": []}, {}
            return successful_stage(stage, *args)
        second = run_cycle(self.root, LATER, "observe", observe)
        self.assertEqual(second["outcome"], "complete")
        state = load_state(self.root / "state/shadow")
        self.assertAlmostEqual(scorecard(state, LATER)["short"]["initial_brier"], 0.49)
        context = current_context(self.root, state, LATER)
        self.assertIn("F-1", [q["id"] for q in context["records"]["question"]])
        report = self.root / "state/shadow/Intelligence/2026-12-24.md"
        self.assertIn("0.490", report.read_text())

    def test_model_timeout_is_a_failed_manifest(self):
        def timeout(*args):
            raise subprocess.TimeoutExpired("opencode", 600)
        manifest = run_cycle(self.root, NOW, "timeout", timeout)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(load_state(self.root / "state/shadow")["sequence"], 0)

    def test_partial_collection_saves_facts_without_calling_judgment_models(self):
        def collect_only(stage, *args):
            self.assertEqual(stage, 'collect')
            return {'quality': 'partial', 'records': [initial_records()[1]], 'gaps': ['One source unavailable']}, {}
        manifest = run_cycle(self.root, NOW, 'partial-source', collect_only)
        self.assertEqual(manifest['outcome'], 'partial')
        self.assertEqual(manifest['gaps'], ['One source unavailable'])
        self.assertEqual(manifest['usage']['blue']['status'], 'skipped_partial_collection')
        records = load_state(self.root / 'state/shadow')['records']
        self.assertEqual(len(records['evidence']), 1)
        self.assertEqual(len(records['vintage']), 0)
        self.assertEqual(len(records['dossier_section']), 0)

    def test_render_failure_can_resume_saved_plan_without_model_calls(self):
        with patch("lib.learning_cycle.write_outputs", side_effect=OSError("render unavailable")):
            failed = self.run_cycle(run_id="render-recovery")
        self.assertEqual(failed["outcome"], "failed")
        before = load_state(self.root / "state/shadow")["sequence"]
        def should_not_call(*args):
            raise AssertionError("model must not repeat")
        recovered = run_cycle(self.root, NOW, "render-recovery", should_not_call)
        self.assertEqual(recovered["outcome"], "complete")
        self.assertEqual(before, load_state(self.root / "state/shadow")["sequence"])

    def test_live_mode_requires_successful_shadow_days(self):
        path = self.root / "config/learning_policy.json"
        policy = {**json.loads(path.read_text()), "mode": "live"}
        path.write_text(json.dumps(policy))
        with self.assertRaises(ValueError):
            self.run_cycle(run_id="too-early")

    def test_publication_path_allowlist_excludes_source_and_secrets(self):
        specification = importlib.util.spec_from_file_location("publisher", ROOT / "scripts/publish-generated.py")
        module = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(module)
        self.assertTrue(module.allowed("state/shadow/data/forecast_ledger/transactions/00000001-cycle.json"))
        self.assertTrue(module.allowed("state/runs/test/manifest.json"))
        self.assertTrue(module.allowed("state/shadow/static_intelligence/openai.md"))
        self.assertFalse(module.allowed("static_intelligence/private.md"))
        for path in [".env", "private/income.json", "config/hypotheses.json", "state/.learning-cycle.lock", "state/runs/a/../../private.json"]:
            self.assertFalse(module.allowed(path))


if __name__ == "__main__":
    unittest.main()
