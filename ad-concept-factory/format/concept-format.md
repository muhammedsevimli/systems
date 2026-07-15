# 50 Concepts · Output Format and Diversity Rule

> After the analysis, the system writes exactly 50 static ad concepts. They all follow this structure.
> The goal: when you wake up, 50 fresh concepts are ready in front of you; you move the ones you like into design and cut the rest. Idea block ends.

## Structure of the output file
The system writes the output to `outputs/YYYY-MM-DD-<theme>.md` in this order:

### A) Input summary + extracted pattern (one paragraph)
How many winning ads, how many reviews were read; the repeating hook type, common promise, common emotion, most common objection and the customer sentence that refutes it. "The logic that clearly works" is summarized here in one paragraph.

### B) 50 concepts (split into rotation groups)
Each concept consists of THREE lines (a tweet-sized promise: hook + visual direction + one-line rationale):

```text
### Concept N · <short name>  [hook type · segment]
- hook: <a single-sentence opener in your brand's voice>
- visual: <single image / video / carousel / UGC> + a one-line concrete static visual/scene direction
- rationale: <which winning ad or which customer sentence it came from + why it can land, one line>
```

### C) Morning shortlist note
The 5 concepts the system finds strongest (with their numbers) and why you should start with them. For quick morning selection. No em dash in this note either: if you need a separator, use a middle dot ( · ) or a colon.

### D) Platform note
Ready in "you" (informal) for Instagram/Facebook. At the end, a note on the measured register for LinkedIn.

---

## Diversity rule (MOST IMPORTANT · not 50 filler)
50 concepts are NOT 50 copies of one hook. The system rotates on three axes. The same hook type appears at most twice in a row; then the axis changes.

### Axis 1 · Hook type (10 types · about 5 concepts of each)
1. **Pain / regret** (the pain the customer avoids).
2. **Sensory / curiosity** (aroma, texture, moment; the "feel it" hook).
3. **Number / value** (per-cup math, duration, ratio; a concrete number).
4. **Social proof** (customer review, how many people, rating).
5. **Contrarian / myth-busting** (the thing everyone gets wrong).
6. **Humor / acceptance** (the viral angle in the most-liked comment).
7. **Objection-busting** (answer the price/commitment/"will it work" hesitation head-on).
8. **Ritual / identity** (the person the user wants to be, the habit).
9. **Comparison** (before/after, yours vs the alternative).
10. **Gift / special moment** (a reason to buy for someone else).

### Axis 2 · Segment (the brand's sub-audiences · each concept speaks to one)
The system extracts the segments from `brand/01-brand.md` and distributes them. For an example coffee brand: filter drinker · espresso/moka · office/workplace · beginner · developed palate · budget-focused · gift buyer · commitment-shy. Each concept is written to a clear segment; the segments rotate through the round.

### Axis 3 · Emotion (each concept pushes one emotion)
relief · avoiding regret · pleasure/delight · belonging · smart spending · trust · curiosity · pride. The emotion rotates too; the same emotion does not pile up back to back.

### Combination logic
Each concept = one hook type × one segment × one emotion. 10 hook types × several segments × several emotions opens more than enough room for 50 genuinely different concepts. The system writes the `[hook type · segment]` tag in the heading line so the diversity is visible and you pick from the box you want.

## Firm rules
- If you use the customer's sentence verbatim, take it from a real review, never invent. Take the logic of the winning ad, do not copy its words.
- No made-up numbers / discounts / guarantees. If it is not in `brand/01-brand.md`, use a `[put your own number/offer here]` placeholder.
- No fake urgency, exaggeration, or non-existent guarantee (even if it appears in a review or an old ad). Do not contradict the "what you are NOT" line in `brand/01-brand.md`.
- Tone from `brand/02-voice.md`. No banned words. No em dash.
- Each concept carries a single idea, the hook is one sentence, clear. The visual direction is concrete enough to be drawn without the designer having to ask.
- Do not re-produce to fill the count of 50. If 50 genuinely different ideas do not come out, enrich the input (more winning ads and reviews), but still deliver the requested 50 and honestly mark the weak ones in the "morning shortlist" note.
