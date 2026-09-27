# How to run it

## Commands

Open Claude Code in this folder and type:

| Command | What it does |
|---|---|
| `setup` | First-time setup: give your listing, answer the questions in chat; Claude sets up `you/JOB.md` and the scheduler. |
| `daily run` | Full flow: collect CVs, read, score, reject, shortlist, invite and rejection drafts, report. The scheduler calls this too. |
| `screen` | Only read, score and write to the table. No drafts. Try this on day one. |
| `inspect candidates/inbox/ayse-cv.pdf` | The full score breakdown for a single CV, with the evidence in the CV behind each score. Does not write to the table. |
| `invite` | Interview invite drafts for the shortlist. Sends them from Gmail if `send: yes`. |
| `reject` | Polite rejection drafts for the rejected. Sends them in the next run if `send: yes`. |
| `status` | Summarizes the table. You set the ones you called in to `interview` and the one you hired to `hired`. |
| `screen me https://...` | Candidate mode: with your own CV and a listing, the score the hiring side would see and the rejection risks, before you apply. |
| `cleanup` | Deletes all candidate data when the position closes. Shows the list first and deletes nothing until you say "yes". |

## Folder structure

```
cv-screening-agent/
  CLAUDE.md            the agent's rules (AGENTS.md has the same content)
  you/JOB.md           listing, must-haves, red lines, interview details, settings
  candidates.csv       tracking table
  candidates/
    inbox/             incoming CVs (pdf, docx, txt, md)
    samples/           12 fictional CVs (read only in demo mode)
  reports/2026-09-27.md   the day's report: shortlist, rejected, score breakdown, ASK THE OWNER
  invites/<candidate>.md       interview invite drafts
  rejections/<candidate>.md    rejection drafts
  screen-me/<date>-<company>.md   candidate mode reports
  tools/read_cv.py     PDF / Word / text → plain text
  tools/setup.py       install / remove the scheduler
  tools/daily_run.py   the runner the scheduler calls
  tools/cleanup.py     delete personal data
```

## Scoring

| Item | Points |
|---|---|
| Role and responsibility overlap | 40 |
| Must-haves (-8 for each missing) | 25 |
| Experience band (inside the band 15, 1 year off 8, more 0) | 15 |
| Location and work mode | 10 |
| Tool, language, certificate preferences (2 each) | 10 |

A red line violation rejects regardless of score. Years of experience are calculated from the dates in the CV; a "for X years" sentence in the summary does not count. The threshold is set with `threshold:` and the shortlist size with `shortlist:`; 70 and 5 are a good start. To change them, just tell Claude.

## Table statuses

`shortlist` · `invite-ready` · `invite-sent` · `backup` (above the threshold, the shortlist was full) · `rejected` · `reject-ready` · `reject-sent` · `question-pending` (needs an ASK THE OWNER answer, no email goes out) · `interview` · `offer` · `hired` · `withdrew`

## Scheduler

```bash
py tools/setup.py          # installs it for the time: value in you/JOB.md
py tools/setup.py --remove
py tools/daily_run.py      # one run by hand; log in reports/log-<date>.txt
py tools/daily_run.py --dry-run   # shows which command it would run, without running it
```

The runner uses `claude -p --permission-mode bypassPermissions`: nobody is at the keyboard, so it does not ask for permissions. It uses Chrome only on the Gmail path or when sending is on (`--chrome`). The limits in `CLAUDE.md` keep it from doing anything outside this folder; still, run the first few by hand and read the reports.

## Demo mode

The `you/JOB.md` that ships is the fictional Derin Kozmetik listing and it says `demo: yes`. With this setting the agent copies the 12 fictional CVs in `candidates/samples/` into `candidates/inbox/`, reads them, scores them, rejects, and writes the report and the drafts. No email goes out and Chrome is not opened. To see the system, type `screen` or `daily run` once, then `cleanup` and `setup`. If the listing is the demo listing and `demo: yes` is missing, the agent does not run at all.

## Common snags

- **"UNREADABLE: scanned PDF":** the CV is made of an image and has no text in it. Ask the candidate for a PDF with text or a Word file; the candidate stays `question-pending` in the table.
- **"Reading PDFs needs a library":** run `py -m pip install pypdf`, or tell Claude "install it".
- **Old .doc file:** it cannot be read. Open it in Word and save it as .docx, or ask the candidate for a PDF.
- **The same CV gets read again:** check whether the file name and sha are in `candidates.csv`. If you delete the table by hand, the agent thinks the CV is new.
- **I disagree with a rejection:** say it in chat ("move Can Demir to the shortlist"). Claude updates the table and removes the rejection draft; the rejection email does not go out before the next run anyway.
- **"Gmail session is signed out" in the report:** sign in to Gmail in Chrome and start the run again. The agent never asks for or types a password.
