# Idea Miner · SaaS Idea Scorer ⛏️

Write the field you care about once, and the system scans Hacker News, Reddit, and web and community forums on its own. It collects the real demand where people say "I wish there was", "I would pay for this", "I do it by hand every month and I am sick of it", turns each one into an idea, scores it against four criteria, and ranks the 5 best ideas you could build this week with the reasoning behind each. A no-code SaaS idea miner that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

The system finds the idea, you choose the idea. You paste nothing.

## What it does

You say "I want to build something" but you do not know what. You give three months to the first idea that comes to mind, and at the end you are holding a product nobody pays for. Meanwhile people write their pain out in the open every day: "I wish there was", "I am looking for a solution to this", "I do this by hand every month", "I would pay for this".

This system scans for those sentences itself, turns them into readable ideas, scores them 1-5 on four criteria (market size, feasibility for you, competition gap, market fit for your region), filters them through your profile, and hands you a justified queue. It works in two phases:

1. **Automatic scan.** You write the field you care about into `you/01-profile.md`. The system scans Hacker News, Reddit, and web and community forums with Claude Code's web and shell tools, and writes the real demand sentences carrying money language into `signals/` with their sources. You paste nothing.
2. **Scoring.** It turns the sentences in `signals/` into ideas, scores them against the four criteria with a reason under each score, filters them through your profile, and writes the top 5 ideas into `outputs/`. "Start here this week" at the top, the eliminated ones at the bottom.

Honest limit: Hacker News (public JSON) and web and forum search are fully automatic. Reddit is fully automatic too, but through the public RSS search feed, not the keyless `.json` endpoint, which now returns `403`; RSS returns `200` without a key, and rate limits are handled with retries. X wants a login, so the system does not pull it; it builds a one-click search link and you look by hand if you want. The main scan runs fine without X.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal knowledge required (the system runs the Reddit pull with `curl` itself).
- A folder and 15 minutes. You are not learning anything new, just writing your field, what you can build, and your limits into a file.
- An internet connection. Every source the system uses is public, no account or key needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/idea-miner.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/idea-miner idea-miner
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set this idea miner up for my field". It fills in the profile and source files with you.

These are the files the system reads. Fill in the profile and source part with your own:

- `you/01-profile.md`: the field you care about, **your region and how you collect payment**, which fields you know, what you can build, your limits, your unfair advantage
- `you/02-sources.md`: the search queries the scan runs (Hacker News, Reddit, web and forums, X) + the decision log
- `format/criteria.md`: the 1-5 rubric for the four criteria (comes ready, tune if you want)
- `format/output-format.md`: the structure of the 5-idea report (comes ready)
- `signals/`: the system writes the demand it scans here itself; you put nothing in this folder

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First scan the demand:

> scan the demand in my field

The system pulls the sources itself and writes the real demand sentences, with their links, into the `signals/` folder. You do not click. Then get the report:

> score the signals and give me the best 5 saas ideas

The system merges the signals into ideas, scores the four criteria with a reason under each, and writes the top 5 into `outputs/`. For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Signals:** are the pulled sentences real. Does every signal carry a source and a link, are there invented quotes. If it wrote a source it could not reach as "could not be reached" instead of inventing, it passed.
- **Scores:** is there a one-line reason under every score, or bare numbers. If every score carries a reason, it passed.
- **Competition:** did it name the existing product and write the point of difference, or did it propose a clone. If it wrote the difference, it passed.
- **Lane:** did it push an idea that hits one of your limits, or write what it saw and why it skipped it. If it skipped it, it passed.
- **Honesty:** if no explicit "I would pay" sentence came out of the scan, did it inflate the market score anyway, or mark the money signal as indirect. If it stayed honest, it passed.

## The mine deepens · let the system grow with you

When you notice a new good search query or source, add it to `you/02-sources.md`. When you decide to build an idea, or look at one and drop it, say "I decided on this". The system writes it with the date under the "decision log" at the bottom of `you/02-sources.md`, and later reports read it and do not propose the same idea again. The system rescans the same queries every week; the query list and the decision log become the persistent memory of your market instinct.

## Example output

`EXAMPLE-OUTPUT.md` has a full report the system produced for a fictional operator (`you/EXAMPLE-01-profile.md`, an English speaking market, local appointment businesses and small ecommerce): the scan summary, the full score table, the top 5 idea cards with a reason under every score, the "start here this week" pick, and the eliminated ones. The operator is fictional; the demand signals are real, 13 sentences pulled live from Hacker News, Reddit's public RSS feed, and review sites on 24 July 2026 (`signals/EXAMPLE-signals-2026-07-24.md`, with links, no usernames or personal data).

## Who it is for

Anyone who wants to build something: solo builders, indie founders, operators, agency people, small teams. Anyone who wants to stop starting from the first idea that pops into their head and start from demand that is already written down in public. You do not need to code; the system gives you the idea, the reasoning, and the ranking, and the decision stays with you.

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
