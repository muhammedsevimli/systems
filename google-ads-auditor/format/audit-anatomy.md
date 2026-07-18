# Audit Anatomy · Five Audits + Calculating the Wasted Amount

> The system runs every report through these five audits. The rule: all numbers come ONLY from the columns in the data. Find the total by summing line costs; do not invent any other number.

## Audit 1 · Wasted spend (per search term · MAIN AUDIT)
Compare each search term with `account/01-account.md` and put it in one of three buckets:

- **relevant + converting:** fits your business, conversions > 0. Do not touch, working well.
- **relevant + not converting (watch):** fits your business but conversions = 0. **This is NOT wasted.** Maybe it needs more data/time or a landing page improvement. Put it in a separate "watch" bucket, do NOT count it in the total.
- **wasted:** does not fit your business. One of these intents: informational ("how to make/clean/polish"), DIY ("painting", "making"), competitor/other brand name, "cheap/second hand", or a "what you are NOT" segment from `account/01-account.md` (wholesale, lumber, raw material...). It has cost, it does not convert for your business.

**Special case · converting but off-strategy:** if a term brought conversions BUT falls into "what you are NOT" (e.g. "wholesale ..."), do NOT put it in wasted. Put it in a separate "off-strategy / low return" line, honestly write that it converted, show its ROAS. Do not ignore a single conversion and show the whole thing as waste.

### How the wasted amount is calculated
SUM the `Cost` column of the lines in the wasted bucket. This total = the wasted amount. No number outside the formula.
- Show which lines were summed one by one, with their costs (transparency).
- Also give the percentage: wasted amount / total cost.

## Audit 2 · Missing negative keywords
Extract the recurring or clearly irrelevant root words in the wasted terms. Each is a negative keyword suggestion. Example roots: `how`, `clean`, `polish`, `painting`, `cheap`, `plastic`, `second hand`, `wholesale`, `lumber`, `raw material`, competitor brand name.
- Next to each negative suggestion, write which search line(s) it came from and the total cost of those lines (how much you stop per month if you add this negative).
- Suggest the negative keyword with the narrowest possible root so it does not accidentally cut a converting term. E.g. root "clean" for "how to clean", but "plastic" is enough for "cheap plastic".

## Audit 3 · Wrong match type (broad match leak)
Check whether most of the wasted lines come from `Broad match`. If so, flag that campaign/ad group.
- Suggestion: convert broad match to `Phrase match` or `Exact match` + add the negatives.
- **Caution:** if the same broad match is also bringing a converting term (e.g. there is a broad-match but converting search in the data), do NOT kill it. Say "move the converting term to a separate phrase/exact match ad group, clean the broad match with negatives". Do not give a suggestion that would cut the converting search.

## Audit 4 · Budget misallocation (if the campaigns report exists)
Extract each campaign's cost share (campaign cost / total cost) and ROAS (conv. value / cost).
- High cost share + ROAS clearly below the target ROAS = budget misallocated. Flag it: "eats %X of the budget, ROAS Y, target is Z. cut or rebuild."
- Also name the one working well (above target ROAS): "this campaign is above target, the cut budget can be shifted here."
- If there is no campaigns report, do this audit roughly from the search-term campaigns but add the note "for a precise budget audit, give the campaigns report too".

## Audit 5 · Low CTR / high cost signals (secondary)
CTR = Clicks / Impr. CPC = Cost / Clicks. If a line/campaign deviates clearly from the account average, flag it:
- very high impressions, low CTR: the ad copy or the match is broad, showing to irrelevant people.
- very high CPC, low conversions: expensive and unprofitable.
This is a secondary priority; the main story is Audit 1-4. Show one or two of the most obvious signals, do not list them all.

## Estimated savings (only from the data)
- If you cut the wasted 0-conversion spend, savings = the wasted amount (you keep the same conversions because those lines are already 0 conversions).
- If a conversion value column exists: show in one line roughly where ROAS goes when the wasted is cut (total conv. value / remaining cost). Add the note "estimated, the spend may not fully relocate" next to it.
- **NO invented multiplier.** A claim not in the data, like "doubles it" or "grows your revenue by %30", is forbidden.

## Anti-invention summary
- Numbers only from the columns in the data. Wasted = the sum of the marked line costs.
- 0 conversions alone is not waste; it is waste only if the term also does not fit your business.
- A converting but off-strategy term goes in a separate bucket, its conversion is written.
- If data is missing, say "give that report/column", do not speak with certainty on half an audit.
- The system does not touch the account; it always speaks in the suggestion voice.
