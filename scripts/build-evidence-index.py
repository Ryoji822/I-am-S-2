#!/usr/bin/env python3
"""
Build the Evidence Index for a given run date.

Reads:
  - Information/<DATE>/collected-raw.md         (INFO-NNN sections written by Phase 1)
  - Information/raw/<DATE>/x_posts.jsonl        (optional, written by fetch-x-posts.py)

Writes:
  - Information/raw/<DATE>/firecrawl.jsonl     (Evidence Records derived from INFO-NNN)
  - Information/raw/<DATE>/x_posts.jsonl       (rewritten in-place: assigns Evidence IDs)
  - Information/raw/<DATE>/_meta.json          (run metadata)
  - Information/processed/<DATE>.jsonl         (merged + de-duplicated by content_hash)
  - Information/evidence_index.json            (updated index, append-or-replace by EVD ID)

Usage:
  python3 scripts/build-evidence-index.py [--date YYYY-MM-DD] [--dry-run] [--repo-root PATH]

Behavior:
  - Idempotent: re-running on the same date overwrites that day's entries cleanly.
  - Single-writer: only this script mints EVD-* IDs. fetch-x-posts.py writes
    `pending_evidence_id: null` placeholders that this script later fills in.
  - On parse errors in collected-raw.md, the offending block is skipped (logged) but
    other INFO-NNN sections are still processed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT_DEFAULT = THIS_DIR.parent

sys.path.insert(0, str(THIS_DIR))
from lib.evidence_schema import (  # noqa: E402
    SCHEMA_VERSION,
    compute_hash,
    mint_evidence_id,
    validate_record,
)

JST = timezone(timedelta(hours=9))

# Regex to split collected-raw.md into INFO-NNN blocks.
INFO_HEADER_RE = re.compile(r"^###\s+INFO-(\d+)\s*$", re.MULTILINE)


def today_jst() -> str:
    return datetime.now(JST).strftime("%Y-%m-%d")


def now_iso_jst() -> str:
    return datetime.now(JST).isoformat(timespec="seconds")


def parse_collected_raw(md_path: Path) -> list[dict]:
    """Parse collected-raw.md INFO-NNN sections into a list of intermediate dicts.

    Each dict has the fields needed to build an Evidence Record:
      legacy_info_id, source_url, source_title, source_type_hint,
      retrieval_method, language, summary_for_indexing, kiq_hint,
      reliability_admiralty, raw_text_block (the original markdown of this section).
    Sections missing 引用URL are skipped (cannot anchor without a source_url).
    """
    text = md_path.read_text(encoding="utf-8")
    blocks: list[dict] = []

    headers = list(INFO_HEADER_RE.finditer(text))
    for i, m in enumerate(headers):
        info_num = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[start:end].strip("\n")

        url = _extract_field(body, "引用URL") or _extract_field(body, "URL")
        if not url or not url.lower().startswith(("http://", "https://")):
            print(
                f"  [skip] INFO-{info_num}: no usable 引用URL (got {url!r})",
                file=sys.stderr,
            )
            continue

        title = _extract_field(body, "タイトル") or ""
        source_label = _extract_field(body, "ソース") or ""
        published = _extract_field(body, "公開日") or ""
        adm = _extract_field(body, "信頼性コード") or ""
        kiqs_raw = _extract_field(body, "関連KIQ") or ""
        summary = _extract_field(body, "要約") or ""

        kiq_hint = [
            k.strip()
            for k in re.split(r"[、,]", kiqs_raw)
            if k.strip() and k.strip().upper().startswith(("KIQ", "PIR"))
        ]

        section_md = f"### INFO-{info_num}\n{body}"

        blocks.append(
            {
                "legacy_info_id": f"INFO-{info_num}",
                "source_url": url.strip(),
                "source_title": title.strip(),
                "source_label": source_label.strip(),
                "source_type": _classify_source_type(source_label),
                "published_hint": published.strip(),
                "retrieval_method": "firecrawl",
                "language": _detect_language(title + " " + summary),
                "summary_for_indexing": summary.strip()[:500],
                "kiq_hint": kiq_hint,
                "reliability_admiralty": adm.strip(),
                "raw_text_block": section_md,
                "quotable_excerpt": _make_excerpt(summary, title),
            }
        )

    return blocks


def _extract_field(body: str, label: str) -> str | None:
    """Pull a `- **<label>:** value` style line. Returns trimmed value or None."""
    pattern = re.compile(
        r"^[-\*]\s*\*\*" + re.escape(label) + r"\s*[:：]\*\*\s*(.+?)\s*$",
        re.MULTILINE,
    )
    m = pattern.search(body)
    return m.group(1) if m else None


def _classify_source_type(source_label: str) -> str:
    s = source_label.lower()
    if "公式" in source_label or "official" in s or "blog" in s:
        return "official"
    if "github" in s:
        return "github"
    if "twitter" in s or "x.com" in s or "x posts" in s:
        return "social"
    if "regulator" in s or "sec" in s or "ftc" in s or "規制" in source_label:
        return "regulatory"
    if "research" in s or "arxiv" in s or "論文" in source_label:
        return "research"
    if source_label:
        return "news"
    return "other"


def _detect_language(text: str) -> str:
    if re.search(r"[぀-ヿ一-鿿]", text):
        return "ja"
    return "en"


def _make_excerpt(summary: str, title: str) -> str:
    base = (summary or title or "").strip()
    if not base:
        return ""
    return base[:240]


def build_record_from_info_block(
    block: dict, evidence_id: str, run_date: str, retrieved_at: str, raw_path_hint: str
) -> dict:
    record = {
        "evidence_id": evidence_id,
        "schema_version": SCHEMA_VERSION,
        "run_date": run_date,
        "legacy_info_id": block["legacy_info_id"],
        "source_url": block["source_url"],
        "source_title": block["source_title"],
        "source_type": block["source_type"],
        "retrieved_at": retrieved_at,
        "retrieval_method": block["retrieval_method"],
        "content_hash": compute_hash(block["raw_text_block"]),
        "language": block["language"],
        "raw_path": raw_path_hint,
        "quotable_excerpt": block["quotable_excerpt"] or block["source_title"][:240] or block["source_url"],
        "summary_for_indexing": block["summary_for_indexing"],
        "kiq_hint": block["kiq_hint"],
        "reliability_admiralty": block["reliability_admiralty"],
        "degraded": False,
    }
    return record


def assign_x_posts_evidence_ids(
    pending_records: list[dict], next_seq: int, run_date: str, raw_path_hint: str
) -> tuple[list[dict], int]:
    """Take x_posts.jsonl rows with pending_evidence_id=null and fill in EVD-* IDs."""
    out: list[dict] = []
    seq = next_seq
    for r in pending_records:
        if r.get("evidence_id"):
            out.append(r)
            continue
        if r.get("pending_evidence_id") is None and "evidence_id" not in r:
            evidence_id = mint_evidence_id(run_date, seq)
            seq += 1
            new = dict(r)
            new["evidence_id"] = evidence_id
            new["schema_version"] = new.get("schema_version", SCHEMA_VERSION)
            new["raw_path"] = new.get("raw_path", raw_path_hint)
            new.pop("pending_evidence_id", None)
            out.append(new)
        else:
            out.append(r)
    return out, seq


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for i, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"  [warn] {path}:{i} JSON parse error: {e}", file=sys.stderr)
    return out


def write_jsonl(path: Path, records: list[dict], dry_run: bool) -> None:
    if dry_run:
        print(f"  [dry-run] would write {len(records)} records to {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"  wrote {len(records)} records to {path}")


def update_evidence_index(
    index_path: Path, records: list[dict], run_date: str, dry_run: bool
) -> None:
    if dry_run:
        print(f"  [dry-run] would update {index_path} with {len(records)} entries for {run_date}")
        return
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  [warn] {index_path} unreadable, recreating", file=sys.stderr)
            index = {}
    else:
        index = {}

    index.setdefault("schema_version", SCHEMA_VERSION)
    index["last_updated"] = now_iso_jst()
    index.setdefault("evidence", {})

    # Drop existing entries for this run_date so re-runs are clean.
    index["evidence"] = {
        k: v for k, v in index["evidence"].items() if v.get("run_date") != run_date
    }

    for r in records:
        eid = r.get("evidence_id")
        if not eid:
            continue
        index["evidence"][eid] = {
            "run_date": r.get("run_date", run_date),
            "url": r.get("source_url", ""),
            "hash": r.get("content_hash", ""),
            "raw_path": r.get("raw_path", ""),
            "legacy_info_id": r.get("legacy_info_id"),
        }

    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"  updated index: {index_path} (+{len(records)} for {run_date})")


def deduplicate_by_hash(records: list[dict]) -> tuple[list[dict], int]:
    seen: dict[str, str] = {}
    out: list[dict] = []
    dup_count = 0
    for r in records:
        h = r.get("content_hash")
        if not h:
            out.append(r)
            continue
        if h in seen:
            dup_count += 1
            continue
        seen[h] = r["evidence_id"]
        out.append(r)
    return out, dup_count


def main() -> int:
    ap = argparse.ArgumentParser(description="Build Evidence Index for a run date.")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today JST)")
    ap.add_argument("--repo-root", default=str(REPO_ROOT_DEFAULT))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    run_date = args.date or today_jst()

    md_path = repo_root / "Information" / run_date / "collected-raw.md"
    raw_dir = repo_root / "Information" / "raw" / run_date
    firecrawl_jsonl = raw_dir / "firecrawl.jsonl"
    xposts_jsonl = raw_dir / "x_posts.jsonl"
    meta_json = raw_dir / "_meta.json"
    processed_jsonl = repo_root / "Information" / "processed" / f"{run_date}.jsonl"
    index_json = repo_root / "Information" / "evidence_index.json"

    print(f"[build-evidence-index] run_date={run_date} dry_run={args.dry_run}")

    if not md_path.exists():
        print(f"  collected-raw.md not found at {md_path} — skipping firecrawl parse")
        info_blocks: list[dict] = []
    else:
        info_blocks = parse_collected_raw(md_path)
        print(f"  parsed {len(info_blocks)} INFO-NNN blocks from {md_path}")

    retrieved_at = now_iso_jst()
    raw_path_hint = str(firecrawl_jsonl.relative_to(repo_root))

    firecrawl_records: list[dict] = []
    for idx, block in enumerate(info_blocks, start=1):
        evidence_id = mint_evidence_id(run_date, idx)
        firecrawl_records.append(
            build_record_from_info_block(
                block,
                evidence_id=evidence_id,
                run_date=run_date,
                retrieved_at=retrieved_at,
                raw_path_hint=raw_path_hint,
            )
        )

    pending_x = read_jsonl(xposts_jsonl)
    next_seq = len(firecrawl_records) + 1
    x_path_hint = str(xposts_jsonl.relative_to(repo_root))
    x_records, next_seq = assign_x_posts_evidence_ids(
        pending_x, next_seq=next_seq, run_date=run_date, raw_path_hint=x_path_hint
    )
    print(f"  firecrawl evidence: {len(firecrawl_records)}, x_posts evidence: {len(x_records)}")

    # Validate
    schema_failures = 0
    for r in firecrawl_records + x_records:
        errs = validate_record(r)
        if errs:
            schema_failures += 1
            print(f"  [schema] {r.get('evidence_id', '?')}: {errs[0]}", file=sys.stderr)

    write_jsonl(firecrawl_jsonl, firecrawl_records, args.dry_run)
    write_jsonl(xposts_jsonl, x_records, args.dry_run)

    merged = firecrawl_records + x_records
    deduped, dup_count = deduplicate_by_hash(merged)
    if dup_count:
        print(f"  removed {dup_count} duplicate(s) by content_hash")
    write_jsonl(processed_jsonl, deduped, args.dry_run)

    update_evidence_index(index_json, deduped, run_date, args.dry_run)

    if not args.dry_run:
        meta = {
            "schema_version": SCHEMA_VERSION,
            "run_date": run_date,
            "built_at": retrieved_at,
            "firecrawl_count": len(firecrawl_records),
            "x_posts_count": len(x_records),
            "merged_count": len(merged),
            "deduped_count": len(deduped),
            "duplicate_count": dup_count,
            "schema_failures": schema_failures,
        }
        meta_json.parent.mkdir(parents=True, exist_ok=True)
        meta_json.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"  wrote meta to {meta_json}")

    print(
        f"[build-evidence-index] done: total={len(merged)} deduped={len(deduped)} "
        f"dups={dup_count} schema_failures={schema_failures}"
    )
    return 0 if schema_failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
