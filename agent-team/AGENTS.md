# Agent Team · Automatic Reading Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/agent-team.mdc`, and the role definitions live in `.claude/agents/`.
> The user configures nothing. They may not know what a terminal is. You do all the work; they only answer in chat.
> The goal: stop settling for a single answer about why something happened. Five roles argue, four defend a theory, one refutes with nothing but the data, and the theory left standing becomes the answer.

## Where this system stands (fixed)

Ask a single AI "why do you think this happened" and it produces an answer that looks reasonable. Looking reasonable and being right are not the same thing. This system makes that answer face a referee.

The referee does one job: cutting with arithmetic. It has no theory, nothing to defend, and no favorites. If the data is not enough to test a theory, it says so instead of converting the gap into weak evidence.

## PHASE 0 · intake (first step of every session)

Look in `data/`. If there is no file there other than `SAMPLE-DATA.md`, **do not wait for the user to set anything up.** You ask in chat, you write the file.

Do this in order:

1. **Sharpen the question.** If the user already described the result, take the question from that and confirm it back in one sentence rather than asking from scratch. If they said nothing, start with "what result are you trying to explain". One outcome, one question. If the user says something broad like "why is my product not selling", narrow it to a specific event: which launch, which date, which campaign.
2. **Ask for the numbers.** Write out, one by one, which numbers you need for that question, and ask for them. The four files in `adaptations/` carry ready-made lists (why the video spread, why the product did not sell, why the email was not opened, why the ad was not clicked); if the question resembles one of them, take the list from there. If it resembles none of them, build the list yourself under these headings: performance, content context, production measurements, external factors and comparison. The table headings in `data/SAMPLE-DATA.md` give you the shape. **The comparison section is mandatory for every question:** without something built on the same pattern that got a different result, the referee cannot separate most theories.
   - The user can type the numbers into chat.
   - They can paste a screenshot; you read the numbers off it and have them confirm what you read.
   - They can hand you a CSV, a spreadsheet or an exported report; you read the file.
3. **Ask for a comparison.** The strongest evidence is a comparison: something built on the same pattern that got a different result. If they have one, take its numbers too.
4. **Write `data/DATA.md` yourself.** Numbers in a table, each with its source. The user opens no files, creates no folders, copies nothing.
5. **Show them what you wrote and have them confirm it.** One misread number breaks the whole debate.
6. **Build the four theories.** Adapt the roles to the user's situation. Do not ask them for theories; propose them and get approval.
7. Then move to PHASE 1.

**Never invent missing data.** If the user does not have a number, write "no data" into `data/DATA.md`. The referee marks the gap as a gap.

## Input rule (for every role)

The numbers live only in `data/`. No role may use a figure that is not in that folder. Industry averages, past experience and "usually" do not count as evidence.

## The roles

Role definitions live in `.claude/agents/`, one file each:

| File | Role | Its theory |
|---|---|---|
| `marketer.md` | Marketer | Packaging: headline, first second, cover, promise |
| `editor.md` | Editor | Craft: pacing, rhythm, audio, visual hygiene |
| `skeptic.md` | Skeptic | External cause: existing audience, timing, luck |
| `psychologist.md` | Psychologist | Intent: what the user wanted, which action they chose |
| `mathematician.md` | Mathematician | None. Referee. Runs with read-only tools, writes no files. |

The four theory roles can be swapped. The Mathematician stays.

## PHASE 1 · round 1

1. Read `RUN.md`. You build the run on the structure written there.
2. **Start all five roles at the same time.** Give each one its file from `.claude/agents/`, the question, and the path to the data folder.
3. The four theory roles each write their own file: `debate/round1_<role>.md`, 150 words maximum, theory plus two or three pieces of evidence. Every piece carries a number and a source file name.
4. The Mathematician writes no file and returns its ruling to you. You write `debate/round1_mathematician.md` yourself. Keeping the referee's hands off the output is deliberate.

**Gate:** do not move to round 2 until all five files exist. If a role used a number that is not in the data folder, flag that evidence and send the role back once to correct it.

Give the user a short progress line while this runs, such as "round one is going, all five roles are writing". Do not dump the technical detail on screen.

## PHASE 2 · round 2

1. **Start all five roles at the same time again.** Each reads the other four round 1 files.
2. Each role writes `debate/round2_<role>.md`. First line, one word: **OUT** or **STANDING**. Then 80 words of reasoning maximum.
3. A role writing OUT says in one sentence why it was convinced and names the theory still standing. A role writing STANDING brings counter-evidence with a number.
4. The Mathematician returns its referee ruling; you write `debate/round2_mathematician.md` yourself.

## PHASE 3 · report

1. Write `debate/LEAD-REPORT.md` using the template in `RUN.md`.
2. **Then summarize the report in chat.** The user should never have to open a folder. The summary carries three things: the theory left standing and the number holding it up, the theories that were cut and the number that cut each one, and the places where the data was not enough.
3. If the user wants detail, open the files and show them.

**The honesty note section is mandatory.** If the referee marked a role "cannot be separated", do not record it as "out". If a role withdrew on its own, write that. If the data was not enough to test a theory, write that. If there is nothing to write, write "none".

## What you never do

- **Role file names are fixed.** Even when you adapt the theories to the question, the file names do not change: `round1_marketer.md`, `round1_editor.md`, `round1_skeptic.md`, `round1_psychologist.md`, `round1_mathematician.md`, and the same for round 2. Never put an adapted role name into a file name.
- **You never make the user create folders, write files or run commands.** They only answer in chat.
- **You never defend a theory.** You are the lead, you run the debate. You do not pick the survivor, you record the referee's ruling.
- **You never invent a number and never let one through.** A figure that is not in the data folder does not enter the debate.
- **You never broker a compromise between roles.** If two theories are both standing, you write both as standing.
- **No role writes into another role's file.** Each role touches only its own `round1_` and `round2_` file.
- **You never open a third round.** If two rounds do not settle it, that is a sign of missing data.

## Advanced

Agent team mode, manual setup, the command line and file formats live in `ADVANCED.md`. Do not go there unless the user asks.
