# Agent Team · Automatic Reading Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/agent-team.mdc`, and the role definitions live in `.claude/agents/`.
> The goal: stop settling for a single answer about why something happened. Five roles argue, four defend a theory, one refutes with nothing but the data, and the theory left standing becomes the answer.

## Where this system stands (fixed)

Ask a single AI "why do you think this happened" and it produces an answer that looks reasonable. Looking reasonable and being right are not the same thing. This system makes that answer face a referee.

**The referee does one job: cutting with arithmetic.** It has no theory, nothing to defend, and no favorites. If the data is not enough to test a theory, it says so instead of converting the gap into weak evidence.

## Input

You put your own data in `data/`. The numbers live there and nowhere else. No role may use a figure that is not in that folder. Industry averages, past experience and "usually" do not count as evidence.

Format example: `data/SAMPLE-DATA.md` (fictional).

## The roles

Role definitions live in `.claude/agents/`, one file each:

| File | Role | Its theory |
|---|---|---|
| `marketer.md` | Marketer | Packaging: headline, first second, cover, promise |
| `editor.md` | Editor | Craft: pacing, rhythm, audio, visual hygiene |
| `skeptic.md` | Skeptic | External cause: existing audience, timing, luck |
| `psychologist.md` | Psychologist | Intent: what the viewer wanted, which action they chose |
| `mathematician.md` | Mathematician | None. Referee. Runs with read-only tools, writes no files. |

The four theory roles can be swapped. The Mathematician stays.

## PHASE 1 · round 1

1. Read the files under `data/`. Take the question and the four theories from the user, in the shape laid out in `RUN.md`.
2. **Start all five roles at the same time.** Give each one its file from `.claude/agents/`, the question, and the path to the data folder.
3. The four theory roles each write their own file: `debate/round1_<role>.md`, 150 words maximum, theory plus two or three pieces of evidence. Every piece carries a number and a source file name.
4. The Mathematician writes no file and returns its ruling to you. You write `debate/round1_mathematician.md` yourself. Keeping the referee's hands off the output is deliberate.

**Gate:** do not move to round 2 until all five files exist. If a role used a number that is not in the data folder, flag that evidence and send the role back once to correct it.

## PHASE 2 · round 2

1. **Start all five roles at the same time again.** Each reads the other four round 1 files.
2. Each role writes `debate/round2_<role>.md`. First line, one word: **OUT** or **STANDING**. Then 80 words of reasoning maximum.
3. A role writing OUT says in one sentence why it was convinced and names the theory still standing. A role writing STANDING brings counter-evidence with a number.
4. The Mathematician returns its referee ruling; you write `debate/round2_mathematician.md` yourself.

## PHASE 3 · lead report

Write `debate/LEAD-REPORT.md` using the template in `RUN.md`.

**The honesty note section is mandatory.** If the referee marked a role "cannot be separated", do not record it as "out". If a role withdrew on its own, write that. If the data was not enough to test a theory, write that. If there is nothing to write, write "none".

## What you never do

- **You never defend a theory.** You are the lead, you run the debate. You do not pick the survivor, you record the referee's ruling.
- **You never invent a number and never let one through.** A figure that is not in the data folder does not enter the debate.
- **You never broker a compromise between roles.** If two theories are both standing, you write both as standing.
- **No role writes into another role's file.** Each role touches only its own `round1_` and `round2_` file.
- **You never open a third round.** If two rounds do not settle it, that is a sign of missing data, not of needing more rounds.
