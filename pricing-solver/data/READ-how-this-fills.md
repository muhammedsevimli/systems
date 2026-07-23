# How this folder fills up

You put nothing in here by hand. The system fills this folder.

You write your competitors' names (and the pricing page address if you know it) into `you/02-competitors.md`. Then you give the Step 1 command from `RUN.md` to Claude Code. The system opens those competitors' pricing pages itself, pulls out the tiers and the figures, and writes them in here as `pulled-YYYY-MM-DD.md`.

## What is in every pull file
- Competitor name, source URL, pull date
- Tier table: tier name, monthly price, annual price, currency, what the price scales by, the features included in the tier
- Status label: `price pulled` · `price not public` · `no source` · `partly pulled`
- A `contradiction note` if the page contradicts itself
- A summary at the end: from how many competitors the price was pulled, how many hide it, how many could not be reached

## The invention ban starts here
The system writes only the figure it REALLY saw on the page.
- If the competitor does not show their price (get a quote, request a demo): the row stays `price not public`. No guess is written. That competitor enters no average.
- If the page did not open (404, blocked): the row stays `no source`, with the address tried and the error. That one enters no average either.
- A feature that is not on the page is not written into a tier, it is marked `not stated on the page`.
- Different currencies are not converted into each other with an invented exchange rate.

## Old files are not deleted
Every pull sits there with its own date. When you run it again three months later the old file stays where it is. That way you also see your competitors' price history: who raised prices, who split a tier, who narrowed the free tier.

## How often to pull
Once a month is enough. If your sector moves fast, every two months works too. Pricing pages do not change often, but when they change, they change quietly.
