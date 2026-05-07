#!/usr/bin/env python3
"""
Evidence Record schema (v1) and validator.

See docs/agentic-intelligence-redesign/EVIDENCE_RECORD_v1.md for the full spec.

Required fields (Phase 1 minimum, set 6):
  evidence_id, source_url, retrieved_at, content_hash, quotable_excerpt, raw_path

CLI:
  python3 -m scripts.lib.evidence_schema validate <path-to-jsonl>
  python3 -m scripts.lib.evidence_schema hash <text>
  python3 -m scripts.lib.evidence_schema mint-id <date> <sequence>
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable

SCHEMA_VERSION = "1.0"

REQUIRED_FIELDS: tuple[str, ...] = (
    "evidence_id",
    "source_url",
    "retrieved_at",
    "content_hash",
    "quotable_excerpt",
    "raw_path",
)

OPTIONAL_FIELDS: tuple[str, ...] = (
    "schema_version",
    "run_date",
    "legacy_info_id",
    "source_title",
    "source_type",
    "retrieval_method",
    "language",
    "summary_for_indexing",
    "kiq_hint",
    "reliability_admiralty",
    "degraded",
    "previous_run_evidence",
    "pending_evidence_id",
)

ALLOWED_FIELDS: frozenset[str] = frozenset(REQUIRED_FIELDS + OPTIONAL_FIELDS)

EVIDENCE_ID_RE = re.compile(r"^EVD-\d{8}-\d{4}$")
HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def compute_hash(content: str) -> str:
    """Return canonical content hash (sha256:hex)."""
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def mint_evidence_id(date: str, sequence: int) -> str:
    """Generate an Evidence ID like EVD-20260507-0001 from date + sequence."""
    if not ISO_DATE_RE.match(date):
        raise ValueError(f"date must be YYYY-MM-DD, got: {date!r}")
    if not (1 <= sequence <= 9999):
        raise ValueError(f"sequence must be 1..9999, got: {sequence}")
    compact = date.replace("-", "")
    return f"EVD-{compact}-{sequence:04d}"


def parse_evidence_id(evidence_id: str) -> tuple[str, int]:
    """Inverse of mint_evidence_id. Returns (date YYYY-MM-DD, sequence)."""
    m = EVIDENCE_ID_RE.match(evidence_id)
    if not m:
        raise ValueError(f"not a valid evidence_id: {evidence_id!r}")
    compact = evidence_id[4:12]
    seq = int(evidence_id[13:17])
    date = f"{compact[0:4]}-{compact[4:6]}-{compact[6:8]}"
    return date, seq


def validate_record(record: dict) -> list[str]:
    """Return a list of validation error messages. Empty list = valid."""
    errors: list[str] = []

    if not isinstance(record, dict):
        return [f"record must be a dict, got: {type(record).__name__}"]

    # Required fields presence + non-empty
    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"missing required field: {field}")
            continue
        value = record[field]
        if value is None or (isinstance(value, str) and value.strip() == ""):
            errors.append(f"required field {field} is empty")

    # Unknown fields (warn, not fail — but we surface as errors so caller can decide)
    for field in record.keys():
        if field not in ALLOWED_FIELDS:
            errors.append(f"unknown field: {field}")

    # Format checks (only if field present)
    eid = record.get("evidence_id")
    if isinstance(eid, str) and not EVIDENCE_ID_RE.match(eid):
        errors.append(f"evidence_id format invalid: {eid!r} (expect EVD-YYYYMMDD-NNNN)")

    chash = record.get("content_hash")
    if isinstance(chash, str) and not HASH_RE.match(chash):
        errors.append(f"content_hash format invalid (expect sha256:<64hex>)")

    rdate = record.get("run_date")
    if isinstance(rdate, str) and not ISO_DATE_RE.match(rdate):
        errors.append(f"run_date format invalid: {rdate!r} (expect YYYY-MM-DD)")

    src_url = record.get("source_url")
    if isinstance(src_url, str) and not re.match(r"^https?://", src_url):
        errors.append(f"source_url must start with http(s)://: {src_url!r}")

    return errors


def iter_jsonl(path: Path) -> Iterable[tuple[int, dict | None, str | None]]:
    """Yield (line_number_1based, parsed_record_or_None, parse_error_or_None)."""
    with path.open("r", encoding="utf-8") as f:
        for i, raw in enumerate(f, start=1):
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            try:
                yield i, json.loads(line), None
            except json.JSONDecodeError as e:
                yield i, None, f"line {i}: JSON parse error: {e.msg} at col {e.colno}"


def validate_jsonl_file(path: Path) -> tuple[int, int, list[str]]:
    """Validate every line of a JSONL file. Returns (total, valid, errors[])."""
    total = 0
    valid = 0
    errors: list[str] = []
    for line_no, record, parse_err in iter_jsonl(path):
        total += 1
        if parse_err:
            errors.append(parse_err)
            continue
        record_errors = validate_record(record)
        if record_errors:
            for e in record_errors:
                errors.append(f"line {line_no}: {e}")
        else:
            valid += 1
    return total, valid, errors


def _cli() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2

    cmd = args[0]
    if cmd == "validate":
        if len(args) < 2:
            print("usage: validate <path-to-jsonl>", file=sys.stderr)
            return 2
        path = Path(args[1])
        if not path.exists():
            print(f"file not found: {path}", file=sys.stderr)
            return 1
        total, valid, errors = validate_jsonl_file(path)
        for e in errors:
            print(f"ERROR {e}", file=sys.stderr)
        print(f"{path}: total={total} valid={valid} errors={len(errors)}")
        return 0 if not errors else 1
    if cmd == "hash":
        if len(args) < 2:
            print("usage: hash <text>", file=sys.stderr)
            return 2
        print(compute_hash(args[1]))
        return 0
    if cmd == "mint-id":
        if len(args) < 3:
            print("usage: mint-id <date> <sequence>", file=sys.stderr)
            return 2
        print(mint_evidence_id(args[1], int(args[2])))
        return 0

    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(_cli())
