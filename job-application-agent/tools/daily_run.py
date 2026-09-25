"""The runner the scheduler calls every day.

What it does:
1. Opens Chrome if it is not running (the Claude in Chrome extension works while the browser is open).
2. Sends the "daily run" command in the system folder with `claude -p --chrome`.
3. Writes the output to reports/log-<date>.txt.

To try it by hand:  py tools/daily_run.py
For a dry run, leave `submit: no` in you/TARGET.md.
"""
from __future__ import annotations

import datetime as dt
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
MAX_TURNS = "200"


def chrome_running() -> bool:
    if platform.system() == "Windows":
        out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq chrome.exe"], capture_output=True, text=True).stdout
        return "chrome.exe" in out
    out = subprocess.run(["pgrep", "-f", "Google Chrome|chrome"], capture_output=True, text=True).stdout
    return bool(out.strip())


def open_chrome() -> None:
    system = platform.system()
    if system == "Windows":
        os.startfile("chrome")  # type: ignore[attr-defined]
    elif system == "Darwin":
        subprocess.Popen(["open", "-a", "Google Chrome"])
    else:
        exe = shutil.which("google-chrome") or shutil.which("chromium") or "google-chrome"
        subprocess.Popen([exe])
    time.sleep(8)


def main() -> int:
    REPORTS.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    log = REPORTS / f"log-{today}.txt"
    claude = shutil.which("claude") or shutil.which("claude.cmd")
    if not claude:
        log.write_text("claude command not found. Is Claude Code installed?\n", encoding="utf-8")
        return 2
    if not chrome_running():
        open_chrome()

    command = [
        claude,
        "-p",
        "--chrome",
        "--permission-mode", "bypassPermissions",
        "--max-turns", MAX_TURNS,
        "--output-format", "text",
        "daily run",
    ]
    start = dt.datetime.now()
    with log.open("a", encoding="utf-8") as f:
        f.write(f"== {start:%Y-%m-%d %H:%M} started ==\n")
        f.flush()
        result = subprocess.run(command, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
        end = dt.datetime.now()
        f.write(f"\n== {end:%H:%M} finished · exit {result.returncode} · {int((end - start).total_seconds() // 60)} min ==\n")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
