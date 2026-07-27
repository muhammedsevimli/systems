# Design Auditor

A system that tells you why the page you built looks cheap. You give it a screenshot; it measures eight headings one by one, writes the reason each one looks amateur with the number behind it, and turns the fix into a single instruction block you can paste anywhere.

**You do not give it code.** You may have built the page with Claude Code, Lovable, Framer or Canva. A screenshot exists in all of them.

## What it does

You build a page with AI. It works, the content is right. But something does not hold when you look at it. You cannot name what is wrong, you can only see that it looks cheap. You are not a designer, so you do not even know what to ask. So you never show anyone what you built.

The system measures eight headings:

1. Type hierarchy
2. Line length and line height
3. Spacing rhythm
4. Color and contrast
5. Shadow, border and corner radius
6. Buttons and tap targets
7. Alignment and grid
8. Image and icon consistency

Every finding gets three lines: **what it is now** (the measured value), **what it should be** (the accepted range), **why** (what that gap does to the reader). At the end you get one fix instruction block, every item written with a concrete value.

**What the system does not do:** it does not redesign your page. It will not suggest changing your copy, your section order or your concept. It will not change your brand color or typeface. It does not audit what a screenshot cannot show, and it does not invent it either; those go in a separate "cannot be measured" section.

## Install

```bash
npx degit muhammedsevimli/systems/design-auditor design-auditor
```

Or hit the green **Code → Download ZIP** and take the `design-auditor` folder.

If you would rather not touch the command line, open Claude Code (or Codex), give it this address and say "set this up for me".

```text
github.com/muhammedsevimli/systems/tree/main/design-auditor
```

## Run

Three steps:

1. Take a screenshot of the page and drop it into `screens/`. One PNG is enough. How to capture a full page: `screens/HOW-TO-ADD.md`.
2. Optionally write your brand colors and typefaces into `you/01-brand.md`. It runs fine empty.
3. Open Claude Code in this folder and type `audit`.

The report lands in `outputs/`. Details in `RUN.md`.

Copy the **Section D · Fix instruction** block at the end of the report and paste it into whatever built the page.

## Does it really work

Yes, with receipts.

A deliberately badly built landing page was prepared and the system was given the screenshot only. No code file, no address.

**How accurate were the estimates from the image:** after the audit finished, the page's real values were pulled from the browser and compared. The counts came out exactly right (eleven distinct type sizes, six distinct corner radii, three distinct shadows, the 1.1x heading to subhead ratio, 2.1:1 contrast on the secondary text). The pixel estimates landed close but not exact: line length was read as 116 and 125 characters against a real 116 and 127, button height as 30px against a real 31px. That is why the system labels pixel values "approximately" instead of presenting them as measured.

**What happened after the fix instruction was applied:**

| Measure | Before | After |
|---|---|---|
| Distinct type sizes | 11 | 5 |
| Distinct corner radii | 6 | 2 |
| Distinct shadows | 3 | 1 |
| Body line width | 1212px | 638px |
| Heading to subhead ratio | 1.1x | 2.75x |
| Secondary text contrast | 2.1:1 | 7.7:1 |
| Button height | 31px | 52px |
| Placeholder residue | 2 | 0 |

Before and after frames: `proof/01-before-desktop.png`, `proof/02-after-desktop.png`. Raw measurements: `proof/measurements-before.json`, `proof/measurements-after.json`. The full audit report it produced: `EXAMPLE-OUTPUT.md`.

The test page is fictional. It is not a real product.

## Folder layout

```text
design-auditor/
  CLAUDE.md                    Claude Code reads this automatically
  AGENTS.md                    Codex, Windsurf, Kilo and 20+ tools read this
  .cursor/rules/               Cursor reads this
  RUN.md                       the three step guide
  format/measures.md           eight headings, method, accepted ranges
  format/report-format.md      the report skeleton
  you/01-brand.md              brand and boundaries (optional)
  screens/                     you drop your screenshots here
  outputs/                     reports land here
  proof/                       test receipts: before and after frames
  EXAMPLE-OUTPUT.md            a real audit report
```

## Where the numbers come from

Nothing here is arbitrary. The line length range (45-75 characters) comes from established readability practice, the contrast threshold (4.5:1) from WCAG 2.1 AA, the tap target floor (44px) from the shared minimum across mobile interface guidelines. The spacing scale (4/8 base) and the shadow rules are common design system practice. Every one of them is written out with its reasoning in `format/measures.md`.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` |

It works in any tool that can read a screenshot.

---

**Muhammed Sevimli** builds these systems. Real sales and growth systems with AI. If you get stuck setting one up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- X: https://x.com/_msevimli
- Instagram: https://instagram.com/msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE)
