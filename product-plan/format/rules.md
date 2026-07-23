# Rules · Core / Decoration Split, Copy Protection, Anti Invention

> This file is the system's decision ruler. It does not score, it sorts.
> This file is not changed, so the system stays impartial. The only file you change is `you/01-profile.md`.

## A) The core / decoration test (every feature goes through these three questions)

Ask every feature, in order:

1. **Removal test:** if you deleted this feature completely, would the product still deliver its main promise? If it would, this feature is NOT core.
2. **First value test:** can the user reach the moment where they say "alright, this works" without this feature? If they cannot, this feature is core.
3. **Frequency test:** what share of users touch this feature in the first week? If it is a minority, it does not go into v1.

Based on the answers, the feature lands in one of four buckets. A one sentence reason is mandatory on every line.

| Bucket | What it means | Rule |
|---|---|---|
| **CORE (v1)** | Without it the product is not the product. It stands on the road to the first value moment. | 5 to 7 items at most. More than that and you cut the list, v1 is bloated. |
| **SUPPORT (v1.5)** | Makes the product comfortable, but its absence is not fatal in the first version. | Queues up after the first 20 users. |
| **DECORATION (later)** | Looks good, works as a sales argument, few people use it. | If the build cost is high it may never go in. |
| **STAY OUT** | Hits your limits, needs permission or compliance, or the infrastructure load is bigger than the product itself. | The reason is always written. It is never dropped silently. |

**Scale features do not go into v1.** Team management, roles, single sign on, enterprise export, advanced permissions, multi language interface: these are jobs for after the product works. Building them in v1 is hiring a doorman for a product with no users.

**Integrations do not go into v1.** Every "integrates with" feature in the target product sits in the SUPPORT or DECORATION bucket. One exception: if the product's main promise does not work without the integration (the data comes from there), it is core.

## B) Niche adaptation (where a clone parts ways with an adaptation)

Once the bucket split is done, a two column table is mandatory:

- **Exists in the target, pointless in your niche:** features that stop making sense because the target's audience is different from yours. Write "why pointless" on every line (e.g. your user does not have that volume, that device, that workflow).
- **Missing from the target, mandatory in your niche:** needs that come out of your profile file and your local market reality, and that the target product does not have at all. Write "why mandatory" on every line.

The second column CANNOT BE LEFT EMPTY. If it is empty the system has not thought hard enough; it rereads the profile file and pulls out at least two items. The second column is the reason your product exists.

## C) Copy protection (hard rule)

The system is not a clone factory. The split below applies to every output.

**Can be pulled out (idea level, already public on the site):**
- Which job the product solves and who it speaks to
- The feature inventory and the order of importance
- The user flow and the first value moment
- The inference about which objects it keeps
- The logic of what the price scales by

**Not copied (marked in a separate list in the output):**
- Brand name, logo, brand colours, type system
- One to one interface design, screen layout, icon set
- Page copy, tagline, marketing sentences
- Copyrighted content, images, video, data sets
- Licensed source code. If the product is open source the license name is written verbatim, with this note: no taking the code, only pulling out the logic. Some open source licenses (for example strong copyleft licenses like AGPL) do not let you take the code and put it into a closed product. Building a product from an idea is free; moving the code is a different matter.

**Banned sentences:** "build the same thing", "clone it", "make it one to one", "ship a free version of it". The system does not write these. The frame of the output is always: pull out the logic, adapt it to your own niche, build it yourself.

**Differentiation is mandatory:** the "what are you doing differently" heading in the plan file cannot stay empty. At least one concrete difference is written: language, a narrower niche, focus on a single pain, pricing unit, a service layer. "Better design" does not count as a difference, it cannot be measured.

## D) Anti invention (the honesty rule)

- Do not write a feature you did not see on the page. A source URL is mandatory on every feature line.
- **Pricing:** take only the figure written LITERALLY on the page. If there is no pricing page, it could not be reached, or it says "contact us", write "no pricing figure available" in the output. Do not write an estimated number, do not say "probably".
- **Unreachable page:** mark it "could not be reached" and write the reason (404, wants a login, blocked). Do not go filling in the information you assumed would come from it.
- **The data schema is an inference.** It is not the product's real database. That warning sits at the top of the schema file. The evidence for the inference is given next to every table (which wording on which page). A table with no evidence is not written.
- **Unknowns are collected under their own heading.** A "this cannot be worked out from the site" list exists in every report. If it is empty the system has not looked critically enough.
- No em dash appears in any output. Separators: full stop, comma, colon, middle dot.
- No motivational language, no income promises, no hype. The system talks like a cool headed product analyst.

## E) Flagging the risky part

These pieces come out of v1, with the reason written:
- Payment infrastructure and holding money (permissions, reconciliation, refund process)
- Collecting personal data and identity matching
- Regulated fields such as health, finance and legal
- Structures that need continuous live operation or an on call rota

This does not mean "never build it". It means not in v1. If the product works, its turn comes.

## F) Honest limit (written on purpose)

- The system reads PUBLIC pages only. The product's real database, real user behaviour and real margin are not written on its site. The output is an outside reading.
- Some sites are closed to automatic reading (bot protection, login wall, `403`). The system tries, and if it cannot reach the page it says "could not be reached" and leaves that part empty.
- Pulling out a product's logic does not guarantee why that product worked. The reason is usually the thing that is not on the site: distribution, timing, community. The plan gives you a build order, not a demand guarantee.
- The plan is a starting point. Once you talk to the first five users the buckets change. That is normal.
