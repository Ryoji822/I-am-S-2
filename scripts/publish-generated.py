#!/usr/bin/env python3
"""CI-only allowlist publication. Never stages arbitrary workspace changes."""

import argparse
import json
import re
import subprocess
from pathlib import Path

from lib.forecast_contract import require


ROOT = Path(__file__).resolve().parents[1]


def allowed(path):
    patterns = [r"state/runs/[A-Za-z0-9_-]+/(manifest|accepted-plan|stage-metadata)\.json",
                r"(?:state/shadow/)?data/forecast_ledger/transactions/[A-Za-z0-9_-]+\.json",
                r"(?:state/shadow/)?Intelligence/\d{4}-\d{2}-\d{2}\.md",
                r"(?:state/shadow/)?reviews/(weekly|monthly|quarterly|semiannual)/\d{4}-\d{2}-\d{2}\.md",
                r"(?:state/shadow/)?state/scores/latest\.json"]
    return any(re.fullmatch(pattern, path) for pattern in patterns)


def git(*arguments):
    return subprocess.run(["git", "-C", str(ROOT), *arguments], check=True,
                          capture_output=True, text=True).stdout


def publish(run_id):
    require(re.fullmatch(r"[A-Za-z0-9_-]{1,100}", run_id), "invalid run ID")
    manifest = json.loads((ROOT / "state/runs" / run_id / "manifest.json").read_text())
    require(manifest["outcome"] in {"complete", "partial"}, "failed run cannot publish")
    require(not git("diff", "--cached", "--name-only").strip(), "index already contains unrelated changes")
    changed = git("ls-files", "--modified", "--others", "--exclude-standard", "-z").split("\0")
    paths = sorted({path for path in changed if allowed(path) and (ROOT / path).is_file()})
    if not paths:
        return
    git("add", "--", *paths)
    staged = git("diff", "--cached", "--name-only", "-z").split("\0")
    require(all(not path or allowed(path) for path in staged), "non-publication path staged")
    git("commit", "-m", f"chore: record intelligence cycle {run_id}")
    # A concurrent remote update fails safely; no automatic rebase of a ledger.
    git("push", "origin", "HEAD")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    publish(parser.parse_args().run_id)
