#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# I-am-S-2 Output Quality Validator
# Checks that pipeline output meets minimum quality requirements
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DATE="${1:-$(TZ=Asia/Tokyo date +%Y-%m-%d)}"

PASS=0
FAIL=0
WARN=0

check_pass() { echo "  ✅ $1"; PASS=$((PASS + 1)); }
check_fail() { echo "  ❌ $1"; FAIL=$((FAIL + 1)); }
check_warn() { echo "  ⚠️  $1"; WARN=$((WARN + 1)); }

echo "=== I-am-S-2 Output Validator ==="
echo "Date: $DATE"
echo ""

cd "$PROJECT_DIR"

# =============================================================================
# 1. File existence checks
# =============================================================================

echo "--- File Existence ---"

if [[ -f "Information/$DATE/collected-raw.md" ]]; then
  check_pass "collected-raw.md exists"
else
  check_fail "collected-raw.md MISSING"
fi

if [[ -f "Information/$DATE/processed.md" ]]; then
  check_pass "processed.md exists"
else
  check_fail "processed.md MISSING"
fi

if [[ -f "state/red-team-$DATE.md" ]]; then
  check_pass "red-team report exists"
else
  check_fail "red-team report MISSING"
fi

if [[ -f "state/arbiter-$DATE.md" ]]; then
  check_pass "arbiter report exists"
else
  check_fail "arbiter report MISSING"
fi

if [[ -f "Intelligence/$DATE.md" ]]; then
  check_pass "daily intelligence report exists"
else
  check_fail "daily intelligence report MISSING"
fi

# =============================================================================
# 2. Content quality checks - collected-raw.md
# =============================================================================

echo ""
echo "--- Collection Quality ---"

COLLECTED="Information/$DATE/collected-raw.md"
if [[ -f "$COLLECTED" ]]; then
  # Check for INFO entries
  INFO_COUNT=$(grep -c "^### INFO-" "$COLLECTED" 2>/dev/null || echo "0")
  if [[ "$INFO_COUNT" -ge 5 ]]; then
    check_pass "Collection has $INFO_COUNT entries (minimum: 5)"
  elif [[ "$INFO_COUNT" -ge 1 ]]; then
    check_warn "Collection has only $INFO_COUNT entries (expected: 5+)"
  else
    check_fail "Collection has 0 INFO entries"
  fi

  # Check for reliability codes
  RELIABILITY_COUNT=$(grep -c "信頼性コード" "$COLLECTED" 2>/dev/null || echo "0")
  if [[ "$RELIABILITY_COUNT" -ge 1 ]]; then
    check_pass "Admiralty codes present ($RELIABILITY_COUNT entries)"
  else
    check_warn "No Admiralty codes found in collection"
  fi

  # Check for DEGRADED flag
  if grep -q "DEGRADED" "$COLLECTED" 2>/dev/null; then
    check_warn "Collection is DEGRADED"
  fi
fi

# =============================================================================
# 3. Content quality checks - Intelligence report
# =============================================================================

echo ""
echo "--- Report Quality ---"

REPORT="Intelligence/$DATE.md"
if [[ -f "$REPORT" ]]; then
  # Check for executive summary (accepts both old and new heading)
  if grep -q "エグゼクティブ・サマリー\|今日のポイント" "$REPORT" 2>/dev/null; then
    check_pass "Executive summary present"
  else
    check_fail "Executive summary MISSING"
  fi

  # Check for ACH section
  if grep -q "ACH\|仮説" "$REPORT" 2>/dev/null; then
    check_pass "ACH/hypothesis section present"
  else
    check_warn "ACH section not found"
  fi

  # Check for scenario section
  if grep -q "シナリオ" "$REPORT" 2>/dev/null; then
    check_pass "Scenario section present"
  else
    check_warn "Scenario section not found"
  fi

  # Check for I&W section
  if grep -q "I&W\|兆候\|警告\|指標" "$REPORT" 2>/dev/null; then
    check_pass "I&W section present"
  else
    check_warn "I&W section not found"
  fi

  # Check for confidence levels
  if grep -q "確度" "$REPORT" 2>/dev/null; then
    check_pass "Confidence levels present"
  else
    check_fail "Confidence levels MISSING (ICD 203 requirement)"
  fi

  # Check for fact/assessment separation
  if grep -q "事実\|Fact" "$REPORT" 2>/dev/null && grep -q "判断\|Assessment" "$REPORT" 2>/dev/null; then
    check_pass "Fact/Assessment separation present"
  else
    check_warn "Fact/Assessment separation not clearly marked"
  fi

  # Check for action recommendations
  if grep -q "行動提言\|推奨\|アクション" "$REPORT" 2>/dev/null; then
    check_pass "Action recommendations present"
  else
    check_warn "Action recommendations not found"
  fi

  # Check report is in Japanese
  if grep -q "[ぁ-ん]" "$REPORT" 2>/dev/null; then
    check_pass "Report is in Japanese"
  else
    check_warn "Report may not be in Japanese"
  fi

  # Check for DEGRADED flag
  if grep -q "DEGRADED" "$REPORT" 2>/dev/null; then
    check_warn "Report is DEGRADED"
  fi

  # Check for unlinked IND-XXX references (should be [IND-XXX](../config/indicators.json))
  BARE_IND=$( { grep -oP '(?<!\[)IND-\d{3}(?!\]\()' "$REPORT" 2>/dev/null || true; } | wc -l | tr -d ' ')
  if [[ "$BARE_IND" -gt 0 ]]; then
    check_warn "$BARE_IND bare IND-XXX reference(s) without Markdown link in report"
  fi

  # Check for unlinked INFO-XXX references (should be [INFO-XXX](...))
  BARE_INFO=$( { grep -oP '(?<!\[)INFO-\d{3}(?!\]\()' "$REPORT" 2>/dev/null || true; } | wc -l | tr -d ' ')
  if [[ "$BARE_INFO" -gt 0 ]]; then
    check_warn "$BARE_INFO bare INFO-XXX reference(s) without Markdown link in report"
  fi

  # Check file size (should be meaningful content)
  REPORT_SIZE=$(wc -c < "$REPORT")
  if [[ "$REPORT_SIZE" -gt 1000 ]]; then
    check_pass "Report size: ${REPORT_SIZE} bytes (substantive)"
  elif [[ "$REPORT_SIZE" -gt 200 ]]; then
    check_warn "Report size: ${REPORT_SIZE} bytes (may be too short)"
  else
    check_fail "Report size: ${REPORT_SIZE} bytes (likely stub/empty)"
  fi
fi

# =============================================================================
# 3.5. Link quality checks - static_intelligence
# =============================================================================

echo ""
echo "--- Static Intelligence Link Quality ---"

for si_file in static_intelligence/*.md; do
  if [[ -f "$si_file" ]]; then
    SI_BARE_IND=$( { grep -oP '(?<!\[)IND-\d{3}(?!\]\()' "$si_file" 2>/dev/null || true; } | wc -l | tr -d ' ')
    SI_BARE_INFO=$( { grep -oP '(?<!\[)INFO-\d{3}(?!\]\()' "$si_file" 2>/dev/null || true; } | wc -l | tr -d ' ')
    if [[ "$SI_BARE_IND" -gt 0 || "$SI_BARE_INFO" -gt 0 ]]; then
      check_warn "$(basename "$si_file"): $SI_BARE_IND bare IND + $SI_BARE_INFO bare INFO reference(s)"
    else
      check_pass "$(basename "$si_file"): all references linked"
    fi
  fi
done

# =============================================================================
# 3.5.1 Report v2 structure (Phase 1 readability layer)
# All checks WARN-only until v2 template is stable. Skip silently if report
# does not opt-in (no "品質状態:" header line).
# =============================================================================

echo ""
echo "--- Report v2 Structure (WARN-only) ---"

if [[ -f "$REPORT" ]] && grep -q '^>\s*品質状態:' "$REPORT"; then
  # 3.5.1.1: required headings
  declare -a REQUIRED_HEADINGS=(
    "^## 0\. 今日のポイント"
    "^## 1\. 主要判断"
    "^## 5\. 低確信度の監視事項"
    "^## 6\. まだわかっていないこと"
    "^## 7\. やるべきこと"
    "^## 付録A"
    "^## 付録B"
  )
  MISSING=0
  for pat in "${REQUIRED_HEADINGS[@]}"; do
    if ! grep -qE "$pat" "$REPORT"; then
      check_warn "report v2: heading missing: ${pat#^}"
      MISSING=$((MISSING + 1))
    fi
  done
  if [[ "$MISSING" -eq 0 ]]; then
    check_pass "report v2: all required headings present"
  fi

  # 3.5.1.2: 品質状態 value is one of the allowed states
  STATUS_LINE=$(grep -E '^>\s*品質状態:' "$REPORT" | head -1 || true)
  if echo "$STATUS_LINE" | grep -qE 'GREEN|YELLOW_COLLECTION_GAP|YELLOW_RED_UNAVAILABLE|RED_QUALITY_FAIL|RED_ARBITER_FAIL'; then
    check_pass "report v2: 品質状態 value is in the allowed set"
  else
    check_warn "report v2: 品質状態 value not in allowed set: $STATUS_LINE"
  fi

  # 3.5.1.3: each ### 1.x judgment block has all 6 labels
  JUDGMENT_BLOCKS=$(grep -cE '^### 1\.[0-9]' "$REPORT" 2>/dev/null || true)
  if [[ "$JUDGMENT_BLOCKS" -gt 0 ]]; then
    LABELS_OK=0
    for label in "事実 (Facts)" "仮定 (Assumptions)" "判断 (Judgment)" "不確実性 (Uncertainty)" "意思決定への含意" "次回収集要求"; do
      COUNT=$(grep -cF "**${label}" "$REPORT" 2>/dev/null || true)
      if [[ "$COUNT" -ge "$JUDGMENT_BLOCKS" ]]; then
        LABELS_OK=$((LABELS_OK + 1))
      fi
    done
    if [[ "$LABELS_OK" -eq 6 ]]; then
      check_pass "report v2: all $JUDGMENT_BLOCKS judgment blocks have all 6 labels"
    elif [[ "$LABELS_OK" -ge 3 ]]; then
      check_warn "report v2: only $LABELS_OK of 6 labels consistently appear in judgment blocks"
    else
      check_warn "report v2: judgment blocks missing most 6-label structure ($LABELS_OK/6)"
    fi
  fi

  # 3.5.1.4: bare EVD-... references should be linked
  BARE_EVD=$( { grep -oP '(?<!\[)EVD-\d{8}-\d{4}(?!\]\()' "$REPORT" 2>/dev/null || true; } | wc -l | tr -d ' ')
  if [[ "$BARE_EVD" -gt 0 ]]; then
    check_warn "report v2: $BARE_EVD bare EVD-... reference(s) without Markdown link"
  fi
else
  echo "  (skipped: report does not yet declare v2 品質状態 header)"
fi

# =============================================================================
# 3.5.2 Static Intelligence v2 Structure (WARN-only)
# Skip silently if a file does not yet declare v2 ヘッダー (`> 最終判断更新:`).
# =============================================================================

echo ""
echo "--- Static Intelligence v2 Structure (WARN-only) ---"

declare -a SI_FILES=(
  "static_intelligence/anthropic.md"
  "static_intelligence/openai.md"
  "static_intelligence/google.md"
  "static_intelligence/xai.md"
  "static_intelligence/bytedance.md"
  "static_intelligence/market-overview.md"
)

for si in "${SI_FILES[@]}"; do
  [[ -f "$si" ]] || continue
  base=$(basename "$si")

  if ! grep -q '^>\s*最終判断更新:' "$si"; then
    echo "  (skipped $base: no v2 ヘッダー)"
    continue
  fi

  v2_missing=0
  for pat in "^## 0\." "^## 1\." "^## 2\." "^## 3\." "^## 4\." "^## 5\." "^## 6\." "^## 7\." "^## 付録"; do
    if ! grep -qE "$pat" "$si"; then
      check_warn "$base: missing heading ${pat#^}"
      v2_missing=$((v2_missing + 1))
    fi
  done
  if [[ "$v2_missing" -eq 0 ]]; then
    check_pass "$base: all 7 sections + 付録 present"
  fi

  # Header lines
  for header in '最終判断更新:' '全体確信度:' '主参照:'; do
    if ! grep -q "^>\s*${header}" "$si"; then
      check_warn "$base: header line missing: $header"
    fi
  done

  # §4 仮説表 must contain "確度の根拠" column
  if ! grep -q '確度の根拠' "$si"; then
    check_warn "$base: §4 仮説表に「確度の根拠」列がない"
  fi

  # §2 should be a table with the required columns
  if ! grep -q '判断との関係' "$si"; then
    check_warn "$base: §2 判断の重心表に「判断との関係」列がない"
  fi

  # No [Arbiter v3.NN] in body (only allowed in 付録)
  body_arbiter=$(awk '/^## 付録/{exit} /\[Arbiter v3\.[0-9]+\]/{print}' "$si" | wc -l | tr -d ' ')
  if [[ "$body_arbiter" -gt 0 ]]; then
    check_warn "$base: $body_arbiter [Arbiter v3.X] reference(s) in body §0-§7 (付録移動推奨)"
  fi
done

# scenario-tracker.md: シナリオ別ミニ構造の簡易チェック
if [[ -f "static_intelligence/scenario-tracker.md" ]] && grep -q '^>\s*最終判断更新:' "static_intelligence/scenario-tracker.md"; then
  scn_count=$(grep -cE '^## SCN-00[1-4]' "static_intelligence/scenario-tracker.md" 2>/dev/null || true)
  if [[ "$scn_count" -ge 4 ]]; then
    check_pass "scenario-tracker.md: 4 SCN sections present"
  else
    check_warn "scenario-tracker.md: only $scn_count SCN sections (expected 4)"
  fi
fi

# =============================================================================
# 3.6. Evidence Layer (Phase 1 of Agentic Intelligence Redesign)
# All checks here are WARN-level until the Evidence layer is stable.
# Skip silently if Phase 1.6 has never been enabled for this date.
# =============================================================================

echo ""
echo "--- Evidence Layer (Phase 1, WARN-only) ---"

EVD_RAW_DIR="Information/raw/$DATE"
EVD_INDEX="Information/evidence_index.json"
EVD_PROCESSED="Information/processed/$DATE.jsonl"

if [[ ! -d "$EVD_RAW_DIR" ]]; then
  echo "  (skipped: $EVD_RAW_DIR not present — Phase 1.6 may not be enabled)"
else
  # 3.6.1: each *.jsonl is valid JSONL + schema-valid
  for jsonl in "$EVD_RAW_DIR"/firecrawl.jsonl "$EVD_RAW_DIR"/x_posts.jsonl; do
    [[ -f "$jsonl" ]] || continue
    if python3 -m scripts.lib.evidence_schema validate "$jsonl" >/tmp/evd-validate.log 2>&1; then
      check_pass "$(basename "$jsonl"): schema valid"
    else
      check_warn "$(basename "$jsonl"): schema errors (see /tmp/evd-validate.log)"
    fi
  done

  # 3.6.2: evidence_index.json valid JSON + references match raw files
  if [[ -f "$EVD_INDEX" ]]; then
    if python3 -c "import json; json.load(open('$EVD_INDEX'))" 2>/dev/null; then
      check_pass "evidence_index.json is valid JSON"
      ORPHAN_COUNT=$(python3 -c "
import json
idx = json.load(open('$EVD_INDEX'))
date = '$DATE'
orphans = 0
for eid, meta in idx.get('evidence', {}).items():
    if meta.get('run_date') != date:
        continue
    raw = meta.get('raw_path', '')
    import os
    if raw and not os.path.exists(raw):
        orphans += 1
print(orphans)
" 2>/dev/null || echo "0")
      if [[ "$ORPHAN_COUNT" -eq 0 ]]; then
        check_pass "evidence_index.json: all $DATE entries reference existing raw files"
      else
        check_warn "evidence_index.json: $ORPHAN_COUNT orphan entries for $DATE (raw_path missing)"
      fi
    else
      check_warn "evidence_index.json is invalid JSON"
    fi
  else
    check_warn "evidence_index.json missing (expected when Phase 1.6 ran)"
  fi

  # 3.6.3: content_hash uniqueness in processed.jsonl
  if [[ -f "$EVD_PROCESSED" ]]; then
    DUP=$(python3 -c "
import json
seen = {}
dup = 0
for line in open('$EVD_PROCESSED'):
    line = line.strip()
    if not line: continue
    r = json.loads(line)
    h = r.get('content_hash')
    if h in seen:
        dup += 1
    else:
        seen[h] = r.get('evidence_id')
print(dup)
" 2>/dev/null || echo "0")
    if [[ "$DUP" -eq 0 ]]; then
      check_pass "processed/$DATE.jsonl: no content_hash duplicates"
    else
      check_warn "processed/$DATE.jsonl: $DUP content_hash duplicate(s) (possible circular reporting)"
    fi
  fi

  # 3.6.4: collected-raw.md INFO-NNN sections have Evidence ID lines
  if [[ -f "$COLLECTED" ]]; then
    INFO_TOTAL=$(grep -c "^### INFO-" "$COLLECTED" 2>/dev/null || true)
    EVD_LINES=$(grep -c '^- \*\*Evidence ID:\*\*' "$COLLECTED" 2>/dev/null || true)
    if [[ "$INFO_TOTAL" -gt 0 ]]; then
      if [[ "$EVD_LINES" -ge "$INFO_TOTAL" ]]; then
        check_pass "collected-raw.md: all $INFO_TOTAL INFO sections have Evidence ID lines"
      elif [[ "$EVD_LINES" -gt 0 ]]; then
        MISSING=$((INFO_TOTAL - EVD_LINES))
        check_warn "collected-raw.md: $MISSING of $INFO_TOTAL INFO sections missing Evidence ID line"
      else
        check_warn "collected-raw.md: 0 of $INFO_TOTAL INFO sections have Evidence ID line (Phase 1 prompt may need update)"
      fi
    fi
  fi
fi

# =============================================================================
# 4. Config integrity checks
# =============================================================================

echo ""
echo "--- Config Integrity ---"

# Check JSON validity
for cfg in config/pirs.json config/companies.json config/collection_plan.json config/hypotheses.json config/scenarios.json config/indicators.json; do
  if [[ -f "$cfg" ]]; then
    if python3 -c "import json; json.load(open('$cfg'))" 2>/dev/null; then
      check_pass "$cfg is valid JSON"
    else
      check_fail "$cfg is INVALID JSON"
    fi
  else
    check_fail "$cfg MISSING"
  fi
done

# Check scenario probabilities sum to ~100
if [[ -f "config/scenarios.json" ]]; then
  PROB_SUM=$(python3 -c "
import json
data = json.load(open('config/scenarios.json'))
total = sum(s['probability'] for s in data['scenarios'])
print(total)
" 2>/dev/null || echo "0")

  if [[ "$PROB_SUM" -ge 95 && "$PROB_SUM" -le 105 ]]; then
    check_pass "Scenario probabilities sum to ${PROB_SUM}%"
  else
    check_warn "Scenario probabilities sum to ${PROB_SUM}% (expected ~100%)"
  fi
fi

# =============================================================================
# Summary
# =============================================================================

echo ""
echo "=== Validation Summary ==="
echo "  ✅ Pass: $PASS"
echo "  ⚠️  Warn: $WARN"
echo "  ❌ Fail: $FAIL"

if [[ "$FAIL" -gt 0 ]]; then
  echo ""
  echo "RESULT: FAIL ($FAIL critical issues)"
  exit 1
elif [[ "$WARN" -gt 0 ]]; then
  echo ""
  echo "RESULT: PASS WITH WARNINGS ($WARN warnings)"
  exit 0
else
  echo ""
  echo "RESULT: PASS"
  exit 0
fi
