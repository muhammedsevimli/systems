@echo off
rem The lookout's shift (Windows). Task Scheduler runs this file.
rem Goes to the folder, opens Claude Code in non-interactive mode with the "radar" command, appends the output to company\radar\shift.log.
rem Permissions: file edits, git, the log script and Python. No other command can run.
cd /d "%~dp0.."
echo ==== %date% %time% >> "company\radar\shift.log"
claude -p "radar" --permission-mode acceptEdits --allowedTools "Bash(git:*)" "Bash(bash company/log.sh:*)" "Bash(python:*)" "Bash(python3:*)" "Bash(py:*)" >> "company\radar\shift.log" 2>&1
