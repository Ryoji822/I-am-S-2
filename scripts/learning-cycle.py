#!/usr/bin/env python3
"""Public CLI. Network/model work is confined to the explicit run command."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from lib.forecast_contract import instant, require
from lib.forecast_learning import apply_plan, load_state, resolve, scorecard, validate_plan
from lib.learning_cycle import read_json, run_cycle
from lib.report_knowledge import load_dossiers, merge_dossiers


ROOT = Path(__file__).resolve().parents[1]


def command_line():
    parser = argparse.ArgumentParser(description="仮説・実績・採点を残す")
    parser.add_argument("command", choices=["run", "status", "validate", "resolve", "score", "apply"])
    parser.add_argument("--date", help="状態を読む日付。runは今日だけ")
    parser.add_argument("--run-id", help="同じIDは重複しない。失敗の再試行は別ID")
    parser.add_argument("--plan", type=Path, help="applyで検証する変更案")
    return parser.parse_args()


def selected_root():
    return ROOT / "state/shadow" if read_json(ROOT / "config/learning_policy.json")["mode"] == "shadow" else ROOT


def validate_repository():
    policy = read_json(ROOT / "config/learning_policy.json")
    require(policy["automatic_calibration"] is False, "automatic calibration requires held-out validation")
    require(policy["public_only"] is True, "this is a public repository")
    require(read_json(ROOT / "config/scenarios.json")["probability_normalization"] is False, "worlds overlap")
    require(len(read_json(ROOT / "config/missions.json")["missions"]) == 3, "three missions required")
    definitions = read_json(ROOT / "config/hypotheses.json")["hypotheses"]
    require(len({r["id"] for r in definitions}) == len(definitions), "duplicate hypothesis IDs")
    for root in [ROOT, ROOT / "state/shadow"]:
        state = load_state(root)
        now = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()
        merge_dossiers(load_dossiers(ROOT, now), state, now)
    for path in (ROOT / "state/runs").glob("*/manifest.json"):
        require(read_json(path)["outcome"] in {"complete", "partial", "failed"}, "unknown outcome")
    return {"valid": True, "hypotheses": len(definitions), "mode": policy["mode"]}


def main():
    args = command_line()
    now = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()
    date = args.date or now[:10]
    require(datetime.fromisoformat(date).date().isoformat() == date, "date must be YYYY-MM-DD")
    root = selected_root()
    if args.command == "run":
        require(date == now[:10], "past dates cannot issue live forecasts; use retrospective reports")
        result = run_cycle(ROOT, now, args.run_id)
    elif args.command == "validate":
        result = validate_repository()
    elif args.command == "status":
        paths = sorted((ROOT / "state/runs").glob("*/manifest.json"))
        result = [read_json(p) for p in paths if read_json(p)["date"] == date]
    elif args.command == "score":
        result = scorecard(load_state(root), now)
    elif args.command == "resolve":
        state = load_state(root)
        records = [resolve(state, identifier, now) for identifier in state["records"]["question"]]
        result = {"run_id": args.run_id or "resolve-" + now[:19].replace(":", "-"),
                  "expected_revision": state["revision"], "quality": "complete",
                  "review_complete": True, "records": records}
    else:
        require(args.plan is not None, "--plan is required")
        plan = read_json(args.plan)
        candidate = validate_plan(load_state(root), plan, instant(now))
        merge_dossiers(load_dossiers(ROOT, now), candidate, now)
        result = {"revision": apply_plan(root, plan, now)["revision"]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if isinstance(result, dict) and result.get("outcome") == "failed" else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(2)
