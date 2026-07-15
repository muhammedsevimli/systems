@echo off
REM ============================================================
REM Ad Concept Factory - automatic production every morning (Windows)
REM This file finds its own parent folder (the project root),
REM moves there, and runs claude headless.
REM Task Scheduler triggers this .cmd every morning.
REM Setup steps: SETUP-automation.md
REM ============================================================

REM Move to the project root (parent of the automation folder)
cd /d "%~dp0.."

REM Write a timestamp to the log file
echo. >> "automation\last-run.log"
echo === %date% %time% - production started === >> "automation\last-run.log"

REM Run claude headless. CLAUDE.md is loaded automatically.
REM It reads the task in daily-task.txt and writes 50 concepts to outputs.
call claude -p "read and apply the task in automation/daily-task.txt. write 50 concepts to the outputs folder with today's date." --allowedTools Read,Write,Glob --permission-mode acceptEdits >> "automation\last-run.log" 2>&1

echo === %date% %time% - production finished === >> "automation\last-run.log"
