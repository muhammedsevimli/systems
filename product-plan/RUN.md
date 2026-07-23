# RUN · Two Commands

> The system works in two steps. Open this file and copy the relevant command.
> You open and copy no pages. You write one URL into `you/02-target.md`, and the system browses the site.
> Thanks to `CLAUDE.md`, Claude Code will already read the profile, target, rules and format files.

## Step 1 · Read the product and pull out its logic (copy)

```
read the product in you/02-target.md and pull out its logic.

rules:
- read you/01-profile.md and you/02-target.md.
- browse the site yourself with your web tools (WebFetch + WebSearch):
  - fetch the home page with WebFetch: what it does, who it speaks to, which features are named.
  - try the features page (/features, /product, /platform).
  - try the pricing page (/pricing, /plans). what does the price scale by, which figures are written literally.
  - try the documentation (/docs, /help, /api). doc headings are the most honest source for the data model.
  - if it is open source, take the license name verbatim.
- if you cannot reach a page, write "could not be reached" and the reason. do not invent the information you assumed would come from it.
- if there is no pricing page or no figure on it, write "no pricing figure available". do not guess a number.
- put a source url on every line. do not write a feature you did not see on the page.
- collect what cannot be worked out from the site under an "unknowns" heading, do not leave it empty.
- write the output into breakdown/breakdown-TODAYS-DATE.md in the structure of format/product-breakdown.md.
```

The system browses the pages itself and writes what is actually there into `breakdown/`. You put nothing in that folder by hand. How it fills up: `breakdown/READ-how-this-fills.md`.

## Step 2 · Turn it into your own plan (copy)

```
turn the breakdown in the breakdown folder into my product plan.

rules:
- first say in one line that you read the profile + target + rules + format + breakdown files.
- put every feature through the three questions in format/rules.md (removal test, first value test, frequency test) and drop it into one of four buckets: CORE v1, SUPPORT v1.5, DECORATION, STAY OUT. one sentence reason per line. core is 7 items at most.
- build the niche adaptation table: what exists in the target but is pointless in my niche, and what is missing from the target but mandatory in my niche. do not leave the second column empty, pull it from my profile.
- write the user flow: sign up, first value moment, reason to come back. how many steps to first value in my version.
- pull out the data schema: which objects exist, their fields, what they relate to. write the evidence for every table (which wording on which page). then write the simplified schema for my v1, no more than 6 tables.
- pull out the pricing logic: what does it scale by, does that unit work in my niche, and if it does not, which unit fits me.
- write the claude code prompt set: between 6 and 10, each prompt doing one job, each chained to the output of the previous one, each ending with a "when you are done you should see this" line. the first prompt builds the schema, the last one ships it.
- write the do not copy list: brand, logo, design, page copy, copyrighted content, licensed code. if there is a license, write its name.
- do not say "build the same thing", "clone it", "make it one to one". i am building a product adapted to my own niche.
- do not leave "what are you doing differently" empty, write at least one concrete difference.
- do not invent features or prices. say "unclear" for anything you are not sure of. do not use em dash, no motivational language.
- write the three files into the outputs folder: TODAYS-DATE-product-plan.md, TODAYS-DATE-data-schema.md, TODAYS-DATE-prompts.md.
```

## One command (when in a hurry: read and turn into a plan together)

```
browse the product in you/02-target.md yourself with your web tools (home page, features, pricing, docs), pull out its logic and turn it into my plan.
write the breakdown into the breakdown folder and the three outputs (product plan, data schema, prompt set) into the outputs folder. follow the rules and format files. adapt it to the niche in my profile, do not propose a clone, mark an unreachable page "could not be reached", invent no price and no feature.
```

## Step 3 · When you decide (copy)
```
i decided <to build / to drop> the idea i took from <product>, reason: <short>. add it to the studied products log at the bottom of you/02-target.md with today's date: which product, what i took, what i did not take, what i decided.
```

## Note
Give one product. If you study two products in the same run the plan gets blurry; study the second one in a separate run, and the system reads both from the studied products log in `you/02-target.md`.
The fuller `you/01-profile.md` is, the more the plan is yours. With an empty profile the output turns into a generic product plan.
Use the prompt set in order. If you could not see a prompt's acceptance line, do not move to the next one, fix that step first.
