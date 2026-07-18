# Trend Radar · Rising Content Angles in Your Niche 📡

Write your niche once, and the system pulls the titles that rose the most in that niche's Reddit communities over the last week on its own. It extracts the repeating hook patterns, sorts them hottest to coldest, and writes a "make this week" brief in your brand's voice. A no-code content trend radar that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A system that ends the weekly "what should I talk about" problem. You put your niche into a file once; then with one command the system extracts the working content angles from real community data and dresses them in your topic and tone. You start not from a blank idea but on top of the problem people are actually talking about that week.

## What it does

The hardest part of making content is "what do I make this week". This system fills that gap with the titles landing the most in your niche's communities RIGHT NOW, then turns that logic into your brand. It works in two phases:

1. **Reddit scan (automatic, real).** It pulls the top rising titles of the last week for each subreddit in `target/01-niche.md` from Reddit's public RSS feed (`top/.rss?t=week`). This step is real and fully automatic: RSS is free, needs no account or key, and has no setup. You do not even click, no manual pasting.
2. **Angle extraction and brief.** It reads the pulled titles (and, if you want, the YouTube/TikTok/Reels examples you paste by hand), extracts the repeating hook patterns, angles, and formats, sorts them hottest to coldest, and writes a "make this week" brief in your brand's voice. For each angle: which hook works, its proof (how many titles repeated it, where it sits in the feed, which community), how it maps to your niche, a sample title, and a format suggestion.

Honest limit: Reddit closed its keyless `.json` endpoint (it now returns `403`), but the public RSS feed is still open and returns `200` without a key; that is why the system uses RSS. RSS has no vote (upvote) count, and the system does not invent one; it reads heat from two real signals: frequency (how many titles repeat the same hook) and feed order (`top/.rss` is already sorted, the top one landed most that week). For YouTube/TikTok/Reels there is no free reliable automatic path; those are an optional "open and paste" layer. An optional Reddit OAuth path for advanced users who also want the vote count is at the bottom of `CLAUDE.md`.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required (the system does the Reddit pull with `curl` itself and hands you the command).
- A folder and 15 minutes. You are not learning anything new, just putting your niche and brand into files.
- An internet connection. Reddit RSS is public, no account needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/trend-radar.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/trend-radar trend-radar
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this trend radar for my niche". It fills in the niche and brand files with you.

These are the files the system reads. Fill in the niche and brand part with your own:

- `target/01-niche.md`: your language/country, your niche in one sentence, the subreddits to scan (at least 3), optional search terms
- `brand/01-brand.md`: who, for whom, which platform/format, what you make, **what you are NOT**
- `brand/02-voice.md`: tone, address, words, **banned words**, sample titles
- `format/trend-analysis.md`: how it extracts hook patterns + the brief structure (comes ready, tune if you want)
- `data/`: the system writes the Reddit data here itself; you paste optional YouTube/TikTok/Reels examples here (the guide is inside the folder)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First scan your niche:

> scan my niche's reddit communities

The system pulls each subreddit's RSS feed itself and writes the top rising titles into the `data/` folder. You do not click. Then get the brief:

> analyze the titles in the data folder and write me a "make this week" brief

The system groups the titles by hook pattern, sorts them hottest to coldest, and writes the top 3-4 angles in your voice with a sample title. For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Data:** are the titles real. Did the system write the HTTP code and how many titles it pulled into the `data/` file, are there invented titles. If it did a real pull, it passed.
- **Heat:** did it invent a vote count, or did it read heat from frequency (repeat count) + feed order. If it read from the signal, it passed.
- **Pattern:** did it copy the English title as is, or take the pattern underneath it and translate it into your niche. If it took the pattern, it passed.
- **Lane:** did it suggest "make this" for a trend that falls under "what you are NOT", or write what it saw but why it skipped it. If it skipped it, it passed.

## The radar sharpens · let the system grow with you

When you notice a new subreddit or search term, add it to `target/01-niche.md`. The system scans the same communities again every week; the list becomes the living trend memory of your niche. When you actually produce an angle and see its result (landed or not), say "this landed / did not land". The system writes it with the date under the "angles that landed" section at the bottom of `target/01-niche.md`, and later briefs feed from there too.

## Example output

`EXAMPLE-OUTPUT.md` has a full brief the system produced for a fictional "houseplant care" content creator: the data summary, the hottest-to-coldest angle list (with frequency + feed order proof), the "make this week" top 4, and the skipped ones. The input was real titles pulled live from Reddit on 18 July 2026 (83 titles, 4 subreddits). The brand is fictional; the Reddit titles are real public post titles (no usernames or personal data).

## Who it is for

Anyone who makes content: YouTubers, short-video makers, social media managers, founders, small shops, teams. Anyone who wants to end the weekly "what do I make" problem and start not from a blank idea but on top of the problem people are actually talking about that week. You do not need to design or code; the system gives you the topic and angle, and you finish the production on your own line.

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
