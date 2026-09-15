# Run it

This file sets up the lead. The lead is your own session: it asks the question, runs the five roles, and reports the result.

There are two ways to run it below. **Path B works on every setup**, try that first. Path A depends on an experimental feature and does nothing if the feature is off.

---

## Fill these in first

Before pasting the prompt, change three things for your own case.

**1. The question.** One sentence, one outcome. Phrase it as "why did this happen". Example: "why did episode 12 get 85,000 views in a single day".

**2. The data.** Say what you put in `data/` and what each file holds. The numbers live there and nowhere else.

**3. Four theories.** One per role. If you want a ready-made scenario, take one of the three files in `adaptations/` and copy the theories from it.

---

## Path B · parallel sub-agents (works everywhere)

Open Claude Code in this folder and paste this:

```text
Your role: the lead of this debate. You defend no theory. You run the debate and report it.

QUESTION: <your one-sentence question>

DATA: the files under data/. The numbers live only there. No agent may use a number
that is not in that folder.

ROLES AND THEORIES:
- Marketer: <theory 1>
- Editor: <theory 2>
- Skeptic: <theory 3>
- Psychologist: <theory 4>
- Mathematician: no theory. Reads the data, tests each theory against the numbers,
  writes which one the data contradicts. Runs read-only, writes no files, returns
  its ruling to you.

ROUND 1
Start five sub-agents AT THE SAME TIME. Give each one its own role file from
.claude/agents/, the question, and the path to the data folder. Each role writes
its own file: debate/round1_<role>.md, 150 words maximum, theory plus 2-3 pieces of
evidence (a number and the source file name). The Mathematician writes nothing and
returns to you; you write debate/round1_mathematician.md yourself.

ROUND 1 GATE
Do not move to round 2 until all five files exist. If a role used a number that is
not in the data folder, flag that piece of evidence and send the role back once to
correct it.

ROUND 2
Start five sub-agents AT THE SAME TIME again. Each reads the other four round 1
files. Each role writes debate/round2_<role>.md: first line one word, OUT or
STANDING, then 80 words of reasoning maximum. A role writing OUT says in one
sentence why it was convinced. A role writing STANDING brings counter-evidence with
a number. The Mathematician returns its referee ruling; you write
debate/round2_mathematician.md yourself.

REPORT
Write debate/LEAD-REPORT.md using the template below.

RULES
- No number is invented. If it is not in the data folder, the claim is not made.
- You defend no theory and you do not pick the survivor. You write the referee's ruling.
- If the referee marked a role "cannot be separated with this data", do not write it
  as "out". Report the distinction as it stands.
- No role writes into another role's file.
```

This path opens five separate sub-agents. Each runs in its own context, cannot see inside the others, and communicates only through the files in `debate/`. The real run was done this way.

---

## Path A · agent team mode (experimental)

Claude Code's agent team feature runs a lead and several teammates over a shared task list instead of opening sub-agents. **This feature is experimental.** If it is off, renamed, or absent from your version you get no error at all, the command simply behaves like a normal session. In that case fall back to Path B.

To enable it, put this in `.claude/settings.json` at the project root:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Quit Claude Code and reopen it in this folder. Then paste the same prompt from Path B, replacing only the "Start five sub-agents at the same time" line at the top of **ROUND 1** and **ROUND 2** with this:

```text
Run five teammates over a shared task list. Give each role its own file from
.claude/agents/. Put five tasks on the shared list for round 1 and five for round 2.
Round 2 tasks do not open until all five round 1 tasks are closed.
```

**Windows note:** in agent team mode the teammates run inside the same process and the live panel does not open in some terminals. If the panel does not appear the run still proceeds; you watch progress as files land in `debate/`. Windows Terminal or WSL is more comfortable for the panel.

Both paths produce the same output: ten files plus the lead report.

---

## Lead report template

`debate/LEAD-REPORT.md` is written in this shape:

```text
# Lead report · <subject> · <date>

Question: <one sentence>
Run: 5 agents, 2 rounds, <which path>. Input: <data files>. <duration> and <tokens>.

| Role | Theory | Round 1 evidence | Round 2 ruling |
|---|---|---|---|
| Marketer | <theory> | <number> | OUT / STANDING + one-sentence reason |
| Editor | <theory> | <number> | ... |
| Skeptic | <theory> | <number> | ... |
| Psychologist | <theory> | <number> | ... |
| Mathematician | referee | tested each theory against the numbers | referee ruling |

**Left standing:** <theory and one paragraph of reasoning, with numbers>

**Honesty note:** if the referee could not separate a role, if a role withdrew on its
own, or if the data was not enough to test a theory, it goes here. This section is
never left empty; if there is nothing to write, write "none".

Files: round1_*.md, round2_*.md (debate/ folder).
```

The theory left standing is your answer. What makes it different from a single agent's answer: it survived a round where four rival explanations were cut by arithmetic, and whatever could not be tested is written down too.
