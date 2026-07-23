# Pulled competitor prices · 2026-07-26

> The SYSTEM wrote this file. Every figure below was pulled from the competitors' public pricing pages, and every row carries its source URL.
> No figure was invented. A competitor whose price is not on the page was marked `price not public` and took no part in any average.
> Pulling tool: WebFetch (the page directly), and WebSearch when the URL could not be found (to find the right page).

---

## 1 · Calendly · `price pulled`
Source: https://calendly.com/pricing · pulled 2026-07-26
Price axis: **per seat** · currency: USD

| Tier | Price | Period | Metric | Features stated on the page |
|---|---|---|---|---|
| Free | $0 | free forever | 1 event type, 1 calendar connection | video calls, mobile app, browser extension |
| Standard | $10/seat/month | billed annually (16 percent saving on annual) | per seat | unlimited event types, multiple calendar connections, HubSpot and Mailchimp integration, payments with Stripe and PayPal, Zapier webhooks, automatic reminders, 24/7 chat support |
| Teams | $16/seat/month | billed annually (20 percent saving on annual) | per seat | everything in Standard, Salesforce integration, round robin meetings, lead routing, advanced admin features, SSO add on |
| Enterprise | "starts at $15k/year" | annual, custom pricing | custom | everything in Teams, Microsoft Dynamics, dedicated account support, SSO/SAML, domain control, audit log, data deletion API, security review |

Notes:
- 14 day trial on all paid tiers.
- The page says "monthly billing is priced higher than annual" but **gives no monthly figures**. The monthly figure counts as `not stated on the page`, it was not guessed.
- The Enterprise row gives a lower bound ("starts at"), not a single tier price. It was left out of the band calculation and stands only as an observation about the top end.

---

## 2 · Setmore · `price pulled`
Source: https://www.setmore.com/pricing · pulled 2026-07-26
Price axis: **per user** + a **usage ceiling** on the free tier · currency: USD

| Tier | Price | Period | Metric | Features stated on the page |
|---|---|---|---|---|
| Free | $0/user/month | free | up to 4 users, 200 appointments a month | taking payments online and in person, branded booking page and mobile app, email reminders and confirmations, iOS and Android app, team tools, integrations |
| Pro | $5/user/month (annual) · $12/user/month (monthly) | annual and monthly | unlimited users | unlimited appointments, SMS and email reminders, two way calendar sync, removing Setmore branding, customer blocking, Google Reviews, custom notifications and reminders, priority support, API access, Tap to Pay |
| Enterprise | no figure | not stated | custom | "Contact us" (price not public) |

Extra line item: the **Live Receptionist** add on at $99/month (one region only).

Notes:
- Both the annual and the monthly figures are on the page: $5 and $12. The real annual discount can be computed from those two.
- The Enterprise row is `price not public` and took no part in any average.
- **Outlier note:** $12 down to $5 is roughly a 58 percent annual discount, far outside the 16 to 20 percent the other pages state. The figure was not corrected, it was flagged as an outlier and kept out of the band.

---

## 3 · SimplyBook.me · `price pulled`
Source: https://simplybook.me/en/pricing · pulled 2026-07-26
Price axis: **usage volume (monthly bookings)** + resource count (providers) + number of custom features · currency: EUR

| Tier | Annual | Monthly | Metric | Features stated on the page |
|---|---|---|---|---|
| Free | €0 | €0 | 50 bookings/month, 1 custom feature, 1 provider | booking site, widget, admin app, WordPress integration |
| Basic | €11.90/month | €13.90/month | 100 bookings/month, 3 custom features, 5 providers | client app, accepting payments, deposits, tips, POS |
| Standard | €24.90/month | €29.90/month | 500 bookings/month, 8 custom features, 15 providers | branded client app, HIPAA compliance, SAML SSO |
| Premium | €49.90/month | €59.90/month | 2,000 bookings/month, unlimited custom features, 30 providers | Payments PRO, accounting integrations (QuickBooks, FreshBooks, Xero), white label footer |
| Enterprise | custom | custom | custom bookings, unlimited features, custom providers | multi location cluster interface, dedicated account manager, queue manager, high load API, full white label, data location choice |

Notes:
- The page says annual billing saves roughly 17 percent against monthly, and the figures support that.
- Enterprise is `price not public` and took no part in any average.

---

## 4 · Acuity Scheduling · `price pulled`
Source: https://acuityscheduling.com/pricing · pulled 2026-07-26
Price axis: **resource count (calendars)** · currency: USD
> The first URL tried (`https://www.squarespace.com/scheduling/pricing`) returned HTTP 404. The system tried the right domain and found the page. The wrong URL was kept on the record.

| Tier | Annual | Monthly | Metric | Features stated on the page |
|---|---|---|---|---|
| Starter | $16/month | $20/month | 1 calendar | payments with Stripe/Square/PayPal, email reminders, custom client forms, automatic time zone conversion |
| Standard | $27/month | $34/month | up to 6 calendars | everything in Starter, SMS reminders, memberships and packages, gift certificates |
| Premium | $49/month | $61/month | up to 36 calendars | everything in Standard, HIPAA BAA compliance, hiding Acuity branding, multiple staff and location time zones, custom API and CSS |

Notes:
- 7 day trial, no credit card required.
- **There is NO free plan.** The page states this openly.
- There is a custom quote for enterprise, with no figure (`price not public`).
- The annual discount is written on the page as "20 percent saving", and the figures support it.

---

## 5 · Zenoti · `price not public`
Source: https://www.zenoti.com/pricing · pulled 2026-07-26
The page opened and the content came through. **There is not a single price figure in any currency.** The page pushes the visitor towards "Get a Quote", "Book a Demo" and "Call Now".

> The system PRODUCED NO FIGURE for this competitor. It took NO PART in the average, the median or the band. It stands in the report only as this observation: at the top end of this segment there is a player who does not show their price publicly and prices through a sales conversation.

---

## 6 · Fresha · `no source`
URL tried: https://www.fresha.com/for-business/pricing · pulled 2026-07-26
The page was fetched but the returned content contained no price, no commission rate and no fee information. Only general marketing copy came through.

> The system DID NOT SAY "it probably takes a commission". The row stayed `no source` and took no part in any average.

---

## Local reference · not added (on purpose)
The operator prices in USD, and 3 of the 4 sources whose prices were pulled publish in USD. So no separate local source was needed to build a band in the operator's currency.
> If you price in a currency none of the pulled sources publish in, add at least two local sources with public prices in that currency to section B of `you/02-competitors.md`. Without them the system proposes no figure in your currency, and no exchange rate is invented in its place.

---

## Summary
- Sources scanned: **6**
- `price pulled`: **4** (Calendly, Setmore, SimplyBook.me, Acuity)
- `price not public`: **1** (Zenoti) · took no part in any average
- `no source`: **1** (Fresha) · took no part in any average
- Rows that are `price not public` at the tier level: Setmore Enterprise, SimplyBook Enterprise, Acuity enterprise quote, Calendly Enterprise (a lower bound exists, but no tier price)
- URLs that returned a 404 and were corrected: 1 (Squarespace scheduling). The system found the right one with WebSearch and the correct URL was written into the `you/02-competitors.md` list.
- No figure was guessed. Different currencies (USD, EUR) were NOT converted into each other, and no exchange rate was invented.
