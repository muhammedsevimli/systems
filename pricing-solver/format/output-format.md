# Output format · how the pricing report is written

> The system writes `outputs/YYYY-MM-DD-pricing-report.md` in exactly this structure. No section is skipped. If there is no data for a section, the section is not deleted, "no data, here is why" is written under it.

## Title
`# Pricing Report · <product name> · <date>` and one line under it: how many competitors were scanned, how many prices were pulled, how many hide their price, how many could not be reached.

## A · Data summary and source status
Table: competitor · source URL · status label (`price pulled` / `price not public` / `no source` / `partly pulled`) · price axis · currency.
Under it: which rows were kept out of the average and why. Contradiction notes go here.

## B · Feature by tier matrix
Row = feature, column = competitor and level. Cell values: `entry`, `middle`, `top`, `none`, `not stated on the page`.
Two readings under the matrix:
1. **Given at entry level in the sector:** it is hard to charge separately for these.
2. **Top tier triggers:** the things people pay to move up for.

## C · Value axis
- One line per competitor on the axis they use.
- Two questions for the operator's business: which number does the value grow with, which number does the cost grow with.
- The main axis chosen + the reason. If a second axis is needed, that one + its reason.
- The axes not chosen and why not (one line each).

## D · The three tier proposal
A separate card for every tier:
- **Name and price** (currency and tax display clear, billing period clear)
- **Who it is for** (one sentence, a concrete profile)
- **What is in it** (item by item)
- **Deliberately NOT in this tier** (item + one line reason)
- **What the price stands on** (which pulled figure, by which logic; referencing the source row)

Under the cards:
- **Why the middle tier is the one you want chosen** (the mechanism is written: the carrying feature left out of the entry tier, the jump between middle and top, the top tier only speaking to a large customer). NO percentage or count estimate is written.
- **Floor check:** is the entry tier above the variable cost.
- **Risky deviations:** the places where you knowingly moved away from the sector norm, and the fallback plan if an objection comes.

## E · Local market adaptation (options, not decisions)
Every heading in the form `Option A / Option B / which one in which situation`:
1. Currency (fixed in your own currency, or indexed to another)
2. Currency swings and the review threshold
3. Should tax be visible in the price (one figure with tax included, or `+ tax`)
4. Local payment habits (card, bank transfer, instalments) and annual billing
5. A second pricing page if you have customers in another region
The reason in every item is tied back to pulled local data. If there is no local data, "no local reference could be pulled" is written and no figure is proposed.

## F · Price change protocol
- What happens to existing customers (a price lock period or a staged move, pick one)
- How many days ahead, through which channel
- At which thresholds a price rise happens (no rise until at least two thresholds happen together)
- Banned behaviour (a silent rise, narrowing the limits at the same price)
- The places that need a "this clause needs legal confirmation" note

## G · What this report does not know
The honesty section. Here the system writes plainly:
- Demand was not measured. This report reads the competitors' structure and the cost, it does not know how many people will pay how much.
- The figures of the competitors who hide their prices are unknown.
- The pulled pages are date stamped, a competitor may have changed their price.
- The next step: ask a real buyer about the price, and measure where the objection comes in the sales conversation.
