# Second Brain 🧩

Write your work into files once so AI already knows the history on every task. A no-code working memory that runs in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A lasting system that saves you from re-explaining "which project are we on, what did we decide last month, what did that customer want" in every new task. You build the brain once; before every task the system loads only the part that task needs, on its own.

## What it does

When you write a proposal, an email, or a plan, you no longer remind it of last time's price, the last thing you discussed with that customer, or the decisions you made. The system keeps your work's core, projects, decisions, people, and resources in files. Before each task it reads the index and the core first, then pulls the right file for the job. Every new decision gets written back into a file, so the brain fills up week by week.

Here is the difference from a brand kit: this is not a single "voice", it is the whole memory of your work. The system loads what the task needs, not everything, so the context stays clean and the brain grows more useful the bigger it gets.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 20 minutes. You are not learning anything new, just putting the work you carry in your head into files.

## Supported tools

The same context rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/second-brain.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/second-brain second-brain
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this second brain system for my work". It fills in the files with you.

Then fill the files in `memory/` with your own work:

- `01-core.md`: who, what you do, for whom, current priority, what you are not, proof
- `02-voice.md`: tone, address, words, **banned words** (if you produce text)
- `03-projects.md`: active projects, status, next step
- `04-people.md`: customers, partners, who for what
- `05-decisions.md`: accumulated decisions, "do not touch now", what is featured
- `06-resources.md`: tools, links, templates (do NOT store passwords, only note where they are)

`00-index.md`, `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `WEEKLY-LOOP.md` stay as they are, no need to change them. If you add a new file, just add a line to the `00-index.md` map.

Then ask for output without giving any work information:

> write a short instagram post to send to a new customer. do not ask me about the work, work from the brain.

The system first says which files it read ("core + voice + decisions read"), then writes a piece that fits your work, in the right tone, pushing your featured offer. You gave it not one word about the work.

## Does it really work? Test it in 30 seconds

- **Memory:** ask for output without giving work info. If it pulls the right files and knows your work, it passed.
- **Context:** ask "where are we on that project". If it loads `03-projects.md` and states the right status, it passed.
- **Decision protection:** pitch it the work you said "do not touch now". If it declines and reminds you of the decision, it passed.
- **Write-back:** say "new decision: ... save this to the brain". If it added it to the top of `05-decisions.md` with the date, it passed.

## Weekly loop

Once a week, 5 minutes (`WEEKLY-LOOP.md`): what happened, are the projects current, any new person/resource, did the priority change, is the index correct. Do this and the brain grows with you and stale info moves to the archive.

## Example output

`EXAMPLE-OUTPUT.md` has four real pieces the system produced for a fictional business ("Pixel Studio", a one-person web studio), with not one word of work info in the prompt. It loads different files for different tasks. (All examples are fictional.)

## Who it is for

Anyone carrying several jobs, projects, and customers at once: founders, freelancers, one-person studios, small teams. Anyone tired of writing the same brief for the tenth time. You do not need to code.

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI. If you get stuck setting it up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.net/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
