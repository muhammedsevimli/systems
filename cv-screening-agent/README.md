# CV Screening Agent

A system that reads the CVs sent to your job listing for you, compares each one with the listing and scores it out of 100, rejects anyone who crosses your red lines with the reason written down, writes the shortlist to a table, and drafts interview invites and polite rejection emails. Whether the emails get sent is your call, with a single line.

**The system runs on your own computer, and the CVs are never uploaded anywhere.** It ignores information such as age, gender, marital status and photo, and does not score it. The final decision is yours.

## What it does

When 50 CVs come in for one listing, most of the day goes into repeating the same work: open the CV, compare it with the listing's requirements one by one, work out the years of experience from the dates, set aside the ones that do not fit, note the shortlist somewhere, write a separate email to each candidate. This system finishes that loop before you wake up and leaves a report on your desk.

1. It collects the new CVs in the `candidates/inbox/` folder (or under a Gmail label). It reads PDF, Word and plain text. It never looks at a CV it has already read.
2. It compares each CV with `you/JOB.md` and scores it out of 100: role overlap, must-haves, years of experience, location and preferences.
3. It rejects anyone who crosses your red lines regardless of score, and anyone below the threshold with the reason written down.
4. It builds the shortlist from the candidates above the threshold and puts the rest on the backup list.
5. It drafts interview invites for the shortlist and polite rejections for the rejected. The rejection email never states the reason; the reason lives only in your report.
6. It writes the `candidates.csv` table and the day's report. The report has each candidate's score breakdown and an "ASK THE OWNER" list: a contradiction in a CV, a requirement left unclear in the listing, a candidate just below the threshold who would pass with a single decision.

**What it does not do:** it never counts a skill the CV does not mention, and it never infers anything from a title or a company. If a CV contradicts itself, it does not reject the candidate; it asks you. With `send: no` it sends not a single email.

**Candidate mode:** If you are job hunting, you can use the same system for your own application. Type `screen me`, give your CV and the listing; the system writes the score the hiring side would see, why you might be rejected, where you are strong, and what your CV does not show. Before you apply.

## Setup

What you need: [Claude Code](https://claude.com/claude-code) and Python 3.10+. `pypdf` for reading PDFs (Claude installs it if it is missing). If the CVs come from Gmail, or you want the system to send the emails, Chrome with the [Claude in Chrome](https://claude.com/chrome) extension. You do not open or fill in any file; Claude does all of it in chat.

1. Open Claude Code, give it this address and say "set this up for me":

```text
github.com/muhammedsevimli/systems/tree/main/cv-screening-agent
```

   Claude downloads the folder (with `npx degit`; if you like the command line: `npx degit muhammedsevimli/systems/cv-screening-agent cv-screening-agent`).

2. If you like, see the demo first: type `screen` in the folder. A full screening runs with the fictional listing and the 12 fictional CVs that ship with it, and no email goes out.

3. Type `setup` in the folder. Claude asks for your listing (paste the text or give the link), extracts the must-haves and preferences from the listing itself and shows them for your OK; asks in chat about the experience band, location, your red lines, the shortlist size, where the CVs will come from and the time; writes `you/JOB.md`; installs the scheduler. The send switch starts off.

4. Type `screen` and read the first table and the reasons. If you like it, type `daily run` or wait for the morning; it runs by itself at the time you gave during `setup`.

5. Read the reports for a few days. Once you trust the system, say "turn sending on" and Claude flips the switch.

The other commands (`inspect`, `invite`, `reject`, `status`, `screen me`, `cleanup`) and the details are in `RUN.md`.

## Fair screening and privacy

- Age, date of birth, gender, marital status, children, pregnancy, photo, place of birth, neighborhood, religion, nationality, disability, health, political views, association membership and military service status are not scored and never appear in any reason. If a CV contains them, they are read and ignored; the report only says in how many CVs they were present.
- If you try to make one of them a red line, the system refuses and proposes the criterion that meets the real need of the job (an experience band instead of age, for example).
- Every rejection is written with its reason, and you see it. Rejection emails go out in the next run; you can change your mind in between.
- CVs are personal data. They stay on your computer and are never uploaded to any site. The candidate folders, reports and drafts are in `.gitignore`; they never go into the repo. When the position closes, type `cleanup` and all of it is deleted.
- These rules are the system's own rules; they are not legal advice.

## Does it really work

Yes, with a demo run. All of it is in `TEST-RESULT.md`: the fictional listing and 12 fictional CVs (3 of them PDF, 1 Word) were read, and who was rejected and why, the shortlist, the ASK THE OWNER questions and the drafts written are all there. Candidate mode was tested separately. The things that were not tested are written down too.

## What you should know

- The score is a comparison between what the CV says and what the listing says; it does not measure the candidate's real ability. A badly written CV can push a good candidate to a low score. Reading the candidates just below the threshold and the ASK THE OWNER list is your job.
- For the scheduled run, the computer must be on at that time. On the Gmail path Chrome must be reachable; if Chrome is closed, the runner opens it.
- The `reports/log-*.txt` files are raw run logs; do not share them.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Codex, Cursor, Windsurf and other tools that read AGENTS.md | `AGENTS.md` (the Gmail steps need Claude in Chrome) |

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI. If you get stuck setting it up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.com/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
