#!/usr/bin/env python3
"""Choose whether this GitHub Actions run resumes a failed cycle.

Lookup failures skip. They do not start collection, and they do not become a new
failed run that would hide the original checkpoint.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.learning_cycle import usable_resume_directory
from lib.resume_cycle import (SKIP_LOOKUP, inspect_checkpoint, jst_date, known_saved_dates,
                              resume_action, seed_checkpoints, select_run,
                              separate_checkpoint_artifact)


WORKFLOW_NAME = "Daily Intelligence Learning Cycle"


def emit(decision, checkpoint_dir=""):
    values = {"action": decision.get("action", "skip"), "reason": decision.get("reason", SKIP_LOOKUP),
              "github_run_id": str(decision.get("github_run_id", "")),
              "attempt": "" if decision.get("attempt") in {None, ""} else str(decision.get("attempt")),
              "artifact_name": decision.get("artifact_name", ""),
              "checkpoint_dir": checkpoint_dir}
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            for key, value in values.items():
                handle.write(f"{key}={value}\n")
    print(values["reason"])


def normalize_run(payload):
    return {"github_run_id": str(payload["databaseId"]), "attempt": int(payload["attempt"]),
            "created_at": payload["createdAt"], "conclusion": payload.get("conclusion"),
            "branch": payload.get("headBranch") or "main",
            "workflow_name": payload.get("workflowName") or WORKFLOW_NAME}


def github_json(*arguments):
    completed = subprocess.run(["gh", *arguments], check=True, capture_output=True, text=True)
    return json.loads(completed.stdout)


def fetch_runs(requested_run_id):
    rows = github_json("run", "list", "--workflow", "daily-intelligence.yml", "--branch", "main",
                       "--limit", "40", "--json",
                       "databaseId,conclusion,createdAt,headBranch,attempt,status,workflowName,event")
    runs = [normalize_run(row) for row in rows if row.get("workflowName") in {None, WORKFLOW_NAME}]
    wanted = (requested_run_id or "").strip()
    numeric = wanted[4:].split("-", 1)[0] if wanted.startswith("gha-") else wanted
    if numeric.isdigit() and all(run["github_run_id"] != numeric for run in runs):
        viewed = github_json("run", "view", numeric, "--json",
                             "databaseId,conclusion,createdAt,headBranch,attempt,workflowName")
        if viewed.get("workflowName") in {None, WORKFLOW_NAME}:
            runs.append(normalize_run(viewed))
    return runs


def artifact_state(run_id, attempt):
    repository = os.environ["GITHUB_REPOSITORY"]
    payload = github_json("api", f"repos/{repository}/actions/runs/{run_id}/artifacts")
    name = f"checkpoint-{run_id}-{attempt}"
    matches = [item for item in payload.get("artifacts", []) if item.get("name") == name]
    if not matches:
        return "missing"
    if matches[0].get("expired"):
        return "expired"
    return "ready"


def download_checkpoint(run_id, attempt, destination):
    name = f"checkpoint-{run_id}-{attempt}"
    destination.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", str(run_id), "--name", name, "--dir", str(destination)],
                   check=True)


def decide_from_github():
    event = os.environ.get("EVENT_NAME", "workflow_dispatch")
    requested = os.environ.get("REQUESTED_RUN_ID", "")
    now = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()
    today = jst_date(now)
    if event == "schedule":
        return {"action": "full", "reason": "定期実行は収集から始めます。"}, ""
    root = Path(__file__).resolve().parents[1]
    current = os.environ.get("GITHUB_RUN_ID")
    runs = fetch_runs(requested)
    stored = known_saved_dates(root)
    selected = select_run(today, requested, runs, current)
    if selected["action"] == "skip":
        return selected, ""
    run = selected["run"]
    if today in stored or jst_date(run["created_at"]) != today:
        return resume_action(event=event, today=today, requested=str(run["github_run_id"]),
                             runs=[run], saved_dates=stored, artifact_state="ready",
                             checkpoint_date=today, stages=["collect"], current_run_id=current), ""
    state = artifact_state(run["github_run_id"], run["attempt"])
    if state != "ready":
        return resume_action(event=event, today=today, requested=str(run["github_run_id"]),
                             runs=[run], saved_dates=set(), artifact_state=state,
                             checkpoint_date=None, stages=[], current_run_id=current), ""
    destination = Path(os.environ.get("CHECKPOINT_DOWNLOAD_DIR", root / "resume-checkpoint"))
    download_checkpoint(run["github_run_id"], run["attempt"], destination)
    inspection = inspect_checkpoint(destination, now, today)
    if inspection["state"] != "ready":
        return resume_action(event=event, today=today, requested=str(run["github_run_id"]),
                             runs=[run], saved_dates=set(), artifact_state=inspection["state"],
                             checkpoint_date=inspection.get("date"),
                             stages=inspection.get("stages") or [], current_run_id=current), ""
    try:
        folder, stages = usable_resume_directory(root, inspection["directory"], now)
    except (ValueError, KeyError, TypeError, OSError):
        return resume_action(event=event, today=today, requested=str(run["github_run_id"]),
                             runs=[run], saved_dates=set(), artifact_state="invalid",
                             checkpoint_date=today, stages=[], current_run_id=current), ""
    return resume_action(event=event, today=today, requested=str(run["github_run_id"]),
                         runs=[run], saved_dates=stored, artifact_state="ready",
                         checkpoint_date=today, stages=stages, current_run_id=current), str(folder)


def main(argv):
    if len(argv) > 1 and argv[1] == "seed":
        seed_checkpoints(Path(argv[2]), Path(argv[3]))
        return 0
    if len(argv) > 1 and argv[1] == "export":
        separate_checkpoint_artifact(Path(argv[2]), Path(argv[3]))
        return 0
    try:
        decision, directory = decide_from_github()
    except Exception as error:
        decision, directory = {"action": "skip", "reason": f"{SKIP_LOOKUP}（{type(error).__name__}）"}, ""
    if decision.get("action") == "resume" and not directory:
        decision = {"action": "skip", "reason": f"{SKIP_LOOKUP}（checkpoint_dir）"}
    emit(decision, directory)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
