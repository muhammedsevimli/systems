# Product Breakdown Format · The PHASE 1 Output

> The system writes the site it scanned into `breakdown/breakdown-YYYY-MM-DD.md` in this structure.
> Rule: a source URL on every line. Information with no source is not written.

## A) Scan details
One table. Which page was tried, what happened.

| Page | URL | Result |
|---|---|---|
| Home page | <url> | fetched / could not be reached (reason) |
| Features | <url> | fetched / could not be reached (reason) |
| Pricing | <url> | fetched / could not be reached (reason) |
| Documentation | <url> | fetched / could not be reached (reason) |
| License / terms of use | <url> | fetched / none |

## B) The product in one sentence
What it does, for whom. In the wording on the page, without decoration. Source URL.

## C) Who it speaks to (the audience written on the page)
Item by item. The audience wording that appears on the page, verbatim. Add no interpretation; if it is not on the page, say "no audience stated on the page".

## D) Feature inventory (raw list)
Every feature named on the pages. NO sorting at this stage, sorting happens in PHASE 2.

| # | Feature | Where it appears (URL) | What it does in one sentence |
|---|---|---|---|

## E) User flow (as far as it can be read off the page)
- Sign up: how it starts, is a card required, is there a trial.
- First value moment: what does the user see first that makes them say "this works". After how many steps.
- Reason to come back: why does the user return (notifications, reports, accumulated data, the team).
Write the evidence next to every line. If it cannot be worked out from the page, write "unclear".

## F) Data model clues (raw)
Doc headings, metric definitions, settings pages, API headings. Every clue about which objects exist.

| Clue (verbatim) | Where from (URL) | Which object it points at |
|---|---|---|

## G) Pricing logic
- What the price scales by: <usage volume / number of users / number of units / feature bundle / unclear>
- Tiers and LITERAL figures: the numbers written on the page, verbatim. If there are none, "no pricing figure available".
- Free trial / free tier: is there one, how much.
- Common to every plan: <list>
- What the upper tiers unlock: <list>
Source URL mandatory.

## H) License and terms of use
If the product is open source, the license name verbatim. If not, "closed source" or "no license information on the page".

## I) Unknowns (what cannot be worked out from the site)
Item by item. This list is not left empty. For example: "it does not say how many days the data is kept", "it is unclear how many people the team plan covers".

## J) One line summary
How many pages were fetched, how many could not be reached, how many features were collected.
