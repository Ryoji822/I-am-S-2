#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARGS=(run)
if [[ -n "${PIPELINE_DATE:-}" ]]; then ARGS+=(--date "$PIPELINE_DATE"); fi
if [[ -n "${PIPELINE_RUN_ID:-}" ]]; then ARGS+=(--run-id "$PIPELINE_RUN_ID"); fi
exec python3 "$ROOT/scripts/learning-cycle.py" "${ARGS[@]}"
