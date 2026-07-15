# Ad Concept Factory · 50 Static Ad Concepts 🏭

Put your brand's working ads and real customer voice into files once, and the system produces 50 fresh static ad concepts in your brand's voice every morning (or with one command). A no-code concept factory that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

The hardest part of writing an ad is the blank page. This system fills that page with the ads that already work for you and the customer's own sentences, then turns that logic into new angles. It feeds from your own proof, not your competitor's: your best-performing ads plus your real customer reviews. When you wake up, 50 concepts are ready in front of you; you move the ones you like into design and cut the rest.

## What it does

You give three inputs: (1) your brand's winning (best-performing) ads, (2) customer reviews, (3) the most-liked comments on social media. The system extracts what works from these (which hook, which promise, which emotion repeats), then dresses that logic in your brand and voice (read from `brand/`) and produces 50 static ad concepts. Each concept is three lines: hook, visual direction, one-line rationale (which winning ad or customer sentence it came from).

The 50 concepts are not filler. The system rotates on three axes: hook type (pain, sensory, number, social proof, contrarian, humor, objection-busting, ritual, comparison, gift) x segment x emotion. It does not write the same hook 50 times with the words swapped; each concept carries a single idea, and its heading shows a `[hook type · segment]` tag so the diversity is visible.

Important distinction: this system mines your OWN winning ads and customer voice, not competitor ads. If you want to crack competitor ads, that is a separate system (Ad Spy).

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting your brand and inputs into files.
- At least 3-4 winning ads, 8-10 customer reviews, 3-5 liked comments. The richer the input, the clearer the pattern.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/ad-concept-factory.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/ad-concept-factory ad-concept-factory
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this ad concept factory for my brand". It fills in the brand and input files with you.

These are the files the system reads. Fill in the brand and input part with your own:

- `brand/01-brand.md`: who, for whom, what you sell, what you are not, proof
- `brand/02-voice.md`: tone, address, words, **banned words**, sample sentences
- `brand/03-winning-memory.md`: angles that landed (starts empty, the system fills it)
- `format/input-breakdown.md`: the headings the inputs are split into (comes ready, tune if you want)
- `format/concept-format.md`: the structure and diversity rule of the 50 concepts (comes ready, tune if you want)
- `inputs/winning-ads.md`, `inputs/customer-reviews.md`, `inputs/liked-comments.md`: you paste your inputs here (the paste guide and a filled example are inside the folder)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then one command. After you fill the input files, run:

> analyze the winning ads, customer reviews, and most-liked comments in the inputs folder and produce 50 static ad concepts

The system breaks down the inputs, extracts the pattern, writes 50 diverse concepts in your voice, and puts them in the `outputs/` folder. For the full command, see `RUN.md`.

## Want it automatic every morning?

The core job runs with one command. If you want "run it while I sleep, 50 concepts ready in the morning", you set up a task that runs the same single command every morning (Windows Task Scheduler or Mac cron). Step-by-step setup: `automation/SETUP-automation.md`. There is no invisible magic automation; the every-morning file is just the scheduled form of the same single command. If you do not want that, you run the command by hand whenever you like; both give the same output.

## Does it really work? Test it in 30 seconds

- **Diversity:** are the 50 concepts genuinely different, or the same hook with the words swapped. If the `[hook type · segment]` tags in the headings rotate, it passed.
- **Voice:** did it avoid your banned words. If yes, it passed.
- **No invention:** did it invent a number, discount, or guarantee you do not have, or leave a placeholder. If it left a placeholder, it passed.
- **Proof:** did each concept's rationale line say which winning ad or customer sentence it came from. If yes, it passed.

## The winning memory grows · let the system sharpen with you

When a concept truly lands (a sale, a click, a save), say "this landed, add it to the winning memory". The system writes it into `brand/03-winning-memory.md` with the date: which hook type, why it landed, the angle to make primary next round. When a new winning ad or a very-liked comment appears, add it to the relevant `inputs/` file. As the input gets richer, the pattern gets sharper; the system resembles your business more with each round.

## Example output

`EXAMPLE-OUTPUT.md` has the full 50 concepts the system produced for a fictional brand ("Değirmen Coffee"): input summary, extracted pattern, 50 concepts split into ten groups, a morning shortlist note, and a platform note. The only input was 4 fictional winning ads, 10 customer reviews, and 3 liked comments. (All examples are fictional; there are no real brands, customers, or numbers.)

## Who it is for

Anyone who runs ads or produces ad creatives regularly: e-commerce brands, performance marketers, agencies, founders, small teams, local shops. Anyone who has a working ad and real customer reviews and wants to turn them into fresh concepts every week. You do not need to design or code; the system gives text and direction, and you finish the design in Canva or with your designer.

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
