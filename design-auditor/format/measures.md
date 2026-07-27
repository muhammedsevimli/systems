# Measures · eight headings, method and accepted ranges

> This file is the system's ruler. Each heading has three parts: **how it is measured** from a screenshot, **the accepted range**, and **what happens to the reader** when it falls outside.
> The numbers are not arbitrary. They come from established typographic and accessibility practice. A source note closes each heading.

---

## 1. Type hierarchy

**How it is measured:** Group every piece of text on the page by size. Count how many distinct sizes there are. Work out the ratio between the largest heading and the body text. Count how many distinct weights are in use.

**Accepted range:**
- **3 to 5** distinct type sizes on a page. Six or more is noise, two or fewer is flat.
- At least **1.5x** size difference between heading and body. Below that the hierarchy does not separate visually.
- **At most 3** distinct weights.
- Two consecutive steps must be visibly different. 18px and 17px are not two hierarchy steps, they are an accident.

**Outside the range:** The reader cannot tell what to look at first. The page says "everything matters equally", which means "nothing matters". This is the most common cause of an amateur look.

**Source note:** Standard type scale practice (major third / fourth). The ratio is what counts, not the specific scale.

---

## 2. Line length and line height

**How it is measured:** Count the characters in the longest body line (spaces included, an approximate count is fine). Express line height as a multiple of the type size.

**Accepted range:**
- Body line length between **45 and 75 characters**. On mobile 35-50.
- Body line height **1.5 to 1.7** times the type size.
- Headings run tighter: **1.1 to 1.3**. Give a heading body line height and it falls apart.
- The gap between paragraphs must be **clearly larger** than the line height, otherwise the paragraph boundary disappears.

**Outside the range:** Past 75 characters the eye loses its place travelling from the end of one line to the start of the next, the reader rereads the same line and tires. Under 45 the eye jumps constantly. Neither makes the text unreadable, both make it unwanted. This is the most commonly missed measure on vibe coded pages, because by default text spreads to the full width of its container.

**Source note:** The classic readability range. `max-width: 65ch` is the one line fix.

---

## 3. Spacing rhythm

**How it is measured:** Measure the notable gaps (between sections, between a heading and the text under it, card padding, button padding). Check whether they share a common factor.

**Accepted range:**
- Every gap is a multiple of a single scale: a **4 or 8 pixel base**. So 12, 16, 24, 32, 48, 64. Values like 13, 19, 27 are off scale.
- **Proximity rule:** elements that belong together sit closer than the gap between separate groups. The space between a heading and its own paragraph must be tighter than the space between that paragraph and the next heading. Reverse it and the reader binds the heading to the wrong paragraph.
- Section gaps should be **at least 3x** the body type size, otherwise sections bleed into each other.

**Outside the range:** The page feels cramped, or randomly spaced. The reader spends energy working out what belongs to what. This is the cheapest heading to fix and the one that changes the most.

**Source note:** 4/8 base grid, common design system practice.

---

## 4. Color and contrast

**How it is measured:** Count the distinct colors (brand color, text color, backgrounds, borders, status colors). Estimate the contrast ratio between body text and its background. Check for pure black (`#000000`).

**Accepted range:**
- At least **4.5:1** contrast between body text and background. At least 3:1 for large headings.
- **At most 1 accent color** plus a neutral gray scale. A second saturated color is only allowed for status (error, warning, success).
- **Do not use pure black text.** A near black (a dark gray, for example toward `#18181B`) reads softer and looks more expensive.
- Secondary text must separate from primary text without dropping below 4.5:1. "Faint gray caption text" is the most common accessibility mistake there is.

**Outside the range:** Low contrast text is unreadable on a phone in daylight. Too many colors give away that a tool built the page rather than a designer. Pure black creates a hard edge on screen, one of the quiet causes of a cheap look.

**Source note:** WCAG 2.1 AA text contrast thresholds (4.5:1 normal, 3:1 large text).

---

## 5. Shadow, border and corner radius

**How it is measured:** Do cards, buttons and boxes carry shadows, how many distinct shadows are in use, are they soft or hard. Do a border and a shadow sit on the same element. How many distinct corner radii are there.

**Accepted range:**
- **At most 2 distinct shadow levels** (near surface, far surface). Three or more destroys the depth read.
- **A border and a shadow are never used together.** Both are ways of saying "this box is a separate surface"; say both and the box thickens and cheapens. Pick one.
- Shadows should be **soft and low opacity**, with light coming from above (vertical offset larger than horizontal). A shadow spreading equally in every direction reads as fake.
- One corner radius across the page (or two for nested elements). Making the button 4, the card 16 and the input 9 is noise.
- On nested elements the inner radius must be smaller than the outer, not the other way round.

**Outside the range:** Default shadows (whatever the tool ships with) are almost always too dark and too broad. Someone looking at it cannot name what is wrong, but the "template" feeling comes from exactly here.

---

## 6. Buttons and tap targets

**How it is measured:** Count every button and link. How many look primary (filled, accent colored). Measure button height and padding. Check whether buttons doing the same job look the same.

**Accepted range:**
- **One primary button per screen.** Secondary actions are outlined or plain text. Two filled buttons side by side leave the reader unable to tell which is the main action.
- Tap target **at least 44x44 pixels**. A small button gets missed on mobile.
- Horizontal button padding should be **roughly 2x** the vertical. Equal padding makes a button look stubby.
- Two buttons doing the same job on the same page must look **identical**. A button that is 40 in one place and 44 in another gives away that it was written by hand.
- Button copy should name the action. Instead of empty verbs like "Submit", "Click", "Continue", say what will happen.

**Outside the range:** More than one primary button directly lowers conversion. This heading is as much about outcome as appearance.

**Source note:** The 44px tap target, the shared floor of the mobile interface guidelines.

---

## 7. Alignment and grid

**How it is measured:** Count the distinct left edges on the page (are text, cards and headings aligned to the same line). Estimate the width of the container the content sits in. Check whether centered and left aligned text are mixed.

**Accepted range:**
- **A single left edge** across the page (or deliberately two: container and indent). Three or more is randomness.
- **Long body text is never centered.** Centering only works for short text (a heading, a one line subhead, a button). A centered paragraph longer than three lines does not get read.
- The content container must be **capped** on wide screens. Text running edge to edge says the page was never thought about.
- Cards on the same row must be **equal height**, even when their content differs in length.

**Outside the range:** Misalignment is not noticed item by item, but in aggregate it leaves a careless impression. This is the sneakiest heading.

---

## 8. Image and icon consistency

**How it is measured:** Count the icons. Do they come from the same drawing language (same stroke weight, same fill, same corner treatment). Are image aspect ratios consistent. Is there any placeholder residue.

**Accepted range:**
- Every icon from **a single set**. A mix of filled and outline icons is the fastest inconsistency to spot.
- Icon stroke weight should match the weight of the text beside it. A heavy icon next to light text reads as patched together.
- Images should be cropped to **the same aspect ratio**, not stretched.
- **No placeholder residue:** gray boxes, broken image icons, "image goes here" text, sample names, filler copy. If even one is present the finding is HIGH severity.
- Emoji are not used as icons.

**Outside the range:** Mixed icons and placeholder residue say the page is not finished. The visitor assumes the product is not finished either.

---

## Severity

| Level | Test |
|---|---|
| **HIGH** | Breaks the first three seconds, or makes text unreadable, or shows unfinished work. Contrast failures, placeholder residue, multiple primary buttons and missing hierarchy usually land here. |
| **MEDIUM** | Makes reading or navigating harder but the page still works. Line length, spacing scale drift and alignment noise usually land here. |
| **LOW** | Refinement only. Fixing it helps but nobody complains. Corner radius inconsistency and shadow tuning usually land here. |

If a page has no HIGH findings, say so plainly. Never invent a finding.
