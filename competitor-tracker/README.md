# Competitor Tracker 🧩

A system that watches your competitors for you and leaves a single report every Monday. It scans the public feeds of the competitors you choose once a week, finds what is new since last week, summarizes each item, and suggests the angle you could adapt it into for your own brand.

The report does not hand you a pile of links. For each new item it writes two things: what was published (a short summary) and how it adapts to your brand (a concrete angle). So by the time you finish reading, the idea for this week's content is already in front of you. The final call is yours: use the suggestion as is, change it, or skip it.

It runs from a single file. No setup, no keys, no cost. You type `node rakip-takip.mjs` and get the report.

> Note: the system, its files, and the reports it writes are in Turkish (this is a Turkish-first system). The code and steps below are easy to follow in any language, but the output is Turkish.

## What it does

Checking on competitors one by one is a chore that keeps getting postponed, and even when you do it, nobody sits down to answer "how would we use this?" This system ends that: it scans the feeds, filters only what is new since last week (never counts the same item twice), summarizes each new item, and suggests an adaptation angle for your brand. You just read and decide.

## What you need

- **Node.js 18 or newer.** Install it once and the `node` command works. No other package to install; the system runs with zero dependencies (Node's built-in `fetch`).
- **Your competitors' RSS addresses.** RSS is a machine-readable list of a site's or channel's new content. Most blogs offer `site.com/feed`; YouTube channels have a ready address (below).
- No terminal experience needed. You open a command line in the folder and type one line.

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads just this system:

```bash
npx degit muhammedsevimli/systems/competitor-tracker competitor-tracker
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** Open this folder in Claude Code / Cursor / Codex and say "set up this competitor tracker for my competitors". It fills in your competitor list and brand files with you.

## How to run it

Open a command line in the folder and type:

```bash
node rakip-takip.mjs
```

The system fetches each competitor's RSS, finds content new since last week, summarizes each item, produces an adaptation suggestion for your brand, and writes a `rapor-YYYY-MM-DD.md` file into the `raporlar/` folder. On screen you see a summary like:

```text
rapor yazildi: raporlar/rapor-2026-07-08.md
yeni hareket: 6 · ulasilamayan: 0 · izlenen: 5 · uyarlama: heuristik
```

On the first run, all new content from the last 7 days goes into the report. On every later run the system saves what it saw into `veri/snapshot.json`, so the same item never shows up as "new" two weeks in a row. The `veri/` and `raporlar/` folders are created on the first run; do not touch them by hand.

To see what a report looks like beforehand, the package includes a ready example: `ornek-rapor.md`.

### Offline test

Want to confirm it works without internet? One minute:

```bash
node rakip-takip.mjs --offline ornek-besleme.json
```

If today's report appears in `raporlar/`, each item has a "what was published" and a "how it adapts to your brand" line, and running it a second time says "yeni hareket: 0", the system works.

## Adding competitors

Open `rakipler.json`. It ships with representative examples: site, news, youtube, and two instagram competitors. Replace them with your own.

For RSS competitors all you need is a name and an RSS address:

```json
[
  { "ad": "Rakip A (blog)", "rss": "https://competitor-site.com/feed" },
  { "ad": "Rakip B (youtube)", "rss": "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID" }
]
```

How to find the RSS address:

- **Blog or news site:** usually `site.com/feed` or `site.com/rss`. If you open it in a browser and see XML, it is correct.
- **YouTube channel:** `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`. Get the channel ID from the channel's About page or URL (the block starting with `UC`).

Add as many competitors as you want; the system scans them all. Add a `not` field to a competitor and that note shows up in the report under the heading (a reminder like "check if this one cut prices").

### Teach the system your brand (for adaptation)

The system does not only say "what the competitor did", it says "how it adapts to your brand". To do that well, fill the three files in `marka-hafizasi/` once: `marka.md` (what you do), `kitle.md` (for whom), `ses.md` (how you talk). A few lines are enough. It still runs if you leave them empty, the suggestions are just more generic. (If you set up the Drop 1 "Brand Memory" system, you can copy the same three files here.)

Do not put customer data or private info here; only general information describing your own brand.

## Instagram tracking (two layers)

Instagram has no public RSS, so IG support comes in two layers. To add an instagram competitor, write this line in `rakipler.json` instead of an RSS:

```json
{ "tur": "instagram", "handle": "rakipmarka" }
```

`handle` is the competitor's username (leading `@` optional).

- **Layer 1, manual (default, no key, always works).** If you give no token, the system never connects to Instagram. Instead an "Instagram · manuel kontrol" section appears in the report: for each IG competitor it writes the `instagram.com/handle` link and a 2-minute checklist. You paste what you see into the blank below it, and the report is complete. This path never breaks.
- **Layer 2, automatic via Apify (optional).** To pull posts automatically instead of checking by hand, provide a token from your own Apify account. It starts on a free account, and scanning a few competitors weekly is effectively free. With a token, IG competitors are summarized and adapted just like RSS ones:

```bash
# Windows (PowerShell)
$env:APIFY_TOKEN="your-apify-token"; node rakip-takip.mjs

# Mac/Linux
APIFY_TOKEN="your-apify-token" node rakip-takip.mjs
```

If Apify does not respond or errors out, the system does not stop; that account falls back to the "manuel kontrol" section and finishes the report anyway. You can change the actor with `APIFY_IG_ACTOR` and the post count with `APIFY_IG_RESULTS`.

## Who writes the adaptation (two modes)

The `uyarlama: heuristik` or `uyarlama: ai` line on screen tells you how the suggestions were produced.

- **Heuristic mode (default, no key):** it places the content into one of five lenses (sales, system, taste, decision fatigue, owned demand) and gives you a ready starting angle. No internet or key required.
- **AI mode (optional):** give an AI key and the system passes your `marka-hafizasi/` files as context and asks for a suggestion actually written in your voice for each item. Any OpenAI-compatible provider works:

```bash
# Windows (PowerShell)
$env:AI_API_KEY="your-key"; $env:AI_MODEL="gpt-4o-mini"; node rakip-takip.mjs
```

If the AI does not respond in time, the system does not stop; it falls back to the heuristic suggestion for that item and finishes the report.

## Email delivery (optional)

Instead of opening the report file by hand every week, have it dropped straight into your inbox. No extra package needed; the email file (`eposta-gonder.mjs`) ships with the package and uses no external libraries. Give your own email account's SMTP details as environment variables and run the command with `--eposta`:

```bash
# Windows (PowerShell)
$env:SMTP_HOST="smtp.gmail.com"
$env:SMTP_USER="your-address@gmail.com"
$env:SMTP_PASS="your-app-password"
$env:SMTP_TO="where-the-report-goes@gmail.com"
node rakip-takip.mjs --eposta
```

If you use Gmail, your normal password will not work; create an "App Password" from your Google account and put it in `SMTP_PASS`. Outlook, Yandex, and your own domain work the same way. Without `SMTP_PORT` it uses 465. The report is always written to `raporlar/` as well; if the email cannot be sent, the system says so clearly and the file stays put.

## Every Monday automatically

If you do not want to run it by hand every Monday, add a weekly task in Windows Task Scheduler: program `node`, argument `rakip-takip.mjs` (add `--eposta` for email), start folder this folder. If you want it to arrive even when your computer is off, there is a server-side version too, covered in the setup guide.

## Security note

`rakipler.json` contains only public RSS addresses, no customer data, keys, or login info. Your SMTP password and AI key are never written into files; they are given only as environment variables and stay on your machine. The system reads only public feeds and sends the report only to the email address you provide.

## Who it is for

Anyone who needs to keep up with competitors but has no time: founders, creators, agencies, small teams. You do not need to code.

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
