import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from lib.forecast_learning import apply_plan, load_state, resolve, scorecard


NOW = "2026-09-22T08:00:00+09:00"
END = "2026-12-22T23:59:59+09:00"
DUE = "2027-01-05T23:59:59+09:00"
LATER = "2026-12-24T08:00:00+09:00"


def record(kind, identifier, **values):
    return {"type": kind, "id": identifier, "visibility": "public", **values}


def initial_records():
    metric = record("metric", "MET-1@1", unit="ratio", region="Japan",
                    population="fixed-five-tasks-v1", quality_protocol="quality-v1")
    evidence = record("evidence", "EVD-1", url="https://example.org/baseline",
                      published_at="2026-09-20T08:00:00+09:00",
                      retrieved_at="2026-09-21T08:00:00+09:00",
                      source_group="primary-one", claim_type="observed_fact",
                      summary="Fixed task baseline", content_hash="sha256:" + "a" * 64)
    question = record("question", "F-1", statement="The fixed task cost ratio reaches 1.3",
                      metric_id="MET-1@1", horizon="short", forecast_type="binary",
                      event_family_id="cost-change", mission_ids=["MIS-CO"],
                      scenario_ids=["W2"], causal_link_ids=["LINK-COST-PROFIT"],
                      window_start="2026-11-25T00:00:00+09:00", deadline=END,
                      resolution_due=DUE, operator=">=", threshold=1.3,
                      resolution_mode="period", minimum_cases=20,
                      condition_question_id=None, successor_of=None,
                      missing_policy="unresolvable", source_priority=["primary-one"])
    vintage = record("vintage", "F-1-v1", question_id="F-1", issued_at=NOW,
                     knowledge_cutoff=NOW, probability=0.7, point=None, interval=None,
                     confidence="low", confidence_reason="Limited baseline",
                     evidence_ids=["EVD-1"], method_version="method-v1",
                     baseline_probability=0.5, baseline_point=None)
    return [metric, evidence, question, vintage]


def actual_records(value=1.1, suffix="1"):
    evidence = record("evidence", "EVD-ACTUAL-" + suffix,
                      url="https://example.org/actual", published_at=LATER,
                      retrieved_at=LATER, source_group="primary-one",
                      claim_type="observed_fact", summary="Observed task costs",
                      content_hash="sha256:" + "b" * 64)
    observation = record("observation", "OBS-" + suffix, metric_id="MET-1@1",
                         value=value, unit="ratio", region="Japan",
                         population="fixed-five-tasks-v1", quality_protocol="quality-v1",
                         period_start="2026-11-25T00:00:00+09:00", period_end=END,
                         published_at=LATER, retrieved_at=LATER, cases=20,
                         complete=True, evidence_ids=[evidence["id"]],
                         supersedes=None)
    return [evidence, observation]


class ForecastLearningTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.add("initial", initial_records(), NOW)

    def tearDown(self):
        self.temp.cleanup()

    def add(self, run_id, records, now=LATER, revision=None):
        state = load_state(self.root)
        plan = {"run_id": run_id, "expected_revision": revision or state["revision"],
                "quality": "complete", "review_complete": True, "records": records}
        return apply_plan(self.root, plan, now=now)

    def test_immutable_question_and_vintage(self):
        for original in initial_records()[2:]:
            changed = {**original, "statement": "changed"} if original["type"] == "question" else {**original, "probability": 0.9}
            before = load_state(self.root)
            with self.assertRaises(ValueError):
                self.add("rewrite", [changed])
            self.assertEqual(before, load_state(self.root))

    def test_replay_is_idempotent_and_content_collision_fails(self):
        initial = initial_records()
        plan = {"run_id": "initial", "expected_revision": "0", "quality": "complete",
                "review_complete": True, "records": initial}
        before = load_state(self.root)
        apply_plan(self.root, plan, now=NOW)
        self.assertEqual(before, load_state(self.root))
        with self.assertRaises(ValueError):
            apply_plan(self.root, {**plan, "records": initial[:2]}, now=NOW)

    def test_stale_update_is_rejected(self):
        with self.assertRaises(ValueError):
            self.add("stale", actual_records(), revision="0")

    def test_future_and_late_retrieved_evidence_rejected(self):
        for field in ["published_at", "retrieved_at"]:
            records = initial_records()
            records[1] = {**records[1], field: "2026-09-23T08:00:00+09:00"}
            records[3] = {**records[3], "id": "F-1-v2"}
            records[1] = {**records[1], "id": "EVD-FUTURE"}
            records[3] = {**records[3], "evidence_ids": ["EVD-FUTURE"]}
            with self.assertRaises(ValueError):
                self.add("future-" + field, [records[1], records[3]], NOW)

    def test_missing_is_waiting_then_unresolvable(self):
        state = load_state(self.root)
        self.assertEqual(resolve(state, "F-1", NOW)["status"], "open")
        self.assertEqual(resolve(state, "F-1", LATER)["status"], "awaiting_data")
        self.assertEqual(resolve(state, "F-1", "2027-01-06T08:00:00+09:00")["status"], "unresolvable")

    def test_period_cannot_resolve_early(self):
        self.add("actual", actual_records())
        result = resolve(load_state(self.root), "F-1", NOW)
        self.assertEqual(result["status"], "open")

    def test_resolution_and_brier_example(self):
        self.add("actual", actual_records())
        state = load_state(self.root)
        resolution = resolve(state, "F-1", LATER)
        self.assertEqual(resolution["status"], "resolved_false")
        self.add("resolve", [resolution])
        score = scorecard(load_state(self.root), as_of=LATER)
        self.assertAlmostEqual(score["short"]["initial_brier"], 0.49)
        self.assertEqual(score["short"]["scored_questions"], 1)
        self.assertEqual(score["short"]["calibration_status"], "insufficient")

    def test_wrong_scope_and_quality_rejected(self):
        for field, value in [("region", "US"), ("population", "other"),
                             ("unit", "yen"), ("quality_protocol", "changed")]:
            actual = actual_records()
            actual[1] = {**actual[1], field: value}
            with self.assertRaises(ValueError):
                self.add("scope-" + field, actual)

    def test_incomplete_or_wrong_period_does_not_resolve(self):
        for field, value in [("complete", False), ("cases", 19),
                             ("period_start", "2026-11-26T00:00:00+09:00")]:
            with self.subTest(field=field):
                actual = actual_records(suffix=field)
                actual[1] = {**actual[1], field: value}
                self.add("incomplete-" + field, actual)
                self.assertEqual(resolve(load_state(self.root), "F-1", LATER)["status"], "awaiting_data")

    def test_revision_retains_initial_and_latest_scores(self):
        self.add("actual", actual_records())
        self.add("resolution-1", [resolve(load_state(self.root), "F-1", LATER)])
        revised = actual_records(1.5, "2")
        revised[1] = {**revised[1], "supersedes": "OBS-1"}
        self.add("actual-revised", revised)
        self.add("resolution-2", [resolve(load_state(self.root), "F-1", "2026-12-25T08:00:00+09:00")], "2026-12-25T08:00:00+09:00")
        scores = scorecard(load_state(self.root), as_of="2026-12-25T08:00:00+09:00")
        self.assertAlmostEqual(scores["short"]["initial_brier"], 0.49)
        self.assertAlmostEqual(scores["short"]["latest_brier"], 0.09)
        self.assertEqual(len(load_state(self.root)["records"]["resolution"]), 2)

    def test_failed_plan_preserves_all_state(self):
        before = load_state(self.root)
        plan = {"run_id": "failed", "expected_revision": before["revision"],
                "quality": "failed", "review_complete": False,
                "records": actual_records()}
        with self.assertRaises(ValueError):
            apply_plan(self.root, plan, now=LATER)
        self.assertEqual(before, load_state(self.root))

    def test_private_and_example_records_rejected(self):
        for extra in [{"visibility": "private"}, {"example_only": True}]:
            actual = actual_records()
            actual[0] = {**actual[0], **extra}
            with self.assertRaises(ValueError):
                self.add("private", actual)

    def test_inputs_are_unchanged(self):
        records = actual_records()
        before = copy.deepcopy(records)
        self.add("actual", records)
        self.assertEqual(before, records)

    def test_no_scores_are_not_perfect_accuracy(self):
        scores = scorecard(load_state(self.root), as_of=NOW)
        for horizon in ["short", "medium", "long", "exploration"]:
            self.assertIsNone(scores[horizon]["initial_brier"])
            self.assertEqual(scores[horizon]["scored_questions"], 0)

    def test_unrelated_link_cannot_be_changed(self):
        records = initial_records()
        question = {**records[2], "id": "F-unknown-link", "causal_link_ids": ["UNKNOWN"]}
        with self.assertRaises(ValueError):
            self.add("unknown-link", [question], NOW)

    def test_forged_resolution_is_rejected_atomically(self):
        actual = actual_records()
        state = self.add("actual", actual)
        result = {**resolve(state, "F-1", LATER), "outcome": 1}
        before = load_state(self.root)
        with self.assertRaises(ValueError):
            self.add("forged", [result])
        self.assertEqual(before, load_state(self.root))

    def test_false_condition_is_not_a_successful_prediction(self):
        records = initial_records()
        question = {**records[2], "id": "F-2", "condition_question_id": "F-1"}
        vintage = {**records[3], "id": "F-2-v1", "question_id": "F-2"}
        self.add("conditional", [question, vintage], NOW)
        self.add("actual", actual_records())
        self.assertEqual(resolve(load_state(self.root), "F-2", LATER)["status"], "condition_not_met")

    def test_numeric_prediction_keeps_units_and_interval_coverage(self):
        records = initial_records()
        question = {**records[2], "id": "F-numeric", "forecast_type": "numeric"}
        vintage = {**records[3], "id": "F-numeric-v1", "question_id": "F-numeric",
                   "probability": None, "baseline_probability": None, "point": 1.2,
                   "baseline_point": 1.5, "interval": [1.0, 1.4]}
        self.add("numeric", [question, vintage], NOW)
        self.add("actual", actual_records())
        self.add("numeric-resolution", [resolve(load_state(self.root), "F-numeric", LATER)])
        result = scorecard(load_state(self.root), LATER)["short"]["numeric_by_metric"]["MET-1@1"]
        self.assertAlmostEqual(result["mae"], 0.1)
        self.assertEqual(result["interval_coverage"], 1)

    def test_warning_cannot_be_cleared_by_reusing_old_evidence(self):
        warning = record("warning", "WARN-1", risk_id="RISK-SAFETY", issued_at=NOW,
                         level="warning", evidence_ids=["EVD-1"], reason="Test concern",
                         response_days=7, time_to_impact_days=None, next_check="Next evidence", supersedes=None)
        self.add("warning", [warning], NOW)
        cleared = {**warning, "id": "WARN-2", "level": "normal", "supersedes": "WARN-1"}
        with self.assertRaises(ValueError):
            self.add("clear-without-evidence", [cleared], NOW)

    def test_scores_include_method_and_same_metric_cohorts(self):
        self.add("actual", actual_records())
        self.add("resolution", [resolve(load_state(self.root), "F-1", LATER)])
        result = scorecard(load_state(self.root), LATER)["short"]["method_comparisons"]
        self.assertEqual(result[0]["method_version"], "method-v1")
        self.assertEqual(result[0]["metric_id"], "MET-1@1")
        self.assertEqual(result[0]["calibration_status"], "insufficient")


if __name__ == "__main__":
    unittest.main()
