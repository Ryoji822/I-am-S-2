"""Daily proposals, adversarial review, atomic acceptance, deterministic reports."""

import fcntl
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from .forecast_contract import FIELDS, instant, require
from .forecast_learning import apply_plan, append_records, digest, load_state, validate_plan
from .forecast_scoring import resolve
from .learning_model import SOURCE_HOSTS, capture_collected, model_config, run_model
from .learning_render import atomic_text, write_failure_snapshot, write_outputs
from .legacy_information import historical_context
from .report_knowledge import load_dossiers, merge_dossiers


STAGES = {"collect": "phase1-collect.md", "blue": "phase2-analyze.md",
          "red": "phase3-red-team.md", "arbiter": "phase4-arbiter.md"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def current_context(root, state, now):
    catalogs = {name: read_json(root / "config" / f"{name}.json") for name in
                ["missions", "world_scenarios", "causal_links", "risks", "metrics", "forecast_candidates", "collection_plan"]}
    # Bound the model context; the ledger itself retains all older history.
    records = state["records"]
    reviewed = {r["resolution_id"] for r in records["review"].values()}
    terminal = {"resolved_true", "resolved_false", "resolved_value", "invalidated", "unresolvable", "condition_not_met"}
    resolutions = {q: resolve(state, q, now) for q in records["question"]}
    eligible = [q for q in records["question"].values()
                if resolutions[q["id"]]["status"] not in terminal or resolutions[q["id"]]["id"] not in reviewed]
    questions = sorted(eligible, key=lambda q: (resolutions[q["id"]]["status"] not in terminal, q["deadline"]))[:20]
    ids = {q["id"] for q in questions}
    selected = {"hypothesis": list(records["hypothesis"].values()), "question": questions,
                "metric": list(records["metric"].values())[-40:]}
    for kind, values in records.items():
        if kind in selected:
            continue
        if kind == "dossier_section":
            selected[kind] = []  # Latest complete sections and their IDs are supplied below.
            continue
        subset = [r for r in values.values() if "question_id" not in r or r["question_id"] in ids]
        selected[kind] = subset if kind in {"vintage", "resolution", "review"} else subset[-40:]
    linked_evidence = set()
    for values in selected.values():
        for record in values:
            for field in ["evidence_ids", "supporting_evidence_ids", "opposing_evidence_ids"]:
                linked_evidence.update(record.get(field, []))
    evidence = {r["id"]: r for r in selected["evidence"]}
    selected["evidence"] = list({**evidence, **{key: records["evidence"][key] for key in linked_evidence}}.values())
    return {"now": now, "revision": state["revision"], "catalogs": catalogs,
            "records": selected, "record_fields": FIELDS,
            "dossiers": merge_dossiers(load_dossiers(root, now), state, now),
            "legacy_information": historical_context(root, now),
            "allowed_source_domains": SOURCE_HOSTS,
            "context_limit": "期限順20予測、種類ごと直近40記録。全履歴は保存。対象外を未確認とする。"}


def initial_definitions(root, state):
    return [r for r in read_json(root / "config/hypotheses.json")["hypotheses"]
            if r["id"] not in state["records"]["hypothesis"]]


def validate_stage(stage, result, policy):
    expected = {"collect": {"quality", "records", "gaps"}, "blue": {"records", "reason"},
                "red": {"accepted", "issues", "reason"}, "arbiter": {"records", "reason"}}
    require(set(result) == expected[stage], "invalid stage result fields")
    if "records" in result:
        require(isinstance(result["records"], list) and len(result["records"]) <= 80, "stage record limit exceeded")
        require(all(isinstance(r, dict) for r in result["records"]), "stage record must be an object")
    if stage == "collect":
        require(result["quality"] in {"complete", "partial", "failed", "stale"}, "unknown collection quality")
        require(isinstance(result["gaps"], list), "collection gaps must be a list")
        require(all(r.get("type") in {"evidence", "observation"} for r in result["records"]), "collector cannot make judgments")
        require(sum(r.get("type") == "evidence" for r in result["records"]) <= policy["max_new_evidence"], "evidence limit exceeded")
    if stage == "red":
        require(type(result["accepted"]) is bool and isinstance(result["issues"], list), "invalid red review")
        require(result["accepted"] and not result["issues"], "red review rejected proposal")


def update_plan(state, run_id, outputs, bootstrap, now):
    collected = outputs["collect"]
    require(collected["quality"] in {"complete", "partial"}, "no usable fresh collection")
    accepted = outputs["arbiter"]["records"]
    blue = outputs["blue"]["records"]
    require(all(record in blue for record in accepted), "arbiter introduced an unreviewed record")
    require(all(record["type"] not in {"evidence", "observation", "resolution"} for record in accepted), "arbiter cannot rewrite evidence or resolve forecasts")
    proposed = bootstrap + collected["records"] + accepted
    quality = collected["quality"]
    if quality == "partial":
        require(not accepted, "partial run cannot change judgments")
        # Definitions are initialized only on a complete run.
        proposed = collected["records"]
    plan = {"run_id": run_id, "expected_revision": state["revision"], "quality": quality,
            "review_complete": True, "records": proposed}
    candidate = validate_plan(state, plan, instant(now))
    proposed = [r for r in proposed if state["records"][r["type"]].get(r["id"]) != r]
    resolutions = [resolve(candidate, q, now) for q in candidate["records"]["question"]]
    resolutions = [r for r in resolutions if r["id"] not in candidate["records"]["resolution"]]
    return {**plan, "records": proposed + resolutions}


def execute_stages(root, state, bootstrap, now, runner, policy, run_directory):
    outputs, usage = {}, {}
    context = current_context(root, append_records(state, bootstrap), now)
    with tempfile.TemporaryDirectory(prefix="ias2-model-") as temporary:
        for stage, prompt in STAGES.items():
            stage_now = datetime.now(timezone.utc).isoformat() if runner is run_model else now
            stage_context = {**context, "now": stage_now, "previous_stages": outputs,
                             "instructions": (root / "prompts" / prompt).read_text(encoding="utf-8")}
            require(len(json.dumps(stage_context, ensure_ascii=False).encode()) <= 400_000, "model context budget exceeded")
            result, cost = runner(stage, stage_context, Path(temporary) / stage, policy)
            validate_stage(stage, result, policy)
            if stage == "collect" and runner is run_model:
                result = {**result, "records": capture_collected(result["records"])}
            outputs, usage = {**outputs, stage: result}, {**usage, stage: cost}
            atomic_text(run_directory / "stage-metadata.json", json.dumps(usage, ensure_ascii=False, indent=2) + "\n")
            # Only accepted public derivatives are persisted after the entire run validates.
    return outputs, usage


def manifest_base(run_id, date, now, policy, state, root):
    prompts = {key: digest((root / "prompts" / file).read_text(encoding="utf-8")) for key, file in STAGES.items()}
    return {"schema_version": "2.0", "run_id": run_id, "date": date, "started_at": now,
            "mode": policy["mode"], "model": policy["model"], "opencode_version": policy["opencode_version"],
            "code_version": "learning-v3-dossiers", "prompt_hashes": prompts, "revision_before": state["revision"],
            "quality": "failed", "outcome": "failed", "gaps": [], "usage": {},
            "daily_budget": policy["daily_budget"], "monthly_budget": policy["monthly_budget"]}


def run_locked(root, now, run_id, stage_runner, policy):
    directory = root / "state/runs" / run_id
    manifest_path = directory / "manifest.json"
    ledger_root = root / "state/shadow" if policy["mode"] == "shadow" else root
    state = load_state(ledger_root)
    if manifest_path.exists():
        previous = read_json(manifest_path)
        if previous["outcome"] != "failed" or run_id not in state["runs"]:
            return previous
    date = instant(now).astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()
    manifest = manifest_base(run_id, date, now, policy, state, root)
    plan_path = directory / "accepted-plan.json"
    try:
        if plan_path.exists():
            saved = read_json(plan_path)
            plan, usage, gaps, finished = (saved[k] for k in ["plan", "usage", "gaps", "finished_at"])
            dossiers = saved["dossiers"]
        else:
            outputs, usage = execute_stages(root, state, initial_definitions(root, state), now, stage_runner, policy, directory)
            finished = datetime.now(timezone.utc).isoformat() if stage_runner is run_model else now
            plan = update_plan(state, run_id, outputs, initial_definitions(root, state), finished)
            candidate = validate_plan(state, plan, instant(finished))
            dossiers = merge_dossiers(load_dossiers(root, finished), candidate, finished)
            gaps = outputs["collect"]["gaps"]
            atomic_text(plan_path, json.dumps({"plan": plan, "usage": usage, "gaps": gaps,
                        "finished_at": finished, "dossiers": dossiers}, ensure_ascii=False, indent=2) + "\n")
        accepted = apply_plan(ledger_root, plan, now=finished)
        accepted = load_state(ledger_root, through_run=run_id)
        manifest = {**manifest, "quality": plan["quality"], "outcome": plan["quality"], "gaps": gaps,
                    "finished_at": finished, "revision_after": accepted["revision"], "usage": usage,
                    "dossier_hash": digest(dossiers)}
        write_outputs(root, accepted, manifest, plan["records"], dossiers)
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.SubprocessError) as error:
        manifest = {**manifest, "outcome": "failed", "quality": "failed", "error_type": type(error).__name__,
                    "finished_at": now, "gaps": ["収集・反証・検証・保存のいずれかが完了しませんでした。新しい正式判断は公表していません。"],
                    "revision_after": load_state(ledger_root)["revision"]}
        metadata = directory / "stage-metadata.json"
        if metadata.exists():
            manifest = {**manifest, "usage": read_json(metadata)}
        try:
            prior_dossiers = merge_dossiers(load_dossiers(root, now), state, now)
            write_failure_snapshot(root, state, manifest, prior_dossiers)
        except (ValueError, KeyError, TypeError, OSError):
            pass  # Preserve the failed manifest even when no baseline can be rendered.
        # The exception message may include provider secrets or private input; do not persist it.
    atomic_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def run_cycle(root, now, run_id=None, stage_runner=run_model):
    root = Path(root)
    policy = read_json(root / "config/learning_policy.json")
    require(policy["mode"] in {"shadow", "live"}, "invalid operation mode")
    if policy["mode"] == "live":
        days = {read_json(path)["date"] for path in (root / "state/runs").glob("*/manifest.json")
                if read_json(path).get("mode") == "shadow" and read_json(path).get("outcome") == "complete"}
        require(len(days) >= policy["shadow_days"], "14 successful shadow dates are required before live operation")
    run_id = run_id or "daily-" + instant(now).astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()
    require(re.fullmatch(r"[A-Za-z0-9_-]{1,100}", run_id), "invalid run ID")
    (root / "state").mkdir(exist_ok=True)
    with (root / "state/.learning-cycle.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return run_locked(root, now, run_id, stage_runner, policy)
