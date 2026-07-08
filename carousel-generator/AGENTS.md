# Carousel + Hook Generator · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/carousel-generator.mdc`.
> The goal: never restate your brand, voice, and topic from scratch for every carousel; get slides + hooks with one command.

## When a carousel is requested, read these files IN ORDER (required)
1. `brand/01-brand.md` · who, for whom, what we sell, what we are not, proof.
2. `brand/02-voice.md` · how we talk, how we address, banned words.
3. `brand/03-swipe.md` · angles and hooks that landed before (the earned-tactics file).
4. `format/hook-patterns.md` · the hook formula bank.
5. `format/carousel-format.md` · slide anatomy and the slide-count rule.

Do not produce a carousel without reading these five files. When a topic is given, first say "brand + voice + swipe + format read".

## Generate command
The user runs the command in `GENERATE.md` or simply says "make a carousel about: <topic>".
Output ALWAYS follows the structure in `format/carousel-format.md` and the tone in `brand/02-voice.md`.

## Non-negotiable output rules
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite the slide from scratch.
- Never contradict the "what we are NOT" lines in `brand/01-brand.md`.
- Produce 3 hooks per carousel (different angles: pain, number, contrarian). The user picks one.
- The cover (first slide) must stop the scroll. The last slide is one clear CTA. Middle slides carry one idea each, 2-3 short sentences per slide.
- NO made-up numbers, no fake references. If you need proof, pull it from the proof line in `brand/01-brand.md`; otherwise leave a "[put your own number here]" placeholder, never invent.
- The visual note (a "visual:" line under each slide) directs the designer/Canva; the system does not design, it gives text + direction.
- Em dash (long dash) appears NOWHERE in the output: not in slide text, not in a heading, not in a note/separator line. If you need a separator, use a period, comma, colon, or middle dot (·).

## Where the output goes
Write each run as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-<topic-slug>.md`.
Inside the file: the 3 chosen hooks + slide-by-slide text + visual notes + platform note (IG/LinkedIn).

## Write back when a new angle lands (write-back)
If a hook or angle worked well (the user says "this landed"), add it to the top of `brand/03-swipe.md` with the date.
This way the swipe-file (earned-tactics file) grows with every carousel, and the system gets closer to your work.
