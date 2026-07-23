# 5-Idea Report · Output Format

> The system writes every scoring run in this structure. The output goes to `outputs/YYYY-MM-DD-idea-report.md`.

## The structure of the output file (five sections)
A) Scan summary (one paragraph).
B) Score table (all ideas, four criteria + total + signal strength).
C) The top 5 ideas · detail cards.
D) Start here this week (one pick + why).
E) Eliminated and waiting (one line each).

## A) Scan summary
One paragraph: how many signals were pulled automatically from which sources (Hacker News, Reddit, web and forums), whether any source could not be reached, how many separate ideas they came down to, and which pain is strongest. Example: "6 signals were pulled automatically from Hacker News and 3 from web and forums (Reddit was rate-limited in this environment). The 9 signals came down to 5 separate ideas. The most repeated pain: <...>. The clearest money language: <...>."

## B) Score table (all ideas)
| # | Idea (one sentence) | Market | Feasibility | Competition gap | Region fit | Total | Signal |
|---|---|---|---|---|---|---|---|
| 1 | <...> | 5 | 4 | 4 | 5 | 18 | strong |
Sort descending by total. The signal column: strong / medium / weak.

## C) The top 5 ideas · detail cards
For each idea:

### Idea N · <short name> · total <x>/20 · signal <strength>
- **the idea:** <what, for whom, solving which pain. one sentence.>
- **where it came from:** <which signal or signals. how many independent sources. is there money language.>
- **scores:** market <x> · feasibility <x> · competition gap <x> · region fit <x>
  - market <x>: <one-line reason>
  - feasibility <x>: <one-line reason>
  - competition gap <x>: <what the existing solution is, where the gap is>
  - region fit <x>: <one-line reason, against the region in the profile>
- **first MVP (the smallest version you could build this week):** <one sentence. a panel, a bot, a form; what it does.>
- **risk / gap:** <the biggest uncertainty or missing piece. if the signal is weak, "confirm this first".>
- **pricing idea:** <monthly subscription / per use / one time. how you would collect it in your region.>

## D) Start here this week
Mark the top idea (or the highest scoring one you can actually build) as a single pick. Two or three sentences: why this one, what the first step is, where you would find the first 3 potential customers.

## E) Eliminated and waiting
Ideas that were scored but did not make the top 5, one line each: the idea + why it is waiting (weak signal / low feasibility / saturated market / one of your limits).

## Hard rules
- Do not invent signals or ideas; stand only on what was collected.
- Every score has a reason under it. Do not write a score without a reason.
- Do not propose a clone; write the point of difference on the competition line.
- Flag the risky field (license, regulation) and lower feasibility.
- Tone: cool-headed analyst. No motivational language, no income promises, no hype. No em dash.
- One line at the very end: "the decision is yours; this report is a ranked compass, not an order."
