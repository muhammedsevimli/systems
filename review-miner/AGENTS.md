# Review Miner · Customer Review Sales Miner · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/review-miner.mdc`.
> The goal: instead of reading the scattered customer reviews under your product one by one every time, with one command extract the repeating themes, find the most common objection, and get a sales angle + objection response + ad hook for each theme.

## What the system does (two phases)
1. **Input preparation:** you bring customer reviews into the `reviews/` folder. Two ways: (a) you paste the reviews by hand (the MAIN and reliable way), (b) you give a single public product/review page link and the system tries to open that page and read the VISIBLE reviews (best effort; if the page reviews are behind login/scroll/JavaScript it cannot read them, then you paste).
2. **Analysis + sales arsenal (automatic):** the system scans all reviews, clusters the repeating themes into three groups (why they buy, what they trust, what holds them back), finds the most common objection, then turns each main theme into sales language in your brand's voice read from `brand/`: sales angle + objection response + ad hook. Under each angle it puts the REAL review it came from (proof).

> HONEST LIMIT: on most platforms like Trendyol, Amazon, Shopify, Judge.me, reviews load into the page later (via JavaScript), on scroll, or after login. There is NO free, reliable automatic review-download path. So the MAIN way is to copy the reviews by hand and paste them into `reviews/` (a 2-minute job). Link reading works only on simple sites that show reviews as plain page text; if it does not work the system tells you to "paste", it does not invent. Theme extraction, objection finding, and sales-arsenal generation are fully automatic.

## PHASE 1 · Input preparation
- If the user pasted review TEXT: go straight to PHASE 2.
- If the user gave a LINK: try to open that single page and read the visible reviews. If the reviews are on the page as plain text, extract them and write them to a file in `reviews/`, then say how many reviews you found. If the page does not show reviews (asks for login, comes back empty, behind JavaScript) DO NOT invent; tell the user "I could not read the reviews from this page, could you copy and paste them into `reviews/`, how to do it is in `reviews/READ-paste-guide.md`".
- If there are no reviews, DO NOT start generating; at least 8-10 reviews is the lower bound of a good scan, a theme does not come from a single review.

## PHASE 2 · When an analysis + sales arsenal is requested, read these files IN ORDER (required)
1. `brand/01-brand.md` · who, for whom, what we sell, what we are not, proof.
2. `brand/02-voice.md` · how we talk, how we address, banned words.
3. `brand/03-objection-memory.md` · objections that came up before and the responses that landed (persistent memory).
4. `format/review-breakdown.md` · how you tag each review, how you cluster the themes.
5. `format/output-format.md` · the structure you write the output in.
6. all files in the `reviews/` folder · the raw reviews to be analyzed (except the guide file starting with `READ-`).

Do not produce anything without reading these. When you start, first say "brand + voice + objection memory + format + raw reviews read, N reviews found" (N = the real review count).

## Analysis steps (what the system does inside)
1. **Tag:** mark each review by the headings in `format/review-breakdown.md`: sentiment (positive / mixed / criticism), main theme, the concrete word/sentence used.
2. **Cluster:** collect the repeating themes into three groups and COUNT how many reviews each theme appears in:
   - **Why they buy:** the reason for buying, the pain solved, the triggering moment.
   - **What they trust:** which feature of the product/brand they trust (scent, texture, shipping, personal touch, result).
   - **What holds them back:** complaint, hesitation, objection, reason for return.
3. **Find the most common objection:** mark the objection that repeats most in the "what holds them back" group. This is the thing you need to answer UP FRONT on your sales page and in your ad.
4. **Translate into sales language:** for each main theme, produce in your voice via `brand/01-brand.md` and `brand/02-voice.md`: (a) sales angle, (b) objection response, (c) ad hook. The hook and angle feed from the customer's OWN words.
5. **Attach proof:** under each angle / response, put a short quote from the real review it came from. Do not write a claim without a source.

## Non-negotiable output rules (the anti-invention core)
- **DO NOT INVENT a benefit that is NOT in the reviews.** The whole power of the system is gathering the truth that came out of the customer's own mouth. A feature, result, guarantee, or emotion not mentioned in the reviews does NOT enter a sales angle. Claims with no proof in the reviews, like "rejuvenates your skin" or "in a week", are banned.
- **The objection response comes from real language.** When you answer an objection (e.g. "the jar is small"), if there is ANOTHER real customer sentence that refutes it (e.g. "I use a little, it lasts for months"), use it. Otherwise use the real offer in `brand/01-brand.md`. If neither exists, leave a `[put your own honest response / offer to this objection here]` placeholder, DO NOT invent a response.
- **NO made-up numbers, fake discounts, or non-existent guarantees.** If your number/offer is not in `brand/01-brand.md` or in the reviews, leave a placeholder.
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite from scratch.
- Never contradict the "what you are NOT" lines in `brand/01-brand.md` (even if a customer says "I would have bought it on discount", do not build that angle if you are not a discounter).
- Under each sales angle / objection response / hook, write a one-line "which reviews it came from". Transparency is credibility.
- Em dash (long dash) appears NOWHERE in the output: not in angle text, not in a heading, not in a note line. If you need a separator, use a period, comma, colon, or middle dot (·).

## Where the output goes
Write each analysis as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-<product-or-theme>.md`.
Inside the file, the structure of `format/output-format.md`: (A) scan summary, (B) theme clusters (three groups), (C) the most common objection, (D) sales arsenal (per theme: angle + objection response + hook), (E) proof trail, (F) no-invention note, (G) platform note (Instagram "you", LinkedIn measured register).

## The objection memory grows (persistent memory / self-improving loop)
When an objection response or sales angle truly works (lands in a sale, in an ad), write it to `brand/03-objection-memory.md` with the date: which objection, which response landed, which customer sentence was the source. The system runs again every month with new reviews; this file becomes the living objection-and-response memory of your industry, and later runs feed from there too.
