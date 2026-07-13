# RUN · Two Steps

> Turning reviews into sales copy is two steps. Open this file, copy the relevant command, and fill in the `<...>` parts for yourself.
> Thanks to `CLAUDE.md`, Claude Code will already read the brand + voice + objection memory + format files.

## Step 1 · Bring the reviews into the system

You have two ways:

**A) Pasting (the main way, works on every platform):** copy your product's reviews (Trendyol, Amazon, Shopify, Instagram, Google, Etsy, Judge.me, wherever they come from) and paste them into a file in the `reviews/` folder (e.g. `reviews/moisturizer.md`). How to paste is in `reviews/READ-paste-guide.md`. At least 8-10 reviews is a good start, the more reviews the clearer the themes.

**B) Link attempt (on simple pages):** if you have a single page link that shows the reviews as plain text, give this command:

```
read the customer reviews at this link and save them to the reviews/ folder: <LINK>

- extract the reviews visible on the page as plain text.
- separate each review with ---, and grab the rating and date if present.
- if you cannot read reviews from the page (it asks for login, comes back empty, does not load) do not invent. tell me "could not read, paste".
```

If the system can read them it saves them and tells you how many it found. If it cannot, you switch to pasting (most large platforms need pasting, this is normal).

## Step 2 · Analyze and produce the sales arsenal (copy)

```
analyze all the customer reviews in the reviews folder and produce a sales arsenal for me.

rules:
- first say in one line that you read the brand + voice + objection memory + format + raw reviews files, and how many reviews you found.
- tag each review by sentiment (positive / mixed / criticism) and theme.
- cluster the repeating themes into three groups and count how many reviews each appears in: why they buy, what they trust, what holds them back.
- mark the most common objection in the "what holds them back" group and write how many reviews it appears in.
- for each main theme produce in my brand's voice: sales angle, objection response, ad hook.
- build the angles and hooks from the customer's own words. do not invent a benefit, result, or guarantee that is not in the reviews.
- when you answer an objection, if there is another real customer sentence that refutes it use that; otherwise use my real offer from the brand; if neither exists, leave a placeholder.
- under each angle write which reviews it came from with a short quote (proof trail).
- do not use the banned words in 02-voice.md, do not use em dashes.
- write the output to the outputs/ folder as YYYY-MM-DD-product.md. at the end, give a LinkedIn measured-register note.
```

## Short version (when in a hurry)

```
analyze the customer reviews in reviews/: cluster the themes (why they buy / what they trust / objections), find the most common objection, produce a sales angle + objection response + ad hook for each main theme, build them all from the customer's own words, do not invent. write the output to outputs/. follow the voice and format files, no em dashes.
```

## Note
The more reviews you give, the clearer the themes come out. At least 8-10 reviews, ideally 20-50. Give both five-star and low-star reviews together: sales angles come from the positive reviews, objection responses come from the criticism. One-star reviews are gold, that is where you see what holds people back the most.
