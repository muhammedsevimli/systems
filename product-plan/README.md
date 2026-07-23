# Product Plan · Build Plan From a URL 🧭

Give the address of a product you like, and the system browses that site on its own (home page, features, pricing, docs), takes the product's logic apart, and writes three files adapted to your business: the product plan, the data schema, and a Claude Code prompt set you paste in order. It also writes which feature does not belong in your first version, and why. A no-code product analyser that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

It is not a clone factory. You give one URL. You paste nothing.

## What it does

There is a tool you like and you say "I could build something like that". Then you stare at the screen. Which feature comes first, how you keep the data, what you write to Claude Code: none of it is clear. So you either never start or you stop halfway.

This system fills that gap. It works out what the product does and who it does it for, splits the features into core and decoration (which one the product cannot exist without), finds the user flow and the first value moment, infers what is kept in the background, and reads what the price scales by. Then it reorders all of that for your niche and turns it into a build order. It works in two phases:

1. **Automatic site reading.** You write a URL into `you/02-target.md`. With Claude Code's web tools (WebFetch + WebSearch) the system browses the home page, the features page, the pricing page and the documentation itself. It writes what is actually there, with the source link, into `breakdown/`. A page it cannot reach is marked "could not be reached"; it invents no content.
2. **Turning it into your plan.** It merges the breakdown with your profile and writes three files into `outputs/`: the product plan (buckets, adaptation table, v1 order), the data schema (tables and relations), the prompt set (pasted in order, each with an acceptance line).

Honest limit: only public pages are read. A page behind a login or a paywall is not read, and some sites are closed to automatic reading (bot protection, `403`). The system tries, and if it cannot open the page it says so.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal knowledge required.
- A folder and 15 minutes. You are not learning anything new, just writing who you serve, what you can build and what your limits are into a file.
- An internet connection. Every page the system reads is public, no account or key needed.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/product-plan.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/product-plan product-plan
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set this product plan up for my business". It fills in the profile and target files with you.

These are the files the system reads. Fill in the profile and target part with your own:

- `you/01-profile.md`: who you serve, **your region and how you collect payment**, what you can build, your limits, your unfair advantage
- `you/02-target.md`: the target URL, what you are curious about + the studied products log
- `format/rules.md`: the core / decoration test, the copy protection, the anti invention rules (comes ready)
- `format/plan-format.md`: the structure of the three outputs (comes ready)
- `format/product-breakdown.md`: the structure of the site reading output (comes ready)
- `breakdown/`: the system writes what it pulls off the site here itself; you put nothing in this folder

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then two commands. First read the product:

> read the product in you/02-target.md and pull out its logic

The system browses the pages itself and writes what is actually written there into `breakdown/`. Then get the plan:

> turn the breakdown into my product plan

The system writes three files into `outputs/`. For the full commands, see `RUN.md`.

## This is not a clone factory

The system never says "build the same thing". Brand, logo, design, page copy and licensed source code go into the do not copy list. The only thing that can be lifted is logic: which job it solves in which order, which data it keeps, how it walks the user to first value. The system reads your profile and builds two tables: what exists in the target but is pointless in your niche, and what is missing from the target but mandatory in your niche. The second table is the reason your product exists, and it is not left empty.

## Does it really work? Test it in 30 seconds

- **Sources:** does every feature line carry a source URL, or are there features you cannot find on the site. If every line has a link, it passed.
- **Pricing:** did it write only the figures literally on the page, or did it guess. If there was no pricing page and it wrote "no pricing figure available" instead of inventing, it passed.
- **Buckets:** is there a one sentence reason next to every feature, and is CORE 7 items or fewer. If yes, it passed.
- **Adaptation:** is the "missing from the target, mandatory in your niche" column filled, and does every row point back to a line in your profile. If it does, it passed.
- **Schema:** does the schema file open with the "this is an inference, not the real database" warning, and does every table carry its evidence. If it does, it passed.
- **Clone check:** search the output for "build the same thing", "clone", "one to one". If none of them appear and "what are you doing differently" is filled, it passed.

## The log grows · let the system grow with you

Every product you study adds one line to the "studied products log" at the bottom of `you/02-target.md`: which product, what you learned, which idea you took, what you did not take. From the second product on, the system reads the log too and shows the repeating patterns ("every product of this type has this") under a separate heading. Over time this log becomes the persistent record of your product instinct.

## Example output

`EXAMPLE-OUTPUT.md` has the full three file run the system produced for a fictional operator (`you/EXAMPLE-01-profile.md`, a small studio building simple sites for neighbourhood businesses): the product plan, the data schema and the prompt set. The operator is fictional; the target product is real and public, and every feature, price and license line was pulled live from its own pages on 24 July 2026 with the source links kept (`breakdown/EXAMPLE-breakdown-2026-07-24.md`).

## Honest limit

- The system reads public pages only. A page behind a login or a paywall is not read. Some sites are closed to automatic reading; the system tries, and writes down what it could not open.
- The system invents no feature and no price. If there is no figure on the pricing page it writes "no pricing figure available".
- The data schema is an inference, not the product's real database. The evidence sits next to every table.
- The plan gives you a build order, not a demand guarantee. Why a product worked is usually the thing that is not written on its site.

## Who it is for

Anyone who wants to build a product: solo builders, indie founders, operators, agency people, small teams. Anyone who has a tool they admire and wants a build order instead of a blank screen. You do not need to code; the system gives you the logic, the schema and the prompts, and the decision stays with you.

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
