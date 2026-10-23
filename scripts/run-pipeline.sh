#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARGS=(run)
if [[ -n "${PIPELINE_DATE:-}" ]]; then ARGS+=(--date "$PIPELINE_DATE"); fi
if [[ -n "${PIPELINE_RUN_ID:-}" ]]; then ARGS+=(--run-id "$PIPELINE_RUN_ID"); fi
if [[ -n "${REQUIRE_RESUME:-}" && -z "${RESUME_CHECKPOINT_DIR:-}" ]]; then
  echo "再開なのにチェックポイントがありません。収集からはやり直しません。" >&2
  exit 2
fi
if [[ -n "${RESUME_CHECKPOINT_DIR:-}" ]]; then
  if [[ -z "${PIPELINE_RUN_ID:-}" ]]; then
    echo "PIPELINE_RUN_ID is required when resuming" >&2
    exit 2
  fi
  python3 "$ROOT/scripts/prepare-resume.py" seed "$RESUME_CHECKPOINT_DIR" "$ROOT/state/runs/$PIPELINE_RUN_ID/checkpoints"
  ARGS+=(--resume-from "$RESUME_CHECKPOINT_DIR")
fi
exec python3 "$ROOT/scripts/learning-cycle.py" "${ARGS[@]}"
