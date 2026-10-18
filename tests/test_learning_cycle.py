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


def issued_records():
    initial = initial_records()
    initial[-1] = {**initial[-1], "issued_at": NOW, "knowledge_cutoff": NOW}
    return initial


EXCLUDED = "正式判断として公表せず除外しました"


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
        self.assertEqual(manifest['error_location'][-1]['function'], 'fail')

    def test_red_rejection_keeps_ledger_unchanged(self):
        def reject(stage, *args):
            return ({"accepted": False, "issues": ["unverified"], "reason": "Missing source"}, {}) if stage == "red" else successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-reject", reject)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(manifest['validation_failure'], 'red review rejected proposal')
        self.assertEqual(load_state(self.root / "state/shadow")["sequence"], 0)

    def test_arbiter_cannot_add_a_new_unreviewed_judgment(self):
        evidence = initial_records()[1]
        stray = {"type": "warning", "id": "SECRET PROVIDER TEXT", "reason": "SECRET_PROVIDER_TEXT"}
        def invented(stage, *args):
            if stage == "collect":
                return {"quality": "complete", "records": [evidence], "gaps": []}, {}
            if stage == "arbiter":
                return {"records": [stray], "reason": "New idea"}, {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-invented", invented)
        state = load_state(self.root / "state/shadow")
        self.assertEqual(manifest["outcome"], "complete")
        self.assertNotEqual(manifest["revision_after"], manifest["revision_before"])
        self.assertIn("EVD-1", state["records"]["evidence"])
        self.assertEqual(state["records"]["warning"], {})
        self.assertEqual(manifest["gaps"], [f"裁定が主分析にない記録を含めていたため、その記録は{EXCLUDED}（1件）。"])
        published = json.dumps(manifest, ensure_ascii=False) + (self.root / "state/shadow/Intelligence/2026-09-22.md").read_text()
        self.assertNotIn("SECRET_PROVIDER_TEXT", published)
        self.assertNotIn("SECRET PROVIDER TEXT", published)
        self.assertEqual(load_state(self.root)["sequence"], 0)

    def test_stray_arbiter_record_keeps_verbatim_reviewed_judgments(self):
        initial = issued_records()
        reviewed = [initial[0], *initial[2:]]
        stray = {"type": "warning", "id": "invented", "reason": "SECRET_PROVIDER_TEXT"}
        unsafe = {"type": "warning", "id": "SECRET PROVIDER TEXT", "reason": "SECRET_PROVIDER_TEXT"}
        def stages(stage, *args):
            if stage == "collect":
                return {"quality": "complete", "records": [initial[1]], "gaps": ["One source thin"]}, {}
            if stage == "blue":
                return {"records": reviewed, "reason": "Reviewed proposal"}, {}
            if stage == "arbiter":
                return {"records": [*reviewed, stray, unsafe], "reason": "Added an extra record"}, {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-stray", stages)
        state = load_state(self.root / "state/shadow")
        saved = json.loads((self.root / "state/runs/test-stray/accepted-plan.json").read_text())
        saved_ids = [record["id"] for record in saved["plan"]["records"]]
        self.assertEqual(manifest["outcome"], "complete")
        self.assertNotEqual(manifest["revision_after"], manifest["revision_before"])
        self.assertEqual(manifest["gaps"], [
            "One source thin",
            f"裁定が主分析にない記録を含めていたため、その記録は{EXCLUDED}（2件。表示できる識別子：warning:invented）。"])
        for identifier in ["MET-1@1", "EVD-1", "F-1", "F-1-v1"]:
            self.assertIn(identifier, saved_ids)
            self.assertIn(identifier, {row["id"] for rows in state["records"].values() for row in rows.values()})
        self.assertNotIn("invented", saved_ids)
        self.assertEqual(state["records"]["warning"], {})
        published = json.dumps({"manifest": manifest, "plan": saved["plan"]}, ensure_ascii=False)
        published += (self.root / "state/shadow/Intelligence/2026-09-22.md").read_text()
        self.assertNotIn("SECRET_PROVIDER_TEXT", published)
        self.assertNotIn("SECRET PROVIDER TEXT", published)
        self.assertIn("warning:invented", published)
        self.assertEqual(load_state(self.root)["sequence"], 0)
        def should_not_call(*args):
            raise AssertionError("model must not repeat")
        self.assertEqual(manifest, run_cycle(self.root, NOW, "test-stray", should_not_call))

    def test_edited_arbiter_copy_is_not_published(self):
        initial = issued_records()
        reviewed = [initial[0], *initial[2:]]
        mutated = {**initial[-1], "probability": 0.99, "confidence_reason": "SECRET_PROVIDER_TEXT"}
        def stages(stage, *args):
            if stage == "collect":
                return {"quality": "complete", "records": [initial[1]], "gaps": []}, {}
            if stage == "blue":
                return {"records": reviewed, "reason": "Reviewed proposal"}, {}
            if stage == "arbiter":
                return {"records": [initial[0], initial[2], mutated], "reason": "Changed the probability"}, {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-mutated", stages)
        state = load_state(self.root / "state/shadow")
        saved_ids = [record["id"] for record in json.loads(
            (self.root / "state/runs/test-mutated/accepted-plan.json").read_text())["plan"]["records"]]
        self.assertEqual(manifest["outcome"], "complete")
        self.assertIn("F-1", state["records"]["question"])
        self.assertIn("EVD-1", state["records"]["evidence"])
        self.assertNotIn("F-1-v1", saved_ids)
        self.assertEqual(state["records"]["vintage"], {})
        self.assertIn("vintage:F-1-v1", manifest["gaps"][0])
        published = json.dumps(manifest, ensure_ascii=False) + (self.root / "state/shadow/Intelligence/2026-09-22.md").read_text()
        self.assertNotIn("SECRET_PROVIDER_TEXT", published)
        self.assertNotIn("0.99", published)

    def test_reviewed_evidence_from_arbiter_still_rejects_the_run(self):
        evidence = initial_records()[1]
        def rewrite(stage, *args):
            if stage in {"blue", "arbiter"}:
                return {"records": [evidence], "reason": "Smuggle evidence through review"}, {}
            return successful_stage(stage, *args)
        manifest = run_cycle(self.root, NOW, "test-rewrite", rewrite)
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(manifest["validation_failure"], "arbiter cannot rewrite evidence or resolve forecasts")
        self.assertEqual(manifest["revision_after"], manifest["revision_before"])
        self.assertEqual(load_state(self.root / "state/shadow")["sequence"], 0)
        self.assertFalse((self.root / "state/runs/test-rewrite/accepted-plan.json").exists())

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
