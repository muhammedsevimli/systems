# RUN · One Command

> The audit is one step. First export the report from Google Ads and put it in the `data/` folder (how: `data/READ-data-export-guide.md`), then run this command.
> Thanks to `CLAUDE.md`, Claude Code will already read the account + anatomy + format files.

## Step 1 · Prepare the report (not a command, done by hand)
1. Fill in `account/01-account.md` with your own business (what you sell, for whom, target ROAS/CPA, what you are NOT). Filled-in example: `account/EXAMPLE-01-account.md`.
2. Export the **Search terms report** from Google Ads (and the **Campaigns report** too, if available), paste it into the `data/` folder. How to export: `data/READ-data-export-guide.md`.

## Step 2 · Audit the account (copy)

```
audit my google ads account. read the reports in the data folder, find my wasted ad spend and produce a prioritized fix list.

rules:
- first say in one line that you read the account + anatomy + format + data files.
- classify each search term: relevant+converting / relevant+not-converting (watch) / wasted (does not fit the business).
- calculate the wasted amount ONLY by summing the cost column of the marked lines. show which lines you summed with their costs. write what percentage of spend it is.
- do not count a relevant-but-not-converting term as wasted, put it in a separate "watch" bucket.
- find the missing negative keywords: the recurring root words in the wasted terms.
- if the wasted mostly comes from broad match, flag that campaign but do not give a suggestion that would cut a converting term.
- if the campaigns report exists, find the high-cost low-roas campaign, write its budget share and roas.
- derive the estimated savings ONLY from the data, do not use an invented multiplier.
- do not invent any number that is not in the data. if data is missing say "give that report/column too".
- write the output to the outputs/ folder as YYYY-MM-DD-audit.md. do not use em dashes.
```

## Short version (when in a hurry)
```
audit the google ads reports in the data folder. calculate the wasted spend by summing line costs, extract the missing negatives and the high-cost low-return campaign, give a prioritized fix list. only from the data, no inventing. write the output to outputs/.
```

## Step 3 · When you apply a fix (copy)
```
i applied this fix: <added a negative / cut the campaign / changed the match type>. add it to the "applied fixes" section of account/01-account.md with today's date. when you audit the new report next month, take this into account, do not suggest the same thing again, compare the result.
```

## Note
The longer the date range you export, the more accurate the audit. Last 30 days is a good start. With few rows (fewer than 10 search terms) the ranking comes out weak. Always include the conversions and conversion value columns; without them, separating the wasted from the converting gets hard.
