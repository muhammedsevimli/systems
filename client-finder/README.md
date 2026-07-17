# Client Finder · Prospect Finding + First Message 🔦

Write your niche once, and the system builds Meta Ad Library links. Paste the brands running ads in that niche right now, and the system reads which of them has a budget, ranks the prospects, and writes each one a first message built on a specific detail from their own ad. A no-code prospect finder that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

The hardest part of finding clients is not knowing who to write to. This system builds that list from brands running ads: if they are running ads, they have a budget. You put your niche into a file once; then two commands give you a ranked prospect list and a tailored first message for each one. You start not from an empty list but from brands that are clearly spending money.

## What it does

There are two reasons a cold message goes to the trash: writing to the wrong person, and writing the same thing to everyone. This system closes both. It works in two phases:

1. **Link generation.** It builds a Meta Ad Library (public) search link for each search term in `target/01-niche.md`. You click the link and see the brands currently running ads in that niche.
2. **Ranking and messages.** You paste the brands you saw into the `prospects/` folder. The system breaks down each prospect (what they sell, how long they have been running ads, how many variants, what their weak point is), scores them on three axes (budget signal + how solvable the weakness is with your service + fit with your price range), ranks the prospects, and writes a TAILORED first message for each. Under every message: a "which observation came from which ad" and "why they might reply" line.

The anchor of the ranking is the budget signal. An ad running uninterrupted for months is running because it makes money; a single two-week-old ad may still be in the test phase. The system separates the two and writes the score with its reasoning, so you can make your own call when you disagree.

Honest limit: the Meta Ad Library is public and free, but there is no free automatic download for product ads. The ad text is visible in the browser; so the "seeing a brand" step is a one-click open-and-paste job. The breakdown, budget signal reading, scoring, ranking, and message generation are fully automatic.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting your service and niche into files.
- A browser to open the Meta Ad Library. No account needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/client-finder.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/client-finder client-finder
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this client finder for my service". It fills in the service and niche files with you.

These are the files the system reads. Fill in the service and niche part with your own:

- `brand/01-service.md`: what you sell, to whom, packages + real price range, which weak point you solve, what you are NOT
- `brand/02-voice.md`: tone, register, words, **banned words**, sample sentences
- `target/01-niche.md`: which niche, which country you are prospecting in + search terms (the system builds links from these)
- `format/prospect-breakdown.md`: the headings each prospect is split into + the ranking score (comes ready, tune if you want)
- `format/message-format.md`: the structure of the first message (comes ready, tune if you want)
- `prospects/`: you paste the brands you saw in the library here (the paste guide is inside the folder)

Next to every file you have to fill in there is a filled-in fictional example (`brand/EXAMPLE-01-service.md`, `brand/EXAMPLE-02-voice.md`, `target/EXAMPLE-01-niche.md`, `prospects/EXAMPLE-prospects.md`). If you get stuck, look at the example.

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First get the links:

> build the meta ad library links for my niche

Click the link, paste the brands you see into `prospects/<niche>.md` (how to paste is in `prospects/READ-paste-guide.md`). Then rank:

> analyze the brands in the prospects folder, give me a ranked prospect list and a tailored first message for each one

The system breaks down the prospects, scores them, ranks them, and writes the messages. For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Budget signal:** did it mark the brand running ads for months as "has budget" and treat the two-week-old brand as the test phase. If it separated them, it passed.
- **Tailored:** does every message have a SPECIFIC detail from that brand's ad, or does it say "I saw your ads". If the detail is there, it passed.
- **Honesty:** did it inflate a prospect that is not your work, or did it say "this is outside your niche, do not write". If it filtered honestly, it passed.
- **Voice:** did it use one of your banned words or bulk-send language. If not, it passed.
- **No inventing:** did it invent a reference or number you do not have, or leave a placeholder. If it left a placeholder, it passed.
- **One question:** does the message end with one clear question, or a pile of options. If it is one question, it passed.

## The niche list grows · let the system sharpen with you

When you notice a new search term or niche, add it to `target/01-niche.md`. Write the word the audience actually uses, not the corporate definition; one term means one list. When a message actually gets a reply, say "this got a reply". The system writes it with the date at the bottom of `target/01-niche.md` (which weak point, which sentence landed), and later runs feed from there too.

## Example output

`EXAMPLE-OUTPUT.md` has a full run the system produced for a fictional service (someone producing ad creative for e-commerce brands): the breakdown table of 6 prospects, the ranked list with the score breakdown, and a tailored first message for four of them. Two prospects have no message, and the reason is written out. The only input was the ads of 6 fictional brands. (All examples are fictional; there are no real brands, people, or numbers.)

## Who it is for

Anyone looking for clients: freelancers, agencies, consultants, small studios, people just starting to sell a service. If you sell a service to brands that run ads (creative, copy, design, video, ad management, e-commerce ops), it is directly useful. You do not need to code; the system gives you the list and the message, and you do the sending.

This is not a bulk messaging tool. No automatic sending, no buying lists, no copy-paste templates. The system exists so you can write a small number of prospects a message worth reading.

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
