# Ad Concept Factory · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> The same rule lives in `CLAUDE.md` for Claude Code and in `.cursor/rules/ad-concept-factory.mdc` for Cursor.
> The goal: put your brand's working ads and customer voice into files once; then with one command (or automatically every morning) get 50 fresh static ad concepts in your brand's voice.

## What the system does (single flow)
You give three inputs: (1) your brand's winning (best-performing) ads, (2) customer reviews, (3) the most-liked comments. The system extracts what works from these (which hook, which promise, which emotion repeats), then dresses that logic in your brand and voice (read from `brand/`) and produces **50 static ad concepts**. Each concept is three lines: hook + visual direction + one-line rationale. The output is written as a single file in the `outputs/` folder.

> IMPORTANT DISTINCTION: this system mines your OWN winning ads and customer voice (not competitor ads). If you want to crack competitor ads, that is a separate system (Ad Spy). The input here is your own proof: your best ads + your real customer sentences.

## PHASE · When 50 concepts are requested, read these files IN ORDER (required)
1. `brand/01-brand.md` · who, for whom, what we sell, what we are not, proof.
2. `brand/02-voice.md` · how we talk, how we address, banned words.
3. `brand/03-winning-memory.md` · angles marked as landed in previous rounds (if any).
4. `format/input-breakdown.md` · the headings you split the inputs into.
5. `format/concept-format.md` · the structure and diversity rule you write the 50 concepts in.
6. `inputs/winning-ads.md` · your brand's best-performing ads.
7. `inputs/customer-reviews.md` · real customer reviews.
8. `inputs/liked-comments.md` · the most-liked comments on social media.

Do not produce anything without reading these. When you start, first say "brand + voice + winning memory + format + winning ads + customer reviews + liked comments read".

## Analysis steps (what the system does inside)
1. **Break down:** split each winning ad in `inputs/` into the headings in `format/input-breakdown.md` (hook, promise, for whom, emotion, format, proof). Collect the repeating pain, praise, and objection from the customer reviews. Extract the viral angle (humor, righteous anger, "wow" moment) from the liked comments.
2. **Read the pattern:** which hook type keeps landing (pain / sensory / number / social proof / contrarian / humor), what the common promise type is, what the common emotion is, which objection appears often. This is "the logic that clearly works". The customer's own sentence is the strongest hook: use it as raw material.
3. **Dress it in your brand:** adapt that logic to YOUR product and voice via `brand/01-brand.md` and `brand/02-voice.md`. Produce 50 concepts (in the structure and diversity rule of `format/concept-format.md`).

## Non-negotiable output rules
- **The 50 concepts must be TRULY diverse, not filler.** Do not write the same hook 50 times with the words swapped. Follow the rotation grid in `format/concept-format.md` (hook type x segment x emotion). Each concept carries a single idea.
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite the concept from scratch.
- Never contradict the "what we are NOT" lines in `brand/01-brand.md`. If an ad or review contains fake urgency, exaggeration, or a non-existent guarantee, do NOT copy it; take the logic, not the language.
- NO made-up numbers, fake discounts, or non-existent guarantees. If your offer/number is not in `brand/01-brand.md`, leave a `[put your own number/offer here]` placeholder, never invent.
- If you use a customer review as a direct quote, take it from a real review, never invent one. If the input is empty, do not produce concepts; say "fill in the input files first".
- In each concept's "rationale" line, state which winning ad or which customer sentence it came from. Transparency is credibility.
- Em dash (long dash "—") appears NOWHERE in the output: not in a hook, not in a visual direction, not in a rationale, not in a heading, not in the final "morning shortlist" / summary note. If you need a separator, use a period, comma, colon, or middle dot (·).
- **FINAL SCAN (mandatory, right before writing the file):** scan all the text you produced end to end for em dashes (—). If you find even one, replace them all with a middle dot ( · ), then write the file. Summary and shortlist notes included, no exceptions.

## Where the output goes
Write each round as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-<theme-or-morning>.md`.
Inside the file: (a) input summary + extracted pattern, (b) 50 concepts (grouped by rotation headings), (c) a "morning shortlist" note (which 5 concepts you start with), (d) a platform note (Instagram "you" / LinkedIn measured register).

## Persistent memory (self-improving loop)
When a concept truly lands (a sale, a click, a save), write it with the date under the "angles that landed" section at the bottom of `brand/03-winning-memory.md`. Later rounds read this section too; the system resembles your business more with each round. When a new winning ad or a very-liked comment appears, add it to the relevant `inputs/` file: as the input gets richer, the pattern gets sharper.

## Automation note (honest)
The core job runs ON-DEMAND with one command: give the `RUN.md` Step 1 command and 50 concepts land in `outputs/`. If you want "leave it on my desktop every morning", you set up a task that runs this single command automatically every morning (Windows Task Scheduler or Mac cron). Setup: `automation/SETUP-automation.md`. There is no invisible magic automation: the every-morning file is just the scheduled form of the same single command.
