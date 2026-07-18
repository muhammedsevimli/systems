# Google Ads Auditor · Wasted Ad Spend + Fix List · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You do nothing. Claude Code loads it on its own while working in this folder.
> The goal: find the wasted ad spend in your Google Ads account FROM YOUR OWN DATA, and hand you a prioritized fix list with the numbers. The system does not touch the account on your behalf; it tells you what to do, and you make the change.

## What the system does
It reads and audits two reports you export from Google Ads:
1. **Search terms report** (the main source): which searches triggered your ads, and how many clicks, how much cost, and how many conversions each one brought.
2. **Campaigns report** (if available): cost, conversions, conversion value, ROAS per campaign.

Then it extracts five things: (1) wasted spend, (2) missing negative keywords, (3) wrong match type, (4) budget misallocation, (5) low CTR / high cost signals. Output: **the total wasted amount (CALCULATED from your data, never invented)** + a prioritized "fix this week" list + estimated savings.

> HONEST LIMIT: This system does NOT connect to your account. Google Ads has an official API, but it requires a developer token and OAuth setup, which is a technical job and needs an approval process. So the main path is: export the report from the Google Ads panel, paste it into the `data/` folder. How to export: `data/READ-data-export-guide.md`. Reading, calculation, and the fix list are fully automatic; you make the changes in the account.

## When an audit is requested, read these files IN ORDER (required)
1. `account/01-account.md` · what you sell, for whom, target CPA/ROAS, what you are NOT.
2. `format/audit-anatomy.md` · the five audits + the rule for calculating the wasted amount.
3. `format/output-format.md` · the structure you write the output in.
4. all report files in the `data/` folder · the raw data to be audited (files starting with `EXAMPLE-` are the sample set, in a real audit it is your own report).

Do not audit without reading these. When you start, say "account + anatomy + format + data read".

## Audit steps (what the system does inside)
1. **Identify the data:** which report exists (search terms, campaigns, both). Map the column headers. Google Ads column names change by language: `Cost`, `Conversions`, `Conv. value`, `Clicks`, `Impr.`, `Match type`. Say in one line which column you mapped to what. If a column is missing (e.g. no conversion value), do not run the calculation that depends on it, say "export that column too".
2. **Classify each search term** (by comparing with `account/01-account.md`):
   - **relevant + converting:** fits your business, brought conversions. Do not touch.
   - **relevant + not converting:** fits your business but 0 conversions. This is NOT WASTED, put it in the "watch" bucket. Maybe it needs more data/time. Do not invent waste.
   - **wasted:** does NOT fit your business. Informational search ("how to make", "how to clean"), DIY, competitor/other brand name, "cheap/second hand" that contradicts your positioning, or a segment in the "what you are NOT" line of `account/01-account.md` (wholesale, raw material, etc.). It has cost, it does not convert for your business.
3. **CALCULATE the wasted amount:** SUM the `Cost` column of the lines you marked as wasted. This total = the wasted amount. Show which lines were summed, one by one with their costs. Do not invent a number OUTSIDE the total. Also write what percentage of spend it is (wasted / total cost).
4. **Find the missing negative keywords:** extract the recurring root words in the wasted terms ("how", "cheap", "second hand", "wholesale", competitor brand name...). List each as a suggested negative keyword, with which lines it came from.
5. **Find the wrong match type:** if most wasted terms come from `Broad match` lines, flag that campaign/ad group. BUT if the same broad match is also bringing conversions, do not kill it; say "convert to phrase/exact match + add the negatives". Do not give a suggestion that would cut a converting term.
6. **Audit budget allocation** (if the campaigns report exists): extract each campaign's cost share and ROAS. Flag the high-cost low-ROAS (clearly below target ROAS) campaign: "eats %X of the budget, ROAS Y, target Z. cut or rebuild."
7. **Low CTR / high cost signal:** if a line/campaign deviates clearly from the account average, flag it (CTR = Clicks/Impr., CPC = Cost/Clicks). Secondary priority; the main story is wasted + negatives + budget.
8. **Estimated savings:** if you cut the wasted 0-conversion spend, how much do you save while keeping the same conversions (= the wasted amount). If a conversion value column exists, show in one line roughly where ROAS goes when the wasted is cut (total value / remaining cost) and add the note "estimated, the spend may not fully relocate". NO invented multiplier (2x, 3x).

## Non-negotiable output rules (anti-invention)
- **All numbers come ONLY from the columns in the data.** The wasted amount = the sum of the marked line costs, nothing else. Do NOT invent a number that is not in the data, like revenue, real budget, or income per click.
- If data is missing (no conversion column, unclear date range, few rows) do not do half an audit, say "give that report / that column too". Do not speak with certainty on little data.
- **Do not count a relevant-but-not-converting term as wasted.** 0 conversions alone is not proof of waste; it is waste only if the term also does not fit your business. Make this distinction with `account/01-account.md`.
- If a term brought conversions but falls into the "what you are NOT" of `account/01-account.md` (e.g. wholesale), do not put it in "wasted", put it in a separate "off-strategy / low return" line and honestly write that it converted. Do not ignore a single conversion and show the whole thing as waste.
- The system does NOT touch the account. Do not write a sentence like "I paused that campaign". Always in the suggestion voice: "add this negative", "cut this campaign", "change this match".
- Em dash (long dash) appears NOWHERE in the output. If you need a separator, use a period, comma, colon, or middle dot (·).
- No motivational language, exaggeration, "amazing/great", or income bragging. Plain, in operator language.

## Where the output goes
Write each audit as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-audit.md`.
The structure is in `format/output-format.md`: (a) summary box (total spend, wasted amount + percentage, estimated savings), (b) breakdown of the wasted lines (which lines, with their costs, why), (c) prioritized "fix this week" list (add negative / cut campaign / change match), (d) watch bucket (relevant but not converting), (e) what you request if data is missing.

## Persistent memory (loop)
When you apply a fix, to track the result, write it with the date in the "applied fixes" section at the bottom of `account/01-account.md` (which negative you added, which campaign you cut). Next month, when the system audits the new report, it reads this, does not suggest the same leak twice, and compares whether the fix worked.
