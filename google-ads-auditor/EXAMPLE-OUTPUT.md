# Google Ads Audit · Jul 18, 2026

> Source: `data/EXAMPLE-search-terms.md` + `data/EXAMPLE-campaigns.md` (fictional "Oak Handcrafted Wood" sample set).
> NOTE: This is a sample set. For a real audit, put your own report in the `data/` folder, and this file is regenerated with your own data.
> Column mapping: Cost, Conversions, Conv. value, Clicks, Impr., Match type. All columns present, none missing.

## (a) Summary box

| | |
|---|---|
| Audited period | Jun 18, 2026 · Jul 17, 2026 (last 30 days) |
| Total ad spend | $4,015 |
| Wasted amount | $1,615 · 40% of spend |
| Off-strategy / low return | $260 (wholesale · 1 conversion came in, handled separately) |
| Watch bucket (relevant but not converting) | $330 (not wasted) |
| Estimated monthly savings | $1,615 (the cut lines are 0 conversions, no conversion loss) |
| Estimated ROAS (if the wasted is cut) | 11,550 / 2,400 = 4.81x (2.88x today). Estimated, the spend may not fully relocate. |

## (b) Wasted breakdown

These lines fall into the "what you are NOT" definition of `account/01-account.md`, have cost, and brought 0 conversions.

| Search term | Campaign | Match | Cost | Conv. | Why wasted |
|---|---|---|---|---|---|
| how to make a wooden cutting board | General Wood Product - Broad | Broad | 280 | 0 | informational (how) |
| how to clean a cutting board | General Wood Product - Broad | Broad | 300 | 0 | informational (how) |
| how to polish wood | General Wood Product - Broad | Broad | 160 | 0 | informational (how) |
| wooden spoon painting | General Wood Product - Broad | Broad | 95 | 0 | DIY / do it yourself (painting) |
| cheap plastic cutting board | General Wood Product - Broad | Broad | 190 | 0 | cheap + plastic, against the segment |
| second hand wooden plate | General Wood Product - Broad | Broad | 70 | 0 | second hand |
| oak lumber prices | General Wood Product - Broad | Broad | 240 | 0 | lumber / raw material |
| wood raw material | General Wood Product - Broad | Broad | 80 | 0 | raw material |
| ikea cutting board | General Wood Product - Broad | Broad | 200 | 0 | competitor / other brand |

Wasted total = 280 + 300 + 160 + 95 + 190 + 70 + 240 + 80 + 200 = **$1,615**
Percentage of total spend = 1,615 / 4,015 = **40%**.
Note: 9 of the 9 lines are from the `General Wood Product - Broad` campaign and all are `Broad match`. The leak is concentrated in a single campaign.

### Off-strategy / low return (converted but off-target, not counted as wasted)

| Search term | Campaign | Match | Cost | Conv. | Conv. value | ROAS |
|---|---|---|---|---|---|---|
| wholesale cutting boards | General Wood Product - Broad | Broad | 260 | 1 | 300 | 1.15 |

"Wholesale" falls into the "what you are NOT" of `account/01-account.md`. 1 conversion came in ($300 value) so I did not put it in wasted, but ROAS is 1.15 · far below the 4x target. Off-segment, low return. Your call: if you cut it, $260 of spend stops and $300 of value also goes.

## (c) Fix this week (in priority order)

1. **Add negative keywords (highest impact · stops $1,615/mo).**
   Add these negatives to the `General Wood Product - Broad` campaign or at the account level. Next to each, the monthly spend it stops:
   - `how` · $740 (how to make 280 + how to clean 300 + how to polish 160)
   - `lumber` · $240
   - `plastic` (or `cheap`) · $190
   - `ikea` · $200
   - `raw material` · $80
   - `painting` · $95
   - `second hand` · $70
   Total stopped = $1,615/mo. Add the negatives with a narrow root so they do not cut the converting terms.
   Optional: the `wholesale` negative ($260/mo) · but it brought 1 conversion, so add it before only if you genuinely do not want the wholesale segment.

2. **Rebuild the `General Wood Product - Broad` campaign (budget share problem).**
   This campaign eats 51.9% of the total budget ($2,085) but its ROAS is 0.79 · far below the 4x target. More than half of the budget goes here and it is losing money. Cut it and clean it. Shift the freed budget to `Cutting Board - Search` (ROAS 4.19), which runs above target.

3. **Change the match type · but keep the converting one.**
   The entire wasted amount comes from this campaign's `Broad match`. BUT there is a converting term in the same broad match: `olive wood cutting board` ($210, 3 conversions, $1,350 value, ROAS 6.43). Do not kill the broad match wholesale.
   Do: move `olive wood cutting board` to a separate `Phrase` or `Exact match` ad group (ideally under `Cutting Board - Search`), then clean or pause `General Wood Product - Broad` with negatives. That way you do not lose the converting search.

4. **(secondary) Low CTR / high CPC signal.**
   The account average CTR is 5.5%. The wasted informational terms inflate this campaign with high impressions and low return (e.g. `how to clean a cutting board` 2,000 impressions, 0 conversions; `oak lumber prices` CPC $4.0, 0 conversions). Once you do items 1 and 2, this fixes itself, no extra work needed.

## (d) Watch bucket (NOT wasted)

| Search term | Campaign | Cost | Conv. | Why watch |
|---|---|---|---|---|
| wooden serving board | Cutting Board - Search | 330 | 0 | A product that fits your business (you sell serving boards) but 0 conversions. |

This term is relevant, so I did not count it as wasted. But it did not convert either. Look again in the next audit. If it is not converting, you may need to check the landing page, price, or conversion tracking side. Do not cut it for now.

## (e) Data status / next step

- This audit was done on the sample set. **Put your own report in the `data/` folder**, and the file is regenerated with your own data. How to export: `data/READ-data-export-guide.md`.
- In the sample set all columns were complete (conversions, conversion value, date range, match type). If your own report has no conversion value column, I cannot produce the ROAS and estimated ROAS line, so export that column too.
- If you apply a fix (added a negative, cut a campaign) write it with the date in the "applied fixes" section at the bottom of `account/01-account.md`. In next month's audit I will not suggest the same leak twice, and I compare whether the fix worked (`RUN.md` Step 3 · write-back).
