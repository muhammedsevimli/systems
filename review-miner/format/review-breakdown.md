# Review Breakdown Anatomy

> The system tags each review in `reviews/` by these headings, then clusters the themes. If a review has no information for a line, it leaves that line blank, it does not invent.

## Headings tagged for each review
1. **Sentiment:** positive / mixed (both praises and gets hung up) / criticism (complaint, low rating).
2. **Main theme:** the actual subject of the review in one word (e.g. dryness, scent, size, shipping, price, sensitivity, texture).
3. **Concrete word/sentence:** the striking expression from the customer's own mouth (this is the RAW MATERIAL for sales language, keep it verbatim).
4. **Buying signal (if any):** does it say why they bought / which pain it solved.
5. **Trust signal (if any):** does it say what they trust (scent, result, personal touch, shipping, repurchasing).
6. **Objection/hesitation (if any):** does it say what tripped them up, why they knocked off points, what they found lacking.

## Theme clustering (after tagging one by one)
The tagged reviews are collected into three groups. HOW MANY reviews each theme appears in is counted (frequency = importance signal):

1. **Why they buy (reasons for buying):** which pain, which triggering moment, which need repeats. (E.g. "my skin dries out in winter", "I avoid chemicals", "it did not suit my sensitive skin".)
2. **What they trust (trust factors):** which side of the product/brand they trust, what they praise, why they repurchase. (E.g. scent, fast absorption, not leaving greasy, shipping speed, hand-written note.)
3. **What holds them back (objections):** which complaint, hesitation, reason for return repeats. (E.g. "the jar is small", "expensive", "not clear how many days to take effect", "the lid leaked".)

## The most common objection (the most important read)
The objection that repeats most in the "what holds them back" group is marked. Rule:
- **The most common objection = the thing you need to answer UP FRONT on your sales page and in your ad.** If the customer wrote it, dozens who did not write it also gave up buying for the same reason.
- Look for a real customer sentence that REFUTES the objection: while one customer says "small", another may have said "a little goes a long way, it lasts for months". This is the ready and convincing response to the objection.
- If there is no real sentence that refutes it, use the honest response in the brand's `01-brand.md`; if that is missing too, leave a placeholder.

## Translating into sales language (three outputs per main theme)
Each main theme (especially the most common ones) is turned into three:
- **Sales angle:** which benefit you bring forward in that theme, in the customer's own words. (Raw material: the striking sentences you kept in step 3.)
- **Objection response:** the answer given up front to the hesitation around that theme (in another customer's words if possible).
- **Ad hook:** the 1-2 opening sentences that stop the scroll, again in the customer's language.

## Anti-invention (the core of this system)
- The system does NOT produce a benefit, result, timeframe, or guarantee that is NOT in the reviews. Proof is a customer sentence; a claim with no proof is not written.
- Claims with no basis in the reviews, like "in a week", "rejuvenates your skin", "certain results", are banned.
- Under each sales angle / objection response / hook, which real review(s) it came from is written. A line with no source is deleted.

## An honest note about review access (tell the audience)
- **The main way is pasting.** On most platforms like Trendyol, Amazon, Shopify, Judge.me, reviews load into the page via JavaScript, on scroll, or after login; there is no free, reliable automatic download path. You copy the reviews by hand and paste them into `reviews/` (a 2-minute job).
- **Link reading is best effort.** If you have a simple site link that shows reviews as plain page text, the system tries to read it; if it cannot, it says "paste", it does not produce invented reviews.
- Theme extraction, finding the most common objection, and sales-arsenal generation are fully automatic; the only manual thing is getting the reviews into the system.
