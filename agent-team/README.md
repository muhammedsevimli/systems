# Agent Team

A system that makes five agents argue about one question. Four roles each defend a theory. The fifth role, the Mathematician, defends nothing and tests every theory against the numbers in your data folder. A role whose theory gets cut withdraws in round two. The theory left standing is your answer.

Ask a single AI "why do you think this happened" and it writes an answer that sounds reasonable. This system makes that answer face a referee.

## What it does

You have a result and you do not know the cause. A video spread unexpectedly, a product did not sell, an email went unopened. Four or five explanations are floating in your head, they all sound sensible, and you cannot tell them apart.

Here is what the system does:

1. You drop your data into `data/`. The numbers live there and nowhere else.
2. Five agents open. Four defend a theory, one is the referee.
3. **Round 1:** each role writes its theory and cites two or three numbers from the data. The Mathematician marks every theory "consistent with the data" or "contradicted by the data" and shows the arithmetic.
4. **Round 2:** each role reads what the others wrote. If convinced, it writes **OUT** and says in one sentence why it withdrew. If not, it writes **STANDING** and brings counter-evidence.
5. The lead writes the one-page report on whatever is left standing.

**One rule holds for every role:** you speak only with numbers from the data folder. No invented figures, no "usually", no "in my experience". If you have no number, you do not make the claim.

## Install

```bash
npx degit muhammedsevimli/systems/agent-team agent-team
```

Or the green **Code → Download ZIP**. If you would rather not touch a terminal, open Claude Code and give it this address, then say "set this up for my work":

```text
github.com/muhammedsevimli/systems/tree/main/agent-team
```

## Run it

1. Put your data in `data/`. Format example: `data/SAMPLE-DATA.md`.
2. Open `RUN.md`, fill in the question and the four theories for your own case.
3. Open Claude Code in this folder and paste that prompt.
4. Output lands in `debate/`: `round1_<role>.md`, `round2_<role>.md`, `LEAD-REPORT.md`.

There are two ways to run it, both written out in `RUN.md`. Agent team mode is experimental; if it is not enabled, the same prompt runs as parallel sub-agents and gives the same result.

## Does it really work

Yes, on a real run.

A short video had spread far beyond the previous episode in the same series and the cause was not obvious. Five roles ran, two rounds turned.

**Three roles were cut, one stood.** The production-quality theory was cut because the two episodes being compared had nearly identical audio and edit measurements, and a variable that stayed constant cannot produce a 14.7x gap. The existing-audience theory was cut because only 4.1% of viewers were followers: carrying the unique-viewer count through followers would have required 24 viewers per follower. The opening-scene theory was withdrawn by its own agent after the referee said the data could not separate it, because an earlier episode without that opening had reached an even larger number.

**Left standing:** viewer intent. Saves and comments were 74.5% of total engagement, with saves at 3.38x likes.

**Time and cost:** 5 agents, 2 rounds, about 4 minutes, roughly 570k tokens. Details in `COST.md`.

The report format from that run is in `EXAMPLE-OUTPUT.md`.

## Folder layout

```text
agent-team/
  CLAUDE.md                Claude Code reads this automatically
  AGENTS.md                Codex, Windsurf, Kilo and 20+ tools read this
  .cursor/rules/           Cursor reads this
  .claude/agents/          the five role files
  RUN.md                   the lead prompt, two ways to run it
  data/SAMPLE-DATA.md      example data format
  adaptations/             three ready-made scenarios with their theories
  debate/                  output lands here
  COST.md                  how many agents, how many rounds, which model
  EXAMPLE-OUTPUT.md        a lead report written on the sample data
```

## The roles

| Role | What it argues |
|---|---|
| Marketer | The result came from packaging: headline, first second, cover, promise. |
| Editor | The result came from craft: pacing, rhythm, audio, visual hygiene. |
| Skeptic | The result came from outside: existing audience, timing, luck, someone who carried it. |
| Psychologist | The result came from intent: what the viewer wanted to do and which action they chose. |
| Mathematician | No theory. Reads the data, tests each theory against the numbers, writes which one the data contradicts. This is the referee. |

You can swap the four theory roles for your own. The Mathematician stays. `adaptations/` holds three ready scenarios: a product that did not sell, an email that was not opened, an ad that was not clicked.

## Why the referee is a separate role

| Situation | Without a referee |
|---|---|
| All four theories sound sensible | Every one writes persuasively, none gets cut, you end up with four answers. |
| A role invents a number | The others treat it as real and build on top of it. |
| A theory contradicts the data | The role never notices, it just picks friendlier evidence. |
| Two theories fit the same data | The better-written one wins, not the stronger one. |

The Mathematician has no theory, so it has nothing to defend. In the test run the referee marked one role "cannot be separated with this data" rather than cutting it. Saying the data is not enough when the data is not enough is the sign that the thing works.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` + `.claude/agents/` |
| Cursor | `.cursor/rules/` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` |

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
