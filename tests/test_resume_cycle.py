import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from lib.forecast_learning import load_state
from lib.learning_cycle import load_resume_outputs, read_json, run_cycle
from lib.resume_cycle import (
    FULL_REASON,
    SKIP_BAD_ID,
    SKIP_EXPIRED,
    SKIP_INVALID,
    SKIP_MISSING,
    SKIP_NO_FAILURE,
    SKIP_NOT_FAILED,
    SKIP_NOT_FOUND,
    SKIP_SAVED,
    SKIP_WRONG_DATE,
    SKIP_WRONG_DAY,
    checkpoint_document,
    inspect_checkpoint,
    known_saved_dates,
    remote_saved_dates,
    resume_action,
    saved_dates,
    seed_checkpoints,
    separate_checkpoint_artifact,
)
from test_forecast_learning import initial_records
from test_learning_cycle import NOW, successful_stage


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-10-23"
TOKEN = "UNPUBLISHED_JUDGMENT_TOKEN"
WORKFLOW = ROOT / ".github/workflows/daily-intelligence.yml"


def failure(run_id, created_at, attempt=1, conclusion="failure", branch="main"):
    return {"github_run_id": str(run_id), "attempt": attempt, "created_at": created_at,
            "conclusion": conclusion, "branch": branch}


def decide(**kwargs):
    values = {"event": "push", "today": TODAY, "requested": "", "runs": [], "saved_dates": set()}
    values.update(kwargs)
    return resume_action(**values)


class ResumeDecisionTests(unittest.TestCase):
    def test_schedule_always_starts_from_collection(self):
        decision = decide(event="schedule", runs=[failure("1", "2026-10-22T23:10:00Z")],
                          saved_dates={TODAY}, artifact_state="ready")
        self.assertEqual(decision["action"], "full")
        self.assertEqual(decision["reason"], FULL_REASON)

    def test_push_and_dispatch_use_the_same_resume_rules(self):
        runs = [failure("9", "2026-10-22T23:10:00Z")]
        push = decide(event="push", runs=runs, artifact_state="ready", stages=["collect"])
        manual = decide(event="workflow_dispatch", runs=runs, artifact_state="ready", stages=["collect"])
        self.assertEqual(push, manual)
        self.assertEqual(push["action"], "resume")
        self.assertEqual(push["github_run_id"], "9")
        self.assertIn("主分析以降だけを実行します", push["reason"])
        self.assertIn("収集はやり直しません", push["reason"])

    def test_latest_today_failure_is_selected_across_the_jst_boundary(self):
        runs = [failure("new", "2026-10-23T02:00:00Z"),
                failure("morning", "2026-10-22T23:10:00Z"),
                failure("yesterday", "2026-10-22T14:00:00Z")]
        decision = decide(runs=runs, artifact_state="ready", stages=["collect", "blue"])
        self.assertEqual(decision["github_run_id"], "new")
        self.assertIn("反証以降だけを実行します", decision["reason"])

    def test_saved_day_skips_even_when_a_checkpoint_exists(self):
        decision = decide(runs=[failure("1", "2026-10-22T23:10:00Z")], saved_dates={TODAY},
                          artifact_state="ready", stages=["collect"])
        self.assertEqual(decision, {"action": "skip", "reason": SKIP_SAVED})

    def test_missing_expired_or_invalid_checkpoint_does_not_recollect(self):
        run = failure("1", "2026-10-22T23:10:00Z")
        self.assertEqual(decide(runs=[run], artifact_state="missing")["reason"], SKIP_MISSING)
        self.assertEqual(decide(runs=[run], artifact_state="expired")["reason"], SKIP_EXPIRED)
        self.assertEqual(decide(runs=[run], artifact_state="invalid")["reason"], SKIP_INVALID)
        for state in ("missing", "expired", "invalid"):
            self.assertEqual(decide(runs=[run], artifact_state=state)["action"], "skip")

    def test_no_failure_or_other_day_does_not_recollect(self):
        self.assertEqual(decide(runs=[])["reason"], SKIP_NO_FAILURE)
        yesterday = failure("1", "2026-10-22T10:00:00Z")
        self.assertEqual(decide(runs=[yesterday])["reason"], SKIP_NO_FAILURE)
        self.assertEqual(decide(requested="1", runs=[yesterday])["reason"], SKIP_WRONG_DAY)
        self.assertEqual(decide(requested="1", runs=[failure("1", "2026-10-22T23:10:00Z", conclusion="success")])["reason"],
                         SKIP_NOT_FAILED)
        self.assertEqual(decide(requested="404", runs=[])["reason"], SKIP_NOT_FOUND)
        self.assertEqual(decide(requested="../not-a-run")["reason"], SKIP_BAD_ID)

    def test_explicit_pipeline_id_selects_that_attempt(self):
        decision = decide(requested="gha-44-3",
                          runs=[failure("44", "2026-10-22T23:10:00Z", attempt=1)],
                          artifact_state="ready", stages=["collect", "blue", "red", "arbiter"])
        self.assertEqual(decision["action"], "resume")
        self.assertEqual(decision["attempt"], 3)
        self.assertEqual(decision["artifact_name"], "checkpoint-44-3")
        self.assertIn("保存だけを実行します", decision["reason"])

    def test_current_run_is_not_treated_as_the_source(self):
        decision = decide(runs=[failure("8", "2026-10-22T23:10:00Z")], current_run_id="8")
        self.assertEqual(decision["reason"], SKIP_NO_FAILURE)

    def test_checkpoint_date_must_be_today(self):
        decision = decide(runs=[failure("1", "2026-10-22T23:10:00Z")], artifact_state="wrong_date",
                          checkpoint_date="2026-10-22")
        self.assertEqual(decision["reason"], SKIP_WRONG_DATE)


class CheckpointFileTests(unittest.TestCase):
    def test_saved_dates_ignore_failures_and_report_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run = root / "state/runs/day"
            run.mkdir(parents=True)
            (run / "manifest.json").write_text(json.dumps({"date": TODAY, "outcome": "failed"}))
            self.assertEqual(saved_dates(root), set())
            (run / "manifest.json").write_text(json.dumps({"date": TODAY, "outcome": "partial"}))
            self.assertEqual(saved_dates(root), {TODAY})

    def test_later_main_commit_counts_as_saved_without_checkout(self):
        with tempfile.TemporaryDirectory() as temporary:
            origin = Path(temporary) / "origin.git"
            work = Path(temporary) / "work"
            later = Path(temporary) / "later"
            work.mkdir()
            subprocess.run(["git", "init", "--bare", "-b", "main", str(origin)], check=True, capture_output=True)
            self.git(work, "init", "-b", "main")
            self.git(work, "config", "user.email", "t@example.com")
            self.git(work, "config", "user.name", "t")
            failed = work / "state/runs/one"
            failed.mkdir(parents=True)
            (failed / "manifest.json").write_text(json.dumps({"date": TODAY, "outcome": "failed"}))
            self.git(work, "add", "state")
            self.git(work, "commit", "-m", "fail")
            self.git(work, "remote", "add", "origin", str(origin))
            self.git(work, "push", "origin", "main")
            subprocess.run(["git", "clone", str(origin), str(later)], check=True, capture_output=True)
            self.git(later, "config", "user.email", "t@example.com")
            self.git(later, "config", "user.name", "t")
            saved = later / "state/runs/two"
            saved.mkdir(parents=True)
            (saved / "manifest.json").write_text(json.dumps({"date": TODAY, "outcome": "complete"}))
            self.git(later, "add", "state")
            self.git(later, "commit", "-m", "save")
            self.git(later, "push", "origin", "main")
            self.assertEqual(saved_dates(work), set())
            self.assertEqual(remote_saved_dates(work), {TODAY})
            self.assertEqual(known_saved_dates(work), {TODAY})

    def git(self, repo, *arguments):
        subprocess.run(["git", "-C", str(repo), *arguments], check=True, capture_output=True, text=True)

    def test_inspect_and_seed_flatten_a_nested_download(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            nested = root / "download" / "checkpoint-stage"
            nested.mkdir(parents=True)
            document = checkpoint_document("collect", {"quality": "complete", "records": [], "gaps": []},
                                           run_id="gha-1-1", date=TODAY, validated_at="2026-10-23T08:00:00+09:00")
            (nested / "collect.json").write_text(json.dumps(document))
            ready = inspect_checkpoint(root / "download", "2026-10-23T09:00:00+09:00", TODAY)
            self.assertEqual(ready["state"], "ready")
            self.assertEqual(ready["stages"], ["collect"])
            destination = root / "seeded"
            self.assertEqual(seed_checkpoints(root / "download", destination), ["collect.json"])
            self.assertTrue((destination / "collect.json").is_file())
            expired = dict(document)
            expired["expires_at"] = "2026-10-01T00:00:00+00:00"
            (nested / "collect.json").write_text(json.dumps(expired))
            self.assertEqual(inspect_checkpoint(root / "download", "2026-10-23T09:00:00+09:00", TODAY)["state"], "expired")

    def test_export_keeps_judgments_out_of_the_run_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / "state/runs/gha-1-1/checkpoints"
            folder.mkdir(parents=True)
            for name, text in [("collect.json", "collection"), ("blue.json", TOKEN), ("red.json", TOKEN)]:
                (folder / name).write_text(text)
            destination = root / "checkpoint-stage"
            copied = separate_checkpoint_artifact(root, destination)
            self.assertEqual(copied, ["blue.json", "collect.json", "red.json"])
            self.assertEqual((folder / "collect.json").read_text(), "collection")
            self.assertFalse((folder / "blue.json").exists())
            self.assertFalse((folder / "red.json").exists())
            self.assertEqual((destination / "blue.json").read_text(), TOKEN)
            self.assertIn(TOKEN, (destination / "blue.json").read_text())

    def test_publish_allowlist_excludes_checkpoints(self):
        specification = importlib.util.spec_from_file_location("publisher", ROOT / "scripts/publish-generated.py")
        module = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(module)
        self.assertTrue(module.allowed("state/runs/gha-1-1/manifest.json"))
        self.assertFalse(module.allowed("state/runs/gha-1-1/checkpoints/collect.json"))
        self.assertFalse(module.allowed("state/runs/gha-1-1/checkpoints/blue.json"))

    def test_workflow_resumes_without_a_second_collection(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("resume_from_run_id", text)
        self.assertIn("省略時は当日JSTの最新の失敗実行", text)
        self.assertIn("cancel-in-progress: false", text)
        self.assertIn("group: intelligence-learning-${{ github.ref }}", text)
        self.assertIn("actions: read", text)
        self.assertIn("checkpoint-${{ github.run_id }}-${{ github.run_attempt }}", text)
        self.assertIn("retention-days: 30", text)
        paths = text.split("paths:", 1)[1].split("permissions:", 1)[0]
        for required in ("scripts/**", ".github/workflows/**", "tests/**", "prompts/**", "schemas/**", "config/**"):
            self.assertIn(required, paths)
        self.assertNotIn("state/**", paths)
        self.assertNotIn("Information/**", paths)
        self.assertIn("steps.resume.outputs.action == 'resume'", text)
        self.assertIn("github.event_name == 'schedule'", text)
        self.assertIn("REQUIRE_RESUME", text)


class ResumeCycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "config", self.root / "config")
        shutil.copytree(ROOT / "prompts", self.root / "prompts")
        shutil.copytree(ROOT / "schemas", self.root / "schemas")

    def tearDown(self):
        self.temp.cleanup()

    def policy_and_state(self):
        policy = read_json(self.root / "config/learning_policy.json")
        return policy, load_state(self.root / "state/shadow")

    def test_blue_failure_keeps_verified_collection_and_not_the_error(self):
        evidence = initial_records()[1]
        called = []

        def stages(stage, context, directory, policy):
            called.append(stage)
            if stage == "collect":
                return {"quality": "complete", "records": [evidence], "gaps": ["one source thin"]}, {}
            if stage == "blue":
                raise RuntimeError("SECRET_PROVIDER_RESPONSE")
            return successful_stage(stage, context, directory, policy)

        manifest = run_cycle(self.root, NOW, "fail-blue", stages)
        checkpoint = json.loads((self.root / "state/runs/fail-blue/checkpoints/collect.json").read_text())
        self.assertEqual(manifest["outcome"], "failed")
        self.assertEqual(called, ["collect", "blue"])
        self.assertEqual(checkpoint["publication"], "withheld")
        self.assertEqual(checkpoint["result"]["records"], [evidence])
        self.assertFalse((self.root / "state/runs/fail-blue/checkpoints/blue.json").exists())
        stored = (self.root / "state/runs/fail-blue/manifest.json").read_text()
        stored += (self.root / "state/shadow/Intelligence/2026-09-22.md").read_text()
        self.assertNotIn("SECRET_PROVIDER_RESPONSE", stored)
        self.assertNotIn("SECRET_PROVIDER_RESPONSE", json.dumps(checkpoint))

    def test_resume_runs_only_the_failed_stage_and_what_follows(self):
        evidence = initial_records()[1]

        def fail_blue(stage, context, directory, policy):
            if stage == "collect":
                return {"quality": "complete", "records": [evidence], "gaps": ["kept"]}, {}
            raise RuntimeError("stop after collection")

        run_cycle(self.root, NOW, "fail-blue", fail_blue)
        called = []

        def resume(stage, context, directory, policy):
            called.append(stage)
            self.assertIn("collect", context["previous_stages"])
            self.assertEqual(context["previous_stages"]["collect"]["records"], [evidence])
            if stage == "blue":
                self.assertNotIn("blue", context["previous_stages"])
            return successful_stage(stage, context, directory, policy)

        manifest = run_cycle(self.root, NOW, "resume-blue", resume,
                             resume_from=self.root / "state/runs/fail-blue/checkpoints")
        self.assertEqual(called, ["blue", "red", "arbiter"])
        self.assertEqual(manifest["outcome"], "complete")
        self.assertEqual(manifest["resumed_stages"], ["collect"])
        self.assertIn("EVD-1", load_state(self.root / "state/shadow")["records"]["evidence"])
        self.assertFalse((self.root / "state/runs/resume-blue/checkpoints/blue.json").exists())
        self.assertTrue((self.root / "state/runs/resume-blue/checkpoints/collect.json").is_file())

    def test_red_failure_resumes_at_red_and_withholds_the_judgment_from_the_report(self):
        def fail_red(stage, context, directory, policy):
            if stage == "blue":
                return {"records": [], "reason": TOKEN}, {}
            if stage == "red":
                raise RuntimeError("red failed")
            return successful_stage(stage, context, directory, policy)

        failed = run_cycle(self.root, NOW, "fail-red", fail_red)
        blue = json.loads((self.root / "state/runs/fail-red/checkpoints/blue.json").read_text())
        self.assertEqual(failed["outcome"], "failed")
        self.assertEqual(blue["result"]["reason"], TOKEN)
        published = failed_text(self.root)
        self.assertNotIn(TOKEN, published)
        destination = self.root / "checkpoint-stage"
        separate_checkpoint_artifact(self.root, destination)
        self.assertIn(TOKEN, (destination / "blue.json").read_text())
        self.assertNotIn(TOKEN, run_record_text(self.root))
        called = []

        def resume(stage, context, directory, policy):
            called.append(stage)
            self.assertEqual(context["previous_stages"]["blue"]["reason"], TOKEN)
            return successful_stage(stage, context, directory, policy)

        manifest = run_cycle(self.root, NOW, "resume-red", resume,
                             resume_from=destination)
        self.assertEqual(called, ["red", "arbiter"])
        self.assertEqual(manifest["resumed_stages"], ["collect", "blue"])
        self.assertNotIn(TOKEN, (self.root / "state/shadow/Intelligence/2026-09-22.md").read_text())
        self.assertFalse((self.root / "state/runs/resume-red/checkpoints/blue.json").exists())

    def test_partial_collection_resumes_without_judgment_models(self):
        evidence = initial_records()[1]

        def collect(stage, *args):
            self.assertEqual(stage, "collect")
            return {"quality": "partial", "records": [evidence], "gaps": ["one source"]}, {}

        run_cycle(self.root, NOW, "partial", collect)

        def forbidden(*args):
            raise AssertionError("judgment models must not run")

        manifest = run_cycle(self.root, NOW, "resume-partial", forbidden,
                             resume_from=self.root / "state/runs/partial/checkpoints")
        self.assertEqual(manifest["outcome"], "partial")
        self.assertEqual(manifest["resumed_stages"], ["collect"])
        self.assertEqual(manifest["usage"]["blue"]["status"], "skipped_partial_collection")

    def test_verified_prefix_stops_before_a_corrupt_later_stage(self):
        evidence = initial_records()[1]
        folder = self.root / "checkpoints"
        folder.mkdir()
        policy, state = self.policy_and_state()
        document = checkpoint_document(
            "collect", {"quality": "complete", "records": [evidence], "gaps": []},
            run_id="source", date="2026-09-22", validated_at=NOW)
        (folder / "collect.json").write_text(json.dumps(document))
        (folder / "blue.json").write_text("{")
        outputs = load_resume_outputs(folder, state, NOW, policy)
        self.assertEqual(list(outputs), ["collect"])
        called = []
        manifest = run_cycle(self.root, NOW, "from-prefix", lambda stage, *args: called.append(stage) or successful_stage(stage, *args),
                             resume_from=folder)
        self.assertEqual(called, ["blue", "red", "arbiter"])
        self.assertEqual(manifest["outcome"], "complete")

    def test_expired_or_foreign_checkpoint_is_rejected(self):
        folder = self.root / "checkpoints"
        folder.mkdir()
        policy, state = self.policy_and_state()
        document = checkpoint_document(
            "collect", {"quality": "complete", "records": [], "gaps": []},
            run_id="source", date="2026-09-21", validated_at="2026-09-21T09:00:00+09:00")
        (folder / "collect.json").write_text(json.dumps(document))
        with self.assertRaises(ValueError):
            load_resume_outputs(folder, state, NOW, policy)
        document["date"] = "2026-09-22"
        document["expires_at"] = "2026-09-22T00:00:00+09:00"
        document["validated_at"] = NOW
        (folder / "collect.json").write_text(json.dumps(document))
        with self.assertRaises(ValueError):
            load_resume_outputs(folder, state, NOW, policy)

    def test_completed_cycle_does_not_leave_judgment_checkpoints(self):
        def reject(stage, *args):
            if stage == "blue":
                return {"records": [], "reason": TOKEN}, {}
            if stage == "red":
                return {"accepted": False, "issues": [TOKEN], "reason": TOKEN}, {}
            return successful_stage(stage, *args)

        manifest = run_cycle(self.root, NOW, "withheld", reject)
        self.assertEqual(manifest["outcome"], "complete")
        self.assertNotIn(TOKEN, tree_text(self.root))
        self.assertTrue((self.root / "state/runs/withheld/checkpoints/collect.json").is_file())
        self.assertFalse((self.root / "state/runs/withheld/checkpoints/blue.json").exists())

    def test_pipeline_refuses_to_collect_when_resume_has_no_checkpoint(self):
        completed = subprocess.run(["bash", str(ROOT / "scripts/run-pipeline.sh")],
                                   cwd=self.root, capture_output=True, text=True,
                                   env={"REQUIRE_RESUME": "true", "PATH": "/usr/bin:/bin"})
        self.assertEqual(completed.returncode, 2)
        self.assertIn("収集からはやり直しません", completed.stderr)
        self.assertFalse((self.root / "state/runs").exists())


def failed_text(root):
    parts = []
    manifest = root / "state/runs/fail-red/manifest.json"
    report = root / "state/shadow/Intelligence/2026-09-22.md"
    for path in (manifest, report):
        parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def run_record_text(root):
    parts = []
    for path in (root / "state/runs").rglob("*"):
        if path.is_file():
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def tree_text(root):
    parts = []
    for path in root.rglob("*"):
        if path.is_file():
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


if __name__ == "__main__":
    unittest.main()
