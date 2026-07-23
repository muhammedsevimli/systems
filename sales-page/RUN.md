# RUN · One Command

> Write your product into `you/01-product.md` and paste your form endpoint and payment link into `you/02-links.md`. Then open Claude Code in this folder and copy the command below.
> Thanks to `CLAUDE.md`, Claude Code will already read the product, links, format and template files.

## One command (copy)

```
build my sales page.

rules:
- first say in one line that you read you/01-product.md, you/02-links.md and format/page-format.md.
- write the sales copy in the order of format/page-format.md: title, subtitle, who it is for, pain, solution, what is included, proof, faq, price, refund, contact, cta. write the copy into outputs/<slug>-copy.md.
- using the format/template.html skeleton, produce a working single file html sales page and write it as outputs/<slug>-sales-page.html. do not pull external css, external fonts or external scripts, keep it one file.
- put the form endpoint from you/02-links.md into the form action and the payment link into the button href. if one is missing leave a visible warning in its place, do not quietly put a #.
- do not invent a field i left empty in the product file. if there is no proof, do not put the proof section on the page at all, and write no invented review and no invented percentage.
- do not use guarantees, certain results, fake urgency or motivational language. do not use em dash.
- do not imply anything from my "what it is not" list on the page.
- fill the format/launch-checklist.md list in for the product and write it to outputs/<slug>-launch-checklist.md.
- at the end, tell me in a single list which fields were empty and what i need to add.
```

## If you only want to update the copy

```
rewrite the sales copy, we will produce the html afterwards. make the title more concrete, it should say what i am selling in the first sentence.
```

## If you only want to update the links

```
i updated you/02-links.md. change the form action and the payment link in the html page in outputs to the new values, do not touch anything else.
```

## What you do next

1. Double click `outputs/<slug>-sales-page.html`. The page opens in your browser.
2. Fix any sentence you do not like inside `outputs/<slug>-copy.md` and say "i updated the copy, rebuild the html".
3. Test the items in `outputs/<slug>-launch-checklist.md` one by one.
4. Drag the file onto a free static host (Netlify Drop, Cloudflare Pages, GitHub Pages). You get an address.
5. Write that address into the publish log at the bottom of `you/02-links.md`.

## Note

The system sets up no payment provider, opens no account, and asks you for no password or API key. You get the ready made payment link once yourself and the system wires it into the page. Collection, fees, refunds and invoicing run in your own provider account.
