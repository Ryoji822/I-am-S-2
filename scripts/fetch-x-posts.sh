#!/bin/bash
# Wrapper script for fetch-x-posts.py
# Ensures proper PATH and python environment on macOS

export PATH="/Users/s18675/.pyenv/shims:/usr/local/bin:/usr/bin:/bin:$PATH"
export HOME="/Users/s18675"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$SCRIPT_DIR/.." || exit 1

# Configure git for commits
git config user.name "X-Posts Bot" 2>/dev/null
git config user.email "bot@i-am-s-2.local" 2>/dev/null

exec python3 "$SCRIPT_DIR/fetch-x-posts.py"
