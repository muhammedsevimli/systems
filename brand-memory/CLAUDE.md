# Brand Memory · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You do nothing. Claude Code loads it on its own while working in this folder.
> The same rule also lives in `AGENTS.md` (Codex, Google Antigravity, Windsurf and 20+ tools) and `.cursor/rules/brand-memory.mdc` (Cursor).
> The goal: never explain your brand from scratch again.

## Before every piece of output, read these 3 files (required, no exceptions)
1. `memory/01-brand-identity.md`: who, for whom, what we sell, what we are not.
2. `memory/02-voice.md`: how we talk, which words are banned.
3. `memory/03-decisions.md`: what we decided in the past, what we are featuring now.

Do not produce any content, email, proposal, or copy without reading these three files.

## Output rules
- Every piece of text you write follows the tone in `02-voice.md`. Do NOT use banned words.
- Never contradict the "What you are NOT" lines in `01-brand-identity.md`.
- Do not touch the topics in the "Do NOT touch right now" list in `03-decisions.md`.
- When you need credibility, use the proof lines in `01-brand-identity.md`.

## Write back new decisions
If a new rule, preference, or decision becomes clear during work (e.g. "this headline pattern worked well", "we are dropping this word"), add it to the top of `03-decisions.md` with the date. Write in English. This way the memory grows every session.

## Weekly loop
Every week, run the 5-minute ritual in `WEEKLY-LOOP.md`. The memory stays current and the tone does not drift.
