# Agent Team

A system that makes five agents argue about one question. Four roles each defend a theory. The fifth role, the Mathematician, defends nothing and tests every theory against the numbers. A role whose theory gets cut withdraws in round two. The theory left standing is your answer.

Ask a single AI "why do you think this happened" and it writes an answer that sounds reasonable. This system makes that answer face a referee.

## Install · pull it from GitHub

Three ways, the easiest one first.

**1. Hand the link to the tool that installs it.** Open Claude Code or Codex, give it this address and say "install this into this folder":

```text
github.com/muhammedsevimli/systems/tree/main/agent-team
```

**2. One line if you know the command line:**

```bash
npx degit muhammedsevimli/systems/agent-team agent-team
```

**3. If you want neither:** go to the address above, hit the green **Code** button, **Download ZIP**, and open the folder.

## Run it · the rest is a conversation

Open Claude Code or Codex in the folder you pulled and talk to it. Describing your result is enough:

```text
I have a result I want explained: the short video I posted last week got 42,000
views in a day, and the previous episodes were stalling at 5,000.
```

The tool takes it from there. First it sharpens the question, then it writes out which numbers it needs, one by one, and asks you for them. You type the numbers, paste a screenshot, or hand over an exported report. The tool writes the data file itself and shows it to you so it knows it read everything correctly.

Then five agents run, two rounds turn, and the report comes back in chat: the theory left standing, the theories that were cut and the number that cut each one, and the places where the data was not enough. You never have to touch a folder, a prompt file or an output file by hand.

## What it does

You have a result and you do not know the cause. A video spread unexpectedly, a product did not sell, an email went unopened. Four or five explanations are floating in your head, they all sound sensible, and you cannot tell them apart.

Here is what the system does:

1. The numbers are collected into one data file. They live nowhere else.
2. Five agents open. Four defend a theory, one is the referee.
3. **Round 1:** each role writes its theory and cites two or three numbers from the data. The Mathematician marks every theory "consistent with the data" or "contradicted by the data" and shows the arithmetic.
4. **Round 2:** each role reads what the others wrote. If convinced, it writes **OUT** and says in one sentence why it withdrew. If not, it writes **STANDING** and brings counter-evidence.
5. The theory left standing lands in a one-page report and gets summarized in chat.

**One rule holds for every role:** you speak only with numbers from the data file. No invented figures, no "probably", no "usually". If you have no number, you do not make the claim.

## The roles

| Role | What it argues |
|---|---|
| Marketer | The result came from packaging: headline, first second, cover, promise. |
| Editor | The result came from craft: pacing, rhythm, audio, visual hygiene. |
| Skeptic | The result came from outside: existing audience, timing, luck, someone who carried it. |
| Psychologist | The result came from intent: what the viewer wanted to do and which action they chose. |
| Mathematician | No theory. Reads the data, tests each theory against the numbers, writes which one the data contradicts. This is the referee. |

The tool adapts the four theory roles to your situation. The Mathematician stays; it is the working part of the system.

Four ready scenarios ship with it: a video that spread, a product that did not sell, an email that was not opened, an ad that was not clicked. If your question resembles one of them, the tool takes the list of numbers from there. If it does not, the tool builds the list itself.

## Why the referee is a separate role

| Situation | Without a referee |
|---|---|
| All four theories sound sensible | Every one writes persuasively, none gets cut, you end up with four answers. |
| A role invents a number | The others treat it as real and build on top of it. |
| A theory contradicts the data | The role never notices, it just picks friendlier evidence. |
| Two theories fit the same data | The better-written one wins, not the stronger one. |

The Mathematician has no theory, so it has nothing to defend. In the test run the referee marked one role "cannot be separated with this data" rather than cutting it. Saying the data is not enough when the data is not enough is the sign that the thing works.

## Does it really work

Yes, on a real run.

A short video had spread far beyond the previous episode in the same series and the cause was not obvious. Five roles ran, two rounds turned.

**Three roles were cut, one stood.** The production-quality theory was cut because the two episodes being compared had nearly identical audio and edit measurements, and a variable that stayed constant cannot produce a 14.7x gap. The existing-audience theory was cut because only 4.1% of viewers were followers: carrying the unique-viewer count through followers would have required 24 viewers per follower. The opening-scene theory was withdrawn by its own agent after the referee said the data could not separate it, because an earlier episode without that opening had reached an even larger number.

**Left standing:** viewer intent. Saves and comments were 74.5% of total engagement, with saves at 3.38x likes.

**Time and cost:** 5 agents, 2 rounds, about 4 minutes, roughly 570k tokens. Details in `COST.md`.

The report format from that run is in `EXAMPLE-OUTPUT.md`.

## Advanced

Command-line setup, agent team mode, file formats and the folder layout are in `ADVANCED.md`. If the flow above is enough for you, there is no reason to go there.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` and `.claude/agents/` |
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
