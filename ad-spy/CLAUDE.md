# Ad Spy · Competitor Ad Analyzer · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You do nothing. Claude Code loads it on its own while working in this folder.
> The goal: never restate your competitor's live ads from scratch every time; write your competitors once, then get a breakdown + 10 ad concepts adapted to your brand with one command.

## What the system does (two phases)
1. **Link generation (automatic):** from the competitor list in `brand/03-competitors.md`, it builds a Meta Ad Library (public) search link for each competitor. You click the link and see that competitor's currently running (active) ads.
2. **Breakdown + generation (automatic):** you paste the active ads you saw in the library into the `competitor-ads/` folder. The system breaks down each ad (hook, promise, for whom, format, proof, how long it has been running), finds the repeating pattern, then dresses that logic in your brand and voice (read from `brand/`) and produces 10 ad concepts.

> HONEST LIMIT: the Meta Ad Library is public, but there is no free automatic download (API) for commercial product ads; the ad text is visible in the browser. So the step of SEEING an ad in the library is a one-click manual "open and paste" step. The breakdown, pattern extraction, and 10-concept generation are fully automatic. Details: bottom of `format/ad-breakdown.md`.

## PHASE 1 · When a link is requested
Read `brand/03-competitors.md`. For each competitor, build the Meta Ad Library link with this template and write them one by one:

```text
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<COMPETITOR NAME>&search_type=keyword_unordered&media_type=all
```

- Put the competitor's name in place of `<COMPETITOR NAME>` (replace spaces with %20: "Yumağ Ev" -> "Yumağ%20Ev").
- If you have the competitor's page number (page id), use a more precise link: replace `q=` with `view_all_page_id=<NUMBER>`.
- `country=US` filters ads shown in the United States; if you want another country, change the two-letter code (TR, DE, GB...).
- After giving the links, tell the user in one line: "click the link, paste the active ads into `competitor-ads/<competitor>.md`, then run the analyze command."

## PHASE 2 · When a breakdown + 10 concepts are requested, read these files IN ORDER (required)
1. `brand/01-brand.md` · who, for whom, what we sell, what we are not, proof.
2. `brand/02-voice.md` · how we talk, how we address, banned words.
3. `brand/03-competitors.md` · the tracked competitors.
4. `format/ad-breakdown.md` · the headings you split each ad into.
5. `format/concept-format.md` · the structure you write the 10 concepts in.
6. all files in the `competitor-ads/` folder · the raw ads to be analyzed.

Do not produce anything without reading these. When you start, first say "brand + voice + competitors + format + raw ads read".

## Analysis steps (what the system does inside)
1. **Break down:** split each ad in `competitor-ads/` into the headings in `format/ad-breakdown.md` (hook, promise, for whom, format, proof, CTA, how long it has been running).
2. **Read the signal:** mark the ad with an older start date (running for months) as a "winning candidate". A long-running ad is running because money is being spent on it; a recently launched one may still be in the test phase.
3. **Extract the pattern:** collect the repeating hook, the common offer type, the common emotion, and who they speak to across all ads. This is "the logic that clearly works".
4. **Dress it in your brand:** adapt that logic to YOUR product and voice via `brand/01-brand.md` and `brand/02-voice.md`. Produce 10 concepts (in the structure of `format/concept-format.md`).

## Non-negotiable output rules
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite the concept from scratch.
- Never contradict the "what we are NOT" lines in `brand/01-brand.md` (do not say it just because the competitor does).
- DO NOT copy the competitor's ad. Take its logic (hook type, offer type, for whom), not its words. The output is in your brand's voice, with your offer.
- NO made-up numbers, fake discounts, or non-existent guarantees. If your offer/number is not in `brand/01-brand.md`, leave a `[put your own number/offer here]` placeholder, never invent.
- Under each concept, write a one-line "which competitor logic it came from" and "why it can land". Transparency is credibility.
- Em dash (long dash) appears NOWHERE in the output: not in concept text, not in a heading, not in a note line. If you need a separator, use a period, comma, colon, or middle dot (·).

## Where the output goes
Write each analysis as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-<competitor-or-theme>.md`.
Inside the file: (a) the competitor ad breakdown table, (b) the extracted pattern summary, (c) the 10 concepts, (d) the platform note (Instagram "you" / LinkedIn measured register).

## The competitor list grows (persistent memory)
When you notice a new competitor, add it to `brand/03-competitors.md`. The system runs again from the same links every month; the competitor list becomes the living ad memory of your industry. When a concept truly lands, write it with the date under the "angles that landed" section at the bottom of `brand/03-competitors.md`, and later runs feed from there too.
