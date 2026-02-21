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
  BARE_IND=$(grep -oP '(?<!\[)IND-\d{3}(?!\]\()' "$REPORT" 2>/dev/null | wc -l | tr -d ' ')
  if [[ "$BARE_IND" -gt 0 ]]; then
    check_warn "$BARE_IND bare IND-XXX reference(s) without Markdown link in report"
  fi

  # Check for unlinked INFO-XXX references (should be [INFO-XXX](...))
  BARE_INFO=$(grep -oP '(?<!\[)INFO-\d{3}(?!\]\()' "$REPORT" 2>/dev/null | wc -l | tr -d ' ')
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
    SI_BARE_IND=$(grep -oP '(?<!\[)IND-\d{3}(?!\]\()' "$si_file" 2>/dev/null | wc -l | tr -d ' ')
    SI_BARE_INFO=$(grep -oP '(?<!\[)INFO-\d{3}(?!\]\()' "$si_file" 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$SI_BARE_IND" -gt 0 || "$SI_BARE_INFO" -gt 0 ]]; then
      check_warn "$(basename "$si_file"): $SI_BARE_IND bare IND + $SI_BARE_INFO bare INFO reference(s)"
    else
      check_pass "$(basename "$si_file"): all references linked"
    fi
  fi
done

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
