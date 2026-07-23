# Breakdown · 2026-07-24 · Target: plausible.io

> The system wrote this file. The pages were really browsed with Claude Code's web tools (WebFetch) on 24 July 2026.
> Operator profile: fictional (`you/EXAMPLE-01-profile.md`). Target: a real, public product site.
> Every line here is what is actually written on the page. A page that could not be reached is marked "could not be reached".

## A) Scan details

| Page | URL | Result |
|---|---|---|
| Home page | https://plausible.io/ | **fetched** |
| Pricing | https://plausible.io/#pricing | **fetched** (the pricing section sits inside the home page) |
| Documentation (heading map) | https://plausible.io/docs | **fetched** |
| Documentation (metric definitions) | https://plausible.io/docs/metrics-definitions | **fetched** |
| License / open source | https://plausible.io/open-source-website-analytics | **fetched** |
| Localised pricing page (guessed path, tried) | https://plausible.io/docs/local-pricing-2026 | **could not be reached · HTTP 404, no such page.** Because the page does not exist, nothing that would have come from it was written into the output. |

No separate `/features` page was tried: the home page already carried a named feature list, and the inventory was pulled from there.

## B) The product in one sentence
Privacy focused website analytics. On the page it positions itself as the simpler and lighter alternative to Google Analytics.
Source: https://plausible.io/

## C) Who it speaks to (the audience written on the page)
- Ecommerce businesses
- SaaS companies
- Agencies and freelancers
- Content creators and publishers
- Enterprise organisations

Source: https://plausible.io/

## D) Feature inventory (raw list, no sorting)

| # | Feature | Where it appears | What it does in one sentence |
|---|---|---|---|
| 1 | Single page simple dashboard | plausible.io | Every number on one screen, nothing buried in a submenu |
| 2 | Lightweight tracking script (54x smaller than Google Analytics) | plausible.io | The site does not slow down |
| 3 | Cookieless measurement with no persistent identifier | plausible.io | No consent banner needed |
| 4 | Hosting in the EU | plausible.io | Data location claim |
| 5 | Open source code | plausible.io + open source page | The code is public and can be inspected |
| 6 | Real time traffic | plausible.io, /docs | How many people are on the site right now |
| 7 | Automatic scroll depth measurement | plausible.io, /docs | How much of the page was read |
| 8 | AI tool traffic tracking | plausible.io | The share of traffic coming from AI sources |
| 9 | Search Console integration | plausible.io, /docs | Search performance in the same dashboard |
| 10 | UTM campaign tracking + channel grouping | plausible.io, /docs | Grouping traffic by source |
| 11 | Codeless goal setup and revenue tracking | plausible.io, /docs | Conversion and revenue measurement |
| 12 | Funnel analysis | plausible.io, /docs | Step by step, where you lose people |
| 13 | User journeys | plausible.io, /docs | The path a visitor follows |
| 14 | Bot filtering | plausible.io | Stripping out fake traffic |
| 15 | Data import from Google Analytics | plausible.io, /docs | Carrying historical data over |
| 16 | Team management, roles, shared views | plausible.io, /docs | Several people looking at the same data |
| 17 | Custom events and saved segments | plausible.io, /docs | Events and filters you define yourself |
| 18 | Annotations | /#pricing, /docs | A "we did this on this day" note on the chart |
| 19 | Email and Slack reports | /#pricing, /docs | The numbers come to you |
| 20 | Traffic spike notification | /docs | Being told when there is a sudden jump |
| 21 | Dashboard embed | /docs | Showing the dashboard on another page |
| 22 | Shared link | /docs | Handing the dashboard link out |
| 23 | Stats API, Events API, Sites API | /docs | Reading and writing data from outside |
| 24 | Data Studio connector | plausible.io, /docs | Moving the data into another reporting tool |
| 25 | White label integration | /docs | An agency presenting it under its own brand |
| 26 | Single sign on (SSO) | /#pricing (Enterprise), /docs | Enterprise login management |
| 27 | Two factor authentication | /docs | Account security |
| 28 | Automatic 404 page tracking | /docs, /docs/metrics-definitions | Seeing broken pages |
| 29 | File download tracking | /docs, /docs/metrics-definitions | Download counts |
| 30 | Outbound link click tracking | /docs, /docs/metrics-definitions | Clicks that leave the site |
| 31 | Form submission tracking | /docs, /docs/metrics-definitions | How many people submitted a form |
| 32 | Period comparison | /docs | This month against last month |
| 33 | Combined view (many sites on one screen) | /docs | The bulk view for an agency |
| 34 | Page and traffic exclusion | /docs | Keeping internal traffic out of the numbers |
| 35 | Data export / raw event export | /docs, /#pricing (Enterprise) | Taking the data out |

Total: 35 named features.

## E) User flow (as far as it can be read off the page)
- **Sign up:** 30 day free trial, no credit card required. The order in the docs: create an account, add the site, place the tracking script. Source: https://plausible.io/#pricing and https://plausible.io/docs
- **First value moment:** once the tracking script is on the site, seeing a real time visitor appear in the single page dashboard. Three steps according to the doc flow: account, add site, place script. Source: https://plausible.io/docs
- **Reason to come back:** accumulated historical data, email and Slack reports, traffic spike notifications, goal conversions. Source: https://plausible.io/docs
- **Unclear:** what is visible in the dashboard before the script is placed is not written on the page. What a user who never finishes setup sees is unclear.

## F) Data model clues (raw)

| Clue (verbatim) | Where from | Which object it points at |
|---|---|---|
| "Add your website", "The Sites page", Sites API | /docs | Site object (every domain the user tracks is its own record) |
| Events API, "Custom properties: attach custom data when sending pageviews and events" | /docs, /docs/metrics-definitions | Event object (every pageview and custom event is one record) + free form fields attached to the event |
| "Total Visits/Sessions: set of actions a user takes on your site", "Bounce Rate", "Visit Duration", "Entry Pages", "Exit Pages" | /docs/metrics-definitions | Session object (a grouping layer above events) |
| "Goals/Events: track desired actions", "Conversion Rate", "Unique Conversions", "Total Conversions" | /docs/metrics-definitions | Goal object + conversion counters attached to the goal |
| "Total Revenue", "Average Revenue: average revenue of orders tracked" | /docs/metrics-definitions | An amount field attached to the event (revenue events) |
| "Funnels: sequence of steps and visitor drop off points" | /docs/metrics-definitions | Funnel object (ordered goal steps) |
| "Saved Segments", "Filters and segments" | /docs, /#pricing | Saved filter object |
| "Annotations" | /docs, /#pricing | A dated record attached to a note |
| "Locations: countries, regions and cities", "Browser", "Operating System", "Screen Size" | /docs/metrics-definitions | Dimension fields kept on the event (country, browser, operating system, screen) |
| "Source", "Channels", "UTM Parameters", "Referrer Drilldown" | /docs/metrics-definitions | Source fields kept on the event |
| "Team settings", "Users and roles", "Shared links" | /docs | Team, user, role and shared link objects |
| "Subscription plans", "Change plan", "Download invoices" | /docs | Subscription object + invoice |
| "Import from Google Analytics", "Import stats", "Export stats" | /docs | Transfer job object |
| "5 year data retention" (Business) | /#pricing | Retention period, a field tied to the plan |

## G) Pricing logic
- **What the price scales by:** monthly pageview volume. Feature and capacity gates sit on top of that (number of sites, number of team members, data retention period).
- **Tiers and literal figures (written on the page, verbatim):**
  - Starter: 9 dollars / month, up to 10 thousand monthly pageviews
  - Growth: 14 dollars / month, up to 3 sites and 3 team members
  - Business: 19 dollars / month, up to 10 sites and 10 team members, 5 year data retention
  - Enterprise: no figure written ("custom"), more than 10 sites, SSO, scheduled raw data export
- **Free trial:** 30 days, no credit card required.
- **Annual payment:** the page carries a "2 months free" line.
- **Common to every plan:** the simple dashboard, email and Slack reports, Google Analytics import, goals and custom events, saved segments, annotations.
- Source: https://plausible.io/ and https://plausible.io/#pricing

## H) License and terms of use
Open source. The license name appears on the page verbatim as: **"GNU Affero General Public License Version 3 (AGPLv3) or any later version"**. The page explicitly allows self hosting ("You can install and run Plausible on your own server") and says the code is readable on GitHub.
Source: https://plausible.io/open-source-website-analytics

## I) Unknowns (what cannot be worked out from the site)
- The pageview limit for the plans above Starter is not written on the home page, only the site and team limits are.
- What happens when the pageview limit is exceeded is not written.
- The data retention period on the Starter plan is not written (5 years appears only for Business).
- How long a session has to stay quiet before it ends (the session window) is not written.
- How the same visitor is deduplicated without cookies is not explained technically.
- There is no Enterprise price, it says "custom". No figure was produced.
- Whether there is region specific pricing or a local payment option could not be found (the guessed local pricing page returned 404).

## J) One line summary
5 pages fetched, 1 page could not be reached (404), 35 named features collected, 14 data model clues found, the license identified, and only the 3 figures literally written on the pricing section taken, with no figure invented for Enterprise.
