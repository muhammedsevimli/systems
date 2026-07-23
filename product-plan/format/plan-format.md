# Plan Format · The Three Outputs of PHASE 2

> Every run writes THREE files into `outputs/`. All three follow this structure.
> Common rule: no em dash, no motivational language, no "build the same thing", no line without a reason.

---

# FILE 1 · `YYYY-MM-DD-product-plan.md`

## 1. Run details
Target URL, scan date, how many pages were read, how many could not be reached. One paragraph.

## 2. What this product does, and for whom
No more than two paragraphs. The product's logic, without decoration.

## 3. Feature buckets
One table, a reason on every line. Buckets: CORE (v1), SUPPORT (v1.5), DECORATION (later), STAY OUT.

| Feature | Bucket | Reason (one sentence) |
|---|---|---|

CORE is 5 to 7 rows at most. Cut if there are more.

## 4. Niche adaptation table (cannot be left empty)

**Exists in the target, pointless in your niche**

| Feature | Why pointless |
|---|---|

**Missing from the target, mandatory in your niche**

| Need | Why mandatory | Where it came from (profile line) |
|---|---|---|

## 5. User flow
- In the target: sign up, first value moment, reason to come back. How many steps to first value.
- In your version: the same three rings, but for your user. Write how many steps you cut the first value moment down to, and say in one sentence how you cut it.

## 6. What are you doing differently (differentiation, cannot stay empty)
At least one concrete difference. "Better design" does not count.

## 7. v1 scope and build order
Numbered list. Every step does one job. Every step ends with a "when you are done you should see this" line.
Order rule: data first, then the shortest road to the first value moment, then persistence, then the reason to come back, polish last.

## 8. What did not make v1, and why
Short list. One sentence reason on every line. This section is the most valuable part of the plan, it is not skipped.

## 9. Pricing logic
- What the price scales by in the target (with evidence). If there is no figure, "no pricing figure available".
- Does that unit work in your niche, and if not, why.
- The unit proposal that fits your niche, with a one sentence reason.

## 10. Do not copy list
Brand, logo, design, copy, copyrighted content, licensed code. If there is a license, the name verbatim and one sentence on what it means.

## 11. Unknowns and risks
What cannot be worked out from the site. Pieces that need permission or compliance. Weak assumptions.

---

# FILE 2 · `YYYY-MM-DD-data-schema.md`

## 0. Warning line (mandatory, at the very top)
This schema is not the product's real database. It is an inference made from public pages.

## 1. The schema inferred from the target product
For every table:

### `table_name`
- **Why it exists:** one sentence.
- **Evidence:** which wording on which page (URL).
- **Fields:** item by item, every field a single word or a short name.
- **Relation:** which table it hangs off.

A table with no evidence is not written.

## 2. Your v1 schema (simplified)
The same structure, but fewer tables. Rule: the v1 schema should not go past 6 tables. If it does, v1 is bloated, merge them.
Under every table, one sentence on "what I dropped from the target schema and why".

## 3. Relation map (one block, plain text)
```text
table_a  1 to n  table_b
table_b  1 to n  table_c
```

## 4. Questions that will break the schema
Decisions that will hurt later. For example: how long the data is kept, how deletion works, what happens when the same record arrives twice.

---

# FILE 3 · `YYYY-MM-DD-prompts.md`

Prompts to paste into Claude Code in order. Rules:

1. **Every prompt does one job.** If there are two jobs, split it in two.
2. **Chain rule:** every prompt takes the OUTPUT of the previous one as input and says so in its first sentence ("on top of the thing you built in the previous step...").
3. **Acceptance line is mandatory:** every prompt ends with a single "when you are done you should see this" line. If you did not see it, do not move to the next one.
4. **Between 6 and 10 prompts.** If there are more, v1 is bloated, go back to the plan file.
5. **Prompts contain no code.** They describe what you want in plain English. Do not dictate the technology inside the prompt, set a boundary instead, like "keep it simple and in a single file".
6. **The first prompt always builds the schema.** The last prompt is always shipping it and showing it to the first user.
7. Every prompt's heading says what it does and carries an estimated time.

Template:

```text
## Prompt N · <what it does> (<estimated time>)

<plain English instruction. first sentence chains to the previous step. one job. boundaries.>

when you are done you should see this: <one line acceptance criterion>
```

At the end of the file, one section: **If you get stuck** · the three most common sticking points and what to do about them.
