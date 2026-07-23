# Sales Page + Payment · Single File Page Builder 🧾

Write your product or service into one file: what it is, who it is for, which pain it answers, the price, the proof. The system writes the sales copy, produces a working `.html` page that opens on a double click, wires your email form and your ready made payment link into it, and hands you a launch checklist to test before you go live. Drag the page onto a free static host and it is live. A no-code sales page builder that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

No dependencies, no build step, no account. One file.

## What it does

The product or the service is ready and you have no page to point people at. You keep saying "coming soon". You think a page needs a designer and taking money needs infrastructure. So for months you have been quoting prices in DMs and sending bank details.

This system produces that page. There is nothing to install and nothing to build: a single `.html` file comes out, it opens on a double click, and it holds up on a phone and in dark mode.

## The system does NOT set up payments (honest limit, up front)

The system sets up no payment provider, opens no account in your name, processes no card details, configures no fees, and asks you for no password and no API key. You get a ready made payment link on the Stripe, Gumroad, Lemon Squeezy or Paddle side (a one time job), you paste that link into a file, and the system wires it to the button on the page. Collection, refunds and invoicing run in your own provider account. Email collection is the same: you give your own form endpoint (Formspree, Google Form, Klaviyo, Mailchimp) and the system wires it to the form. The list stays in your account.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal knowledge required.
- A folder and 20 minutes. You are not learning anything new, just writing your own product into a file.
- A ready made payment link and a form endpoint, if you want to take money and collect emails. Both are free to start and both are a one time setup on your side.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/sales-page.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/sales-page sales-page
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set this sales page up for my product". It fills the product and links files in with you.

These are the files the system reads. Fill in the product and links part with your own:

- `you/01-product.md`: what the product is, who for, which pain, what is included, price, proof, FAQ, refund, contact, what it is NOT
- `you/02-links.md`: your form endpoint, your ready made payment link, button labels, accent colour + the publish log
- `format/page-format.md`: the section order and the writing rules (comes ready)
- `format/template.html`: the single file page skeleton with placeholders (comes ready)
- `format/launch-checklist.md`: the pre launch test list template (comes ready)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then one command:

> build my sales page

The system writes three files into `outputs/`: the copy, the page, the checklist. For the full command, see `RUN.md`.

## How it works

Three phases, one command:

1. **Copy.** `you/01-product.md` is read and the sales copy is written: title, subtitle, who it is for, pain, solution, what is included, proof, FAQ, price, refund, contact. It lands in `outputs/<slug>-copy.md`, and you can fix any sentence by hand.
2. **Page.** The copy and the links are placed into the `format/template.html` skeleton and `outputs/<slug>-sales-page.html` is produced. Single file, no external font or script, mobile friendly, dark and light theme friendly.
3. **Launch checklist.** `outputs/<slug>-launch-checklist.md` is produced. Before you go live you test, one by one: does the form really deliver mail, does the payment link go to the right product, are the price and the refund terms written.

## What it does not invent

- If you gave no proof, there is no proof section on the page. No invented customer review, no invented star rating, no invented "300 people bought it", no invented "up 40 percent".
- If you wrote no refund policy, it does not invent "14 day no questions asked", it warns that you have to write it.
- If you gave no payment link or form address, it does not quietly wire the button to nothing; it leaves a visible red warning on the page so you catch it before publishing.
- No guarantees, no certain results, no fake urgency, no motivational language.
- It implies nothing you said you do not offer.

## Does it really work? Test it in 30 seconds

- **Single file:** open the produced `.html` in a text editor and search for `http` inside `<link`, `<script` and `@import`. If there is no external source, it passed.
- **Empty field:** empty the proof field in `you/01-product.md` and have the page rebuilt. If the proof section disappears instead of an invented review appearing, it passed.
- **Missing link:** delete the payment link and rebuild. If a visible warning button appears instead of a silent `#`, it passed.
- **Phone:** open the file on your phone. If nothing overflows and the button fits the screen, it passed.
- **Dark mode:** toggle your phone's dark mode. If the text is readable in both modes, it passed.
- **"What it is NOT":** search the page for the things you wrote in the do not offer list. If none of them are implied, it passed.

## Honest limit

- The system builds the page, it does not guarantee sales. Whether a page really sells only shows up once traffic arrives.
- You open the payment provider account once yourself, the system does not open it.
- The page is static. No stock tracking, no member login, no coupons, no automatic delivery. Those are the provider's job.
- Tax, invoicing and distance selling obligations are your responsibility, and they differ by region. The system puts the seller, price, refund and contact lines on the page; it does not give legal advice.

## Example output

`EXAMPLE-OUTPUT.md` has a full run the system produced for a fictional business (`you/EXAMPLE-01-product.md`, a beginner pottery course at a small studio): the sales copy section by section and the filled launch checklist. The page that came out of the same run sits in `outputs/beginner-pottery-course-sales-page.html`, and you can open it on a double click. The proof field in the example was deliberately left empty, so there is no proof section on the page; that is the anti invention rule at work.

## Who it is for

Anyone with something to sell and no page for it: workshop and course runners, freelancers, service providers, small studios, indie makers, anyone selling a digital product. You do not need to code and you do not need a designer.

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI. If you get stuck setting it up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.net/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
