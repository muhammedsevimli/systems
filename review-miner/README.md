# Review Miner · Customer Review Sales Miner 🔎

Paste the scattered customer reviews under your product, and the system extracts the repeating themes, finds the most common objection, and writes a sales angle, an objection response, and an ad hook for each theme. A no-code customer review sales miner that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A system that saves you from reading the reviews one by one from scratch every time you write sales copy, asking "what does my customer actually love, what trips them up". You dump the reviews into a folder once; then with one command the system builds a sales arsenal out of the customer's own words. You start not from a blank page but on top of the truth that came out of the customer's mouth.

## What it does

The hardest part of writing sales copy is the blank page. This system fills that page with the real reviews your customer is writing RIGHT NOW, then turns that truth into your brand's voice. It works in two phases:

1. **Input preparation.** You paste your product's reviews (Trendyol, Amazon, Shopify, Instagram, Google, Etsy, wherever they come from) into the `reviews/` folder. This is the main way and it works on every platform. If you have a simple site link that shows reviews as plain text, the system tries to read it too.
2. **Analysis and sales arsenal.** The system scans all reviews, clusters the repeating themes into three groups (why they buy, what they trust, what holds them back), counts how many reviews each theme appears in, finds the most common objection, and turns each main theme into sales language in your voice read from `brand/`: sales angle, objection response, ad hook. Under each angle, the real review it came from (proof).

Honest limit: on most platforms like Trendyol, Amazon, Shopify, Judge.me, reviews load into the page later (via JavaScript), on scroll, or after login. There is no free, reliable automatic review-download path. So the main way is to copy the reviews by hand and paste them into `reviews/` (a 2-minute job). Theme extraction, finding the most common objection, and sales-arsenal generation are fully automatic.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting your brand into files and pasting the reviews.
- At least 8-10 reviews that came to your product. The more reviews, the clearer the themes.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/review-miner.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/review-miner review-miner
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this review miner for my brand". It fills in the brand files with you.

These are the files the system reads. Fill in the brand part with your own, and paste the reviews:

- `brand/01-brand.md`: who, for whom, what you sell, what you are not, proof
- `brand/02-voice.md`: tone, address, words, **banned words**, sample sentences
- `brand/03-objection-memory.md`: objections that came up and responses that landed (starts empty, the system fills it)
- `format/review-breakdown.md`: how each review is tagged (comes ready, tune if you want)
- `format/output-format.md`: the structure of the sales arsenal (comes ready, tune if you want)
- `reviews/`: you paste the customer reviews here (the paste guide is inside the folder)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two steps. First paste the reviews (`reviews/READ-paste-guide.md` explains it), then analyze:

> analyze the reviews in reviews and produce a sales arsenal adapted to my brand

The system clusters the themes, finds the most common objection, and writes a sales angle, an objection response, and an ad hook for each main theme, all built from the customer's own words. For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Voice:** did it avoid your banned words. If yes, it passed.
- **Proof:** did it put the real review each sales angle came from under it. If yes, it passed.
- **No invention:** did it invent a benefit, result, or guarantee not in the reviews, or leave a placeholder. If it left a placeholder, it passed.
- **Objection:** did it mark the most common objection in the "what holds them back" group and count how many reviews it appears in. If it counted, it passed.

## The objection memory grows · let the system sharpen with you

When an objection response or sales angle truly works (lands in a sale, in an ad), say "this landed, add it to the objection memory". The system writes it to `brand/03-objection-memory.md` with the date: which objection, which response landed, which customer sentence was the source. The system runs again every month with new reviews; this file becomes the living objection-and-response memory of your industry, and later runs feed from there too.

## Example output

`EXAMPLE-OUTPUT.md` has a full sales arsenal the system produced for a fictional brand ("Reyhan Natural Care"): the scan summary, the theme clusters, the most common objection, and a sales angle + objection response + ad hook per theme. The only input was 20 reviews that came to a fictional moisturizer. (All examples are fictional; there are no real brands, customers, or numbers.)

## Who it is for

Anyone who sells a product: e-commerce brands, local shops, founders, performance marketers, agencies, small teams. Anyone with customer reviews who wants to turn them into sales copy, objection responses, and ad hooks. You do not need to design or code; the system gives text and direction, and you finish the design in Canva or with your designer.

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
