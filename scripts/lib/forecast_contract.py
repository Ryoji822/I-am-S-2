"""Contracts for public forecast records; history is never edited in place."""

import math
import re
from datetime import datetime, timezone
from urllib.parse import urlparse


FIELDS = {
    "metric": "unit region population quality_protocol",
    "hypothesis": "statement horizon mission_ids causal_link_ids confirming_observation refuting_observation",
    "hypothesis_review": "hypothesis_id reviewed_at assessment supporting_evidence_ids opposing_evidence_ids alternative_explanations reason next_check supersedes",
    "evidence": "url published_at retrieved_at source_group claim_type summary content_hash",
    "question": "statement metric_id horizon forecast_type event_family_id mission_ids scenario_ids causal_link_ids window_start deadline resolution_due operator threshold resolution_mode minimum_cases condition_question_id successor_of missing_policy source_priority",
    "vintage": "question_id issued_at knowledge_cutoff probability point interval confidence confidence_reason evidence_ids method_version baseline_probability baseline_point",
    "observation": "metric_id value unit region population quality_protocol period_start period_end published_at retrieved_at cases complete evidence_ids supersedes",
    "resolution": "question_id status outcome observation_ids resolved_at rule_reason supersedes",
    "review": "question_id resolution_id reviewed_at cause_hypotheses supporting_evidence_ids opposing_evidence_ids affected_link_ids next_check method_change",
    "link_review": "link_id reviewed_at assessment evidence_ids review_ids reason next_check supersedes",
    "warning": "risk_id issued_at level evidence_ids reason response_days time_to_impact_days next_check supersedes",
    "decision": "mission_ids recorded_at status action conditions cost response_days reversible evidence_ids outcome supersedes",
}
KINDS = tuple(FIELDS)
HORIZONS = {"short": (28, 93), "medium": (93, 366),
            "long": (366, 1096), "exploration": (1096, 3653)}
RESOLVED = {"resolved_true", "resolved_false", "resolved_value"}
STATUSES = RESOLVED | {"draft", "open", "awaiting_data", "unresolvable",
                       "invalidated", "condition_not_met"}
LINKS = {"LINK-PRICE-COST", "LINK-COST-PROFIT", "LINK-AUTO-HOURS", "LINK-HOURS-INCOME",
         "LINK-OWNERSHIP-PROFIT", "LINK-INCOME-DEMAND", "LINK-SAFETY-SUPPLY"}
MISSIONS = {"MIS-SOC", "MIS-CO", "MIS-IND"}
RISKS = {"MD-SOC", "MD-CO", "MD-IND", "RISK-SAFETY", "RISK-DEMAND", "RISK-SUPPLY"}


def instant(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be an ISO string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp requires timezone")
    return parsed.astimezone(timezone.utc)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def probability(value):
    return number(value) and 0 <= value <= 1


def reference(records, kind, identifier):
    require(identifier in records[kind], f"unknown {kind} reference")
    return records[kind][identifier]


def evidence_refs(record, records, cutoff=None):
    ids = record["evidence_ids"]
    require(isinstance(ids, list) and bool(ids) and len(ids) == len(set(ids)), "evidence IDs required and unique")
    for identifier in ids:
        evidence = reference(records, "evidence", identifier)
        if cutoff is not None:
            require(instant(evidence["published_at"]) <= cutoff, "future publication")
            require(instant(evidence["retrieved_at"]) <= cutoff, "evidence retrieved after cutoff")


def validate_shape(record):
    kind = record.get("type")
    require(kind in FIELDS, "unknown record type")
    require(set(record) == {"type", "id", "visibility", *FIELDS[kind].split()}, "missing or unknown fields")
    require(isinstance(record["id"], str) and re.fullmatch(r"[A-Za-z0-9_@.:-]{1,120}", record["id"]), "invalid record ID")
    require(record["visibility"] == "public", "private data cannot enter public ledger")


def validate_evidence(record, records, now):
    url = urlparse(record["url"])
    require(url.scheme in {"http", "https"} and bool(url.netloc), "evidence needs a source URL")
    require(not url.username and not url.password, "credentials forbidden in evidence URLs")
    require(record["claim_type"] in {"observed_fact", "announced_plan", "reported_claim", "expert_opinion", "analysis"}, "unknown claim type")
    require(instant(record["published_at"]) <= instant(record["retrieved_at"]) <= now, "evidence timestamps out of order")
    require(re.fullmatch(r"sha256:[a-f0-9]{64}", record["content_hash"]), "content hash required")
    require(bool(record["summary"]) and bool(record["source_group"]), "source description required")


def validate_question(record, records, now):
    reference(records, "metric", record["metric_id"])
    require(record["horizon"] in HORIZONS, "unknown horizon")
    require(record["forecast_type"] in {"binary", "numeric", "time"}, "unknown forecast type")
    if record["forecast_type"] == "time":
        require(records["metric"][record["metric_id"]]["unit"] in {"days", "hours", "unix_seconds"}, "time prediction needs a time unit")
    require(record["resolution_mode"] in {"event", "period"}, "unknown resolution mode")
    require(instant(record["window_start"]) < instant(record["deadline"]) <= instant(record["resolution_due"]), "invalid observation window")
    require(record["operator"] in {">=", ">", "<=", "<", "=="}, "invalid operator")
    require(number(record["threshold"]), "numeric threshold required")
    require(type(record["minimum_cases"]) is int and record["minimum_cases"] > 0, "positive sample requirement")
    require(record["missing_policy"] == "unresolvable", "missing data must not become false")
    require(bool(record["source_priority"]), "source priority required")
    require(bool(record["mission_ids"]) and set(record["mission_ids"]) <= {"MIS-SOC", "MIS-CO", "MIS-IND"}, "invalid missions")
    require(bool(record["scenario_ids"]) and set(record["scenario_ids"]) <= {"W1", "W2", "W3", "W4", "W5"}, "invalid scenarios")
    require(bool(record["causal_link_ids"]) and bool(record["statement"]) and bool(record["event_family_id"]), "question links and statement required")
    require(set(record["causal_link_ids"]) <= LINKS, "unknown causal link")
    for field in ["condition_question_id", "successor_of"]:
        if record[field] is not None:
            require(record[field] != record["id"], "self-reference forbidden")
            reference(records, "question", record[field])
    if record["condition_question_id"]:
        require(records["question"][record["condition_question_id"]]["forecast_type"] == "binary", "condition must be binary")


def validate_vintage(record, records, now):
    question = reference(records, "question", record["question_id"])
    issued = instant(record["issued_at"])
    cutoff = instant(record["knowledge_cutoff"])
    require(cutoff <= issued <= now, "invalid forecast timestamps")
    require((now - issued).total_seconds() <= 3600, "backdated issuance forbidden; use retrospective review")
    require(issued < instant(question["deadline"]), "cannot issue after deadline")
    previous = [v for v in records["vintage"].values() if v["question_id"] == question["id"] and v["id"] != record["id"]]
    if not previous:
        days = (instant(question["deadline"]) - issued).total_seconds() / 86400
        lower, upper = HORIZONS[question["horizon"]]
        require(lower <= days <= upper, "horizon does not match deadline")
        require(issued < instant(question["window_start"]), "first forecast must precede measurement")
    else:
        require(issued > max(instant(v["issued_at"]) for v in previous), "vintage must be newer")
    require(not any(r["question_id"] == question["id"] and r["status"] in RESOLVED for r in records["resolution"].values()), "resolved forecast cannot receive a new vintage")
    evidence_refs(record, records, cutoff)
    require(record["confidence"] in {"low", "medium", "high"} and bool(record["confidence_reason"]), "confidence and reason required")
    require(bool(record["method_version"]), "method version required")
    if question["forecast_type"] == "binary":
        require(probability(record["probability"]) and probability(record["baseline_probability"]), "probability and baseline must be in [0,1]")
        require(record["point"] is None and record["interval"] is None and record["baseline_point"] is None, "binary forecast has no numeric estimate")
    else:
        require(record["probability"] is None and record["baseline_probability"] is None, "numeric forecast has no binary probability")
        require(number(record["point"]) and number(record["baseline_point"]), "point and baseline required")
        interval = record["interval"]
        require(isinstance(interval, list) and len(interval) == 2 and all(number(x) for x in interval), "forecast interval required")
        require(interval[0] <= record["point"] <= interval[1], "point outside interval")


def validate_observation(record, records, now):
    metric = reference(records, "metric", record["metric_id"])
    for field in ["unit", "region", "population", "quality_protocol"]:
        require(record[field] == metric[field], "observation scope differs from metric")
    require(number(record["value"]), "finite observed value required")
    require(type(record["complete"]) is bool and type(record["cases"]) is int and record["cases"] >= 0, "invalid observation coverage")
    require(instant(record["period_start"]) <= instant(record["period_end"]), "invalid measurement window")
    require(instant(record["period_end"]) <= instant(record["published_at"]) <= instant(record["retrieved_at"]) <= now, "invalid observation time")
    evidence_refs(record, records, instant(record["retrieved_at"]))
    if record["supersedes"]:
        old = reference(records, "observation", record["supersedes"])
        for field in ["metric_id", "period_start", "period_end"]:
            require(record[field] == old[field], "revision changes measurement scope")
        require(instant(record["published_at"]) >= instant(old["published_at"]), "revision predates original")


def validate_record(record, records, now):
    validate_shape(record)
    kind = record["type"]
    validator = {"evidence": validate_evidence, "question": validate_question,
                 "vintage": validate_vintage, "observation": validate_observation}.get(kind)
    if validator:
        validator(record, records, now)
    elif kind == "metric":
        require(all(isinstance(record[k], str) and record[k] for k in FIELDS[kind].split()), "metric definition incomplete")
    elif kind == "hypothesis":
        require(record["horizon"] in HORIZONS, "invalid hypothesis horizon")
        require(bool(record["statement"]) and bool(record["confirming_observation"]) and bool(record["refuting_observation"]), "hypothesis needs testable alternatives")
        require(bool(record["mission_ids"]) and bool(record["causal_link_ids"]), "hypothesis needs links")
        require(set(record["mission_ids"]) <= MISSIONS and set(record["causal_link_ids"]) <= LINKS, "unknown mission or causal link")
    elif kind == "hypothesis_review":
        validate_hypothesis_review(record, records, now)
    elif kind == "resolution":
        reference(records, "question", record["question_id"])
        require(record["status"] in STATUSES, "unknown resolution state")
        require(instant(record["resolved_at"]) <= now, "future resolution")
    else:
        validate_review_record(record, records, now)


def validate_hypothesis_review(record, records, now):
    reference(records, "hypothesis", record["hypothesis_id"])
    require(instant(record["reviewed_at"]) <= now, "future hypothesis review")
    require(record["assessment"] in {"supported", "weakened", "undetermined"}, "invalid hypothesis assessment")
    require(bool(record["alternative_explanations"]) and bool(record["reason"]) and bool(record["next_check"]), "hypothesis review needs alternatives and next check")
    for field in ["supporting_evidence_ids", "opposing_evidence_ids"]:
        require(isinstance(record[field], list), "evidence references must be lists")
        for identifier in record[field]:
            evidence = reference(records, "evidence", identifier)
            require(instant(evidence["retrieved_at"]) <= instant(record["reviewed_at"]), "future review evidence")
    require(record["supporting_evidence_ids"] or record["opposing_evidence_ids"] or record["assessment"] == "undetermined", "support or weakening requires evidence")
    if record["supersedes"]:
        previous = reference(records, "hypothesis_review", record["supersedes"])
        require(previous["hypothesis_id"] == record["hypothesis_id"], "review supersedes another hypothesis")
        require(instant(record["reviewed_at"]) > instant(previous["reviewed_at"]), "review must be newer")


def validate_review_record(record, records, now):
    kind = record["type"]
    time_field = {"review": "reviewed_at", "link_review": "reviewed_at",
                  "warning": "issued_at", "decision": "recorded_at"}[kind]
    require(instant(record[time_field]) <= now, "future review")
    if kind == "review":
        question = reference(records, "question", record["question_id"])
        resolution = reference(records, "resolution", record["resolution_id"])
        require(resolution["question_id"] == question["id"], "review targets another forecast")
        require(bool(record["cause_hypotheses"]) and bool(record["next_check"]), "review needs causes and next check")
        require(set(record["affected_link_ids"]) <= set(question["causal_link_ids"]), "review changes unrelated long-term links")
        for field in ["supporting_evidence_ids", "opposing_evidence_ids"]:
            for identifier in record[field]:
                evidence = reference(records, "evidence", identifier)
                require(instant(evidence["retrieved_at"]) <= instant(record[time_field]), "future review evidence")
    elif kind == "link_review":
        require(record["link_id"] in LINKS, "unknown causal link")
        require(record["assessment"] in {"supported", "weakened", "undetermined"}, "invalid link assessment")
        require(bool(record["review_ids"]) and bool(record["reason"]) and bool(record["next_check"]), "link review incomplete")
        for identifier in record["review_ids"]:
            review = reference(records, "review", identifier)
            require(record["link_id"] in review["affected_link_ids"], "unrelated causal link")
        evidence_refs(record, records, instant(record["reviewed_at"]))
        if record["supersedes"]:
            old = reference(records, "link_review", record["supersedes"])
            require(old["link_id"] == record["link_id"], "link revision targets another link")
            require(instant(record["reviewed_at"]) > instant(old["reviewed_at"]), "link review must be newer")
    elif kind == "warning":
        require(record["level"] in {"normal", "watch", "warning", "critical"}, "invalid warning level")
        evidence_refs(record, records, instant(record["issued_at"]))
        require(bool(record["reason"]) and bool(record["next_check"]), "warning needs reason and next check")
        validate_warning(record, records)
    else:
        require(record["status"] in {"proposed", "chosen", "executed", "reviewed"}, "invalid decision status")
        require(bool(record["action"]) and bool(record["conditions"]), "decision requires action and conditions")
        evidence_refs(record, records, instant(record["recorded_at"]))
        require(type(record["reversible"]) is bool and set(record["mission_ids"]) <= MISSIONS, "invalid decision scope")
        require(record["cost"] is None or isinstance(record["cost"], str), "cost needs a unit and basis or null")
        if record["supersedes"]:
            old = reference(records, "decision", record["supersedes"])
            require(instant(record["recorded_at"]) > instant(old["recorded_at"]), "decision revision must be newer")


def validate_warning(record, records):
    require(record["risk_id"] in RISKS, "unknown risk")
    for field in ["response_days", "time_to_impact_days"]:
        require(record[field] is None or number(record[field]) and record[field] >= 0, "unknown duration must be null")
    previous = [r for r in records["warning"].values() if r["risk_id"] == record["risk_id"]]
    if not previous:
        require(record["supersedes"] is None, "first warning cannot supersede another risk")
        return
    old = max(previous, key=lambda r: instant(r["issued_at"]))
    require(record["supersedes"] == old["id"], "warning must supersede latest state of this risk")
    require(instant(record["issued_at"]) > instant(old["issued_at"]), "warning must be newer")
    levels = ["normal", "watch", "warning", "critical"]
    if levels.index(record["level"]) < levels.index(old["level"]):
        new_evidence = [records["evidence"][i] for i in record["evidence_ids"] if i not in old["evidence_ids"]]
        require(any(instant(e["retrieved_at"]) > instant(old["issued_at"]) for e in new_evidence), "warning reduction requires new evidence")
