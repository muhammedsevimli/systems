# Report format

> Every audit report is written in this structure. Section order and headings are fixed.
> File name: `outputs/YYYY-MM-DD-<page-name>-audit.md`

---

## Section A · Inventory

Counted before measuring. Short table:

| What | How many |
|---|---|
| Distinct type sizes | |
| Distinct type weights | |
| Distinct typefaces | |
| Distinct colors (neutrals excluded) | |
| Buttons (primary / secondary) | |
| Sections | |
| Icons | |
| Images | |

One line underneath: which images were audited, was a page address supplied (and if so, was it verified in a browser).

---

## Section B · Eight heading measurement table

All eight headings get a row. A heading with no problem gets "clean", never skip a row.

| # | Heading | What it is now | What it should be | Severity |
|---|---|---|---|---|
| 1 | Type hierarchy | | | |
| 2 | Line length and line height | | | |
| 3 | Spacing rhythm | | | |
| 4 | Color and contrast | | | |
| 5 | Shadow, border, corner radius | | | |
| 6 | Buttons and tap targets | | | |
| 7 | Alignment and grid | | | |
| 8 | Image and icon consistency | | | |

---

## Section C · Findings, ranked by severity

Three lines per finding. A finding without a reason is not written.

### C1 · [HIGH] Finding title
- **Now:** the measured value or observed state. If the measurement is an estimate, say "approximately".
- **Should be:** the accepted range and which heading in `format/measures.md` it comes from.
- **Why:** what this gap does to the reader. One sentence, no trend reasoning.

(Findings are ordered HIGH, then MEDIUM, then LOW. Numbering continues C1, C2, C3.)

---

## Section D · Fix instruction (pasteable)

> This section is the load bearing part of the report. It is written inside a single code block; no explanatory sentence goes INSIDE the block.
> The reader copies this block as is and pastes it into whatever built the page: Claude Code, Codex, Lovable, v0, Framer, Cursor, it does not matter.

The block follows this skeleton:

```text
Apply the following design fixes to this page. Work through the items in order, one at a time.
Do NOT change the page copy, the section order or the content. Touch visual execution only.
Brand colors and typefaces are fixed, leave them alone.

1. [HIGH] <what to do, with the measurement>
   Now: <measured>
   Do: <concrete value or rule>

2. [HIGH] <...>
   Now: <...>
   Do: <...>

3. [MEDIUM] <...>
   ...

When you are done, list every item you changed on one line each.
If you are unsure about an item, ask before applying it.
```

Rules:
- Each item touches **one thing**. Not "fix the typography" but "give the body container `max-width: 65ch`".
- Every item carries a severity tag, ordering starts at HIGH.
- Concrete values only. "Add more spacing" is banned, "set the section gap to 96px" is right.
- The brand protection line always stays in the block.
- No measurement reasoning goes inside the block, the reasoning stays in Section C. The block must be short and applicable.

---

## Section E · What cannot be measured from this image

A screenshot does not show everything. The audit does not invent these, it lists them:

- What happens on hover and on click
- Whether a focus ring exists (keyboard navigation)
- How long the page takes to load
- Animation and transitions
- Dark theme
- Behaviour at screen sizes that were not supplied (mobile, when only a desktop image was given)

Write which of these could not be audited and, where useful, add a one line note: "add a screenshot of X and I will look at it".

---

## Section F · Comparison with the previous audit

Only written when the same page has been audited before. The old report in `outputs/` is read first.

| Previous finding | State |
|---|---|
| | fixed / not fixed / partly |

If a mistake repeats, add it with a date to the "my repeating mistakes" section at the bottom of `you/01-brand.md`.
