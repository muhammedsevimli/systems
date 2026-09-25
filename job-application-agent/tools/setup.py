"""Installs the daily scheduler. Reads the `time:` value in you/TARGET.md.

Windows: adds a "JobApplicationAgent" task to Task Scheduler.
macOS:   writes ~/Library/LaunchAgents/com.jobapplicationagent.plist and loads it.
Linux:   adds a crontab line.

To remove it:  py tools/setup.py --remove
"""
from __future__ import annotations

import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "tools" / "daily_run.py"
TASK = "JobApplicationAgent"
PLIST_LABEL = "com.jobapplicationagent"


def read_time() -> tuple[int, int]:
    text = (ROOT / "you" / "TARGET.md").read_text(encoding="utf-8")
    m = re.search(r"^\s*-?\s*time:\s*(\d{1,2})[:.](\d{2})", text, re.M)
    if not m:
        return 9, 0
    return int(m.group(1)), int(m.group(2))


def python_path() -> str:
    return sys.executable


def windows_install(hour: int, minute: int) -> None:
    tr = f'"{python_path()}" "{RUNNER}"'
    subprocess.run(["schtasks", "/create", "/tn", TASK, "/tr", tr, "/sc", "DAILY",
                    "/st", f"{hour:02d}:{minute:02d}", "/f"], check=True)
    print(f"Task installed: {TASK} · every day at {hour:02d}:{minute:02d}")
    print("Note: the computer must be on and unlocked at that time; if Chrome is closed, the runner opens it.")


def windows_remove() -> None:
    subprocess.run(["schtasks", "/delete", "/tn", TASK, "/f"], check=False)
    print("Task removed.")


def mac_install(hour: int, minute: int) -> None:
    plist = Path.home() / "Library" / "LaunchAgents" / f"{PLIST_LABEL}.plist"
    plist.parent.mkdir(parents=True, exist_ok=True)
    plist.write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>{PLIST_LABEL}</string>
  <key>ProgramArguments</key><array><string>{python_path()}</string><string>{RUNNER}</string></array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>{hour}</integer><key>Minute</key><integer>{minute}</integer></dict>
  <key>WorkingDirectory</key><string>{ROOT}</string>
</dict></plist>
""", encoding="utf-8")
    subprocess.run(["launchctl", "unload", str(plist)], check=False, capture_output=True)
    subprocess.run(["launchctl", "load", str(plist)], check=True)
    print(f"launchd job installed · every day at {hour:02d}:{minute:02d}")


def mac_remove() -> None:
    plist = Path.home() / "Library" / "LaunchAgents" / f"{PLIST_LABEL}.plist"
    subprocess.run(["launchctl", "unload", str(plist)], check=False)
    plist.unlink(missing_ok=True)
    print("launchd job removed.")


def linux_install(hour: int, minute: int) -> None:
    line = f"{minute} {hour} * * * cd '{ROOT}' && '{python_path()}' '{RUNNER}' # {TASK}"
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    new = "\n".join(l for l in current.splitlines() if TASK not in l) + "\n" + line + "\n"
    subprocess.run(["crontab", "-"], input=new, text=True, check=True)
    print(f"crontab line added · every day at {hour:02d}:{minute:02d}")


def linux_remove() -> None:
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    new = "\n".join(l for l in current.splitlines() if TASK not in l) + "\n"
    subprocess.run(["crontab", "-"], input=new, text=True, check=True)
    print("crontab line removed.")


def main() -> int:
    remove = "--remove" in sys.argv
    system = platform.system()
    hour, minute = read_time()
    if system == "Windows":
        windows_remove() if remove else windows_install(hour, minute)
    elif system == "Darwin":
        mac_remove() if remove else mac_install(hour, minute)
    else:
        linux_remove() if remove else linux_install(hour, minute)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
