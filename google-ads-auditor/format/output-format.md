# Output Format · Audit Report

> The system writes the audit into the `outputs/YYYY-MM-DD-audit.md` file in this structure. The goal: the user sees the wasted spend in 30 seconds and knows what to do this week.

## (a) Summary box (at the top)
Read at a glance:
- **Audited period:** the date range in the report (write "not specified" if it is not in the data).
- **Total ad spend:** the total of the cost in the data.
- **Wasted amount:** the sum of the marked line costs + the percentage of spend. (E.g. "$1,615 · 40% of spend".)
- **Off-strategy / low return:** a separate line if any (converting but falling into "what you are NOT").
- **Estimated monthly savings:** if the wasted is cut. + where ROAS goes, if available (with the estimated note).

## (b) Wasted breakdown (transparency)
Table: search term · campaign · match type · cost · conv. · why wasted (informational / DIY / competitor / cheap-second-hand / what you are NOT).
Below the table: "Wasted total = the sum of the costs of these lines: X + Y + Z + ... = TOTAL". Show the total explicitly.
A separate small table: the off-strategy / low return lines (converted but off-target), with their ROAS.

## (c) Prioritized "fix this week" list (the real value)
Numbered, starting from the highest impact. Each item concrete and actionable:
1. **Add negative keyword:** which negatives, at which campaign/account level, how much spend you stop per month if you add them.
2. **Cut / rebuild campaign:** which campaign, why (budget share + ROAS), what to do.
3. **Change match type:** which campaign from broad match to phrase/exact, while keeping the converting term.
4. (if any) low CTR / high CPC flag.
Next to each item, the estimated impact (from the data). Since the system does not touch the account, always the suggestion voice: "add this", "cut this".

## (d) Watch bucket
Relevant but not converting terms. "These are not wasted, but they did not convert either. Look again in the next audit; you may also need to check the landing page / price / conversion tracking side." Do not confuse it with the wasted.

## (e) If data is missing / next step
If there is a missing column or report, request it here (if there is no conversion value, no campaigns report, an unclear date range). Remind the user to do the write-back with `RUN.md` Step 3 when they apply a fix.

## Language rules
- No em dash. Separators: period, comma, colon, middle dot (·).
- Plain, operator language. No exaggeration, motivation, or income bragging.
- Write numbers readably with a thousands separator ($1,615). Keep the currency as it is in the data.
- Every claim should have a data line behind it. Do not say "this is bad" without a reason.
