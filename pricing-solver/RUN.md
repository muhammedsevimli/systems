# RUN · Two Commands

> Pricing is two steps. Open this file and copy the relevant command.
> You paste no prices. You write your competitors' names into `you/02-competitors.md` once, and the system opens the pricing pages itself.
> Thanks to `CLAUDE.md`, Claude Code will already read the product, competitor, rules and format files.

## First (one time, 10 minutes)
1. Open `you/01-product.md`, delete the example, write your own product in. The three most important places: **your cost**, **who you sell to**, **what you do not do**.
2. Write your competitors' names into `you/02-competitors.md`. Add the URL if you know it; if you do not, the name is enough, the system finds the right page.
3. If you sell in a currency none of your competitors publish in, add at least two local products that show **public prices in your currency** to section B. The band in your currency and the way tax is displayed are read from those.

## Step 1 · Pull the competitor prices (copy)

```
pull my competitors' prices.

rules:
- read you/01-product.md and you/02-competitors.md.
- open every competitor's pricing page yourself with WebFetch. if there is no url or it returns a 404, find the right pricing page with WebSearch and fetch it again. write the correct url back into you/02-competitors.md.
- for every tier pull these out verbatim: tier name, price figure, currency, monthly and annual separately, what the price scales by (seat / user / volume / calendar / branch / flat), the features included in the tier, whether there is a free tier, the trial length.
- do not invent a figure for a competitor who does not show their price. write "price not public". that competitor enters no average.
- if you cannot reach the page write "no source", with the address you tried and the error. that one enters no average either.
- do not write a feature into a tier if it is not on the page, say "not stated on the page".
- do not convert currencies into each other, do not invent an exchange rate.
- if the page contradicts itself (a discount claim while the annual total is exactly twelve times the monthly, for example) add a contradiction note, show the arithmetic, do not fill the gap with interpretation.
- write all of it into data/pulled-TODAYS-DATE.md. one summary line at the end: from how many competitors the price was pulled, how many hide it, how many could not be reached.
```

## Step 2 · Produce the pricing report (copy)

```
turn the pulled data into my pricing report.

rules:
- first say in one line that you read the product + competitors + rules + format + pulled data files.
- build the feature by tier matrix. rows are features, columns are competitor and level. a cell that is not on the page gets "not stated on the page". pull two readings out from under the matrix: what the sector gives at entry level, and what triggers a move to the top tier.
- work out the value axis. write which axis each competitor prices on. then answer two questions separately: which number does my customer's value grow with, which number does my cost grow with. same number means one axis; different numbers mean the main axis on the value side and the second axis on the cost side. write a one line reason for every axis you did not pick.
- propose three tiers. for each: price, who it is for, what is in it, what is deliberately NOT in it and why, and which pulled figure the price came from.
- make the middle tier deliberately the one you want chosen and write the mechanism you used. give no numbers about how many people will pick which tier.
- do not give any line item with a marginal cost (sms, messages, transactions) as unlimited in any tier. write it as an included quantity plus an overage price.
- do not put any service from my "i do not do this" list into a tier.
- write the local market adaptation as options, not decisions: currency, currency review threshold, whether tax shows in the price, local payment habits, a second page for customers in another region. option a / option b / which one in which situation for each.
- write the price change protocol: what happens to existing customers, how many days ahead and through which channel, at which thresholds, which behaviour is banned.
- do not make revenue projections, do not invent conversion rates, do not say "set this price and you will sell this much". write what you do not know in its own section at the end.
- do not use em dash. write the output into outputs/TODAYS-DATE-pricing-report.md.
```

## One command (when in a hurry: pull and report together)

```
pull my competitors' pricing pages yourself with your web tools, write them into the data folder with their source urls, then build the feature by tier matrix, pick the value axis with a reason, propose three tiers and write the local market adaptation options plus the price change protocol.
do not invent a figure for a competitor who does not show their price and keep them out of the averages. make no revenue or conversion projections. put the output in the outputs folder.
```

## Note
However good the report is, the pricing decision is yours. The step after the report is this: put the three tiers on one page, talk to five real prospects, and write down where the objection comes. Put it in the price log in `you/02-competitors.md`. The system reads that too in the next report.
Run it again once a month. Old `data/` files are not deleted, so you also see your competitors' price change history.
