"""Turns CV files into plain text. The agent reads every CV with this before scoring.

Usage:
  py tools/read_cv.py candidates/inbox/ayse-cv.pdf     text of a single file
  py tools/read_cv.py candidates/inbox                 text of the NEW CVs in the folder
  py tools/read_cv.py candidates/inbox --list          file list only (new / read)
  py tools/read_cv.py candidates/inbox --all           all of them, including those in candidates.csv

"New" means: neither the file name nor the sha value appears in candidates.csv.
Supported: .pdf  .docx  .txt  .md
  PDF   needs pypdf (pdfminer.six is tried if it is missing). Install: py -m pip install pypdf
  DOCX  needs no extra install (a Word file is a zip archive; its contents are read).
  TXT/MD  read as UTF-8, falling back to Windows Turkish (cp1254) and Latin-1.
The old .doc format cannot be read: "Save as > .docx" in Word is needed.
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "candidates.csv"
SUPPORTED = {".pdf", ".docx", ".txt", ".md"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


class ReadError(Exception):
    pass


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        PdfReader = None  # type: ignore
    if PdfReader is not None:
        reader = PdfReader(str(path))
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as e:  # noqa: BLE001
                raise ReadError("The PDF is encrypted and could not be opened. Ask the candidate for an unencrypted copy.") from e
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    try:
        from pdfminer.high_level import extract_text  # type: ignore
    except ImportError as e:
        raise ReadError(
            "Reading PDFs needs a library. Run this:  py -m pip install pypdf"
        ) from e
    return extract_text(str(path))


def read_docx(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml")
    except (zipfile.BadZipFile, KeyError) as e:
        raise ReadError("The Word file is broken or not a .docx. Ask the candidate for a PDF.") from e
    root = ET.fromstring(xml)
    lines: list[str] = []
    for p in root.iter(f"{W}p"):
        parts: list[str] = []
        for node in p.iter():
            if node.tag == f"{W}t" and node.text:
                parts.append(node.text)
            elif node.tag == f"{W}tab":
                parts.append("\t")
            elif node.tag in (f"{W}br", f"{W}cr"):
                parts.append("\n")
        lines.append("".join(parts))
    return "\n".join(lines)


def read_plain(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1254", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ReadError("Could not decode the text encoding.")


def text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        t = read_pdf(path)
    elif suffix == ".docx":
        t = read_docx(path)
    elif suffix in (".txt", ".md"):
        t = read_plain(path)
    elif suffix == ".doc":
        raise ReadError("The old .doc format cannot be read. It has to be saved as .docx in Word, or ask for a PDF.")
    else:
        raise ReadError(f"Unsupported format: {suffix}")
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    if len(t) < 80:
        raise ReadError(
            "Almost no text came out of the file. Most likely a scanned (image) PDF. "
            "ASK THE OWNER: ask the candidate for a PDF with text, or a Word file."
        )
    return t


def already_read() -> tuple[set[str], set[str]]:
    names: set[str] = set()
    shas: set[str] = set()
    if TABLE.exists():
        with TABLE.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("file"):
                    names.add(row["file"].strip())
                if row.get("sha"):
                    shas.add(row["sha"].strip())
    return names, shas


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        pass
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 2
    target = Path(args[0])
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()
    if not target.exists():
        print(f"not found: {target}")
        return 2

    if target.is_file():
        try:
            print(text(target))
            return 0
        except ReadError as e:
            print(f"UNREADABLE: {target.name}: {e}")
            return 3

    names, shas = already_read()
    files = sorted(p for p in target.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED | {".doc"})
    errors = 0
    new_count = 0
    for path in files:
        s = sha(path)
        seen = path.name in names or s in shas
        if "--list" in flags:
            print(f"{'read' if seen else 'new '}  sha:{s}  {path.name}")
            continue
        if seen and "--all" not in flags:
            continue
        new_count += 1
        print(f"===== {path.name} · sha:{s} =====")
        try:
            print(text(path))
        except ReadError as e:
            errors += 1
            print(f"UNREADABLE: {e}")
        print()
    if "--list" not in flags:
        print(f"== {new_count} files read, {errors} unreadable ==")
    return 0 if errors == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
