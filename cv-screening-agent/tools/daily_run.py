"""The runner the scheduler calls every day.

What it does:
1. If you/JOB.md has `source: gmail` or `send: yes` (and it is not demo mode),
   it opens Chrome if it is not running and starts Claude with `--chrome`. In folder
   mode and in demo mode it never touches the browser.
2. Sends the "daily run" command in the system folder with `claude -p`.
3. Writes the output to reports/log-<date>.txt.

To try it by hand:     py tools/daily_run.py
To see the command:    py tools/daily_run.py --dry-run   (does not run it, only prints it)
"""
from __future__ import annotations

import datetime as dt
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
MAX_TURNS = "150"


def setting(name: str) -> str:
    path = ROOT / "you" / "JOB.md"
    if not path.exists():
        return ""
    m = re.search(rf"^\s*-?\s*{name}:\s*(\S+)", path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip().lower() if m else ""


def chrome_needed() -> bool:
    if setting("demo") == "yes":
        return False
    return setting("source") == "gmail" or setting("send") == "yes"


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


def build_command(claude: str, chrome: bool) -> list[str]:
    command = [claude, "-p"]
    if chrome:
        command.append("--chrome")
    command += [
        "--permission-mode", "bypassPermissions",
        "--max-turns", MAX_TURNS,
        "--output-format", "text",
        "daily run",
    ]
    return command


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        pass
    dry_run = "--dry-run" in sys.argv
    claude = shutil.which("claude") or shutil.which("claude.cmd")
    chrome = chrome_needed()
    if dry_run:
        print("Working folder:", ROOT)
        print("Chrome needed:", "yes" if chrome else "no")
        print("Command:", " ".join(build_command(claude or "claude", chrome)))
        return 0

    REPORTS.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    log = REPORTS / f"log-{today}.txt"
    if not claude:
        log.write_text("The claude command was not found. Is Claude Code installed?\n", encoding="utf-8")
        return 2
    if chrome and not chrome_running():
        open_chrome()

    start = dt.datetime.now()
    with log.open("a", encoding="utf-8") as f:
        f.write(f"== {start:%Y-%m-%d %H:%M} started ==\n")
        f.flush()
        result = subprocess.run(build_command(claude, chrome), cwd=ROOT, stdout=f, stderr=subprocess.STDOUT,
                                text=True, encoding="utf-8", errors="replace")
        end = dt.datetime.now()
        f.write(f"\n== {end:%H:%M} finished · exit {result.returncode} · "
                f"{int((end - start).total_seconds() // 60)} min ==\n")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
