#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# I-am-S-2 Intelligence Pipeline Orchestrator
# FM 2-0 based daily intelligence cycle
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TODAY="${PIPELINE_DATE:-$(TZ=Asia/Tokyo date +%Y-%m-%d)}"
TIMEOUT_SECONDS=600  # 10 minutes per phase (default)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info()  { echo -e "${BLUE}[INFO]${NC}  $(TZ=Asia/Tokyo date +%H:%M:%S) $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC}    $(TZ=Asia/Tokyo date +%H:%M:%S) $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $(TZ=Asia/Tokyo date +%H:%M:%S) $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $(TZ=Asia/Tokyo date +%H:%M:%S) $*"; }

# Track which static_intelligence files changed
STATIC_CHANGED=false

# =============================================================================
# Setup
# =============================================================================

cd "$PROJECT_DIR"

log_info "=== I-am-S-2 Intelligence Pipeline ==="
log_info "Date: $TODAY"
log_info "Project: $PROJECT_DIR"

# Create daily directories
mkdir -p "Information/$TODAY"
mkdir -p "Intelligence"
mkdir -p "state"
mkdir -p "static_intelligence"

# Record static_intelligence checksums before pipeline
STATIC_CHECKSUM_BEFORE=""
if ls static_intelligence/*.md 1>/dev/null 2>&1; then
  STATIC_CHECKSUM_BEFORE=$(cat static_intelligence/*.md 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
fi

# =============================================================================
# Phase execution helper
# =============================================================================

run_phase() {
  local phase_num="$1"
  local phase_name="$2"
  local model="$3"
  local prompt_file="$4"
  local timeout="${5:-$TIMEOUT_SECONDS}"
  local max_retries="${6:-0}"

  local attempt=1
  local total_attempts=$((max_retries + 1))

  while [[ $attempt -le $total_attempts ]]; do
    if [[ $attempt -gt 1 ]]; then
      log_warn "Phase $phase_num: retry attempt $attempt/$total_attempts"
      sleep 5
    fi

    log_info "--- Phase $phase_num: $phase_name (model: $model, attempt: $attempt/$total_attempts) ---"

    local start_time
    start_time=$(date +%s)

    local prompt_content
    prompt_content=$(cat "$PROJECT_DIR/prompts/$prompt_file")
    prompt_content="${prompt_content//YYYY-MM-DD/$TODAY}"

    if timeout "$timeout" opencode run --model "zai/$model" "$prompt_content" 2>&1; then
      local end_time
      end_time=$(date +%s)
      local duration=$((end_time - start_time))
      log_ok "Phase $phase_num completed in ${duration}s (attempt $attempt)"
      return 0
    else
      local exit_code=$?
      log_error "Phase $phase_num attempt $attempt failed (exit code: $exit_code)"
    fi

    attempt=$((attempt + 1))
  done

  log_error "Phase $phase_num failed after $total_attempts attempts"
  return 1
}

# =============================================================================
# Phase 1: COLLECT (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 1: COLLECT"
log_info "=========================================="

if ! run_phase 1 "COLLECT" "glm-5.1" "phase1-collect.md" 1800 0; then
  log_warn "Phase 1 failed. Applying fallback: copying previous day's data"

  # Find the most recent collected-raw.md from a DIFFERENT date
  PREV_DATE=$(ls -d Information/????-??-?? 2>/dev/null | sort -r | while read -r d; do
    dname=$(basename "$d")
    if [[ "$dname" != "$TODAY" ]]; then echo "$dname"; break; fi
  done)

  if [[ -n "$PREV_DATE" && -f "Information/$PREV_DATE/collected-raw.md" ]]; then
    cp "Information/$PREV_DATE/collected-raw.md" "Information/$TODAY/collected-raw.md"
    # Add DEGRADED flag
    sed -i.bak '1s/^/> ⚠️ DEGRADED: Phase 1 failed. Data copied from '"$PREV_DATE"'\n\n/' \
      "Information/$TODAY/collected-raw.md" 2>/dev/null || true
    rm -f "Information/$TODAY/collected-raw.md.bak"
    log_warn "Copied data from $PREV_DATE with DEGRADED flag"
  else
    log_error "No previous data available. Creating minimal stub."
    cat > "Information/$TODAY/collected-raw.md" << EOF
# 収集データ: $TODAY

> ⚠️ DEGRADED: Phase 1 failed. No data collected.

## メタデータ
- 収集日時: $TODAY
- 収集クエリ数: 0
- 収集結果数: 0
- 品質フラグ: DEGRADED (Phase 1 failure, no previous data available)

## 収集結果

データなし
EOF
  fi
fi

# Verify Phase 1 output exists
if [[ ! -f "Information/$TODAY/collected-raw.md" ]]; then
  log_error "Phase 1 output missing. Cannot continue."
  exit 1
fi

# =============================================================================
# Phase 1.5: Inject X_posts (local RSSHub data, no AI needed)
# =============================================================================

log_info "=========================================="
log_info "Phase 1.5: Inject X_posts into collected-raw.md"
log_info "=========================================="

X_POSTS_DIR="$PROJECT_DIR/X_posts/$TODAY"
if [[ -d "$X_POSTS_DIR" ]]; then
  X_POST_COUNT=0
  # Get current highest INFO number
  LAST_INFO=$(grep -oP 'INFO-\K\d+' "Information/$TODAY/collected-raw.md" 2>/dev/null | sort -n | tail -1)
  INFO_NUM=${LAST_INFO:-0}

  python3 - "$X_POSTS_DIR" "$INFO_NUM" << 'PYEOF' >> "Information/$TODAY/collected-raw.md"
import sys, os, re

x_dir = sys.argv[1]
info_num = int(sys.argv[2])

company_map = {
    "anthropic": ("Anthropic", "KIQ-001-01"),
    "openai": ("OpenAI", "KIQ-001-01"),
    "google-deepmind": ("Google/DeepMind", "KIQ-001-01"),
}

official_handles = {
    "AnthropicAI", "OpenAIDevs", "GoogleDeepMind",
    "sama", "demishassabis", "sundarpichai",
}

output_lines = []
output_lines.append("\n\n## X (Twitter) 投稿データ（ローカルRSSHub経由）\n")

for fname in sorted(os.listdir(x_dir)):
    if not fname.endswith(".md"):
        continue
    company_key = fname.replace(".md", "")
    company_name, default_kiq = company_map.get(company_key, (company_key, "KIQ-001-01"))

    filepath = os.path.join(x_dir, fname)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse sections: ## @handle (Name - Role)
    sections = re.split(r'^## @', content, flags=re.MULTILINE)
    for section in sections[1:]:  # skip header
        # Extract handle and name
        header_match = re.match(r'(\S+)\s+\((.+?)\s*-\s*(.+?)\)', section)
        if not header_match:
            continue
        handle = header_match.group(1)
        name = header_match.group(2)
        role = header_match.group(3)

        reliability = "A-3" if handle in official_handles else "D-3"

        # Extract posts: **HH:MM JST** | [原文](URL)\n\n> content
        posts = re.findall(
            r'\*\*(.+?)\*\*\s*\|\s*\[原文\]\((.+?)\)\s*\n\n((?:>.*\n?)+)',
            section
        )
        for time_str, url, quoted in posts:
            info_num += 1
            text = re.sub(r'^>\s?', '', quoted, flags=re.MULTILINE).strip()
            # Truncate for INFO format
            summary = text[:500] + "..." if len(text) > 500 else text

            output_lines.append(f"""
### INFO-{info_num:03d}
- **タイトル:** @{handle} ({name}) のX投稿
- **ソース:** X (Twitter) - @{handle} ({role})
- **公開日:** {os.path.basename(x_dir)}
- **信頼性コード:** {reliability}
- **関連KIQ:** {default_kiq}
- **関連企業:** {company_name}
- **要約:** {summary}
- **引用URL:** {url}
""")

print("".join(output_lines))
PYEOF

  X_POST_COUNT=$(python3 -c "
import os, re, sys
d = '$X_POSTS_DIR'
c = 0
for f in os.listdir(d):
    if f.endswith('.md'):
        t = open(os.path.join(d, f)).read()
        c += len(re.findall(r'\[原文\]', t))
print(c)
" 2>/dev/null || echo 0)

  log_ok "Injected $X_POST_COUNT X posts from $X_POSTS_DIR"
else
  log_info "No X_posts data for $TODAY (X_posts/$TODAY/ not found). Skipping."
fi

# =============================================================================
# Phase 1.6: Build Evidence Index (Phase 1 of Agentic Intelligence Redesign)
# =============================================================================
# Gated by ENABLE_EVIDENCE_PHASE1=1. When enabled, parses collected-raw.md
# INFO-NNN sections + x_posts.jsonl pending records, mints EVD-YYYYMMDD-NNNN
# IDs, and writes Information/raw|processed/ + evidence_index.json.
# Skipped when Phase 1 produced DEGRADED data (yesterday's URLs would map
# to today's date and create phantom evidence).

if [[ "${ENABLE_EVIDENCE_PHASE1:-0}" == "1" ]]; then
  log_info "=========================================="
  log_info "Phase 1.6: Build Evidence Index"
  log_info "=========================================="

  if head -5 "Information/$TODAY/collected-raw.md" 2>/dev/null | grep -q "DEGRADED"; then
    log_warn "Phase 1.6: SKIPPED (Phase 1 was DEGRADED — phantom evidence prevented)"
  elif python3 "$PROJECT_DIR/scripts/build-evidence-index.py" --date "$TODAY" --repo-root "$PROJECT_DIR"; then
    log_ok "Phase 1.6: Evidence Index updated for $TODAY"
  else
    log_warn "Phase 1.6: build-evidence-index.py failed — pipeline continues without Evidence layer"
  fi
else
  log_info "Phase 1.6: skipped (set ENABLE_EVIDENCE_PHASE1=1 to enable)"
fi

# =============================================================================
# Phase 2: ANALYZE - Blue Agent (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 2: ANALYZE (Blue Agent)"
log_info "=========================================="

if ! run_phase 2 "ANALYZE" "glm-5.1" "phase2-analyze.md" 1800 0; then
  log_warn "Phase 2 failed. Using collected raw data as processed data"
  cp "Information/$TODAY/collected-raw.md" "Information/$TODAY/processed.md"
  echo -e "\n\n> ⚠️ DEGRADED: Blue Agent analysis failed. Raw data passed through." \
    >> "Information/$TODAY/processed.md"
fi

# =============================================================================
# Phase 3: RED TEAM (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 3: RED TEAM"
log_info "=========================================="

if ! run_phase 3 "RED TEAM" "glm-5.1" "phase3-red-team.md" 1500 0; then
  log_warn "Phase 3 failed. Creating minimal red team report"
  cat > "state/red-team-$TODAY.md" << EOF
# Red Agent反証レポート: $TODAY

> ⚠️ DEGRADED: Red Agent analysis failed.

## 反証結果
Red Agentが実行されなかったため、Blue Agentの分析結果を検証なしでArbiterに渡します。

## バイアスチェック総合結果
未実施（Phase 3 failure）
EOF
fi

# =============================================================================
# Phase 4: ARBITER (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 4: ARBITER"
log_info "=========================================="

if ! run_phase 4 "ARBITER" "glm-5.1" "phase4-arbiter.md" 1500 0; then
  log_warn "Phase 4 failed. Using Blue Agent output directly"
  if [[ -f "Information/$TODAY/processed.md" ]]; then
    cp "Information/$TODAY/processed.md" "state/arbiter-$TODAY.md"
    cp "Information/$TODAY/processed.md" "state/arbiter-latest.md"
    echo -e "\n\n> ⚠️ DEGRADED: Arbiter failed. Blue Agent output passed through." \
      >> "state/arbiter-$TODAY.md"
  fi
fi

# =============================================================================
# Phase 5: STATIC UPDATE (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 5: STATIC UPDATE"
log_info "=========================================="

if ! run_phase 5 "STATIC UPDATE" "glm-5.1" "phase5-static-update.md" 1200 0; then
  log_warn "Phase 5 failed. Skipping static intelligence update"
  echo "# Static Update: $TODAY - SKIPPED (Phase 5 failure)" > "state/static-update-$TODAY.md"
fi

# Check if static_intelligence changed
STATIC_CHECKSUM_AFTER=""
if ls static_intelligence/*.md 1>/dev/null 2>&1; then
  STATIC_CHECKSUM_AFTER=$(cat static_intelligence/*.md 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
fi

if [[ "$STATIC_CHECKSUM_BEFORE" != "$STATIC_CHECKSUM_AFTER" ]]; then
  STATIC_CHANGED=true
  log_info "Static intelligence was updated"
fi

# =============================================================================
# Phase 6: REPORT (glm-5)
# =============================================================================

log_info "=========================================="
log_info "Phase 6: REPORT"
log_info "=========================================="

if ! run_phase 6 "REPORT" "glm-5.1" "phase6-report.md" 1200 0; then
  log_warn "Phase 6 failed. Generating stub report"
  cat > "Intelligence/$TODAY.md" << EOF
# デイリー・インテリジェンス・ブリーフィング: $TODAY

> 分類: UNCLASSIFIED
> 品質: DEGRADED (レポート生成失敗)

## 今日のポイント

本日のレポート生成（Phase 6）が失敗しました。分析データは以下のファイルで直接確認してください:

- 収集データ: Information/$TODAY/collected-raw.md
- Blue Agent分析: Information/$TODAY/processed.md
- Red Agent反証: state/red-team-$TODAY.md
- Arbiter判断: state/arbiter-$TODAY.md

---

*このスタブレポートはI-am-S-2 Intelligence Systemにより自動生成されました。*
EOF
fi

# =============================================================================
# Phase 7: Output validation
# =============================================================================

log_info "=========================================="
log_info "Phase 7: Validation"
log_info "=========================================="

if [[ -x "$SCRIPT_DIR/validate-output.sh" ]]; then
  bash "$SCRIPT_DIR/validate-output.sh" "$TODAY" || log_warn "Validation reported issues"
else
  log_warn "validate-output.sh not found or not executable"
fi

# =============================================================================
# Phase 8: Git commit & push
# =============================================================================

log_info "=========================================="
log_info "Phase 8: Git commit & push"
log_info "=========================================="

cd "$PROJECT_DIR"

# Stage all changes
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
  log_info "No changes to commit"
else
  COMMIT_MSG="intelligence: daily report $TODAY"

  # Add degraded note if applicable
  if grep -rq "DEGRADED" "Intelligence/$TODAY.md" 2>/dev/null; then
    COMMIT_MSG="$COMMIT_MSG [DEGRADED]"
  fi

  git commit -m "$COMMIT_MSG"

  # Pull with conflict detection (local X post fetcher may have pushed)
  PUSH_MAX=3
  for attempt in $(seq 1 $PUSH_MAX); do
    if git push origin main 2>/dev/null; then
      log_ok "Changes committed and pushed (attempt $attempt)"
      break
    else
      if [[ $attempt -lt $PUSH_MAX ]]; then
        log_warn "Push rejected. Pulling and retrying ($attempt/$PUSH_MAX)..."
        if ! git pull --rebase origin main 2>&1; then
          log_error "Pull --rebase failed. Aborting rebase and trying merge..."
          git rebase --abort 2>/dev/null || true
          if ! git pull --no-rebase origin main 2>&1; then
            # If merge also fails, abort merge to keep repo clean
            git merge --abort 2>/dev/null || true
            log_error "Pull failed. Push aborted to avoid corrupted state."
            break
          fi
        fi
      else
        log_error "Push failed after $PUSH_MAX attempts"
      fi
    fi
  done
fi

# =============================================================================
# Phase 9: Slack notification (if static_intelligence updated)
# =============================================================================

if [[ "$STATIC_CHANGED" == "true" ]]; then
  log_info "=========================================="
  log_info "Phase 9: Slack DM notification"
  log_info "=========================================="

  # Read notification config
  NOTIFICATION_CONFIG="$PROJECT_DIR/config/notification.json"
  if [[ -f "$NOTIFICATION_CONFIG" ]]; then
    REPO_URL=$(python3 -c "import json; print(json.load(open('$NOTIFICATION_CONFIG'))['repo_url'])" 2>/dev/null || echo "")
  else
    log_warn "config/notification.json not found. Skipping Slack notification."
    REPO_URL=""
  fi

  if [[ -n "${SLACK_BOT_TOKEN:-}" && -n "$SLACK_USER_ID" ]]; then
    # Open DM channel
    DM_CHANNEL=$(curl -s -X POST "https://slack.com/api/conversations.open" \
      -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
      -H "Content-Type: application/json" \
      -d "{\"users\":\"$SLACK_USER_ID\"}" | python3 -c "import sys,json; print(json.load(sys.stdin).get('channel',{}).get('id',''))" 2>/dev/null || echo "")

    if [[ -n "$DM_CHANNEL" ]]; then
      # Get list of changed static intelligence files as bullet list
      CHANGED_FILES=$(git diff --name-only HEAD~1 HEAD -- static_intelligence/ 2>/dev/null | sed 's/^/• /' | tr '\n' '\n')

      SLACK_MSG="📊 *I-am-S-2 Static Intelligence Updated* ($TODAY)\n\n更新されたファイル:\n$CHANGED_FILES\n\nリポジトリ: ${REPO_URL}/tree/main/static_intelligence"

      curl -s -X POST "https://slack.com/api/chat.postMessage" \
        -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"channel\":\"$DM_CHANNEL\",\"text\":\"$SLACK_MSG\"}" > /dev/null 2>&1

      log_ok "Slack DM sent"
    else
      log_warn "Failed to open DM channel"
    fi
  else
    log_warn "SLACK_BOT_TOKEN not set or user_id missing. Skipping Slack notification."
  fi
fi

# =============================================================================
# Summary
# =============================================================================

log_info "=========================================="
log_ok "Pipeline completed for $TODAY"
log_info "=========================================="
log_info "Outputs:"
log_info "  Report:    Intelligence/$TODAY.md"
log_info "  Raw data:  Information/$TODAY/collected-raw.md"
log_info "  Analysis:  Information/$TODAY/processed.md"
log_info "  Red team:  state/red-team-$TODAY.md"
log_info "  Arbiter:   state/arbiter-$TODAY.md"
log_info "  Static:    static_intelligence/ (updated: $STATIC_CHANGED)"
