# Ad Spy · Competitor Ad Analyzer 🎯

Write your competitors once, and the system builds Meta Ad Library links. Paste the active ads, and the system reads which ads have been running for months, extracts the pattern, and writes 10 ad concepts in your brand's voice. A no-code competitor ad analyzer that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A system that saves you from researching "what is the competitor doing, which ad is working" from scratch on every campaign. You put your competitors into a file once; then with one command the system extracts the working ad logic and dresses it in your product and tone. You start not from a blank page but on top of a proven logic.

## What it does

The hardest part of writing an ad is the blank page. This system fills that page with the ads your competitor is spending money on RIGHT NOW, then turns that logic into your brand. It works in two phases:

1. **Link generation.** It builds a Meta Ad Library (public) search link for each competitor in `brand/03-competitors.md`. You click the link and see that competitor's currently running active ads.
2. **Breakdown and generation.** You paste the active ads you saw into the `competitor-ads/` folder. The system breaks down each ad (hook, promise, for whom, format, proof, how long it has been running), marks the one running for months as a "winning candidate", extracts the repeating pattern, and writes 10 concepts in your voice read from `brand/`. Under each concept: a "which competitor logic it came from" and "why it can land" line.

Honest limit: the Meta Ad Library is public and free, but there is no free automatic download for product ads. The ad text is visible in the browser; so the "seeing an ad" step is a one-click open-and-paste job. The breakdown, pattern extraction, and 10-concept generation are fully automatic.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting your brand and competitors into files.
- A browser to open the Meta Ad Library. No account needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/ad-spy.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/ad-spy ad-spy
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this competitor ad analyzer for my brand". It fills in the brand and competitor files with you.

These are the files the system reads. Fill in the brand and competitor part with your own:

- `brand/01-brand.md`: who, for whom, what you sell, what you are not, proof
- `brand/02-voice.md`: tone, address, words, **banned words**, sample sentences
- `brand/03-competitors.md`: the competitors you track (the system builds Meta Ad Library links from these)
- `format/ad-breakdown.md`: the headings each ad is split into (comes ready, tune if you want)
- `format/concept-format.md`: the structure of the 10 concepts (comes ready, tune if you want)
- `competitor-ads/`: you paste the active ads here (the paste guide is inside the folder)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First get the links:

> generate the meta ad library links for my competitors

Click the link, paste the active ads into `competitor-ads/<competitor>.md` (how to paste is in `competitor-ads/READ-paste-guide.md`). Then analyze:

> analyze the ads in competitor-ads and produce 10 concepts adapted to my brand

The system breaks down the competitors, extracts the pattern, writes 10 concepts. For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Voice:** did it avoid your banned words. If yes, it passed.
- **Signal:** did it mark the ad running for months as a "winning candidate" and treat the recent one as the test phase. If it separated them, it passed.
- **Pattern:** did it copy the competitor's sentence, or take the logic and turn it into your voice. If it took the logic, it passed.
- **Proof:** did it invent a discount or guarantee you do not have, or leave a placeholder. If it left a placeholder, it passed.

## The competitor list grows · let the system sharpen with you

When you notice a new competitor, add it to `brand/03-competitors.md`. The system runs again from the same links every month; the list becomes the living ad memory of your industry. When a concept truly lands (a sale, a click, a save), say "this landed". The system writes it with the date at the bottom of `brand/03-competitors.md`, and later runs feed from there too.

## Example output

`EXAMPLE-OUTPUT.md` has a full analysis the system produced for a fictional brand ("Sırma Home Textiles"): the competitor ad breakdown table, the extracted pattern, and 10 concepts. The only input was the ads of two fictional competitors. (All examples are fictional; there are no real brands, customers, or numbers.)

## Who it is for

Anyone who runs ads: e-commerce brands, performance marketers, agencies, founders, small teams, local shops. Anyone who wants to see a competitor's working ad and translate it into their own language. You do not need to design or code; the system gives text and direction, and you finish the design in Canva or with your designer.

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
