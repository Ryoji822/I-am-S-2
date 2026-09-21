"""Deterministic resolution and scoring, with missing data kept separate."""

import operator
from collections import defaultdict

from .forecast_contract import HORIZONS, RESOLVED, instant, reference, require


OPERATORS = {">=": operator.ge, ">": operator.gt, "<=": operator.le,
             "<": operator.lt, "==": operator.eq}


def for_question(records, kind, identifier, time_field, as_of):
    return sorted((r for r in records[kind].values()
                   if r["question_id"] == identifier and instant(r[time_field]) <= as_of),
                  key=lambda r: instant(r[time_field]))


def candidates(records, question, now):
    available = [r for r in records["observation"].values()
                 if r["metric_id"] == question["metric_id"] and instant(r["retrieved_at"]) <= now]
    replaced = {r["supersedes"] for r in available if r["supersedes"]}
    return [r for r in available if r["id"] not in replaced and r["complete"]
            and r["cases"] >= question["minimum_cases"]
            and any(records["evidence"][e]["source_group"] in question["source_priority"]
                    for e in r["evidence_ids"])]


def matching_observation(records, question, now):
    start, end = instant(question["window_start"]), instant(question["deadline"])
    matches = []
    for observation in candidates(records, question, now):
        left, right = instant(observation["period_start"]), instant(observation["period_end"])
        whole = left == start and right == end and now >= end
        early = (question["resolution_mode"] == "event" and question["forecast_type"] == "binary"
                 and start <= left <= right <= end
                 and OPERATORS[question["operator"]](observation["value"], question["threshold"]))
        if whole or early:
            matches.append(observation)
    if not matches:
        return None
    def priority(observation):
        groups = [records["evidence"][e]["source_group"] for e in observation["evidence_ids"]]
        return min(question["source_priority"].index(g) for g in groups if g in question["source_priority"])
    best = min(priority(o) for o in matches)
    matches = [o for o in matches if priority(o) == best]
    if len({o["value"] for o in matches}) > 1:
        return None
    return sorted(matches, key=lambda o: (instant(o["published_at"]), o["id"]))[-1]


def outcome_for(records, question, now, visiting):
    require(question["id"] not in visiting, "cyclic forecast condition")
    vintages = for_question(records, "vintage", question["id"], "issued_at", now)
    if not vintages:
        return "draft", None, [], "発行に必要な情報を準備中"
    condition = question["condition_question_id"]
    if condition:
        prerequisite = reference(records, "question", condition)
        status, _, _, _ = outcome_for(records, prerequisite, now, visiting | {question["id"]})
        if status == "resolved_false" or status == "condition_not_met":
            return "condition_not_met", None, [], "前提条件が成立しなかったため採点しない"
        if status != "resolved_true":
            status = "unresolvable" if now > instant(question["resolution_due"]) else "awaiting_data"
            return status, None, [], "前提条件の判定を待っている"
    observation = matching_observation(records, question, now)
    if observation:
        value = observation["value"]
        if question["forecast_type"] != "binary":
            return "resolved_value", value, [observation["id"]], "事前に決めた測定条件と実績が一致"
        outcome = int(OPERATORS[question["operator"]](value, question["threshold"]))
        return ("resolved_true" if outcome else "resolved_false"), outcome, [observation["id"]], "事前の閾値を実績に適用"
    if now < instant(question["deadline"]):
        return "open", None, [], "観測期間がまだ終わっていない"
    if now <= instant(question["resolution_due"]):
        return "awaiting_data", None, [], "判定に足りる実績の公表・取得を待っている"
    return "unresolvable", None, [], "公表待ち期限を過ぎても判定できる実績がない"


def resolve(state, question_id, as_of):
    now, records = instant(as_of), state["records"]
    question = reference(records, "question", question_id)
    previous = for_question(records, "resolution", question_id, "resolved_at", now)
    if previous and previous[-1]["status"] == "invalidated":
        return previous[-1]
    status, outcome, observation_ids, reason = outcome_for(records, question, now, set())
    if previous:
        old = previous[-1]
        if (status, outcome, observation_ids) == (old["status"], old["outcome"], old["observation_ids"]):
            return dict(old)
    return {"type": "resolution", "id": f"RES-{question_id}-{len(previous) + 1}",
            "visibility": "public", "question_id": question_id, "status": status,
            "outcome": outcome, "observation_ids": observation_ids, "resolved_at": as_of,
            "rule_reason": reason, "supersedes": previous[-1]["id"] if previous else None}


def score_one(question, vintage, resolution):
    if resolution is None or resolution["status"] not in RESOLVED:
        return None
    outcome = resolution["outcome"]
    if question["forecast_type"] == "binary":
        return {"value": (vintage["probability"] - outcome) ** 2,
                "baseline": (vintage["baseline_probability"] - outcome) ** 2,
                "kind": "brier", "probability": vintage["probability"], "outcome": outcome}
    return {"value": abs(vintage["point"] - outcome),
            "baseline": abs(vintage["baseline_point"] - outcome), "kind": "absolute_error",
            "covered": vintage["interval"][0] <= outcome <= vintage["interval"][1]}


def question_scores(state, as_of):
    records, now = state["records"], instant(as_of)
    result = []
    for question in records["question"].values():
        vintages = for_question(records, "vintage", question["id"], "issued_at", now)
        resolutions = for_question(records, "resolution", question["id"], "resolved_at", now)
        terminal = [r for r in resolutions if r["status"] in RESOLVED]
        first, latest = (terminal[0] if terminal else None), (resolutions[-1] if resolutions else None)
        row = {"question_id": question["id"], "horizon": question["horizon"],
               "event_family_id": question["event_family_id"], "metric_id": question["metric_id"],
               "status": resolve(state, question["id"], as_of)["status"], "initial": None,
               "latest": None, "checkpoints": {}}
        if vintages:
            row = {**row, "vintage_id": vintages[0]["id"],
                   "method_version": vintages[0]["method_version"], "issue_month": vintages[0]["issued_at"][:7],
                   "initial_resolution_id": first["id"] if first else None,
                   "latest_resolution_id": latest["id"] if latest else None,
                   "initial": score_one(question, vintages[0], first),
                   "latest": score_one(question, vintages[0], latest)}
            for days in [30, 90]:
                eligible = [v for v in vintages if (instant(question["deadline"]) - instant(v["issued_at"])).total_seconds() >= days * 86400]
                if eligible:
                    row["checkpoints"][str(days)] = {"vintage_id": eligible[-1]["id"], "score": score_one(question, eligible[-1], latest)}
        result.append(row)
    return result


def average(values):
    return sum(values) / len(values) if values else None


def summarize_horizon(rows):
    first = [r["initial"] for r in rows if r["initial"] and r["initial"]["kind"] == "brier"]
    latest = [r["latest"] for r in rows if r["latest"] and r["latest"]["kind"] == "brier"]
    families = {r["event_family_id"] for r in rows if r["latest"]}
    counts = {status: sum(r["status"] == status for r in rows) for status in {r["status"] for r in rows}}
    numeric = defaultdict(list)
    for row in rows:
        if row["latest"] and row["latest"]["kind"] == "absolute_error":
            numeric[row["metric_id"]].append(row["latest"])
    return {"questions": len(rows), "scored_questions": sum(bool(r["latest"]) for r in rows),
            "independent_families": len(families), "statuses": counts,
            "initial_brier": average([r["value"] for r in first]),
            "latest_brier": average([r["value"] for r in latest]),
            "baseline_brier": average([r["baseline"] for r in latest]),
            "calibration_status": "insufficient" if len(families) < 30 else "descriptive_only",
            "unresolvable_rate": counts.get("unresolvable", 0) / len(rows) if rows else None,
            "invalidated_rate": counts.get("invalidated", 0) / len(rows) if rows else None,
            "numeric_by_metric": {key: {"count": len(items), "mae": average([x["value"] for x in items]),
                                       "baseline_mae": average([x["baseline"] for x in items]),
                                       "interval_coverage": average([int(x["covered"]) for x in items])}
                                  for key, items in numeric.items()},
            "rate_denominator": "all registered questions, including drafts",
            "calibration_bins": calibration_bins(latest), "method_comparisons": method_comparisons(rows), "details": rows}


def method_comparisons(rows):
    groups = defaultdict(list)
    for row in rows:
        if row["latest"]:
            groups[(row["metric_id"], row["method_version"], row["issue_month"])].append(row)
    result = []
    for (metric, method, month), items in sorted(groups.items()):
        families = len({r["event_family_id"] for r in items})
        result.append({"metric_id": metric, "method_version": method, "issue_month": month,
                       "questions": len(items), "independent_families": families,
                       "error": average([r["latest"]["value"] for r in items]),
                       "baseline_error": average([r["latest"]["baseline"] for r in items]),
                       "improvement_over_baseline": average([r["latest"]["baseline"] - r["latest"]["value"] for r in items]),
                       "calibration_status": "insufficient" if families < 30 else "descriptive_only",
                       "automatic_adjustment": False})
    return result


def calibration_bins(scores):
    result = []
    for lower in range(0, 100, 10):
        selected = [s for s in scores if lower / 100 <= s["probability"] < (lower + 10) / 100
                    or (lower == 90 and s["probability"] == 1)]
        result.append({"lower": lower / 100, "upper": (lower + 10) / 100,
                       "count": len(selected), "mean_probability": average([s["probability"] for s in selected]),
                       "observed_rate": average([s["outcome"] for s in selected])})
    return result


def scorecard(state, as_of):
    rows = question_scores(state, as_of)
    return {horizon: summarize_horizon([r for r in rows if r["horizon"] == horizon]) for horizon in HORIZONS}
