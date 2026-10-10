# Run

Everything happens in chat. You do not need to open files; you only read the finished work.

## 1. Set up (once)

Open Claude Code in this folder and type:

```text
setup
```

Claude asks at most five questions, one at a time:

1. Your company's name.
2. What you do and who you sell to.
3. Which channels you publish on (email, Instagram, site...).
4. Two or three rules that describe your voice. Paste an old piece of your writing if you like, and Claude works out the rules.
5. Your red lines: things that must never be written.

It writes `company/COMPANY.md` from your answers. It also prepares the folder so every worker can work at their own desk. If your computer is missing the small tool this needs, it tells you how to install it.

Skip this step if you want to try it first. The folder comes with the fictional company Urla Table.

## 2. Give a job

Write it in plain words. The more concrete it is, the fewer questions the CEO asks:

- Weak: "make some content"
- Good: "write this week's email newsletter and an Instagram announcement for it"

The CEO does the following and logs all of it:

1. Writes the finished state of the job in one sentence and lists the needs. If something is unclear, it asks at most two questions.
2. Hires someone from the staff for each need.
3. Opens a desk for every worker. A desk is a copy of the files that belongs to that worker only.
4. Runs workers who do not wait on each other at the same time, and workers who need each other one after another.
5. When a worker finishes, merges their desk into the main folder and clears the desk away.
6. Puts the auditor last. If the auditor says FIX, it runs the right worker once more with the note (at most two rounds).
7. Leaves the finished work in `company/approval/` and gives you a summary: who worked, how many minutes, roughly how many tokens, the file path.

## 3. Approve or send back

Read the file in `company/approval/`. Then:

```text
approve company/approval/2026-10-10-newsletter-week-41.md
```

or

```text
reject company/approval/2026-10-10-newsletter-week-41.md second paragraph is too long, move the beans to the top
```

When you approve, Claude sends nothing. The file is ready; you do the sending.

## 4. See the board

```text
shift
```

You get the table of the last job: worker, desk, start, finish, number of helpers, status. Below it, what is waiting for approval.

## 5. Grow the staff

```text
hire translator
```

Claude asks three questions (what it will produce, which tools it needs, when it may take a helper), writes the worker's job description as `.claude/agents/translator.md` and shows it to you. If Claude Code asks for permission to write into that folder, approve it. A new worker sometimes only appears on the staff in the next session. If it does not show up in this session, the CEO opens it as a general worker and has it read its job description, and the job still gets done.

## How to read the log

`company/log.jsonl` keeps one event per line:

```json
{"t":"2026-10-10T23:50:07+03:00","who":"ceo","event":"hire","detail":"writer: newsletter copy"}
```

| Event | Meaning |
|---|---|
| `hire` | The CEO hired someone |
| `desk` | A worker got a desk |
| `start` / `finish` | A worker started / finished |
| `helper` | A worker took a helper |
| `merge` | A desk was merged into the main folder |
| `approval_request` | The job landed in the approval folder |
| `approved` / `rejected` | You approved / sent it back |
| `stopped` | A limit was hit or the job was left unfinished |

If you do not want to read the log, type `shift` and Claude turns it into a table.

## Settings

There are three settings at the end of `company/COMPANY.md`. To change one, just say it in chat ("lower the token ceiling to 1 million"):

| Setting | Default | Meaning |
|---|---|---|
| `max_workers` | 5 | At most how many workers per job |
| `max_helpers` | 2 | At most how many helpers in total per job |
| `token_ceiling` | 1500000 | If it would be passed, the CEO stops and asks |

## Optional: the whole shift at once

If your Claude Code has a multi-stage batch run feature, you can say "run it as a workflow" or "ultracode" and run the same order in one go: first the independent workers together, then the auditor, then the fix. The rules do not change: every worker at their own desk, every event in the log, the finished work in approval. This route was not tried in the test run; the manual shift order was.
