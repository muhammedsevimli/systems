#!/usr/bin/env bash
# ============================================================
# Ad Concept Factory - automatic production every morning (Mac / Linux)
# This script moves to its own parent folder (the project root)
# and runs claude headless.
# cron or launchd triggers this script every morning.
# Setup steps: SETUP-automation.md
# ============================================================

# Move to the project root (parent of the automation folder)
cd "$(dirname "$0")/.." || exit 1

{
  echo ""
  echo "=== $(date) - production started ==="
} >> "automation/last-run.log"

# Run claude headless. CLAUDE.md is loaded automatically.
claude -p "read and apply the task in automation/daily-task.txt. write 50 concepts to the outputs folder with today's date." \
  --allowedTools Read,Write,Glob --permission-mode acceptEdits >> "automation/last-run.log" 2>&1

echo "=== $(date) - production finished ===" >> "automation/last-run.log"
