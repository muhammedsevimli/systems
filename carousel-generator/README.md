# Carousel + Hook Generator 🧩

Give a topic, and the system writes 3 cover hooks and a 7-slide carousel in your brand's voice. A no-code carousel generator that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A system that saves you from restating your brand, tone, and slide structure for every carousel. You fill the brand files once; then you give a one-line topic, and the system writes the full carousel to your format and voice.

## What it does

When you write an Instagram or LinkedIn carousel, you no longer set up "who we are, how we talk, how many slides, what the cover should be" from scratch. The system keeps your brand core and the carousel format in five files, and your AI tool reads them automatically on every launch. You just give the topic:

1. It produces **3 hooks** (pain angle, number angle, contrarian angle). Each can be the cover slide, you pick one.
2. It writes **7 slides**: cover + 5 body + close (one clear CTA). A "visual:" note for the designer under each slide.
3. It gives a **LinkedIn translation**: the same slides in a more measured tone.

When an angle lands, you say "this landed", and the system writes it to the swipe-file and uses it as an example on the next carousel.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just putting your brand into files.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/carousel-generator.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/carousel-generator carousel-generator
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this carousel generator for my brand". It fills in the brand files with you.

These are the files the system reads on every carousel. Fill in the brand part with your own brand:

- `brand/01-brand.md`: who, for whom, what you sell, what you are not, proof
- `brand/02-voice.md`: tone, address, words, **banned words**, sample sentences
- `brand/03-swipe.md`: hooks and angles that landed (starts empty, grows with every piece that works)
- `format/carousel-format.md`: slide anatomy and the slide-count rule (comes ready, tune if you want)
- `format/hook-patterns.md`: the hook formula bank (comes ready, tune if you want)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `GENERATE.md` stay as they are, no need to change them.

Then just give the topic:

> make a carousel about: why a small business can sell without discounting

The system reads the five files and writes 3 hooks + 7 slides + visual notes + a LinkedIn translation. You gave it not one word of brand or format info. For the full command, see `GENERATE.md`.

## Does it really work? Test it in 30 seconds

- **Voice:** did it avoid your banned words. If yes, it passed.
- **Format:** is the cover a scroll-stopper, is the last slide a single CTA, is there a "visual:" line on every slide. If yes, it passed.
- **Proof:** did it put a made-up number, or leave a placeholder. If it left a placeholder, it passed.
- **Write-back:** say "that angle landed, save it". If it added it to the top of `brand/03-swipe.md`, it passed.

## Swipe-file · let the system grow with you

When a hook or angle works well (saves, comments, shares), say "this landed". The system writes it to the top of `brand/03-swipe.md` with the date. This way the earned-tactics file grows with every carousel, and the system gets closer to your work.

## Example output

`EXAMPLE-OUTPUT.md` has a full carousel the system produced for a fictional brand ("Meydan Bakery"), with nothing but a one-line topic in the prompt. (All examples are fictional.)

## Who it is for

Anyone with a brand who makes carousels: founders, creators, agencies, small teams, local shops. You do not need to design or code; the system gives text and visual direction, and you finish the design in Canva or with your designer.

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
