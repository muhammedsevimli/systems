# Pricing Solver · Pricing Built on Competitor Data 🧮

Write your product and your competitors into a file, and the system opens the competitors' public pricing pages on its own, pulls out their tiers and figures with the sources, lays out which feature is given at which level, works out what the sector charges by, and hands you a justified three tier structure. For a competitor who hides their price it invents no figure. You paste no prices. A no-code pricing system that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

The system does the research, you make the decision.

## What it does

The product or the service is ready and you set the price by staring at the ceiling. Price it low and the work looks worthless while you exhaust yourself; price it high and nobody comes back. You do not really know what your competitor charges, and even if you did, you would not know how to build your own tiers.

This system really reads the competitors' pricing pages, pulls out the tiers with their sources, builds a feature by tier matrix, picks the value axis with a reason, proposes three tiers, and writes the evidence under every figure. It gives you no orders and promises you no revenue. It works in two phases:

1. **Price pulling.** You write your competitors' names into `you/02-competitors.md`. With Claude Code's web tools (WebFetch + WebSearch) the system opens the pricing pages itself; tier name, figure, currency, billing period, what the price scales by and the included features land in `data/` with the source URL. If the URL is wrong it searches for the right one. If the price is not on the page it writes `price not public` and invents no figure.
2. **Analysis.** From the pulled data come the feature by tier matrix, the value axis choice, a three tier proposal (each with what was deliberately left out), the local market adaptation options and the price change protocol. The output is written into `outputs/`.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal knowledge required.
- A folder and 15 minutes. The three things that matter most: **your cost**, **who you sell to**, **what you do not do**.
- An internet connection. Every page the system reads is a public pricing page, no account or key needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/pricing-solver.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/pricing-solver pricing-solver
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set this pricing solver up for my business". It fills the product and competitor files in with you.

These are the files the system reads. Fill in the product and competitor part with your own:

- `you/01-product.md`: what you sell, to whom, **your cost**, your capacity, **your region and the currency you sell in**, what you do not do
- `you/02-competitors.md`: the competitor list + local references + the price log
- `format/rules.md`: the data quality labels, the value axis ruler, the tier building rules (comes ready)
- `format/output-format.md`: the structure of the report (comes ready)
- `data/`: the system writes the real prices it pulls here itself; you put nothing in this folder

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First pull the prices:

> pull my competitors' prices

Then get the report:

> turn the pulled data into my pricing report

For the full commands, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Sources:** does every figure in `data/` carry a source URL. If it does, it passed.
- **The hidden price:** put a competitor who does not publish prices into the list. If the row comes back `price not public` and stays out of every average, instead of a guessed figure, it passed.
- **Currency:** put competitors from two different currencies in. If it kept the currencies separate and compared through structure instead of inventing a rate, it passed.
- **Deliberately left out:** does every tier carry a "deliberately missing from this tier" list with a one line reason each. If it does, it passed.
- **Marginal cost:** if you sell something with a per use cost (messages, transactions, storage), check whether any tier says "unlimited". If none does, it passed.
- **Demand:** search the report for "you will sell", "conversion", "your revenue". If none of them appear, it passed.

## Honest limit

- **The system does not measure demand.** It reads the competitors' structure and your cost. It does not know and does not guess how many people will pay how much. Revenue projections, conversion rates and "set this price and you will sell this much" are banned in this system.
- **It produces no figure for a competitor who hides their price.** That row stays `price not public` and enters no average. If the page cannot be reached it writes `no source`.
- **It invents no exchange rate.** It does not convert currencies into each other. A price proposal in your currency only comes out if the pulled sources publish in that currency, or if you add local sources that do.
- **The pages are date stamped.** A competitor may have changed their price. Run it again once a month; the old files stay, so you also see the competitors' price change history.
- **It gives no legal advice.** On subscriptions, automatic renewal, cancellation rights and tax it adds a "this clause needs legal confirmation" note, and those rules differ by region.
- The pricing decision is yours. The system gives you a justified structure; the proof comes in a real sales conversation.

## Example output

`EXAMPLE-OUTPUT.md` has the full report the system produced for a fictional operator (`you/EXAMPLE-01-product.md`, a solo operator selling an online booking page with reminders to small local businesses): the source status, the feature by tier matrix, the value axis choice, the three tiers with their evidence, the adaptation options and the price change protocol. The operator is fictional; the competitor prices are real, pulled live from public pricing pages on 26 July 2026 with the source links kept (`data/EXAMPLE-pulled-2026-07-26.md`). One competitor hides their price and one page could not be read, and both were left out of every calculation instead of being filled in.

## Who it is for

Anyone who has to put a number on something: solo operators, freelancers, agencies, small software and service businesses, anyone selling a subscription. You do not need to code, and you do not need a pricing consultant to read competitor pages for you.

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
