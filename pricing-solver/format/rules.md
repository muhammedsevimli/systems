# Rules · data quality, value axis, building tiers

This file is the system's analysis ruler. It is required reading in PHASE 2.

## 1 · Data quality labels (every competitor row gets one of these)
| Label | What it means | Does it enter the average |
|---|---|---|
| `price pulled` | there is a figure on the page and the source URL is recorded | yes |
| `price not public` | the page exists but there is no figure (get a quote / request a demo) | NO |
| `no source` | the page could not be reached (404, blocked, empty content) | NO |
| `partly pulled` | some tiers have figures, others do not | only the tier with a figure enters |

Only `price pulled` rows enter the average, median and band calculations. The number of rows left out is written into the report. If there are fewer than two valid figures in hand, do not produce a band, write "not enough data".

## 2 · The value axis ruler
What the price scales by is called the value axis. The main axes observed:

| Axis | The price grows with | When it fits | Its risk |
|---|---|---|---|
| Seat / user | the number of people in the system | when the value is produced per person | the customer shares an account, part time staff get punished |
| Usage volume | transactions, messages, bookings, credits | when the cost grows with every use | the customer fears a surprise bill and starts using the product LESS |
| Resource count | calendars, branches, locations, providers | when the value grows with physical capacity | a small customer hits the ceiling straight away |
| Feature set | the capability put into the tier | when the capabilities separate cleanly | on its own it takes no share from a growing customer |
| Flat single price | does not grow | when the product does one job and the customers are alike | a big customer pays the same as a small one |

**The axis choosing rule:** answer two questions separately.
1. Which number does the customer's value grow with when it grows.
2. Which number does your cost grow with when it grows.
If it is the same number, build one axis. If they are different, the MAIN axis is built on the value side and the SECOND axis closes the cost side (included quantity plus overage price). Making the cost side the main axis pushes the customer to use the product less, which lowers the value the product carries.

## 3 · Tier building rules
- **Three tiers.** Fewer stops you taking a share from a growing customer, more causes decision paralysis. If there is an enterprise need, the fourth box is "let us talk", with no figure written.
- **A "who it is for" line is mandatory in every tier.** If a tier does not match a customer profile, it is not a tier.
- **What was deliberately left out is mandatory.** Under every tier there is a "deliberately not in this tier" list with a one line reason per item. If a reason cannot be written, that feature goes into the tier.
- **The carrying feature goes in the middle tier.** The carrying feature is the thing that solves the customer's actual problem. The entry tier introduces the product, it does not hand over the carrying feature in full.
- **The jump between middle and top is visible.** Only what a large customer needs goes into the top tier (multiple branches, brand removal, API, priority support). A small customer looking at the top tier should say "I do not need any of this".
- **Nothing with a marginal cost is unlimited.** SMS, messages, transactions, storage: included quantity plus an overage unit price. Writing "unlimited" hands your cost over to the customer's behaviour.
- **Floor check.** The entry tier price cannot go below the variable cost of serving that customer. Read the cost section of `you/01-product.md`, and warn if it does.
- **The annual discount band is read from the data,** not made up. Compute the real discount percentage from the annual and monthly figures of the pulled competitors and write the band.

## 4 · Banned sentences (if one of these enters the output the report is void)
- "Set this price and you will sell this much."
- "Your conversion rate will be roughly this."
- "Your monthly revenue will be this", "with this many customers you reach this turnover."
- "This share of your customers will pick the middle tier."
- "This competitor is probably in this band."
- "If we take the rate as roughly this" (unless it is sourced and dated).
- "Build the competitor's tier exactly."

The system does not measure a demand curve. It does not say what it has not measured. If a question cannot be answered with the data, the answer is "I cannot know this with this data, you will know it if you measure that".

## 5 · When "not enough data" is said
- If there are fewer than two `price pulled` competitors: no band and no median are produced, only structural analysis.
- If the operator did not write their cost: no floor check is done, and a "no cost information given" note is added.
- If a local reference could not be pulled: no figure is proposed in that currency, the structure proposal is given independent of currency, and the gap is written out plainly.
- If the operator did not write who they sell to: tier profiles are not built.

## 6 · Legal boundary
Pricing touches subscription, automatic renewal, cancellation rights, distance selling and tax rules, and those rules differ by region and by what you sell. The system offers observations and options on these matters, it does not give legal advice. On automatic renewal, price change notices and refund terms, a "this clause needs legal confirmation" note is added to the report.
