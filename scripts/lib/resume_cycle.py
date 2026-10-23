"""Resume a failed daily cycle from verified stage checkpoints.

Unpublished judgments stay out of the git publication allowlist. A checkpoint
file is operational input for the next stage, not a public forecast.
"""

import json
import re
import subprocess
from datetime import timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from .forecast_contract import instant


STAGE_ORDER = ("collect", "blue", "red", "arbiter")
JUDGMENT_STAGES = ("blue", "red", "arbiter")
STAGE_FILES = {f"{stage}.json" for stage in STAGE_ORDER}
RETENTION_DAYS = 30
LABELS = {"collect": "収集", "blue": "主分析", "red": "反証", "arbiter": "裁定", "save": "保存"}

SKIP_SAVED = "当日（JST）の調査結果は保存済みです。再開しません。"
SKIP_NO_FAILURE = "当日（JST）の失敗実行がないため、何もしません。収集からはやり直しません。"
SKIP_MISSING = "チェックポイントがないため、収集からはやり直しません。"
SKIP_EXPIRED = "チェックポイントの期限が切れているため、収集からはやり直しません。"
SKIP_INVALID = "チェックポイントを検証できないため、収集からはやり直しません。"
SKIP_WRONG_DAY = "当日（JST）以外の実行からは再開しません。収集からはやり直しません。"
SKIP_WRONG_DATE = "チェックポイントの日付が当日（JST）ではないため、収集からはやり直しません。"
SKIP_NOT_FOUND = "指定した実行が見つからないため、収集からはやり直しません。"
SKIP_NOT_FAILED = "失敗していない実行からは再開しません。収集からはやり直しません。"
SKIP_BAD_ID = "run_id の形式が不正なため、収集からはやり直しません。"
SKIP_LOOKUP = "失敗実行の確認ができないため、収集からはやり直しません。"
FULL_REASON = "定期実行は収集から始めます。"


def jst_date(timestamp):
    return instant(timestamp).astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()


def checkpoint_document(stage, result, *, run_id, date, validated_at):
    """Verified stage output. publication=withheld keeps it out of the daily report."""
    return {"schema_version": "1.0", "stage": stage, "run_id": run_id, "date": date,
            "validated_at": validated_at,
            "expires_at": (instant(validated_at) + timedelta(days=RETENTION_DAYS)).isoformat(),
            "publication": "withheld", "result": result}


def parse_requested_run(text):
    """Accept a GitHub run id or this repo's gha-<id>-<attempt> pipeline id."""
    text = (text or "").strip()
    if not text:
        return None
    pipeline = re.fullmatch(r"gha-(\d+)-(\d+)", text)
    if pipeline:
        return {"github_run_id": pipeline.group(1), "attempt": int(pipeline.group(2))}
    if re.fullmatch(r"\d+", text):
        return {"github_run_id": text, "attempt": None}
    return "invalid"


def select_run(today, requested, runs, current_run_id=None):
    """Pick the failed run to resume. `runs` is newest first."""
    parsed = parse_requested_run(requested)
    if parsed == "invalid":
        return {"action": "skip", "reason": SKIP_BAD_ID}
    visible = [run for run in runs if str(run.get("github_run_id")) != str(current_run_id or "")]
    if parsed is None:
        failures = [run for run in visible if run.get("conclusion") == "failure"
                    and run.get("branch", "main") == "main" and jst_date(run["created_at"]) == today]
        if not failures:
            return {"action": "skip", "reason": SKIP_NO_FAILURE}
        return {"action": "selected", "run": failures[0]}
    match = next((run for run in visible if str(run.get("github_run_id")) == parsed["github_run_id"]), None)
    if match is None:
        return {"action": "skip", "reason": SKIP_NOT_FOUND}
    if match.get("conclusion") != "failure":
        return {"action": "skip", "reason": SKIP_NOT_FAILED}
    if match.get("branch", "main") != "main":
        return {"action": "skip", "reason": SKIP_WRONG_DAY}
    if jst_date(match["created_at"]) != today:
        return {"action": "skip", "reason": SKIP_WRONG_DAY}
    selected = dict(match)
    if parsed["attempt"] is not None:
        selected["attempt"] = parsed["attempt"]
    return {"action": "selected", "run": selected}


def next_stage(stages):
    verified = set(stages or [])
    for stage in STAGE_ORDER:
        if stage not in verified:
            return stage
    return "save"


def resume_reason(run_id, stages):
    done = "、".join(LABELS[stage] for stage in STAGE_ORDER if stage in stages)
    following = next_stage(stages)
    if following == "save":
        return (f"実行 {run_id} のチェックポイント（{done}まで検証済み）から、保存だけを実行します。"
                "収集はやり直しません。")
    return (f"実行 {run_id} のチェックポイント（{done}まで検証済み）から、"
            f"{LABELS[following]}以降だけを実行します。収集はやり直しません。")


def finalize_resume(today, saved_dates, run, artifact_state, checkpoint_date, stages):
    if today in set(saved_dates or []):
        return {"action": "skip", "reason": SKIP_SAVED}
    if jst_date(run["created_at"]) != today:
        return {"action": "skip", "reason": SKIP_WRONG_DAY}
    if artifact_state == "missing":
        return {"action": "skip", "reason": SKIP_MISSING}
    if artifact_state == "expired":
        return {"action": "skip", "reason": SKIP_EXPIRED}
    if artifact_state == "wrong_date" or (checkpoint_date and checkpoint_date != today):
        return {"action": "skip", "reason": SKIP_WRONG_DATE}
    if artifact_state != "ready":
        return {"action": "skip", "reason": SKIP_INVALID}
    if "collect" not in (stages or []):
        return {"action": "skip", "reason": SKIP_MISSING}
    return {"action": "resume", "reason": resume_reason(run["github_run_id"], stages),
            "github_run_id": str(run["github_run_id"]), "attempt": int(run["attempt"]),
            "artifact_name": f"checkpoint-{run['github_run_id']}-{run['attempt']}",
            "stages": [stage for stage in STAGE_ORDER if stage in stages]}


def resume_action(*, event, today, requested, runs, saved_dates, artifact_state="ready",
                  checkpoint_date=None, stages=None, current_run_id=None):
    """Pure decision used by push and workflow_dispatch. Schedule never resumes."""
    if event == "schedule":
        return {"action": "full", "reason": FULL_REASON}
    selected = select_run(today, requested, runs, current_run_id)
    if selected["action"] == "skip":
        return selected
    verified = list(STAGE_ORDER[:1] if stages is None else stages)
    observed_date = today if checkpoint_date is None else checkpoint_date
    return finalize_resume(today, saved_dates, selected["run"], artifact_state, observed_date, verified)


def saved_dates(root):
    """Dates whose investigation was stored. A report file alone is not success."""
    found = set()
    for path in (Path(root) / "state/runs").glob("*/manifest.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("outcome") in {"complete", "partial"} and data.get("date"):
            found.add(data["date"])
    return found


def remote_saved_dates(root):
    """Read origin/main without checking it out.

    A queued resume checks out the commit that triggered it. A previous resume may
    already have pushed today's results onto main after that commit.
    """
    root = Path(root)
    try:
        subprocess.run(["git", "-C", str(root), "fetch", "origin", "main", "--depth=1"],
                       check=True, capture_output=True, text=True)
        listing = subprocess.run(["git", "-C", str(root), "ls-tree", "-r", "--name-only", "origin/main", "state/runs"],
                                 check=True, capture_output=True, text=True)
    except (subprocess.CalledProcessError, OSError):
        return set()
    found = set()
    for path in listing.stdout.splitlines():
        if not path.endswith("/manifest.json"):
            continue
        try:
            shown = subprocess.run(["git", "-C", str(root), "show", f"origin/main:{path}"],
                                   check=True, capture_output=True, text=True)
            data = json.loads(shown.stdout)
        except (subprocess.CalledProcessError, OSError, json.JSONDecodeError):
            continue
        if data.get("outcome") in {"complete", "partial"} and data.get("date"):
            found.add(data["date"])
    return found


def known_saved_dates(root):
    return saved_dates(root) | remote_saved_dates(root)


def inspect_checkpoint(directory, now, today):
    directory = Path(directory)
    found = directory / "collect.json"
    if not found.is_file():
        nested = next((path for path in directory.rglob("collect.json") if path.is_file()), None)
        found = nested
    if found is None:
        return {"state": "missing", "date": None, "stages": [], "directory": None}
    folder = found.parent
    try:
        document = json.loads(found.read_text(encoding="utf-8"))
        observed = document.get("date")
        if observed != today:
            return {"state": "wrong_date", "date": observed, "stages": [], "directory": folder}
        if instant(now) > instant(document["expires_at"]):
            return {"state": "expired", "date": observed, "stages": [], "directory": folder}
    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError):
        return {"state": "invalid", "date": None, "stages": [], "directory": folder}
    stages = []
    for stage in STAGE_ORDER:
        if not (folder / f"{stage}.json").is_file():
            break
        stages.append(stage)
    return {"state": "ready", "date": document["date"], "stages": stages, "directory": folder}


def seed_checkpoints(source, destination):
    """Copy a downloaded checkpoint into the new run directory before the model runs."""
    source, destination = Path(source), Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    seeded = []
    for name in [f"{stage}.json" for stage in STAGE_ORDER]:
        match = next((path for path in source.rglob(name) if path.is_file()), None)
        if match is None:
            continue
        destination.joinpath(name).write_text(match.read_text(encoding="utf-8"), encoding="utf-8")
        seeded.append(name)
    return seeded


def separate_checkpoint_artifact(root, destination):
    """Copy checkpoints for the resume artifact, then drop judgment bodies from run records.

    The learning-* artifact uploads state/runs. Blue, red, and arbiter results are not
    official publications, so they must not remain on that path.
    """
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    runs = Path(root) / "state/runs"
    copied = []
    if runs.is_dir():
        for path in sorted(runs.glob("*/checkpoints/*.json")):
            if path.name not in STAGE_FILES:
                continue
            destination.joinpath(path.name).write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
            copied.append(path.name)
        for path in list(runs.glob("*/checkpoints/*.json")):
            if path.name in {f"{stage}.json" for stage in JUDGMENT_STAGES}:
                path.unlink()
    return copied
