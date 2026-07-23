# Pricing Solver · Pricing Built on Competitor Data · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/pricing-solver.mdc`.
> The goal: set the price of your product or service with data actually pulled from your competitors' public pricing pages, instead of staring at the ceiling.

## Where this system stands (unchangeable)
This system takes the pricing RESEARCH off your hands and leaves the pricing DECISION with you. It opens your competitors' pricing pages itself, pulls out the tiers and the figures with their sources, lays them into a matrix, reads what the sector charges by, and proposes a justified structure. It does not order you to "set this price", and it does not say "set this price and you will sell this much".

## What the system does (two phases)
1. **Automatic price pulling (you paste nothing):** it reads the competitor names and URLs in `you/02-competitors.md`. With Claude Code's web tools (WebFetch + WebSearch) it opens the competitors' public pricing pages itself and writes the tier name, price figure, currency, billing period (monthly / annual), the metric it scales by (seat, user, volume, number of resources) and the features included in the tier, with the source URL, into `data/pulled-YYYY-MM-DD.md`. For a competitor whose price it cannot find it INVENTS NO FIGURE, it marks the row "price not public" or "could not reach the source".
2. **Analysis + price structure (automatic):** from the pulled data it builds a feature by tier matrix, works out the value axis, proposes three tiers, offers the local market adaptation as options, and writes a price change protocol. The output lands in `outputs/YYYY-MM-DD-pricing-report.md`.

## PHASE 1 · When competitor price pulling is requested
Read `you/01-product.md` (what you sell, your cost, your capacity, your limits) and `you/02-competitors.md` (the competitor list). Then, for every competitor in order:

1. **Pull directly:** if there is a URL in `you/02-competitors.md`, open it with `WebFetch`. Pull these out VERBATIM: tier name, price figure, currency, billing period (monthly and annual, with both figures if they are given separately), what the price scales by (seat / user / volume / number of resources / flat), the features included in the tier, whether there is a free tier, the trial length.
2. **If there is no URL or it returns a 404:** find the right pricing page with `WebSearch` (`<competitor name> pricing`, `site:<domain> pricing`, `<competitor name> plans`). Try `WebFetch` again on the address you found. Write the correct URL back into `you/02-competitors.md` (the source list grows).
3. **If the price is not on the page (get a quote / request a demo / contact us):** mark that competitor `price not public`. DO NOT GUESS a figure, DO NOT WRITE "it is probably in this band". That competitor takes NO PART in any average, median or band. It stays in the report only as the observation "there is a player in this segment who hides their price".
4. **If the page cannot be reached at all (404, blocked, empty content):** write `no source · could not be reached`, with the URL you tried and the error you got. That one takes no part in the average either.
5. **Local reference:** if the currency you sell in is not the currency the pulled sources publish in, pull at least two local sources the same way (products with public pricing pages that show prices in your currency). The local band, the way tax is displayed and the local packaging habit are read from those. Figures from competitors in another currency are NOT USED to produce a band in your currency.

For every competitor write these lines into `data/pulled-YYYY-MM-DD.md`: competitor · source URL · pull date · tier table (name, monthly, annual, currency, metric, included features) · status (`price pulled` / `price not public` / `no source`). One summary line at the end: from how many competitors the price was pulled, how many hide their price, how many could not be reached.

## PHASE 2 · When the pricing report is requested, read these files IN ORDER (required)
1. `you/01-product.md` · what you sell, to whom, what it costs you, what your capacity is, what you do not do.
2. `you/02-competitors.md` · which competitors were scanned.
3. `format/rules.md` · the anti invention rules, the value axis ruler, the tier building rules.
4. `format/output-format.md` · the structure the report is written in.
5. Every file in the `data/` folder · the real prices that were pulled.

Do not produce anything before reading these files. Start the job by saying "product + competitors + rules + format + pulled data read".

## Analysis steps (what the system does inside)
1. **Feature by tier matrix:** lay every tier in `data/` into one table. Row = feature, column = competitor and tier level (entry / middle / top). In every cell write at which level that feature is given. If a feature does not appear on that competitor's page, write `not stated on the page` in the cell, do not guess YES or NO. Pull two lines out from under the matrix: (a) what the sector gives at ENTRY level (that is, the thing it is hard to charge for), (b) what acts as a TOP TIER TRIGGER (that is, what people pay to move up for).
2. **Value axis:** work out from the pulled data what the price scales by. The axes usually observed are: number of seats or users, usage volume (transactions, bookings, messages, credits), number of resources (calendars, branches, providers), feature set, flat price. Write which axis each competitor uses. Then CHOOSE the axis for the operator's own business and write the reason: which number does the customer's value grow with, which number does the operator's cost grow with, and if those are not the same number, the main axis is built on the value side and the second axis on the cost side.
3. **Three tiers:** entry, middle, top. For every tier: the price, who it is for, what is in it, which feature was DELIBERATELY left out and why. The middle tier is deliberately the one you want chosen; write the mechanism you used to build that (a carrying feature left out of the entry tier, the price jump between middle and top, a top tier feature that only speaks to a large customer). GIVE NO NUMBERS about how many people will choose which tier.
4. **Local market adaptation:** the currency (fixed in your own currency or indexed), a review threshold against currency swings, whether tax is shown inside the price, the local payment habit (card, bank transfer, instalments), and a second pricing page if you have customers in another region. Write each of these NOT as a decision but as `Option A / Option B + reason + which one in which situation`.
5. **Price change protocol:** what happens to existing customers (a price lock period or a staged move), how many days ahead and through which channel they are told, at which thresholds a price rise happens, which behaviour is banned.

## Unchangeable production rules (anti invention)
- **DO NOT INVENT prices.** Use only figures actually pulled into `data/` with a source URL. If there is no data at all, say "I have no pulled prices, run PHASE 1 first" and do not produce an empty report.
- **DO NOT GUESS a hidden price.** For a competitor who does not show their price, do not produce a figure through "probably", "roughly", "in this segment it is usually". That row stays `price not public` and takes no part in any average, median or band.
- **NO sales or revenue promises.** The sentences "set this price and you will sell this much", "your conversion will be this", "your monthly revenue will be this", "this share of your customers will pick the middle tier" are BANNED. This system does not measure a demand curve, and it does not say what it has not measured.
- **DO NOT INVENT an exchange rate.** Do not use a rate off the top of your head to convert figures in different currencies into one. If you are going to use a rate, write its source and its date. If there is no source, keep the currencies SEPARATE and compare through structure (how many tiers, which axis, which feature at which level), not through the figures.
- **DO NOT WRITE a feature into a tier that is not on the page.** Saying `not stated on the page` in the matrix is fine, guessing is not.
- **IF THE PAGE CONTRADICTS ITSELF, NOTE IT.** For example if the annual total does not match the monthly price times twelve, or if the discount claim on the page does not follow from the figures listed, write that as a `contradiction note` and show the arithmetic. Do not fill the gap with your own interpretation; if you are inferring, label it `inference (not certain)`.
- **DO NOT SAY "copy it".** If a competitor's tier structure is good, do not propose taking it as it is; write which mechanism is working and build the version adapted to the operator's own business.
- **Do not offer what you are not.** Do not put a service that falls into the "I do not do this" list in `you/01-product.md` into a tier. What the operator does not offer has no place in a tier.
- **Do not give away something with a marginal cost as unlimited.** Line items that burn real money on every use, like SMS, messages, transactions and storage, can never be "unlimited" in any tier. They are written as an included quantity plus an overage price.
- **Flag the risky area.** Pricing touches payment, billing, subscription and consumer law, and the rules differ by region. On matters like automatic renewal, the right to cancel and price change notices, add a "this area needs legal confirmation" note and give no legal advice.
- **No em dash anywhere in the output.** If you need a separator, use a full stop, a comma, a colon or a middle dot (·).
- **No motivational language, no exaggeration, no hype.** The system talks like a cool headed analyst.

## Where the output is written
Write every analysis into `outputs/` as a single file: `outputs/YYYY-MM-DD-pricing-report.md`.
In it, in order: (a) the data summary and source status, (b) the feature by tier matrix, (c) the value axis analysis and the reason for the choice, (d) the three tier proposal plus what was deliberately left out, (e) the local market adaptation options, (f) the price change protocol, (g) what this report does not know.

## The competitor list grows, the price log builds up (persistent memory)
When you find a new competitor or the correct pricing page URL, add it to `you/02-competitors.md`. When you change a price, or try a price and take it back, write it with the date into the "price log" section at the bottom of `you/02-competitors.md` (what changed, why, what came of it). The system pulls the competitors' pricing pages again on every scan; the old `data/` files stay, so you also get to see your competitors' price change history.
