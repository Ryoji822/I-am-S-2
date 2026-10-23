"""Daily proposals, adversarial review, atomic acceptance, deterministic reports."""

import fcntl
import json
import re
import subprocess
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from .forecast_contract import ContractViolation, FIELDS, instant, require
from .forecast_learning import apply_plan, append_records, digest, load_state, validate_plan
from .forecast_scoring import resolve
from .learning_model import SOURCE_HOSTS, ModelResponseError, capture_collected, model_config, run_model
from .learning_render import atomic_text, write_failure_snapshot, write_outputs
from .legacy_information import historical_context
from .report_knowledge import collection_index, load_dossiers, merge_dossiers
from .resume_cycle import JUDGMENT_STAGES, checkpoint_document


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
            "record_schema": read_json(root / "schemas/learning-plan.schema.json")["properties"]["records"],
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


def red_rejected(result):
    """A well-formed refusal. Rejection is expected; a broken result is not."""
    return not (result["accepted"] and not result["issues"])


def safe_record_label(record):
    if not isinstance(record, dict):
        return None
    kind, identifier = record.get("type"), record.get("id")
    if kind not in FIELDS or not isinstance(identifier, str):
        return None
    if re.fullmatch(r"[A-Za-z0-9_@.:-]{1,120}", identifier) is None:
        return None
    return f"{kind}:{identifier}"


def exclusion_detail(records):
    """Count plus safe type:id labels. Never copy model text."""
    labels = []
    for record in records:
        label = safe_record_label(record)
        if label:
            labels.append(label)
    shown = ""
    if labels and len(labels) == len(records):
        shown = "：" + "、".join(labels)
    elif labels:
        shown = "。表示できる識別子：" + "、".join(labels)
    return f"（{len(records)}件{shown}）"


def unreviewed_gap(dropped):
    """Developer-authored gap. Never copy arbiter text or unsafe identifiers."""
    return ("裁定が主分析にない記録を含めていたため、その記録は正式判断として公表せず除外しました"
            f"{exclusion_detail(dropped)}。")


def rejection_gap(withheld):
    """Developer-authored gap. Never copy red text or unsafe identifiers."""
    return ("反対点検が変更案を採用しなかったため、その判断は正式判断として公表せず除外しました"
            f"{exclusion_detail(withheld)}。")


def accept_collection(state, result, moment):
    require(result["quality"] in {"complete", "partial"}, "no usable fresh collection")
    validation = {"run_id": "validate-collection", "expected_revision": state["revision"],
                  "quality": result["quality"], "review_complete": False, "records": result["records"]}
    validate_plan(state, validation, instant(moment))


def checkpoint_reusable(stage, result):
    if stage == "collect":
        return result["quality"] in {"complete", "partial"}
    return stage in {"blue", "red", "arbiter"}


def write_stage_checkpoint(run_directory, stage, result, run_id, date, validated_at):
    payload = checkpoint_document(stage, result, run_id=run_id, date=date, validated_at=validated_at)
    atomic_text(run_directory / "checkpoints" / f"{stage}.json",
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def withhold_judgment_checkpoints(run_directory):
    """Drop unpublished judgment bodies after a successful save. Collection stays."""
    for stage in JUDGMENT_STAGES:
        path = Path(run_directory) / "checkpoints" / f"{stage}.json"
        try:
            path.unlink(missing_ok=True)
        except OSError:
            pass


def checkpoint_folder(directory):
    directory = Path(directory)
    direct = directory / "collect.json"
    if direct.is_file():
        return directory
    found = next((path for path in directory.rglob("collect.json") if path.is_file()), None)
    require(found is not None, "collection checkpoint required")
    return found.parent


def accepted_checkpoint_result(document, stage, now, cycle_date):
    require(isinstance(document, dict), "checkpoint must be an object")
    require(document.get("schema_version") == "1.0", "unknown checkpoint")
    require(document.get("publication") == "withheld", "checkpoint is not a publication")
    require(document.get("stage") == stage, "checkpoint stage mismatch")
    require(document.get("date") == cycle_date, "checkpoint date is not the cycle date")
    require(instant(now) <= instant(document["expires_at"]), "checkpoint expired")
    require(isinstance(document.get("result"), dict), "checkpoint result missing")
    return document["result"]


def load_resume_outputs(directory, state, now, policy):
    """Load a contiguous prefix of verified stages. A later corrupt file is ignored."""
    folder = checkpoint_folder(directory)
    cycle_date = instant(now).astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()
    outputs = {}
    for stage in STAGES:
        path = folder / f"{stage}.json"
        if not path.exists():
            break
        try:
            document = read_json(path)
            result = accepted_checkpoint_result(document, stage, now, cycle_date)
            validate_stage(stage, result, policy)
            if stage == "collect":
                accept_collection(state, result, now)
        except (ValueError, KeyError, TypeError, OSError):
            if stage == "collect":
                raise
            break
        outputs[stage] = result
    require("collect" in outputs, "collection checkpoint required")
    return outputs


def usable_resume_directory(root, directory, now):
    root = Path(root)
    policy = read_json(root / "config/learning_policy.json")
    ledger = root / "state/shadow" if policy["mode"] == "shadow" else root
    outputs = load_resume_outputs(directory, load_state(ledger), now, policy)
    return checkpoint_folder(directory), [stage for stage in STAGES if stage in outputs]


def update_plan(state, run_id, outputs, bootstrap, now):
    collected = outputs["collect"]
    require(collected["quality"] in {"complete", "partial"}, "no usable fresh collection")
    blue = outputs["blue"]["records"]
    quarantine = []
    if red_rejected(outputs["red"]):
        # The whole proposal stays unpublished. Arbiter output cannot replace it.
        reviewed = []
        quarantine.append(rejection_gap(blue))
    else:
        accepted = outputs["arbiter"]["records"]
        # Membership is verbatim equality with the red-accepted blue proposal.
        # A stray or edited arbiter record is excluded, not published and not fatal.
        reviewed, dropped = [], []
        for record in accepted:
            (reviewed if record in blue else dropped).append(record)
        if dropped:
            quarantine.append(unreviewed_gap(dropped))
    require(all(record["type"] not in {"evidence", "observation", "resolution"} for record in reviewed), "arbiter cannot rewrite evidence or resolve forecasts")
    proposed = bootstrap + collected["records"] + reviewed
    quality = collected["quality"]
    if quality == "partial":
        require(not reviewed, "partial run cannot change judgments")
        # Definitions are initialized only on a complete run.
        proposed = collected["records"]
    plan = {"run_id": run_id, "expected_revision": state["revision"], "quality": quality,
            "review_complete": True, "records": proposed}
    candidate = validate_plan(state, plan, instant(now))
    proposed = [r for r in proposed if state["records"][r["type"]].get(r["id"]) != r]
    resolutions = [resolve(candidate, q, now) for q in candidate["records"]["question"]]
    resolutions = [r for r in resolutions if r["id"] not in candidate["records"]["resolution"]]
    return {**plan, "records": proposed + resolutions}, quarantine


def execute_stages(root, state, bootstrap, now, runner, policy, run_directory, resumed=None, run_id="checkpoint"):
    resumed = resumed or {}
    prefix = []
    for stage in STAGES:
        if stage not in resumed:
            break
        prefix.append(stage)
    for stage in STAGES:
        if stage in prefix:
            continue
        stale = run_directory / "checkpoints" / f"{stage}.json"
        if stale.exists():
            stale.unlink()
    outputs, usage = {}, {}
    context = current_context(root, append_records(state, bootstrap), now)
    date = instant(now).astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()
    with tempfile.TemporaryDirectory(prefix="ias2-model-") as temporary:
        for stage, prompt in STAGES.items():
            if stage in prefix:
                result = resumed[stage]
                cost = {"status": "resumed_from_checkpoint"}
                validate_stage(stage, result, policy)
                if stage == "collect":
                    accept_collection(state, result, now)
            else:
                stage_now = datetime.now(timezone.utc).isoformat() if runner is run_model else now
                stage_context = {**context, "now": stage_now, "previous_stages": outputs,
                                 "instructions": (root / "prompts" / prompt).read_text(encoding="utf-8")}
                if stage == 'collect':
                    stage_context = {**stage_context, 'dossiers': collection_index(context['dossiers']),
                                     'max_source_documents': 5}
                require(len(json.dumps(stage_context, ensure_ascii=False).encode()) <= 400_000, "model context budget exceeded")
                try:
                    result, cost = runner(stage, stage_context, Path(temporary) / stage, policy)
                except ModelResponseError as error:
                    atomic_text(run_directory / "stage-metadata.json", json.dumps({**usage, stage: error.metadata}, ensure_ascii=False, indent=2) + "\n")
                    raise
                atomic_text(run_directory / "stage-metadata.json", json.dumps({**usage, stage: {**cost, "status": "returned"}}, ensure_ascii=False, indent=2) + "\n")
                validate_stage(stage, result, policy)
                if stage == "collect" and runner is run_model:
                    captured, capture_gaps = capture_collected(result["records"])
                    quality = result['quality']
                    if capture_gaps and quality in {'complete', 'partial'}:
                        quality = 'partial' if captured else 'failed'
                    result = {**result, "records": captured, 'quality': quality,
                              'gaps': result['gaps'] + capture_gaps}
                if stage == "collect" and result['quality'] in {'complete', 'partial'}:
                    moment = datetime.now(timezone.utc).isoformat() if runner is run_model else now
                    accept_collection(state, result, moment)
            outputs, usage = {**outputs, stage: result}, {**usage, stage: cost}
            atomic_text(run_directory / "stage-metadata.json", json.dumps(usage, ensure_ascii=False, indent=2) + "\n")
            if checkpoint_reusable(stage, result):
                validated_at = datetime.now(timezone.utc).isoformat() if runner is run_model else now
                write_stage_checkpoint(run_directory, stage, result, run_id, date, validated_at)
            if stage == 'collect' and result['quality'] == 'partial':
                # Partial evidence cannot authorize any judgment or dossier update.
                reason = '部分収集のため新しい判断を作らず、検証済み資料と欠測だけを保存します。'
                outputs = {**outputs, 'blue': {'records': [], 'reason': reason},
                           'red': {'accepted': True, 'issues': [], 'reason': reason},
                           'arbiter': {'records': [], 'reason': reason}}
                usage = {**usage, **{key: {'status': 'skipped_partial_collection'} for key in ['blue', 'red', 'arbiter']}}
                atomic_text(run_directory / "stage-metadata.json", json.dumps(usage, ensure_ascii=False, indent=2) + "\n")
                break
            if stage == "red" and red_rejected(result):
                # Keep the verified collection. Do not ask the arbiter to publish a refused proposal.
                reason = "反対点検が変更案を採用しなかったため、新しい判断を作らず、検証済み資料だけを保存します。"
                outputs = {**outputs, "arbiter": {"records": [], "reason": reason}}
                usage = {**usage, "arbiter": {"status": "skipped_red_rejection"}}
                atomic_text(run_directory / "stage-metadata.json", json.dumps(usage, ensure_ascii=False, indent=2) + "\n")
                break
            # Only accepted public derivatives are persisted after the entire run validates.
    return outputs, usage


def manifest_base(run_id, date, now, policy, state, root):
    prompts = {key: digest((root / "prompts" / file).read_text(encoding="utf-8")) for key, file in STAGES.items()}
    return {"schema_version": "2.0", "run_id": run_id, "date": date, "started_at": now,
            "mode": policy["mode"], "model": policy["model"], "opencode_version": policy["opencode_version"],
            "code_version": "learning-v3-dossiers", "prompt_hashes": prompts, "revision_before": state["revision"],
            "quality": "failed", "outcome": "failed", "gaps": [], "usage": {},
            "daily_budget": policy["daily_budget"], "monthly_budget": policy["monthly_budget"]}


def resumed_stage_names(usage):
    return [stage for stage in STAGES if isinstance(usage.get(stage), dict)
            and usage[stage].get("status") == "resumed_from_checkpoint"]


def run_locked(root, now, run_id, stage_runner, policy, resume_from=None):
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
            resumed = load_resume_outputs(resume_from, state, now, policy) if resume_from else None
            outputs, usage = execute_stages(root, state, initial_definitions(root, state), now, stage_runner, policy,
                                            directory, resumed=resumed, run_id=run_id)
            finished = datetime.now(timezone.utc).isoformat() if stage_runner is run_model else now
            plan, quarantine_gaps = update_plan(state, run_id, outputs, initial_definitions(root, state), finished)
            candidate = validate_plan(state, plan, instant(finished))
            dossiers = merge_dossiers(load_dossiers(root, finished), candidate, finished)
            gaps = outputs["collect"]["gaps"] + quarantine_gaps
            atomic_text(plan_path, json.dumps({"plan": plan, "usage": usage, "gaps": gaps,
                        "finished_at": finished, "dossiers": dossiers}, ensure_ascii=False, indent=2) + "\n")
        accepted = apply_plan(ledger_root, plan, now=finished)
        accepted = load_state(ledger_root, through_run=run_id)
        manifest = {**manifest, "quality": plan["quality"], "outcome": plan["quality"], "gaps": gaps,
                    "finished_at": finished, "revision_after": accepted["revision"], "usage": usage,
                    "dossier_hash": digest(dossiers)}
        resumed_stages = resumed_stage_names(usage)
        if resumed_stages:
            manifest = {**manifest, "resumed_stages": resumed_stages}
        write_outputs(root, accepted, manifest, plan["records"], dossiers)
        withhold_judgment_checkpoints(directory)
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.SubprocessError) as error:
        manifest = {**manifest, "outcome": "failed", "quality": "failed", "error_type": type(error).__name__,
                    "finished_at": datetime.now(timezone.utc).isoformat() if stage_runner is run_model else now,
                    "gaps": ["収集・反証・検証・保存のいずれかが完了しませんでした。新しい正式判断は公表していません。"],
                    "revision_after": load_state(ledger_root)["revision"]}
        metadata = directory / "stage-metadata.json"
        if isinstance(error, ContractViolation):
            manifest = {**manifest, "validation_failure": str(error)}
        manifest = {**manifest, 'error_location': [
            {'file': Path(frame.filename).name, 'function': frame.name, 'line': frame.lineno}
            for frame in traceback.extract_tb(error.__traceback__)[-4:]]}
        if metadata.exists():
            manifest = {**manifest, "usage": read_json(metadata)}
            resumed_stages = resumed_stage_names(manifest["usage"])
            if resumed_stages:
                manifest = {**manifest, "resumed_stages": resumed_stages}
        try:
            prior_dossiers = merge_dossiers(load_dossiers(root, now), state, now)
            write_failure_snapshot(root, state, manifest, prior_dossiers)
        except (ValueError, KeyError, TypeError, OSError):
            pass  # Preserve the failed manifest even when no baseline can be rendered.
        # The exception message may include provider secrets or private input; do not persist it.
    atomic_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def run_cycle(root, now, run_id=None, stage_runner=run_model, resume_from=None):
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
        return run_locked(root, now, run_id, stage_runner, policy, resume_from=resume_from)
