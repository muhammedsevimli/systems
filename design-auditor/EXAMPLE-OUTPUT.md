# Audit · Shift Sheet home page · 2026-07-27

> Input: `screens/home-desktop.png` (1280 wide, full page) + `screens/home-mobile.png` (390 wide).
> No page address supplied, the audit was done from the screenshot alone. Pixel values are approximate.
> Brand file empty, so color and typeface suggestions are unrestricted.

---

## Section A · Inventory

| What | How many |
|---|---|
| Distinct type sizes | 11 (approximately 12px to 22px) |
| Distinct type weights | 2 (normal, bold) |
| Distinct typefaces | 2, mixed inconsistently (a serif and a sans) |
| Distinct colors (neutrals excluded) | 3 saturated (violet, pink, cyan) |
| Buttons | 4 filled and primary looking, 0 secondary |
| Sections | 6 (nav, hero, features, story, pricing, footer) |
| Icons | 4, all emoji |
| Images | 0 real images, 1 placeholder box |

Images audited: desktop full page, mobile full page. No address supplied, so no browser verification.

---

## Section B · Eight heading measurement table

| # | Heading | What it is now | What it should be | Severity |
|---|---|---|---|---|
| 1 | Type hierarchy | 11 distinct sizes. The h1 is 22px and the subhead under it is 20px, a ratio of 1.1. Two typefaces mixed with no rule | 3-5 sizes, at least 1.5x heading to body, one typeface per role | HIGH |
| 2 | Line length and line height | Hero subhead approximately 116 characters per line, story paragraph approximately 125. Body line height 1.25 | 45-75 characters, body line height 1.5-1.7 | HIGH |
| 3 | Spacing rhythm | Measured gaps of 6, 9, 11, 14, 18, 22, 26, 34. No common factor | All multiples of a 4 or 8 base | MEDIUM |
| 4 | Color and contrast | Body text pure black. Subhead, card copy and pricing bullets all `#B3B3B3`, contrast approximately 2.1:1. Three saturated colors side by side | At least 4.5:1. No pure black. One accent color | HIGH |
| 5 | Shadow, border, corner radius | 3 distinct shadows, all dark and broad. 2px borders and shadows together on every card. 6 distinct corner radii (2, 6, 9, 11, 14, 18) | At most 2 shadows, border or shadow, one radius | HIGH |
| 6 | Buttons and tap targets | Three filled buttons side by side in the hero, each a different color AND a different radius (2px, 11px, 18px). Button height approximately 30px. Padding equal on both axes | One primary button. At least 44px. Horizontal padding roughly 2x vertical | HIGH |
| 7 | Alignment and grid | Content runs edge to edge on a 1280px screen, no container cap. The "Why Shift Sheet" heading is centered while its paragraph is left aligned. The "Pricing" heading is indented 22px from the cards beneath it. Cards and pricing boxes are unequal heights | One left edge, capped container, long text not centered, equal heights | HIGH |
| 8 | Image and icon consistency | All four icons are emoji. A dashed placeholder box reading "[product screenshot here]". The story paragraph ends with "Sample text goes here." | An icon set, no placeholder residue | HIGH |

---

## Section C · Findings, ranked by severity

### C1 · [HIGH] Two pieces of placeholder residue are still on the page
- **Now:** A dashed box roughly 1212x150 pixels in the hero reading "[product screenshot here]". The story paragraph closes with "Sample text goes here."
- **Should be:** Zero placeholder residue (measure 8).
- **Why:** The visitor sees an unfinished page and assumes the product is unfinished too. This is the single most expensive mistake here; the other seven headings could be perfect and the page would still read as amateur.

### C2 · [HIGH] The heading and the subhead are almost the same size
- **Now:** The h1 is approximately 22px, the subhead directly beneath it approximately 20px. A ratio of 1.1. There are 11 distinct sizes on the page, several separated by a single pixel.
- **Should be:** At least 1.5x between heading and body, 3 to 5 distinct sizes total (measure 1).
- **Why:** The largest thing on the page does not read as the largest thing. With no hierarchy the eye has no entry point and the page flattens into a wall of text. The subhead is also visually competing with the headline it is supposed to support.

### C3 · [HIGH] Two typefaces are mixed with no rule
- **Now:** Headings and buttons use a sans, body copy and pricing use a serif, and the split does not follow a role. The hero headline is sans, the subhead directly under it is serif.
- **Should be:** One typeface per role, applied consistently (measure 1).
- **Why:** A serif and a sans can pair well, but only when the split maps to a rule (all headings one, all body the other). Here the switch happens mid block, so it reads as two half finished pages stitched together rather than a pairing.

### C4 · [HIGH] Secondary text is too light to read
- **Now:** The hero subhead, card copy, pricing bullets and footer are all `#B3B3B3`, giving approximately **2.1:1** contrast on white.
- **Should be:** At least 4.5:1 (measure 4, WCAG AA).
- **Why:** None of this survives a phone screen in daylight. The sentences carrying the most information are the least readable ones on the page, and the hero subhead is where the whole value proposition lives.

### C5 · [HIGH] Three filled buttons side by side, each styled differently
- **Now:** "Start free" (violet, 2px radius), "Book a demo" (pink, 11px radius), "See pricing" (cyan, 18px radius). All three filled, all three the same visual weight, three different corner treatments.
- **Should be:** One primary button, the rest outlined or plain text, one radius (measures 5 and 6).
- **Why:** The reader cannot tell which is the main action, so they take none. The three different radii on three buttons doing adjacent jobs also give away that each was styled by hand.

### C6 · [HIGH] Buttons are far below the tap target floor
- **Now:** Hero buttons approximately 31px tall, pricing buttons approximately 30px. Padding is equal horizontally and vertically.
- **Should be:** At least 44px tall, horizontal padding roughly 2x vertical (measure 6).
- **Why:** A 31px button gets missed on a phone. This is a scheduling tool for staff on their phones, so the mobile miss rate is the whole product.

### C7 · [HIGH] Every card carries a 2px border and a heavy shadow at once
- **Now:** Feature cards and pricing boxes have a `2px` border together with `0 9px 22px rgba(0,0,0,0.32)`. Three distinct shadow definitions on the page, all dark.
- **Should be:** Border or shadow, not both. At most 2 shadow levels, low opacity (measure 5).
- **Why:** Both are ways of saying "this box is a separate surface". Saying both thickens the box. The thick border plus dark shadow is what makes these cards read as a template.

### C8 · [HIGH] Content runs edge to edge and alignment is inconsistent
- **Now:** No container cap on a 1280px screen. The "Why Shift Sheet" heading is centered while its paragraph is left aligned and full width. The "Pricing" heading sits 22px in from the cards below it.
- **Should be:** A capped container, a single left edge, long text left aligned (measure 7).
- **Why:** A centered heading over a left aligned paragraph splits the block into two unrelated things. The 22px indent on "Pricing" is small enough that nobody names it and large enough that everybody feels it.

### C9 · [MEDIUM] Lines are too long and set too tight
- **Now:** Hero subhead approximately 116 characters per line, story paragraph approximately 125. Body line height 1.25.
- **Should be:** 45-75 characters, line height 1.5-1.7 (measure 2).
- **Why:** The eye loses its place travelling back to the start of the next line, and the tight leading makes it worse. The text does not become unreadable, it becomes unwanted.

### C10 · [MEDIUM] Spacing does not sit on a scale
- **Now:** Measured gaps of 6, 9, 11, 14, 18, 22, 26, 34 pixels. No common factor.
- **Should be:** All multiples of a 4 or 8 base: 8, 16, 24, 32, 48, 64 (measure 3).
- **Why:** Not noticed item by item, but in aggregate it reads as random. This is the cheapest fix on the list.

### C11 · [MEDIUM] Boxes on the same row are unequal heights
- **Now:** The three feature cards and the three pricing boxes each end at a different height because their content differs in length. The "Team" plan runs noticeably longer than the other two.
- **Should be:** Equal heights on a row, button pinned to the bottom (measure 7).
- **Why:** Stepped card bottoms are uncomfortable to scan, and in a pricing table they actively get in the way of comparing plans, which is the only job that table has.

### C12 · [MEDIUM] Every icon is an emoji
- **Now:** All four icons, the logo included, are emoji (calendar, arrows, stopwatch).
- **Should be:** One icon set, consistent stroke weight (measure 8).
- **Why:** Emoji render differently on every operating system, so you do not control what people see. They are also always filled and colored, which clashes with the light text beside them.

### C13 · [LOW] Body text is pure black
- **Now:** Headings and body are `#000000`.
- **Should be:** A near black (measure 4).
- **Why:** Pure black creates a hard edge against white. On its own nobody complains, but it feeds the cheap look in aggregate.

---

## Section D · Fix instruction (pasteable)

```text
Apply the following design fixes to this page. Work through the items in order, one at a time.
Do NOT change the page copy, the section order or the content. Touch visual execution only.
Brand colors and typefaces are fixed, leave them alone.

1. [HIGH] Clear the placeholder residue.
   Now: a dashed box in the hero reading "[product screenshot here]", and the story paragraph ends with "Sample text goes here."
   Do: replace the dashed box with a real product image; if you do not have one, remove the box entirely. Delete the "Sample text goes here." sentence.

2. [HIGH] Cut the type scale to five steps and fix the hierarchy.
   Now: 11 distinct sizes, and the h1 is only 1.1x the subhead beneath it.
   Do: use only these five sizes: 14 (small), 16 (body), 20 (subheading), 28 (section heading), 44 (page heading). Round every piece of text to one of them. The hero h1 becomes 44 and the subhead becomes 16.

3. [HIGH] Apply one typeface per role.
   Now: a serif and a sans are mixed mid block; the hero headline is sans and the subhead under it is serif.
   Do: pick one family and use it everywhere, or split it strictly by role (all headings one family, all body the other). No switching inside a block.

4. [HIGH] Darken the light gray text.
   Now: hero subhead, card copy, pricing bullets and footer are all #B3B3B3 (2.1:1 contrast).
   Do: set the secondary text color to #52525B (roughly 7:1 on white). No text below 4.5:1.

5. [HIGH] Leave one primary button in the hero.
   Now: "Start free" (violet), "Book a demo" (pink), "See pricing" (cyan), all filled, three different radii.
   Do: keep only "Start free" filled. Make "Book a demo" outlined (transparent background, 1px border, accent text). Make "See pricing" a plain text link. Remove pink and cyan from the page.

6. [HIGH] Enlarge the buttons and balance the padding.
   Now: buttons are approximately 30px tall with equal padding on both axes.
   Do: give every button min-height: 44px and padding: 12px 24px.

7. [HIGH] Separate border from shadow and lighten the shadows.
   Now: cards and pricing boxes carry a 2px border together with 0 9px 22px rgba(0,0,0,0.32). Three distinct shadows on the page.
   Do: remove the borders from the cards. Use one shadow definition: 0 1px 3px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.06). Replace every shadow on the page with it.

8. [HIGH] Cap the container and fix the alignment.
   Now: content runs edge to edge on 1280px. The "Why Shift Sheet" heading is centered over a left aligned paragraph. The "Pricing" heading is indented 22px from the cards below it.
   Do: add a centered container at 1120px wide. Left align the "Why Shift Sheet" heading. Remove the 22px indent on "Pricing". Every section heading starts on the same left edge as its content.

9. [MEDIUM] Fix line width and line height.
   Now: 116 to 127 characters per line, body line height 1.25.
   Do: give every body paragraph max-width: 65ch. Set body line-height to 1.6 and headings to 1.2.

10. [MEDIUM] Put spacing on an 8 base.
    Now: 6, 9, 11, 14, 18, 22, 26, 34 pixels mixed.
    Do: round every gap to one of 8, 16, 24, 32, 48, 64, 96. Section gaps 96px, space under a section heading 24px, card padding 24px.

11. [MEDIUM] Equalise boxes on a row.
    Now: feature cards and pricing boxes end at different heights.
    Do: set align-items: stretch on the row containers, make the boxes flex columns, and pin the button to the bottom with margin-top: auto.

12. [MEDIUM] Replace the emoji icons.
    Now: calendar, arrows and stopwatch are all emoji.
    Do: use one outline icon set (Lucide for example), all at 24px and the same stroke weight. Remove the emoji from the logo too.

13. [LOW] Replace pure black.
    Now: text color is #000000.
    Do: set the primary text color to #18181B.

When you are done, list every item you changed on one line each.
If you are unsure about an item, ask before applying it.
```

---

## Section E · What cannot be measured from this image

- What happens to the buttons on hover and on click
- Whether a focus ring shows during keyboard navigation
- How long the page takes to load
- Animation and transitions
- Dark theme
- Tablet width (only 1280 and 390 images were supplied)

If you want the focus ring audited too, add a screenshot taken while the tab key is held.

---

## Section F · Comparison with the previous audit

First audit of this page. No previous report to compare against.
