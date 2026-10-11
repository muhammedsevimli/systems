#!/usr/bin/env bash
# The lookout's shift (Mac and Linux). cron or launchd runs this file.
# Goes to the folder, opens Claude Code in non-interactive mode with the "radar" command, appends the output to company/radar/shift.log.
# Permissions: file edits, git, the log script and Python. No other command can run.
set -e
cd "$(dirname "$0")/.."
# cron runs with a short PATH; add the usual places Claude Code is installed
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
echo "==== $(date)" >> company/radar/shift.log
claude -p "radar" --permission-mode acceptEdits \
  --allowedTools "Bash(git:*)" "Bash(bash company/log.sh:*)" "Bash(python:*)" "Bash(python3:*)" \
  >> company/radar/shift.log 2>&1
