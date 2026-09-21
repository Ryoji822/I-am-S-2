"""An append-only, hash-chained ledger with one atomic file per accepted run."""

import copy
import fcntl
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from .forecast_contract import KINDS, instant, require, validate_record
from .forecast_scoring import resolve, scorecard


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def ledger_directory(root):
    return Path(root) / "data" / "forecast_ledger" / "transactions"


def empty_state():
    return {"revision": "0", "sequence": 0, "records": {kind: {} for kind in KINDS}, "runs": {}}


def append_records(state, records):
    grouped = {kind: dict(items) for kind, items in state["records"].items()}
    for record in records:
        kind, identifier = record["type"], record["id"]
        old = grouped[kind].get(identifier)
        require(old is None or old == record, "immutable record changed")
        grouped[kind] = {**grouped[kind], identifier: copy.deepcopy(record)}
    return {**state, "records": grouped}


def load_state(root, through_run=None):
    state = empty_state()
    for path in sorted(ledger_directory(root).glob("*.json")):
        transaction = json.loads(path.read_text(encoding="utf-8"))
        payload = transaction["payload"]
        require(transaction["hash"] == digest(payload), "ledger hash mismatch")
        require(payload["previous_revision"] == state["revision"], "ledger chain broken")
        require(payload["sequence"] == state["sequence"] + 1, "ledger sequence broken")
        run_id = payload["plan"]["run_id"]
        require(run_id not in state["runs"], "duplicate committed run")
        state = append_records(state, payload["plan"]["records"])
        state = {**state, "revision": transaction["hash"], "sequence": payload["sequence"],
                 "runs": {**state["runs"], run_id: payload["plan_hash"]}}
        if run_id == through_run:
            return state
    require(through_run is None, "requested run not found")
    return state


def check_resolution(record, state):
    expected = resolve(state, record["question_id"], record["resolved_at"])
    if record["status"] == "invalidated":
        require(bool(record["rule_reason"]) and record["outcome"] is None, "invalidation needs a reason and no outcome")
        require(record["supersedes"] == expected["supersedes"] or record["supersedes"] == expected["id"], "invalidation must reference previous decision")
        return
    require(record == expected, "resolution must match deterministic calculation")


def validate_plan(state, plan, now):
    require(set(plan) == {"run_id", "expected_revision", "quality", "review_complete", "records"}, "invalid plan fields")
    require(isinstance(plan["run_id"], str) and re.fullmatch(r"[A-Za-z0-9_-]{1,100}", plan["run_id"]), "invalid run ID")
    require(plan["quality"] in {"complete", "partial"}, "failed or stale run cannot commit")
    require(type(plan["review_complete"]) is bool, "review status must be boolean")
    require(isinstance(plan["records"], list), "records must be a list")
    require(plan["expected_revision"] == state["revision"], "stale update plan")
    candidate = copy.deepcopy(state)
    for record in plan["records"]:
        require(isinstance(record, dict), "record must be an object")
        kind, identifier = record.get("type"), record.get("id")
        old = candidate["records"].get(kind, {}).get(identifier)
        if old is not None:
            require(old == record, "immutable record changed")
            continue
        if not plan["review_complete"]:
            require(kind in {"evidence", "observation", "metric"}, "unreviewed judgment cannot commit")
        if plan["quality"] == "partial":
            require(kind in {"evidence", "observation", "metric", "resolution"}, "partial run cannot issue new judgments")
        validate_record(record, candidate["records"], now)
        if kind == "resolution":
            check_resolution(record, candidate)
        candidate = append_records(candidate, [record])
    return candidate


def write_transaction(directory, name, transaction):
    descriptor, temporary = tempfile.mkstemp(prefix=".pending-", dir=directory)
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(canonical(transaction) + b"\n")
            output.flush()
            os.fsync(output.fileno())
        os.link(temporary, directory / name)
        directory_fd = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        os.unlink(temporary)


def apply_plan(root, plan, now=None):
    now = now or datetime.now(timezone.utc).isoformat()
    directory = ledger_directory(root)
    directory.mkdir(parents=True, exist_ok=True)
    with (directory.parent / ".write.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state = load_state(root)
        plan_hash = digest(plan)
        if plan.get("run_id") in state["runs"]:
            require(state["runs"][plan["run_id"]] == plan_hash, "run ID reused for different content")
            return state
        validate_plan(state, plan, instant(now))
        payload = {"sequence": state["sequence"] + 1, "previous_revision": state["revision"],
                   "committed_at": now, "plan_hash": plan_hash, "plan": copy.deepcopy(plan)}
        transaction = {"payload": payload, "hash": digest(payload)}
        name = f"{payload['sequence']:08d}-{plan['run_id']}.json"
        write_transaction(directory, name, transaction)
        return load_state(root)
