# Run

Three steps. Five minutes total.

## 1. Drop in a screenshot

Take a screenshot of the page and put it in the `screens/` folder.

For a full page capture, open the browser devtools with `F12`, then press `Ctrl + Shift + P`, type "Capture full size screenshot" and run it. On Mac, `Cmd + Option + I` then `Cmd + Shift + P`, same command.

Name the file after what it is: `home-desktop.png`. Add a mobile capture too and the audit does twice the work.

Details: `screens/HOW-TO-ADD.md`.

## 2. Fill in the brand file (optional)

Write your brand colors and typefaces into `you/01-brand.md` so the system does not suggest changing them.

Leave it empty and it still runs. The system then treats color and typeface changes as fair game.

## 3. Open Claude Code in this folder and type

```text
audit
```

The system reads the images in `screens/`, measures eight headings, and writes the report into `outputs/`.

---

## What you do next

Open the report and copy the **Section D · Fix instruction** block at the bottom, as is.

Paste that block into whatever built the page:

| Where you built the page | Where you paste it |
|---|---|
| Claude Code, Codex, Cursor | straight into the chat |
| Lovable, v0, Bolt | into the project chat |
| Framer, Webflow, Canva | into their own AI assistant, or apply it by hand |
| Hand written code | work through the items in order |

The block stands on its own. You do not need to paste the rest of the report; the reasoning stays with you.

---

## Questions people ask

**Do I not have to give you my code?**
No. The only input is a screenshot. It makes no difference what you built the page with.

**My page is not live, I only have a design file.**
Screenshot the design. It works the same way. Figma, Canva, anything.

**Does the system redesign my page?**
No. It measures what is wrong and writes how to fix it. It will not suggest changing your copy, your section order or your concept.

**My brand color failed the contrast test. Do I have to change my brand color?**
No. If you wrote the color into `you/01-brand.md` the system leaves it alone. Instead it suggests changing the color of the text sitting on it, or where that color is used.

**Can I audit the same page twice?**
Yes. After applying the fixes, take a fresh screenshot and run it again. The system reads the old report and produces a "fixed / not fixed" table.

**How long does it take?**
A few minutes for a single page.
