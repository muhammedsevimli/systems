# The SYSTEM fills this folder (you copy nothing)

> You put nothing into `breakdown/` by hand. When you run Step 1 the system browses the target site itself and writes what it read in here.
> One file per run: `breakdown-YYYY-MM-DD.md`.

## What the system does
It takes the URL in `you/02-target.md` and tries these pages in order with Claude Code's web tools (WebFetch + WebSearch):

1. Home page · what the product does, for whom
2. Features page · `/features`, `/product`, `/platform`
3. Pricing page · `/pricing`, `/plans`
4. Documentation · `/docs`, `/help`, `/api`
5. License / terms of use (if there is one)

From every page it pulls what is actually written and writes it here with the source link.

## What the system writes for every piece of information
- The information (as written on the page, shortened)
- The source URL
- Which heading it belongs to (product definition, feature, flow, data clue, pricing, license)

## What happens to an unreachable page
If the system cannot fetch a page (404, wants a login, bot protection, timeout) it writes "could not be reached" into the scan details table with the reason. It DOES NOT INVENT the information it assumed would come from there. If the pricing page could not be reached there is no price figure in the output, it says "no pricing figure available".

## Honest limit
- Public pages only. A page that wants a login, sits behind a paywall or requires signing up is not read.
- Some sites are closed to automatic reading (bot protection, `403`). The system tries, and writes down what it could not open.
- Everything here is an OUTSIDE reading. The product's real database, real user count and real profit are not written on its site.
- The site's design, copy and images are not copied. Only what it does is read.
