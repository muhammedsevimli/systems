# Sales Page + Payment · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/sales-page.mdc`.
> The goal: write your product or service into one file and get both the copy of a page that can sell and the working single file HTML version of it. Drag the page onto any free static host and it is live.

## Where this system stands (unchangeable)
This system builds the PAGE, it does not touch the MONEY. It sets up no payment provider, opens no account, configures no fees, processes no card details, and asks for no credentials (username, password, API key). You paste the ready made payment link you already have (Stripe Payment Link, Gumroad, Lemon Squeezy, Paddle and the like) into a file as a single line, and the system wires it to the button on the page. Email collection works the same way: you give your own form endpoint (Formspree, Google Form, Klaviyo, Mailchimp embed) as one line and the system wires it to the form. The money flow and the mailing list stay in your own account. The system only writes the page.

## What the system does (three phases)
1. **Copy (the sales writing):** it reads `you/01-product.md`. It reads what the product is, who it is for, which pain it answers, the price, the proof, and writes the sales copy: title, subtitle, who it is for, pain, solution, what is included, proof, price, FAQ, refund and contact, CTA. The copy goes into `outputs/<slug>-copy.md`.
2. **Page (single file HTML):** it takes the `format/template.html` skeleton, drops the copy and the form endpoint and payment link from `you/02-links.md` into place, and produces `outputs/<slug>-sales-page.html`. No dependencies, no build, it opens without an internet connection (single file, pulls no external font or script).
3. **Launch checklist:** it fills the `format/launch-checklist.md` list in for that product and writes it to `outputs/<slug>-launch-checklist.md`. You tick the items off one by one before going live.

## PHASE 1 · When the sales copy is requested, read these files IN ORDER (required)
1. `you/01-product.md` · what the product is, who for, which pain, what is included, price, proof, refund, contact, what it is NOT.
2. `you/02-links.md` · form endpoint, payment link, button labels, colour.
3. `format/page-format.md` · the section order of the page and the writing rule for every section.

Do not produce anything before reading these files. Start the job by saying "product + links + format read".

### The missing information rule (the hardest rule)
If a field inside `you/01-product.md` is EMPTY, DO NOT INVENT that section.
- No proof: DO NOT PUT the proof section on the page at all. Do not write an invented customer review, an invented star rating, an invented "300 people used it", an invented "up 40 percent". At the end of the copy report write "the proof field is empty, no proof section was put on the page; once you have one sentence from your first customers it goes here".
- No price: give a "no price entered" warning instead of a price, and do not produce the page without a price, ask first.
- No refund policy: DO NOT INVENT one (like "14 day no questions asked refund"), warn that "you have to write the refund terms yourself".
- No contact: the page cannot be published, warn.
- General rule: **no information that is not in the file gets onto the page.** If you are not sure, say "this information is not in the file".

### The "what it is NOT" protection
Read the "what it is NOT / what you do not offer" lines in `you/01-product.md`. The page implies nothing the operator does not offer. Example: if the operator wrote "I do not do one to one sessions", DO NOT build a sentence like "reach me any time and we will look at it together".

### Language and voice rules (the sales copy)
- Plain English, like talking. The reader is not technical.
- **No em dash.** If you need a separator, use a full stop, a comma, a colon, a middle dot (·).
- **No inflated promises:** "guaranteed", "certain results", "X percent gain guaranteed", "your life will change", "do not miss out", "only 3 spots left" (when that is not actually true) are banned. Urgency is written only if it is REAL and written in the file.
- **No motivational language.** The page speaks coolly and clearly.
- **No "it is not X, it is Y" contrast pattern.** State the contrast plainly.
- No income promises and no revenue flexing.
- In fields like health, finance and legal, write no outcome promise; add an "this is for information and education" note.
- Use the second person ("you"), do not build corporate language.

## PHASE 2 · Producing the HTML page
Read `format/template.html` and fill in these placeholders:

| Placeholder | Where it comes from |
|---|---|
| `{{TITLE}}` | the main title of the copy |
| `{{SUBTITLE}}` | the one sentence explanation |
| `{{BRAND}}` | the brand / seller name from `you/01-product.md` |
| `{{WHO_FOR}}` | the who it is for items (list) |
| `{{PAIN}}` | the pain paragraph |
| `{{SOLUTION}}` | the solution paragraph |
| `{{INCLUDES}}` | the what is included items (list) |
| `{{PROOF}}` | the proof block. If there is no proof the WHOLE block is deleted |
| `{{PRICE}}` · `{{PRICE_NOTE}}` | the price and its one line note (e.g. tax included, one off payment) |
| `{{FAQ}}` | the frequently asked questions (question + answer) |
| `{{REFUND}}` · `{{CONTACT}}` | the refund terms and the contact line |
| `{{PAYMENT_LINK}}` | the payment link from `you/02-links.md`, into the `href` |
| `{{PAYMENT_BUTTON}}` | the label of the payment button |
| `{{FORM_ACTION}}` | the form endpoint from `you/02-links.md`, into the `<form action>` |
| `{{FORM_TITLE}}` · `{{FORM_NOTE}}` · `{{FORM_BUTTON}}` | the heading, one line note and button label of the email block |
| `{{ACCENT_COLOUR}}` | the brand accent colour (if none is given the template default stays) |

Rules:
- The produced file must be a SINGLE file. DO NOT PULL external CSS, external JavaScript, external fonts or external images. The `<style>` stays inside the page.
- `<meta name="viewport" content="width=device-width, initial-scale=1">` always stays (mobile fit).
- Dark and light theme support through `prefers-color-scheme` is ready in the template, do not delete it.
- If no payment link was given, do not set the button `href` to `#`; leave the button as a visible warning reading `PAYMENT_LINK_HERE` so the user does not forget it.
- If no form endpoint was given, leave `action="FORM_ACTION_HERE"` and put a visible "the form is not connected" note at the bottom of the page.
- No tracking code, no analytics, no cookies, no third party script on the page (the user adds those later themselves).
- No em dash in the page copy.

Write the page as `outputs/<slug>-sales-page.html`. `<slug>` = the product name in lower case with no spaces and no special characters.

## PHASE 3 · Launch checklist
Fill the `format/launch-checklist.md` list in for the specific product (the name of the form endpoint, the name of the payment provider, the price, the refund line) and write it to `outputs/<slug>-launch-checklist.md`. The list is made of items the user will REALLY test before going live; do not say "everything is ready", make them test it.

## Unchangeable production rules
- **DO NOT INVENT information.** A feature, number, review, customer, institution, award or certificate that is not in the file does not go on the page.
- **The proof invention ban applies separately.** No invented review, no invented name, no invented percentage, no invented "X people bought it". No proof means no section.
- **The inflated promise ban.** No sentences like "guaranteed", "certain results", "this page will multiply your sales".
- **Never ask for credentials.** A payment provider account, an API key or a dashboard password is never requested. The system only wires a ready made link into the page.
- **The price and the currency are written exactly as they are in the file**, no invented discount, no fake struck through old price.
- **No em dash anywhere in the output:** not in the copy, not in the HTML, not in the checklist.
- **Legal minimum:** the page carries the seller name, the price, the refund or cancellation terms and a way to make contact. If one of them is missing the system warns. What counts as the legal minimum differs by region and by what you sell, so check the rules that apply where you sell and add the lines they require.
- **Accessibility minimum:** the contrast between text and background is not low, the button is at least 44 pixels tall, the form field has a `<label>`, and the page language is `lang="en"` (change it if you write the page in another language).

## Where the output is written
Three files into `outputs/` on every run:
- `outputs/<slug>-copy.md` · the sales copy (section by section, editable)
- `outputs/<slug>-sales-page.html` · the single file page that opens on a double click
- `outputs/<slug>-launch-checklist.md` · the pre launch test list

## Persistent memory
If you update the product, update `you/01-product.md` and have the page produced again. Write the address and the publish date of the page you put live into the "publish log" section at the bottom of `you/02-links.md`. Note there what happened after a title or price change too; later pages feed off that log.
