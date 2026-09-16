# Advanced

The main flow lives in `README.md`: pull it from GitHub, then talk to the tool. This file is for people who want to take the wheel.

## Folder layout

```text
agent-team/
  CLAUDE.md              Claude Code reads this automatically
  AGENTS.md              Codex, Windsurf, Kilo and 20+ tools read this
  .cursor/rules/         Cursor reads this
  .claude/agents/        the five role files
  RUN.md                 the structure of the run, the lead reads this
  data/                  the numbers get written here
  adaptations/           four ready scenarios
  debate/                output lands here
  COST.md                how many agents, how many rounds, which model
  EXAMPLE-OUTPUT.md      a lead report on the sample data
  ADVANCED.md            this file
```

## Writing the data file by hand

In the main flow the tool writes the data file. If you want to write it yourself, drop a `.md` file into `data/`. There is a format example in `data/SAMPLE-DATA.md` (fictional data, not from any real account).

Rules:

- Put the numbers in a table, one column per thing being compared.
- Write the source of every number. A role has to name the source file in its evidence.
- Write "no data" for any field you do not have. Do not leave it blank and do not invent it.
- Include comparison data. Something built on the same pattern that got a different result beats a number standing on its own.

## Starting the run by hand

The full lead prompt is in `RUN.md`. To paste it into your own session, take the block there and fill in the question and the four theories.

## Agent team mode

Claude Code's agent team feature runs a lead and several teammates over a shared task list instead of opening sub-agents. **This feature is experimental.** If it is off, renamed, or absent from your version you get no error at all, the command simply behaves like a normal session. The main flow works either way.

To enable it, put this in `.claude/settings.json` at the project root:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Quit Claude Code and reopen it in this folder. Then paste the prompt from `RUN.md`, replacing the "start all five roles at the same time" line at the top of each round block with this:

```text
Run five teammates over a shared task list. Give each role its own file from
.claude/agents/. Put five tasks on the shared list for round 1 and five for round 2.
Round 2 tasks do not open until all five round 1 tasks are closed.
```

**Windows note:** in agent team mode the teammates run inside the same process and the live panel does not open in some terminals. If the panel does not appear the run still proceeds; you watch progress as files land in `debate/`. Windows Terminal or WSL is more comfortable for the panel.

The real test run used ordinary parallel sub-agents, not agent team mode. Details in the README.

## Changing model tiers

You can change the `model` line at the top of each role file. Keep the Mathematician on the top tier, the system rests on it. Dropping the four theory roles to a mid tier takes out most of the cost. Details in `COST.md`.

## Changing the roles

You can rewrite the four theory files in `.claude/agents/` for your own situation. Leave `mathematician.md` alone: the referee without a theory is the working part of this system. Its read-only tools are deliberate too, so the referee cannot touch the output of the debate.

Ready scenarios live in `adaptations/`: `video-spread-unexpectedly.md`, `product-didnt-sell.md`, `email-wasnt-opened.md`, `ad-wasnt-clicked.md`. Each carries the question shape, the four theories, and which number strengthens which theory.
