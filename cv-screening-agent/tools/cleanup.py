"""Deletes the candidates' personal data. Run it once the process is over.

  py tools/cleanup.py             lists the files to be deleted, deletes nothing
  py tools/cleanup.py --confirm   deletes the listed files and resets candidates.csv

Deleted:  the contents of candidates/inbox/, reports/, invites/, rejections/, screen-me/
          and the candidate rows in candidates.csv.
Kept:     candidates/samples/ (fictional CVs), you/JOB.md, tools/, docs,
          the .gitkeep files in the folders.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["candidates/inbox", "reports", "invites", "rejections", "screen-me"]
TABLE = ROOT / "candidates.csv"
HEADER = "date,file,sha,candidate,email,score,status,reason,draft,note\n"


def to_delete() -> list[Path]:
    found: list[Path] = []
    for name in FOLDERS:
        folder = ROOT / name
        if not folder.exists():
            continue
        for p in sorted(folder.rglob("*")):
            if p.is_file() and p.name != ".gitkeep":
                found.append(p)
    return found


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        pass
    confirm = "--confirm" in sys.argv
    files = to_delete()
    rows = 0
    if TABLE.exists():
        rows = max(0, len(TABLE.read_text(encoding="utf-8").splitlines()) - 1)

    if not files and rows == 0:
        print("No personal data to delete.")
        return 0

    for p in files:
        print(("deleted  " if confirm else "will delete  ") + str(p.relative_to(ROOT)).replace("\\", "/"))
    print(f"candidates.csv: {rows} candidate rows {'reset' if confirm else 'will be reset'}")

    if not confirm:
        print(f"\n{len(files)} files in total. To delete them:  py tools/cleanup.py --confirm")
        return 0

    for p in files:
        p.unlink()
    for name in FOLDERS:
        folder = ROOT / name
        for d in sorted((x for x in folder.rglob("*") if x.is_dir()), reverse=True):
            try:
                d.rmdir()
            except OSError:
                pass
    TABLE.write_text(HEADER, encoding="utf-8", newline="\n")
    print(f"\nDone: {len(files)} files deleted, candidates.csv is back to an empty table.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
