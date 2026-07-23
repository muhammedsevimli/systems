# Example Output · One Full Report

> This is the output of a real run. Input: `you/EXAMPLE-01-product.md` and the competitor list in `you/02-competitors.md`.
> Fictional operator: Chairtime, a solo operator selling an online booking page with automatic reminders to small local businesses.
> The competitor prices are real. They were pulled live from public pricing pages on 26 July 2026 and the source links were kept (`data/EXAMPLE-pulled-2026-07-26.md`).
> Every run writes one file into `outputs/`. What follows is that file.

---
---

# Pricing Report · Chairtime · 2026-07-26

6 sources scanned. 4 prices pulled. 1 does not show its price publicly (Zenoti). 1 pricing page returned no usable data (Fresha). Only the 4 sources whose prices were pulled entered the average, median and band calculations.

Files read: `you/01-product.md` · `you/02-competitors.md` · `format/rules.md` · `format/output-format.md` · `data/pulled-2026-07-26.md`

---

## A · Data summary and source status

| Source | Source URL | Status | Price axis | Currency |
|---|---|---|---|---|
| Calendly | calendly.com/pricing | `price pulled` | per seat | USD |
| Setmore | setmore.com/pricing | `price pulled` | per user + volume ceiling on the free tier | USD |
| SimplyBook.me | simplybook.me/en/pricing | `price pulled` | booking volume + provider count | EUR |
| Acuity Scheduling | acuityscheduling.com/pricing | `price pulled` | number of calendars | USD |
| Zenoti | zenoti.com/pricing | `price not public` | could not be read | could not be read |
| Fresha | fresha.com/for-business/pricing | `no source` | could not be read | could not be read |

**Left out of the calculations, and why**
- **Zenoti:** the page opened, there is not a single figure in any currency, and the visitor is pushed to a quote and a demo. No figure was guessed. Left outside the band. One observation remains: at the top end of this segment there is a player who hides the price and prices through a sales conversation.
- **Fresha:** the pricing page was fetched but the returned content had no fee, commission rate or subscription figure. No comment was made along the lines of "it probably takes a commission", the row stayed `no source`.
- **The enterprise rows:** Setmore, SimplyBook and Acuity have no figure on their enterprise tiers. Calendly's Enterprise row gives a lower bound ("starts at $15k/year"), not a single tier price. None of them entered the band.
- **Calendly's monthly figures:** the page says "monthly billing is priced higher" but gives no figure. `not stated on the page`, not guessed.

**Outlier note (Setmore):** the annual price is $5/user and the monthly price is $12/user, which is roughly a 58 percent annual saving. Every other page in the set states 16 to 20 percent. The figure was not corrected and was not treated as an error; it was flagged as an outlier and kept out of the annual discount band. `inference (not certain)`: a gap that wide usually means the annual and monthly tiers are not exactly the same product, but the page does not say that, so it was not treated as settled.

**What came out as numbers (from the pulled data only)**
- The first paid tier band in USD (annual billing): $5 (Setmore, per user) · $10 (Calendly, per seat) · $16 (Acuity, flat, 1 calendar). Middle value $10.
- The first paid tier in EUR: €11.90 (SimplyBook). A single observation, so no band was built.
- **USD and EUR were not converted into each other. No exchange rate was invented.** Comparison across currencies was made through structure only.
- The multipliers in the three tier structures: the middle tier is 1.69 times the entry (Acuity 27/16) and 2.09 times (SimplyBook 24.90/11.90). The top tier is 1.81 times the middle (Acuity 49/27) and 2.00 times (SimplyBook 49.90/24.90). **Observed band: middle is roughly entry × 1.7 to 2.1 · top is roughly middle × 1.8 to 2.0.**
- The real annual discount (from the sources that give both a monthly and an annual figure): Acuity roughly 20 percent (16 against 20, 27 against 34, 49 against 61). SimplyBook 14 to 17 percent computed from the listed figures, while the page itself claims roughly 17 percent. Calendly's page states 16 and 20 percent. **Band: 14 to 20 percent.** Setmore is the outlier at roughly 58 percent and was kept out of the band.
- Free tier: 3 of the 4 sources have one (Calendly, Setmore, SimplyBook). Acuity has none and says so openly on the page.

---

## B · Feature by tier matrix

Cell values: `entry` (free or the first paid level), `middle`, `top`, `none`, `not stated` (does not appear on the page, not guessed).

| Feature | Calendly | Setmore | SimplyBook.me | Acuity |
|---|---|---|---|---|
| Free tier | entry (Free) | entry (Free) | entry (Free) | **none** (the page says so openly) |
| Online booking page / widget | entry | entry | entry | entry |
| Email reminders | middle (Standard) | entry (Free) | not stated | entry (Starter) |
| SMS reminders | not stated (no channel named) | middle (Pro) | not stated | middle (Standard) |
| Taking payments online | middle (Standard) | entry (Free) | middle (Basic) | entry (Starter) |
| Deposits | not stated | not stated | middle (Basic) | not stated |
| Two way calendar sync | middle (Standard, multiple calendars) | middle (Pro) | not stated | not stated |
| Brand removal | not stated | middle (Pro) | top (Premium, partial · Enterprise, full) | top (Premium) |
| API access | top (Enterprise) | middle (Pro) | top (Enterprise) | top (Premium) |
| SSO / SAML | top (Teams add on, Enterprise) | not stated | middle (Standard) | not stated |
| Compliance certification (HIPAA and the like) | top (Enterprise, security review) | not stated | middle (Standard) | top (Premium) |
| Multi location management | not stated | not stated | top (Enterprise) | top (Premium) |
| Priority support | middle (Standard, 24/7 chat) | middle (Pro) | not stated | not stated |
| Advanced routing (round robin, lead) | top (Teams) | not stated | not stated | not stated |

### Reading 1 · what the sector gives at entry level
The online booking page and widget: at entry level in 4 of the 4 sources. Email reminders: at entry or first paid level in the 3 sources that name them. Taking payments online: at entry or first paid level in 3 of the 4 sources.
**Conclusion:** it is hard to charge separately for these three. They are the condition of the product existing, and if you put them in a top tier the price objection will come from exactly there.

### Reading 2 · top tier triggers
- **API access:** at the highest level in 4 of the 4 sources (in Setmore's case Pro, which is its only paid tier).
- **Brand removal:** at the top or the only paid level in the 3 sources that name it.
- **Multi location:** at the top level in both sources where it appears.
- **Compliance certification:** at the middle and top levels in the 3 sources where it appears.
- **SMS reminders:** in both sources where they appear (Setmore, Acuity), ONE LEVEL ABOVE entry. Both give email at entry level and put SMS above it.

**The most important finding:** putting SMS above the entry level repeats in two independent sources. The technical reason is most likely that every message sent carries a real unit cost. The same logic maps exactly onto the cost structure in `you/01-product.md`.

---

## C · Value axis

### What the competitors charge by
| Source | Axis |
|---|---|
| Calendly | per seat (people) |
| Setmore | per user (people) + a volume ceiling on the free tier (200 appointments a month) |
| SimplyBook.me | usage volume (50 / 100 / 500 / 2,000 bookings a month) + resource count (providers) + number of custom features |
| Acuity | resource count (1 / 6 / 36 calendars) |

So there is no single correct axis in this sector. There are two big families: **number of people** (Calendly, Setmore) and **capacity or usage** (SimplyBook, Acuity).

### Two questions for your business

**1. Which number does the customer's value grow with.**
The value Chairtime produces is the drop in hours left empty by people who do not turn up. The number of hours a salon can leave empty grows with the number of staff. In a one chair barber the hours saved are few, in an eight person salon far more. Location count is a multiplier in the same direction.
→ **Value axis: staff count (and location count).**

**2. Which number does your cost grow with.**
Your fixed cost (servers, infrastructure) is independent of customer count. Your variable cost is a single line item: SMS sent.
→ **Cost axis: number of SMS sent.**

The two numbers are different. Under the rule in `format/rules.md` §2, the main axis is built on the value side and the second axis closes the cost side.

### The choice
- **Main axis: staff bands.** Not PER person, but as a BAND (1 to 2 staff / up to 8 staff / unlimited staff plus locations). Reason: part time and seasonal staff are common in your target audience. If you price per person the business will share an account to keep the number low, and you will end up auditing staff counts every month. A band keeps the capacity logic of the per person model and removes the audit load.
- **Second axis: included SMS quantity plus overage.** Every tier has an included SMS quantity, and anything above it is billed at a unit price. No tier has unlimited SMS. Reason: every message is real money, and unlimited hands your cost over to the customer's behaviour. The sector has the same reflex (Setmore and Acuity both put SMS above the entry level).

### The axes not chosen and why
- **Booking volume (the SimplyBook model):** not chosen as the main axis. Your carrying value is sending reminders. If you price by volume, the business will avoid sending reminders to save money, the product stops producing value, and the cancellation risk goes up. That perverse incentive is not worth building.
- **Per seat (the Calendly model):** not chosen as the main axis, but its logic was taken in band form. Reason above.
- **Number of calendars (the Acuity model):** in salons the number of calendars already equals the number of staff, so as a separate axis it says nothing extra. A staff band is easier to understand.
- **Flat single price (your current situation):** dropped. A one chair barber and an eight person salon pay the same, so you take no share from a growing customer.
- **Commission model:** could not be assessed. The price data of the source known to use it (Fresha) could not be pulled, so no comment was made about it.

---

## D · The three tier proposal

> Prices in USD, monthly billing. Tax display is covered as an option in section E. The entry price is anchored to the pulled first paid tier band, and the tiers above it follow the multipliers observed in the pulled three tier structures. The EUR figures were NOT converted into USD; only the STRUCTURE was read from them (how many tiers, which multiplier, which feature at which level).

### Tier 1 · Chair · $19/month
- **Who it is for:** a barber, hairdresser, nail studio or single chair clinic working alone or with one helper.
- **What is in it:** 1 to 2 staff · online booking page · email confirmations and reminders · **250 SMS reminders included** · mobile management · a basic no show list.
- **Deliberately NOT in this tier:**
  - Taking deposits online. Reason: the deposit is the feature that solves the no show problem hardest. We move it up a tier as the carrying feature.
  - Two way calendar sync. Reason: in a one person business the clash risk is low, the need starts in the middle segment (Calendly and Setmore also give this above entry level).
  - Brand removal. Reason: at the top or the only paid tier in the 3 sources that name it. Sector norm.
  - Unlimited SMS. Reason: every message is a real cost. It will not exist in any tier.
- **What the price stands on:** the pulled first paid tier band in USD is $5 per user (Setmore, annual), $10 per seat (Calendly, annual) and $16 flat for one calendar (Acuity, annual, which is $20 on monthly billing). Chairtime's entry tier covers 2 staff and includes an SMS allowance that Acuity puts one tier higher, so $19 on monthly billing sits just under the pulled monthly entry figure while carrying more.

### Tier 2 · Salon · $39/month
- **Who it is for:** a single location salon, clinic or vet practice with 3 to 8 staff. The bulk of your target audience.
- **What is in it:** up to 8 staff · everything in Chair · **taking deposits online** · **1,000 SMS included** · two way calendar sync · occupancy and no show reporting per staff member · priority support.
- **Deliberately NOT in this tier:**
  - Brand removal. Reason: a top tier trigger, at the top in all 3 sources that name it.
  - API access. Reason: at the highest level in 4 of the 4 sources. The most consistent top tier trigger in the sector.
  - Multi location management. Reason: a single location business does not need it, and it is the reason the top tier exists.
- **What the price stands on:** in the pulled three tier structures the middle tier is 1.7 to 2.1 times the entry (Acuity 1.69 · SimplyBook 2.09). 19 × 2.05 = 38.95, rounded to 39.

### Tier 3 · Chain · $75/month
- **Who it is for:** a small chain with 2 to 5 locations and a staff count that moves around.
- **What is in it:** unlimited staff, up to 5 locations · everything in Salon · **2,500 SMS included** · brand removal (the booking page carries the chain's brand) · API access · location comparison reporting · setup and staff training (first month).
- **Deliberately NOT in this tier:**
  - Unlimited SMS. Reason: the same rule, nothing with a marginal cost is given as unlimited.
  - On site installation, hardware, call centre. Reason: they are on the "I do not do this" list in `you/01-product.md`. A service you do not offer does not go into a tier.
  - Accounting, invoicing, stock. Reason: the same list.
  - More than 5 locations. Reason: your capacity as a solo operator is limited. Write no figure for anything bigger, put a "let us talk" box.
- **What the price stands on:** the observed top multiplier is 1.8 to 2.0 times the middle (Acuity 1.81 · SimplyBook 2.00). 39 × 1.92 = 74.88, rounded to 75. Note that this sits ABOVE the highest monthly figure in the pulled USD data (Acuity Premium at $61 monthly). That deviation is listed below with its fallback plan.

### Why the middle tier is the one you want chosen
The mechanism has four parts:
1. **The staff band jump.** Your target audience runs from 1 to 8 staff. The entry tier ends at 2 staff, so most of the target audience does not fit in the entry band in the first place.
2. **The carrying feature is in the middle tier.** Taking deposits online, the hardest answer to the no show problem, exists only in Salon.
3. **The top tier is a narrow door.** Everything in Chain (multi location, brand removal, API) is pointless for a single location business. A single location customer looks at Chain and says "I do not need any of this", and stays in the middle.
4. **The value increase outruns the price increase.** From 19 to 39 the price rises 2.05 times, while the staff capacity rises 4 times and the included SMS rises 4 times.

> No number was given, and none will be given, about how many people will choose which tier. This system does not measure demand.

### Floor check
- The fixed cost is about $60 a month (`you/01-product.md`). The entry tier covers the fixed cost at 4 customers (19 × 4 = 76).
- **The variable cost check COULD NOT BE DONE.** `you/01-product.md` says SMS is real money but **gives no unit cost figure**. The system cannot invent the SMS overage price. The rule is this: the overage unit price should be at least 2 times the SMS unit cost you pay (the gap covers support and collection cost). Write the figure into `you/01-product.md` and the next report will check the included quantities too.

### Risky deviations (deliberate, with an objection plan)
1. **We took deposits and online payments out of the entry tier.** The sector norm is the opposite: Setmore gives payments on the free tier, Acuity in the entry tier, SimplyBook in the first paid tier. This is a deliberate deviation, because your carrying value is the deposit. **If the objection comes:** put plain online payment in the entry tier and keep deposits in the middle tier. They are two separate features and they can be split.
2. **We put in no free plan.** 3 of the 4 pulled competitors have a free tier, Acuity does not. The red line in `you/01-product.md` rules out a free forever plan (support load). Acuity made the same choice and states it openly on its page. **The trade:** run a trial period instead of a free plan. In the pulled sources the trial runs from 7 days (Acuity) to 14 days (Calendly, Setmore).
3. **The top tier sits above the pulled ceiling.** $75 monthly is above the highest monthly figure in the pulled USD data ($61, Acuity Premium). For a single purpose tool that is an assertive place to stand. What it rests on is multi location and brand removal. **If the objection comes:** pull the included SMS from 2,500 down to 1,500 and drop the price to $59, and keep brand removal.

---

## E · Local market adaptation (options, not decisions)

### 1. Currency
- **Option A · a fixed price in the currency your buyers use.** Your buyer is a local salon owner and expects a figure in their own currency. Easy to explain, reduces objections. In this example the operator prices in USD and 3 of the 4 pulled sources publish in USD, so the band is directly comparable.
- **Option B · a price indexed to another currency.** Part of your cost (servers, infrastructure) is often billed in a different currency, and indexing protects that part. But a small business customer dislikes a bill that changes every month, and it becomes a cancellation reason.
- **Which one in which situation:** A while your cost currency and your selling currency move together. Consider B only for the segment concerned if more than a quarter of your revenue comes from another currency zone.

### 2. Currency swings and the review threshold
`you/01-product.md` says you do not want to change the price more often than every six months. A structure that fits: keep the price fixed, but set a threshold for the **ratio of your infrastructure cost to your monthly revenue**, and review when that threshold is crossed. You set the figure of the threshold; the system does not invent a ratio for you. The single number you need to measure: infrastructure spend divided by monthly subscription revenue.

### 3. Should tax be visible in the price
- **Option A · write `+ tax`.** You are selling to a business, your buyer usually reclaims the tax, and the listed figure looks lower.
- **Option B · write one figure with tax included.** The buyer sees the total they will pay, and no "plus tax on top?" surprise turns up in the sales conversation.
- **Which one in which situation:** A if your buyer is a registered business that reclaims tax. B if a meaningful share of your buyers cannot reclaim it, or if they are consumers.
- **Note:** whichever you choose, use the SAME display on the page and in the contract. A mixed display produces objections.
- **This clause needs legal confirmation:** whether you are allowed or required to show a tax inclusive price differs by region and by whether you sell to businesses or consumers. Check the rules where you sell.
- **Honesty note:** no local reference source was pulled in this run (see `data/pulled-2026-07-26.md`), so this item does not come from measured local data. It stands as a general observation.

### 4. Annual billing and local payment habits
- In the pulled data the annual discount band is 14 to 20 percent (Acuity roughly 20 percent, SimplyBook 14 to 17 percent, Calendly's page states 16 and 20 percent). Setmore is an outlier at roughly 58 percent and was kept out of the band.
- **Option A · a 17 percent annual discount** (the "2 months free" framing, easy to explain).
- **Option B · no annual discount, extra SMS credit instead** (protects cash flow without cutting your unit price).
- **Payment route:** automatic card renewal on monthly, and open a bank transfer option on annual. Collecting a year up front eases cash flow.
- **Honesty note:** this report contains no MEASURED data about payment habits in your market. This item does not come from the pulled pricing pages, it stands as a general observation. Ask your own customers how they want to pay and write the answer into the price log in `you/02-competitors.md`.

### 5. Customers in another region and dual pricing
You have no customers in another region right now. When you do: **a separate page, a separate currency.** Do not show two currencies side by side on the same page; the buyer will multiply them out, compare, and ask for the cheaper one. Selling into another region also changes the invoicing and tax side, and that **needs legal confirmation**.

---

## F · Price change protocol

### What happens to existing customers
**The route chosen: a 12 month price lock.** Whatever price a customer came in at, they pay it for 12 months. At the end of the 12th month they move to the current price, and they are told before the move.
The alternative route is a staged move (the rise applied in two or three steps). Pick one of the two, do not run both at once, or the customer will not understand which rule applies.

### Notice period and channel
- For a monthly subscriber: **at least 30 days** before the new price, by email plus an in product notice.
- For an annual subscriber: **at least 30 days** before the renewal date, through the same two channels.
- The notice contains three things: the old price, the new price, the effective date. One sentence of reasoning, no defensive paragraph.
- **This clause needs legal confirmation:** price change notices and automatic renewal terms on subscriptions fall under consumer and distance selling rules, and those rules differ by region. Have the periods and the wording checked by a lawyer where you sell.

### At which threshold a price rise happens
No rise until **at least two** of the following happen together:
1. Your SMS unit cost or your infrastructure spend has risen noticeably since the date you last set the price (you define the figure, by updating the cost section of `you/01-product.md`).
2. A new and genuinely used capability has been added to the tier in the last 12 months.
3. More than 12 months have passed since the last price change.

"A competitor raised their price" is not on its own a reason to raise yours. You do not know their cost structure.

### Banned behaviour
- **The silent rise:** charging a higher amount at renewal without notice.
- **Narrowing the limits:** giving less at the same price (dropping the included SMS from 1,000 to 700, for example). That is also a price rise and falls under the same notice rule.
- **Quietly closing an old tier:** either keep the old tier or close it, and announce the decision.
- **A private discount for one customer:** different prices for the same tier, which ends trust the moment it gets out. If you are going to discount, have a rule for it (annual payment, early customer and so on).

---

## G · What this report does not know

1. **Demand was not measured.** This report reads the competitors' structure and your cost. It DOES NOT KNOW and does not guess how many people will say yes to $39. The price proposal is only proven in real sales conversations.
2. **The figures of the ones who hide their price are unknown.** Zenoti gives no price and Fresha's price data could not be pulled. Neither entered any calculation. There is a blind spot at the top end of the segment.
3. **Currencies were not converted.** No USD figure was derived from the EUR figures. SimplyBook's tiers were used for structure only (how many tiers, which multiplier, which feature at which level).
4. **No local reference source was added.** The operator prices in the same currency 3 of the 4 pulled sources publish in, so a separate local band was not needed. If you price in another currency, add at least two local sources with public prices in that currency; without them no figure is proposed in your currency. The tax display and payment habit items in section E are marked as general observations for the same reason.
5. **The pages are date stamped.** All of them were pulled on 2026-07-26. The competitors may have changed their prices. Run it again once a month.
6. **The SMS overage price could not be set.** No SMS unit cost was given in `you/01-product.md`. The rule was written instead of a figure.
7. **Next step:** put these three tiers on one page, talk to five real business owners, and note where the objection comes. Is it the price, the tier contents, or the tax display. Write the answer into the price log in `you/02-competitors.md`, and the system reads that too in the next report.
