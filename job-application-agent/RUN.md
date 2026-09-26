# Running details

## Commands

Open Claude Code in this folder and type:

| Command | What it does |
|---|---|
| `setup` | First-time setup: give your CV, answer the questions in chat; Claude writes `you/CV.md`, `you/TARGET.md` and installs the scheduler. |
| `daily run` | Full flow: search, score, prepare, fill in the form, report. The scheduler calls this too. |
| `scan` | Search and score only. Fills in the table, opens no folders. Try this on day one. |
| `prepare https://www.linkedin.com/jobs/view/123456/` | For a single listing: folder, match, tailored CV, cover letter, answers. |
| `submit 2026-09-25-bora-kozmetik-performance-marketing` | Fills in the form from a ready folder. Submits it if `submit: yes`. |
| `rehearse 2026-09-25-bora-kozmetik-performance-marketing` | 10 interview questions and answer outlines from the listing and the CV. |
| `status` | Summarizes the table. When a reply comes in you mark the listing `reply`, and `interview` if you get an interview. |

## Folder structure

```
job-application-agent/
  CLAUDE.md              the agent's rules (AGENTS.md has the same content)
  you/CV.md              your CV (single source of truth)
  you/TARGET.md          targets, threshold, cap, submit switch, standard answers
  applications.csv       tracking table
  applications/
    2026-09-25-company-role/
      job.md             listing text and requirements
      match.md           score breakdown, strong evidence, gaps
      cv-tailored.md     CV reordered for the listing
      cv-tailored.pdf
      cover-letter.md
      answers.md         form answers, plus any "ASK OWNER" lines
      preview.md         text of the "Review" screen (and the confirmation if submitted)
  reports/2026-09-25.md
  tools/cv_pdf.py        markdown → PDF (headless Chrome/Edge)
  tools/setup.py         install / remove the scheduler
  tools/daily_run.py     the runner the scheduler calls
```

## Scoring

| Item | Points |
|---|---|
| Role and responsibility overlap | 40 |
| Mandatory requirements (-8 for each missing one) | 25 |
| Location and work mode | 15 |
| Industry and company size | 10 |
| Salary (5 if not given) | 10 |

A red line violation rejects the listing regardless of score. The threshold changes with `threshold:` in `you/TARGET.md`; 70 is a good start.

## Table statuses

`rejected` · `candidate` (passed the threshold, cap was full, looked at tomorrow) · `ready` · `preview` (form filled in, submit off) · `submitted` · `external` (company site, you apply) · `question-pending` · `reply` · `interview` · `declined`

## Scheduler

```bash
py tools/setup.py            # installs it based on the time: value in you/TARGET.md
py tools/setup.py --remove
py tools/daily_run.py        # one manual run; log goes to reports/log-<date>.txt
```

The runner uses `claude -p --chrome --permission-mode bypassPermissions`: nobody is at the keyboard, so it does not ask for permission. The limits in `CLAUDE.md` are what keep it from doing anything outside this folder; still, do the first runs by hand and read the reports.

## Demo mode

The `you/CV.md` that ships with the setup is the fictional Elif Aydın, and `you/TARGET.md` says `demo: yes`. With this setting the agent scans real listings, scores them, tailors the CV, fills in the form up to the "Review" step and discards the draft. Nothing is submitted. Run it once to see the system, then type `setup`: you hand over your CV, Claude writes the files and sets `demo: no`. While the CV is the demo person and `demo: yes` is missing, the agent does not run at all.

## Common snags

- **"session logged out" report:** sign in to linkedin.com in Chrome and start the run again. The agent never asks for or types a password.
- **No PDF came out:** the Chrome or Edge path was not found. Put the browser's full path in the `CHROME_PATH` environment variable.
- **A form stayed at `question-pending`:** find the "ASK OWNER" line in the folder's `answers.md`, say the answer in chat (Claude adds it to the standard answers), then type `submit <folder>`.
- **The same listing keeps coming back:** check whether its `job_id` is in `applications.csv`. If you delete the table by hand, the agent thinks the listing is new.
- **LinkedIn security warning:** the agent ends the run. Take a day or two off and lower the cap.
