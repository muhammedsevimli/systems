# Example Output · One Full Run

> This is the output of a real run. Input: one URL and `you/EXAMPLE-01-profile.md`.
> Fictional operator: Kerbside Digital, a one person studio building simple sites for neighbourhood businesses (bakery, salon, cafe, boutique). 20 existing customers. Does not write code, builds with Claude Code.
> The target product is real and public. Every feature, price and license line was pulled live from its own pages on 24 July 2026 and the source links were kept. The raw breakdown is in `breakdown/EXAMPLE-breakdown-2026-07-24.md`.
> Every run writes THREE files into `outputs/`. All three are below, in order.
> This is not a clone plan. The target's logic was pulled out and the plan was adapted to the operator's niche.

---
---

# FILE 1 · `2026-07-24-product-plan.md`

## 1. Run details
Target: https://plausible.io · Scan date: 24 July 2026 · Pages read: 5 (home page, pricing section, doc map, metric definitions, open source page) · Could not be reached: 1 (a guessed local pricing page, HTTP 404). Features collected: 35. Raw breakdown: `breakdown/EXAMPLE-breakdown-2026-07-24.md`.

## 2. What this product does, and for whom
It does website analytics: who came to the site, where from, what they did. Where it differs is simplicity and privacy. It sets no cookies, keeps no persistent identifier, the tracking script is small, and every number sits on a single page. On the page it positions itself against the complexity of the big analytics tools.

Its audience is wide: ecommerce, SaaS, agencies and freelancers, content creators, enterprise. Which means the product gives the same dashboard to a publisher doing a million pageviews a month and to a one page site. The price scales with pageview volume, with site count and team capacity gates on top.

## 3. Feature buckets

| Feature | Bucket | Reason |
|---|---|---|
| Adding a site + tracking script | CORE | Without this there is no data at all, this is the door into the product |
| Cookieless, identifier free measurement | CORE | This is the product's main promise, remove it and what is left is an ordinary counter |
| Single page simple dashboard | CORE | This is where the first value moment is shown, building a menu maze makes no sense |
| Real time "how many people are on right now" | CORE | Proves the setup works in 30 seconds, I am hanging the first value moment on this |
| Source and channel breakdown | CORE | "Where did they come from" is as live a question as "who came" for every customer |
| Contact goals (tap to call, tap to message, tap for directions) | CORE | This is the only real question in this niche, the reason is in the adaptation table below |
| Many sites on one screen (agency view) | CORE | The operator has 20 customers, opening dashboards one by one would lock up the working day |
| Email and Slack reports | SUPPORT | Valuable, but a dashboard link is enough in the first version |
| Shared link (handing the dashboard to the customer) | SUPPORT | With the first 20 customers the operator can share the link by hand |
| Period comparison (this month, last month) | SUPPORT | Only meaningful from the second month, in month one there is nothing to compare |
| Excluding internal traffic | SUPPORT | The operator's own visits distort the numbers, but this can wait a week |
| Bot filtering | SUPPORT | At low traffic the bot share is noticeable, a simple rule in v1.5 is enough |
| Traffic spike notification | SUPPORT | Pleases the customer, cheap to build, but has no place in the first value moment |
| Codeless goal setup | SUPPORT | The operator sets the goals up, defining them through a UI is not needed in v1 |
| Annotations (notes on the chart) | DECORATION | Used once a month, cheap to build but last in the queue |
| Scroll depth | DECORATION | Measuring reading depth on a four page shop site has no payoff |
| Funnel analysis | DECORATION | With a few hundred visitors a month a funnel statistic is noise |
| User journeys | DECORATION | Same reason, there is no volume |
| Saved segments | DECORATION | This user does not build filters, they look at a ready screen |
| Search Console integration | DECORATION | A good sales argument, a separate job to build, would delay v1 |
| AI tool traffic tracking | DECORATION | At this volume no measurable signal comes out |
| File download tracking | DECORATION | A shop site has almost no files to download (a menu PDF is the exception) |
| Dashboard embed | DECORATION | The shared link does the same job more cheaply |
| 404 page tracking | DECORATION | Useful to the operator, not on the customer's agenda |
| Team management, roles | STAY OUT | A scale feature. There is one operator and one business owner, a role matrix is empty work |
| Single sign on (SSO) | STAY OUT | An enterprise feature, never requested in this niche |
| Two factor authentication | STAY OUT | In v1 even login is built in its simplest form, the security layer comes later |
| Google Analytics data import | STAY OUT | Most of these customers have no historical data to move |
| The Stats, Events and Sites API trio | STAY OUT | Nobody is pulling data from outside, and maintenance is not free |
| Data Studio connector | STAY OUT | This user does not use a reporting tool |
| White label integration | STAY OUT | The product already ships under the operator's brand, a separate layer is pointless |
| Raw event export | STAY OUT | An enterprise need, the infrastructure load is bigger than the product itself |
| Revenue and order tracking | STAY OUT | Handling revenue data is a separate responsibility, not in v1 |
| 5 year data retention | STAY OUT | Long retention means storage cost, 12 months is enough in v1 |

CORE: 7 items. That is the ceiling, more would bloat v1.

**The 5 lines that did not enter the bucket table, and why** (what is left of the 35 features in the breakdown, dropped openly rather than silently):
- Lightweight tracking script: not a feature, a quality measure. It went into step 2 of the v1 build order as a boundary ("keep the script small").
- Hosting in the EU: a property of the product. In your niche the equivalent question is "where is my data stored", so note the hosting location in v1 and use it as a sales argument later.
- Being open source: a property of the product and a licensing matter. It went into the do not copy list.
- Outbound link click tracking and form submission tracking: these two merged into the "contact goals" line in CORE. In this niche the meaningful outbound links are the phone, message and map links anyway.

## 4. Niche adaptation table

**Exists in the target, pointless in your niche**

| Feature | Why pointless |
|---|---|
| Google Analytics data import | Most of your customers never had analytics installed, there is no history to move |
| Funnels and user journeys | At 500 to 5000 visitors a month these analyses are statistically noise |
| Team management, roles, SSO | One person opens the dashboard: the business owner. The concept of a role does not exist |
| Data Studio connector and the API trio | This user does not move data into another tool, they look at one screen |
| AI traffic and scroll depth | On a four page shop site there is no measurable equivalent |
| Pricing by pageview volume | Every customer stays on the bottom tier, the price never grows |

**Missing from the target, mandatory in your niche**

| Need | Why mandatory | Where it came from (profile line) |
|---|---|---|
| A contact counter at the very top of the dashboard: taps to call, taps to message, taps for directions | The customer does not ask "how many people visited", they ask "how many people called me". That has to be the product's headline number | "my customer does not ask how many people visited, they ask how many people called me" |
| Plain language on the dashboard ("43 people looked this week, 6 called you") | The user is not technical, an English metric name on the first screen closes the tab | "the owners are not technical, they check things on a phone" |
| A single image monthly summary sent as a message | They do not read reports, they want a screenshot. That image becomes the reason to come back | "they do not read a report, they want one screenshot in a message" |
| Agency screen: 20 customers in one list, the ones whose signal dropped flagged | The operator is the real user. Without seeing which customer's signal fell, they learn about the churn afterwards | "I already have 20 small business customers" |
| Cardless payment: yearly up front, bank transfer | Monthly card subscriptions are a breaking point for this audience | "they dislike monthly card subscriptions, they would rather pay once a year" |
| One screen on a phone (mobile first dashboard) | The user does not open a desktop, they look on their phone | "they check things on a phone, standing behind a counter" |

## 5. User flow

**In the target**
- Sign up: 30 day trial, no card required.
- First value moment: create an account, add the site, place the tracking script on the site, see a real time visitor in the dashboard. Three steps, and the third step requires the user to touch the code of their own site. For a non technical person that is where they drop out.
- Reason to come back: accumulated historical data, email and Slack reports, spike notification.

**In your version**
- Sign up: the business owner never signs up. You built the site already and you place the script. All that goes to them is a link.
- First value moment: the first time the owner taps that link they see a full screen, and the top line reads "6 people called you this week". **On the user's side the step count drops from 3 to 0.** You put the setup load on the operator rather than the product, because the operator is already inside that site.
- Reason to come back: a single image summary that arrives as a message at the start of every month. The user does not have to remember the dashboard, the dashboard finds them.

## 6. What are you doing differently
1. **You measure a different thing.** The target measures visits, you measure contact: calls, messages, directions. Same data, different headline number. For a high street business that is the number closest to revenue.
2. **The setup load is not on the user.** The operator places the script, the business owner touches no technical step.
3. **Your pricing unit is different.** Per tracked site, not by traffic volume. In this niche traffic never grows, the customer count does.
4. **The reporting language is a plain sentence.** Not a metric name: "43 people looked this week, 6 called you".

## 7. v1 scope and build order

1. **Build the data schema.** Five tables: `customer`, `site`, `event`, `daily_summary`, `monthly_summary_image`. When you are done: an empty database is up and the tables exist.
2. **Write the tracking script.** A small script added to the site. It sends one event when the page opens. When you are done: a single event row lands from a test site.
3. **Capture the contact taps.** `tel:` links, message links and map links are recorded automatically as events. When you are done: tapping the phone link on the test page drops a "call" record into the event table.
4. **Build the dashboard (one screen, mobile first).** Contact counts at the top, visits below, source breakdown below that. When you are done: it is readable on one phone screen and the headline number is visible without scrolling.
5. **Add the real time counter.** "2 people on the site right now". When you are done: opening two tabs makes the number two.
6. **Make the site link shareable.** An unguessable dashboard link per customer. When you are done: opening the link in a private window loads the dashboard without a login, and no other customer's data is visible.
7. **Build the agency screen.** All customers in one list, the ones whose contacts dropped this week flagged. When you are done: 3 test customers are in the list and one is tagged "dropping".
8. **Produce the monthly summary image.** One image, four numbers, the month name. When you are done: the image downloads as a file for one customer and can be sent as a message.

## 8. What did not make v1, and why
- Login and passwords: a secret link is enough in v1, building a login screen delays the first version by a week.
- Teams, roles, SSO: no demand at all in this niche.
- Payment infrastructure: in v1 collection happens by hand through bank transfer, a payment integration is a separate compliance job.
- Revenue and order tracking: handling revenue data creates a separate responsibility.
- Funnels, user journeys, segments: meaningless at this traffic volume.
- Analytics import, API, Data Studio: no user for them, but a maintenance cost.
- Long data retention: 12 months in v1, after that it is summarised and kept.

## 9. Pricing logic
- **In the target:** the price scales with monthly pageview volume, with site count and team capacity gates on top. The figures written literally on the page: Starter 9 dollars (up to 10 thousand pageviews), Growth 14 dollars (3 sites, 3 team members), Business 19 dollars (10 sites, 10 team members, 5 year retention), and no figure at all for Enterprise. 30 day free trial, no card required. Source: https://plausible.io/#pricing
- **That unit does not work in your niche.** Your customers' sites get 500 to 5000 views a month. All of them stay on the bottom tier and your revenue never grows. On top of that the payer and the dashboard user are different people: the payer is you or the business, the user is the owner.
- **The unit that fits you:** a flat monthly fee per tracked site. Your revenue grows with your customer count, not with traffic. Put a discount on paying a year up front, because your niche prefers a single yearly payment. Instead of a trial period, give the first month free: the customer is already yours, you do not need to collect card details.
- Note: this section is not a pricing decision, it is an inference about pricing LOGIC. You set the number against your own costs and your customer conversations.

## 10. Do not copy list
- Brand name, logo, brand colours, type system
- The dashboard's one to one screen layout and chart design
- Page copy, tagline, comparison tables
- Documentation text and images
- **Source code.** The product is open source and the license is written on the page verbatim as: "GNU Affero General Public License Version 3 (AGPLv3) or any later version". That license lets you run it on your own server, but it does not let you take the code, change it and sell it as a closed service (you would have to open your changes). This plan does not touch the code at all: it pulls out the logic that is written publicly on the site, adapts it to your niche, and you build your own product from scratch. Source: https://plausible.io/open-source-website-analytics

## 11. Unknowns and risks
- The pageview limit for the plans above Starter is not on the site, and neither is what happens when a limit is passed.
- How long a session has to stay quiet before it ends is not written. In your own schema you have to define that window yourself (suggestion: 30 minutes, then measure and change it).
- How cookieless deduplication is done is not explained technically. In your v1, do not deduplicate visitors; a rough daily number is enough.
- There is no Enterprise price, and no figure was produced.
- **Personal data risk:** if you store the visitor's IP address in raw form you are processing personal data. Do not store raw IPs in v1, keep only the city and throw the IP away. That single decision skips most of the compliance load. Data protection rules differ by region, so check what applies where your customers are.
- **Demand risk:** this plan tells you how to build the product, it does not guarantee anyone will pay for it. Ask 3 of your 20 customers "what would you pay a month for this screen". Do not start the build order before you get an answer.

---
---

# FILE 2 · `2026-07-24-data-schema.md`

> **Warning:** this schema is NOT the target product's real database. It is an inference made from public pages (doc headings, metric definitions, the pricing section). The evidence for the inference sits under every table. No table was written without evidence.

---

## 1. The schema inferred from the target product

### `site`
- **Why it exists:** a user can track more than one domain, and each has to be its own record.
- **Evidence:** the headings "Add your website", "The Sites page", "Sites API" · https://plausible.io/docs · the site count limits in pricing (3 sites, 10 sites) · https://plausible.io/#pricing
- **Fields:** domain, owner, timezone, created at, is public, retention period
- **Relation:** under `account`, above `event`

### `event`
- **Why it exists:** the smallest unit the product collects. A pageview and a custom event land in the same table.
- **Evidence:** "Events API", "Custom properties: attach custom data when sending pageviews and events" · https://plausible.io/docs/metrics-definitions
- **Fields:** site, type (pageview or custom event), page path, timestamp, country, region, city, browser, operating system, screen size, source, channel, UTM fields, referrer, amount (on revenue events), custom fields
- **Relation:** under `site`, inside `session`

### `session`
- **Why it exists:** bounce rate, visit duration, entry and exit pages cannot be computed from single events. There has to be a grouping layer above events.
- **Evidence:** "Total Visits/Sessions: set of actions a user takes on your site", "Bounce Rate", "Visit Duration", "Entry Pages", "Exit Pages" · https://plausible.io/docs/metrics-definitions
- **Fields:** site, started at, ended at, entry page, exit page, page count, bounced, source
- **Relation:** under `site`, above `event`

### `goal`
- **Why it exists:** the user needs to define separately which event counts as "success", and a conversion rate has to be computed.
- **Evidence:** "Goals/Events: track desired actions people take on your site", "Conversion Rate", "Unique Conversions", "Total Conversions", "codeless goals" · https://plausible.io/docs/metrics-definitions
- **Fields:** site, name, type (page goal or event goal), match rule, revenue tracking on
- **Relation:** under `site`, matched against `event`

### `funnel`
- **Why it exists:** where people drop off across ordered steps requires its own definition.
- **Evidence:** "Funnels: sequence of steps and visitor drop off points" · https://plausible.io/docs/metrics-definitions
- **Fields:** site, name, ordered steps (list of goals)
- **Relation:** tied to the `goal` list

### `segment`
- **Why it exists:** saved filters are stored per user.
- **Evidence:** "Saved Segments" · https://plausible.io/#pricing · "Filters and segments" · https://plausible.io/docs
- **Fields:** site, name, filter rules, owner, is shared
- **Relation:** under `site`

### `annotation`
- **Why it exists:** marking a date on the chart is its own record.
- **Evidence:** "Annotations" · https://plausible.io/docs and https://plausible.io/#pricing
- **Fields:** site, date, text, added by
- **Relation:** under `site`

### `account` and `team_member`
- **Why they exist:** several people look at the same data and their roles differ.
- **Evidence:** "Team settings", "Users and roles", "Single Sign-On" · https://plausible.io/docs · the team member limits in pricing · https://plausible.io/#pricing
- **Fields:** email, name, two factor enabled, role, which team
- **Relation:** `account` 1 to n `team_member`, `team_member` n to n `site`

### `shared_link`
- **Why it exists:** the dashboard can be shown externally without a login, which means a separate access record.
- **Evidence:** "Shared links", "Embed dashboard" · https://plausible.io/docs
- **Fields:** site, unguessable key, has password, created at
- **Relation:** under `site`

### `subscription`
- **Why it exists:** the plan, the capacity limits and the invoices are kept.
- **Evidence:** "Subscription plans", "Change plan", "Download invoices", "Trial to paid" · https://plausible.io/docs · tiers and limits · https://plausible.io/#pricing
- **Fields:** account, plan name, monthly pageview limit, site limit, team limit, retention period, term (monthly or yearly), trial end date
- **Relation:** under `account`

### `transfer_job`
- **Why it exists:** importing from an outside source and exporting are long running jobs whose state is tracked.
- **Evidence:** "Import from Google Analytics", "Import stats", "Export stats" · https://plausible.io/docs
- **Fields:** site, source, state, started at, finished at, date range covered
- **Relation:** under `site`

### `report_subscription`
- **Why it exists:** email and Slack reports and spike notifications have to know who they go to and how often.
- **Evidence:** "Email reports", "Slack reports", "Traffic spike notifications" · https://plausible.io/docs
- **Fields:** site, channel (email or Slack), frequency, recipient, threshold (for the spike notification)
- **Relation:** under `site`

**What could not be inferred:** how a visitor is deduplicated without cookies, after how many quiet minutes a session ends, how long raw data is kept before it is rolled up into a summary. None of that is on the site, and none of it was invented.

---

## 2. Your v1 schema (simplified, 5 tables)

### `customer`
- **Why it exists:** every one of the operator's customers is a separate business, and the dashboard and the invoice hang off it.
- **What I dropped from the target schema:** `account`, `team_member` and the role structure. In this niche one person opens the dashboard, a role matrix is empty work.
- **Fields:** business name, contact number, dashboard key, start date, monthly fee, payment term (yearly up front), status
- **Relation:** 1 to n `site`

### `site`
- **Why it exists:** every customer has a site and the data hangs off it.
- **What I dropped from the target schema:** the timezone and retention fields. One timezone, 12 months fixed.
- **Fields:** customer, domain, tracking key, added at
- **Relation:** under `customer`, above `event`

### `event`
- **Why it exists:** the single collection unit. A pageview and a contact tap land in the same table.
- **What I dropped from the target schema:** most of the UTM fields, screen size, custom free form fields and the revenue amount. In this niche nobody uses campaign parameters, and revenue data does not enter v1.
- **Fields:** site, type (page or contact), contact type (call, message, directions), page path, timestamp, city, device (phone or desktop), source
- **Relation:** under `site`
- **Note:** the IP address is NOT STORED. Once the city is derived the IP is thrown away. That single decision removes most of the personal data load.

### `daily_summary`
- **Why it exists:** so the dashboard does not count raw events on every open. Once a day a summary is computed and the dashboard reads the summary.
- **What I dropped from the target schema:** the `session` table entirely. Bounce rate and visit duration are not questions this audience asks. Instead I keep daily counts.
- **Fields:** site, date, visit count, daily unique counter, call count, message count, directions count, top source
- **Relation:** under `site`

### `monthly_summary_image`
- **Why it exists:** this is the reason to come back. One image that goes to the customer as a message at the start of every month.
- **What I dropped from the target schema:** the multi channel structure of `report_subscription`. There is one channel, sent by hand.
- **Fields:** customer, month, image file path, sent, sent at
- **Relation:** under `customer`

**Other tables I dropped and why:** `funnel` and `segment` (meaningless at this traffic volume), `annotation` (used once a month), `shared_link` (the dashboard key already sits on `customer`), `subscription` (collection is manual in v1, there is no plan concept), `transfer_job` (there is no history to move).

## 3. Relation map

```text
customer                1 to n   site
site                    1 to n   event
site                    1 to n   daily_summary
customer                1 to n   monthly_summary_image
event                   n to 1   site        (daily_summary is computed in a nightly batch)
```

## 4. Questions that will break the schema
- **How big does the event table get:** 20 customers, roughly 3000 visits a month each. About 720 thousand rows a year. That is not a problem, but it becomes one at 200 customers. Your decision: delete raw events after 12 months and keep `daily_summary`. Write that on day one, it is hard to retrofit.
- **If the same tap is counted twice:** if the user taps the phone link twice, is that two calls. Decision: the same contact type from the same visitor counts once within 30 minutes. Keep that window in a setting, do not hard code it.
- **How you deduplicate:** if you are not setting cookies you cannot give a firm "unique visitor" number. Decision: write "visits" on the dashboard instead of "unique visitors". Do not promise a number you cannot deliver.
- **What happens to a customer's data when they leave:** deleted or frozen. Decision: keep a status field on `customer` and delay deletion. Data deleted by accident does not come back.
- **If a dashboard key leaks:** use a long unguessable key and make it renewable. One field, but adding it later is painful.

---
---

# FILE 3 · `2026-07-24-prompts.md`

> These prompts are pasted in order. Each does one job and builds on the output of the previous one.
> If you did not see a prompt's "when you are done you should see this" line, DO NOT move to the next one. Fix that step, then carry on.
> There is no code in the prompts, only plain English about what you want. Claude Code picks the technology, you set the boundaries.
> Based on: FILE 1 above (v1 scope) and FILE 2 above (5 tables).

---

## Prompt 1 · Project skeleton and data schema (30 minutes)

```text
i am building a simple visitor and contact dashboard for small businesses. today i only want the skeleton and the data schema, no screens.

there will be five tables:
- customer: business name, contact number, dashboard key, start date, monthly fee, payment term, status
- site: customer, domain, tracking key, added at
- event: site, type (page or contact), contact type (call, message, directions), page path, timestamp, city, device, source
- daily_summary: site, date, visit count, call count, message count, directions count, top source
- monthly_summary_image: customer, month, image file path, sent, sent at

boundaries:
- use as few moving parts as possible. one project folder, one database file. i do not want a complicated setup.
- never store the visitor's ip address anywhere. derive the city, then throw the ip away.
- no screens, no login, no design right now. just the schema and the project coming up.
- write everything you built into a single SETUP.md file, i will read it later.

when you are done you should see this: the project runs, the five tables exist, and you can add a test customer to the database by hand and list it.
```

---

## Prompt 2 · Tracking script and event collection (45 minutes)

```text
on top of the schema you built in the previous step, write the tracking script that goes on the site and the endpoint that records the event.

what i want:
- a small script that can be added to a customer's site with one line. when the page opens it sends a "page" event.
- the event should carry: which site (via the tracking key), the page path, where the visitor came from (referrer), and whether the device is a phone or a desktop.
- a server side endpoint that takes the event and writes it into the event table. derive the city, do not save the ip.
- keep the script small so it does not slow the page down. do not set cookies, do not keep a persistent identifier.

boundary: there is no dashboard yet, the data just needs to land.

when you are done you should see this: opening a test html page drops a single row into the event table containing the page path and the device, and there is no ip field at all.
```

---

## Prompt 3 · Capture the contact taps (30 minutes)

```text
add contact capture to the tracking script from the previous step. this is the most important feature of the product.

what i want:
- when a phone link on the page (anything starting with tel:) is tapped, send a contact event of type "call".
- when a messaging link is tapped (wa.me, whatsapp, or an sms: link), send a contact event of type "message".
- when a map or directions link is tapped, send a contact event of type "directions".
- the same contact type from the same visitor counts once within 30 minutes. keep that 30 minutes as a setting, do not bury it in the code.
- the customer should configure nothing. if the link is already on the page the system catches it by itself.

when you are done you should see this: tapping the phone link on the test page drops a record with type "contact" and contact type "call" into the event table. tapping twice still leaves one record.
```

---

## Prompt 4 · Daily summary job (20 minutes)

```text
on top of the raw events collected in the previous steps, write a job that computes a daily summary.

what i want:
- it runs once a day and writes that day's numbers for every site into the daily_summary table: visit count, calls, messages, directions, top source.
- from now on the dashboard should not count raw events, it should read this summary.
- let me trigger the job by hand too (for testing).
- raw events should be deleted after 12 months and the summary kept. put that cleanup inside the same job but keep the period as a setting.

when you are done you should see this: running the job by hand creates today's row in daily_summary and the numbers match the raw event counts exactly.
```

---

## Prompt 5 · Dashboard screen, mobile first (60 minutes)

```text
on top of the daily summary from the previous step, build the single screen dashboard the customer will see.

screen order, top to bottom:
1. at the very top, a large plain sentence: "43 people looked this week, 6 people called you".
2. below it, three contact boxes: calls, messages, directions. this week and last week side by side.
3. below that, a visits chart for the last 30 days.
4. at the bottom, a where they came from list (source breakdown), five rows at most.

boundaries:
- it must be readable on one phone screen. no scrolling needed to reach the first number.
- do not write metric names, write sentences. no terms like "bounce rate" or "unique visitor".
- the user is not technical. no settings, no filters, no date picker. one view is enough.
- the dashboard address should carry an unguessable key, with no login screen.

when you are done you should see this: opening the dashboard link on a phone shows the "how many people called" number without scrolling, and trying another customer's link does not show their data.
```

---

## Prompt 6 · How many people are on the site right now (20 minutes)

```text
add a live counter to the top of the dashboard you built in the previous step.

what i want:
- the number of visitors who sent an event in the last five minutes. it should read "2 people on the site right now".
- if nobody is there, write "nobody is on right now" instead of a number. showing a zero looks bad.
- it should refresh itself while the page is open, the user should not have to reload.

this counter is the thing that proves the product is installed. the first time i show it to a customer, this is where they will look.

when you are done you should see this: opening the test site in two tabs makes the dashboard number two, and five minutes after closing the tabs it reads "nobody is on right now".
```

---

## Prompt 7 · Agency screen (40 minutes)

```text
next to the dashboard you built in the previous steps, build one more screen just for me. i open this one, not the customer.

what i want:
- every customer in one list: business name, visits this week, contacts this week.
- flag the row of any customer whose contacts dropped noticeably against last week. keep the threshold as a setting.
- tapping a customer in the list opens their dashboard.
- keep this screen hidden, opened with a separate key of mine.

boundary: do not add a new table, compute it from the existing daily summary.

when you are done you should see this: three test customers appear in the list, and when you lower one of their contact counts by hand that row gets a "dropping" flag.
```

---

## Prompt 8 · Monthly summary image (40 minutes)

```text
on top of the data from the previous steps, produce the monthly summary image i will send to the customer as a message.

what i want:
- one image file. on it: the month name, the business name, how many people looked, how many called, how many messaged, how many asked for directions. plus an arrow against last month.
- it will be read on a phone, so make the type large. no more than four numbers.
- it should be produced for one customer with a single command and download as a file. i will send it by hand.
- record the produced image in the monthly_summary_image table so i do not produce it twice.

when you are done you should see this: running the command for one customer downloads an image file, all four numbers are readable when you open it on a phone, and the record shows up in the table.
```

---

## Prompt 9 · Ship it and show the first customer (30 minutes)

```text
put everything we built in the previous steps live, in one place.

what i want:
- bring the project up somewhere cheap or free. keep the database there too, do not stand up a separate service.
- turn "how to add the tracking script to a customer site" into a two sentence instruction, i will do it myself.
- backups: take a daily copy of the database.
- finally update SETUP.md: what we installed where, which setting lives where, and where i look when something breaks.

when you are done you should see this: you add the tracking script to a real customer site and ten minutes later the dashboard link shows real visit and contact numbers.
```

---

## If you get stuck (the three most common places)

1. **No events are landing.** First check that the tracking script actually loads on the page, then check the address of the server endpoint. Go back to the acceptance line of Prompt 2 and do not move on until that step passes.
2. **The contact count looks inflated.** That is usually the same tap being counted again. Check the 30 minute window setting from Prompt 3, it may have been buried in the code.
3. **The dashboard opens slowly.** The dashboard is probably counting raw events. That means the daily summary job from Prompt 4 is not running; make sure the dashboard reads the summary.

## Note
This set is 9 prompts. The rule was 6 to 10, so we are at the edge. If you want to add a new feature, go back to the buckets in the plan file first: is the thing you want to add in the CORE bucket, or are you bloating v1.
