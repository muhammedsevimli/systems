# Product Plan · Build Plan From a URL · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You set nothing up. Claude Code loads it on its own while working in this folder.
> The goal: pull out the logic of a product you like and turn it into a plan adapted to YOUR business, buildable in order. You give one URL; the system browses the site itself, takes its logic apart, and writes three files: the product plan, the data schema, and a Claude Code prompt set.

## Where this system stands (unchangeable, the most important section)
This system is **not a clone factory.** It pulls out the logic of the target product, not a copy of it.

- The system never says "build the same thing". The output is always "the version for your niche, the one you can build".
- Brand name, logo, colour system, one to one interface design, page copy, icon set, copyrighted content and licensed source code are NOT COPIED. The system marks these in a separate "do not copy" list.
- The only thing that can be lifted is a product's **logic**. That is: which job it solves in which order, which objects it keeps, how it walks the user to first value, what it charges by. These sit at the level of ideas and are already written in public on the site.
- The target product's audience and your audience are not the same. The system reads `you/01-profile.md` and reorders every feature for your niche. A feature the target has may not belong in your v1; a feature the target does not have at all may be mandatory in your niche. The system shows both in separate tables.
- If the system detects a license (open source license, terms of use) on the target product, it writes that into the report and adds the note: no taking the code, only pulling out the logic.

## What the system does (two phases)
1. **Automatic site reading (you copy nothing):** it takes the URL in `you/02-target.md`. With Claude Code's WEB TOOLS (WebFetch + WebSearch) it browses the home page, the features page, the pricing page and the documentation if there is any, ITSELF. From every page it pulls what is actually written and writes it, with the source link, into `breakdown/breakdown-YYYY-MM-DD.md`. A page it cannot reach is marked "could not be reached"; it does not invent content.
2. **Turning it into your version (automatic):** it merges the breakdown with `you/01-profile.md` and writes three files into `outputs/`: the product plan, the data schema, the Claude Code prompt set.

## PHASE 1 · When site reading is requested
Read `you/01-profile.md` and `you/02-target.md`. Then, for the target URL, in order:

1. **Home page:** fetch the target URL with `WebFetch`. Pull out: what the product does in one sentence, who it speaks to (the audience wording written on the page), every feature named on the page.
2. **Features page:** if the home page carries a feature link (`/features`, `/product`, `/platform` and the like), fetch that with `WebFetch` too. Widen the feature inventory. Next to every feature write which page it appeared on.
3. **Pricing page:** fetch `/pricing`, `/plans`, or the pricing section on the home page. Pull out: what the price scales by (number of users, usage volume, number of sites, feature bundle), the plan tiers and the numbers written LITERALLY on the page, whether there is a free trial, what is common to every plan.
4. **Documentation:** fetch `/docs`, `/help`, `/support`, `/api` if they exist. Doc headings are the most honest source for the data model: which objects exist, which metrics are kept, which settings hang off what. If there is a metrics or definitions page, fetch that separately.
5. **If a gap remains, `WebSearch`:** if a page could not be reached or the pricing logic is unclear, run a `WebSearch` for "<product name> pricing" / "<product name> features". Take only what appears LITERALLY in the search result, add no interpretation.
6. **License / terms of use:** if the product is open source or a license appears on the page, write the license name verbatim.

Write everything you pull into `breakdown/breakdown-YYYY-MM-DD.md` in the structure of `format/product-breakdown.md`. A source URL is mandatory on every line. One summary line at the end: which pages were fetched, which could not be reached.

## PHASE 2 · When the plan is requested, read these files IN ORDER (required)
1. `you/01-profile.md` · who you are, who you serve, what you can build, what your limits are.
2. `you/02-target.md` · the target URL and what you are curious about.
3. `format/rules.md` · the core / decoration test, the copy protection, the anti invention rules.
4. `format/plan-format.md` · the structure of the three outputs.
5. The most recent breakdown file in the `breakdown/` folder.

Do not produce anything before reading these files. Start the job by saying "profile + target + rules + format + breakdown read".

## PHASE 2 steps (what the system does inside)
1. **Sort the features into buckets.** Put every feature in the breakdown through the test in `format/rules.md` and drop it into one of four buckets: CORE (v1), SUPPORT (v1.5), DECORATION (later), STAY OUT (never, because of your limits or the infrastructure load). A one sentence reason is mandatory on every line. No bucket without a reason.
2. **Build the niche adaptation table.** Two columns: (a) exists in the target but is pointless in your niche, (b) does not exist in the target but is mandatory in your niche. Column (b) comes out of your profile file and your local market reality. This table is where a clone parts ways with an adaptation, and it is not left empty.
3. **Write the user flow.** Three rings: sign up, the first value moment (the first moment the user says "alright, this works"), the reason to come back. Count how many steps it takes to reach first value. Write the single change in your version that lowers that number.
4. **Pull out the data schema.** From the doc headings, the metric definitions and the interface descriptions, work out which objects are kept. Write a plain table list: table name, fields, which table it relates to. Next to every table, one sentence on "why this exists". Then write the simplified version of the same schema for YOUR v1 (fewer tables, fewer fields).
5. **Pull out the pricing logic.** What does the price scale by, and does that work in your niche. If it does not, write why and propose the unit of measure that fits your niche. If there is no number on the page, DO NOT INVENT one, write "no pricing figure available".
6. **Write the prompt set.** Produce prompts to be pasted in order, per the rule in `format/plan-format.md`. Every prompt does one job, takes the output of the previous one as input, and ends with an acceptance line: "when you are done you should see this".
7. **Write the three files.** `outputs/YYYY-MM-DD-product-plan.md`, `outputs/YYYY-MM-DD-data-schema.md`, `outputs/YYYY-MM-DD-prompts.md`.

## Unchangeable production rules
- **DO NOT INVENT features.** Use only information actually pulled and carrying a source link inside `breakdown/`. Do not write a feature you did not see on the page.
- **DO NOT INVENT pricing.** If there is no pricing page or it could not be reached, write "no pricing figure available". Do not guess a number, do not say "it is probably around this much per month".
- **The schema is an INFERENCE.** Write this at the very top of the data schema file: this schema is not the product's real database, it is an inference made from public pages. Next to every table, write which evidence the inference stands on (which wording on which page).
- **If you are not sure, say "unclear".** Do not fill gaps. Collect what stays unclear under its own heading ("this cannot be worked out from the site").
- **Copy protection.** Write a separate "do not copy" list for the brand name, logo, design, page copy, copyrighted content and licensed code. The sentences "build the same thing", "clone it", "make it one to one" appear nowhere in the output.
- **Differentiation is mandatory.** The "what are you doing differently" heading in the plan file cannot be left empty. Write at least one concrete difference (language, niche, pricing unit, focus on a single pain).
- **Flag the risky part.** If there are pieces that need permission or compliance, such as payment infrastructure, personal data, health, legal, finance, take them out of v1 and add the note: this piece needs permission or compliance.
- **No em dash anywhere in the output.** If you need a separator, use a full stop, a comma, a colon or a middle dot (·).
- **No motivational language, no income promises, no hype.** Sentences like "build this and you will blow up" are banned. The system talks like a cool headed product analyst.

## Where the output is written
Every run produces three files, all into `outputs/`:
- `YYYY-MM-DD-product-plan.md` · feature buckets, niche adaptation table, user flow, v1 scope and build order, pricing logic, do not copy list, unknowns.
- `YYYY-MM-DD-data-schema.md` · the schema inferred from the target product (with evidence) and your v1 schema (simplified).
- `YYYY-MM-DD-prompts.md` · Claude Code prompts to paste in order, each with its acceptance line.

## Persistent memory
When you study a new target product, write it with the date into the "studied products log" at the bottom of `you/02-target.md`: which product, what you learned, which idea you took, what you did not take. From the second product on, the system reads the old log too and shows the repeating patterns ("every product of this type has this") under a separate heading. Over time this log becomes the persistent record of your product instinct.
