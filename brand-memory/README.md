# Brand Memory 🧩

Write your brand once so AI never forgets it. A three-file, no-code brand memory that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A lasting system that saves you from explaining your brand from scratch in every new chat, from tone drift, and from AI forgetting the decision you made last month. You fill it in once; the system reads these files on its own before every piece of output.

## What it does

When you write content, an email, or a proposal, you no longer restate "who we are, how we talk, what we sell" every time. The system keeps your brand core (who, for whom, in what voice) in three files, and your AI tool reads them automatically on every launch. New decisions get written back into the files, so the memory grows week by week.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting what is in your head into files.

## Supported tools

The same memory rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/brand-memory.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/brand-memory brand-memory
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this brand memory system for my brand". It fills in the files with you.

Then fill the three files in `memory/` with your own brand:

- `01-brand-identity.md`: who, for whom, what you sell, what you are not, proof
- `02-voice.md`: tone, address, words, **banned words**, sample sentences
- `03-decisions.md`: what to feature this month, what not to touch right now

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `WEEKLY-LOOP.md` stay as they are, no need to change them.

Then ask for output without giving any brand information:

> write a single instagram caption for this week's product. do not ask me about the brand, work from memory.

The system reads the three files and writes copy that fits your brand, in the right tone, featuring this month's product. You gave it not one word about the brand.

## Does it really work? Test it in 30 seconds

- **Memory:** ask for a caption without giving brand info. If it knows your brand, it passed.
- **Voice:** did it avoid your banned words. If yes, it passed.
- **Decision:** did it feature the product you said "do not touch right now". If not, it passed.
- **Write-back:** say "that caption worked, save it". If it added the note to `03-decisions.md`, it passed.

## Weekly loop

Once a week, 5 minutes (`WEEKLY-LOOP.md`): what you learned, what to feature, any tone drift, archive the stale, test with a small piece of output. Do this and the system grows with you.

## Example output

`EXAMPLE-OUTPUT.md` has a real piece the system produced for a fictional brand ("Aegean Table"), with not one word of brand info in the prompt. (All examples are fictional.)

## Who it is for

Anyone with a brand who makes content, email, or proposals with AI: founders, creators, agencies, small teams. You do not need to code.

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
