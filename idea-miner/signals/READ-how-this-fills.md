# The SYSTEM fills this folder (you paste nothing)

## How it fills up
When you run the PHASE 1 scan (`RUN.md` Step 1), the system scans the sources itself with Claude Code's web and shell tools (WebFetch + WebSearch + Bash curl) and writes the real demand sentences it finds here as `collected-YYYY-MM-DD.md`. You do not put anything in this folder by hand.

There is also an `rss/` subfolder: the raw Reddit RSS files the system downloads with curl, one `.rss` per query. Intermediate files, you do not look at them.

## The format the system writes for every signal

```text
## Signal N
Source: <hacker news / reddit / web-forum / marketplace review>
Link: <the link of the page or search that was pulled>
Who is saying it: <e.g. a small ecommerce operator, a salon owner> (if known)
Pain sentence: <the person's own sentence, verbatim, trimmed>
Money language: <explicit ("we pay $40 a month for this") / indirect (the customer who walked, lost revenue) / none>
In how many sources: <one place, or repeated across several>
Existing solution / competitor: <if a product name came up in the scan (for the competition-gap score)>
```

## Honest limit (the system holds to this)
- The system writes only a sentence it ACTUALLY pulled. If it cannot reach a source ("reddit is rate-limited in this environment"), it says so plainly and invents no sentence.
- Explicit money language is the most valuable signal. Indirect money (lost revenue, the customer who walked) counts too, but does not carry the weight of explicit money.
- The better the search queries you give (`you/02-sources.md`), the more accurate the scan.

## Example filled file
`EXAMPLE-signals-2026-07-24.md` in this folder is the output of a real scan the system ran in the local appointment businesses and small ecommerce field. The signals in it were really pulled from Hacker News on 24 July 2026 (`hn.algolia.com`, HTTP 200), quoted verbatim, with links. In your own scan, the signals of your own field land here.
