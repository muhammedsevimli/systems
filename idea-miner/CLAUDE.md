# Idea Miner · SaaS Idea Scorer · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You do nothing. Claude Code loads it on its own while working in this folder.
> The goal: stop thinking "what should I build" from scratch every time. You write the field you care about; the system scans demand on its own, collects the real complaints that carry money language, scores them against four criteria, and returns a "best 5 SaaS ideas you could build this week" report.

## Where this system stands (non-negotiable)
This system hands FINDING the idea to itself and leaves CHOOSING the idea to you. It scans demand, collects signals, scores, and ranks; but it never gives the order "build this". What you build is your call. The system gives you a clean, ranked, justified queue. The decision is yours.

## What the system does (two phases)
1. **Automatic scan (you paste nothing):** it reads the field you care about in `you/01-profile.md` and the search queries in `you/02-sources.md`. Using Claude Code's WEB AND SHELL TOOLS (WebFetch + WebSearch + Bash curl) it scans the sources itself, pulls the REAL sentences where people say "I wish there was", "I am looking for a solution to this", "I would pay for this", "I do it by hand every month and I am sick of it", and saves each one with its source and link into `signals/collected-YYYY-MM-DD.md`. You paste nothing in this step.
2. **Scoring + report (AUTOMATIC):** it reads the collected demand signals in `signals/` one by one, turns each into a SaaS idea, scores it 1-5 on four criteria, filters it for fit through `you/01-profile.md`, and reports the 5 highest total scores with their reasoning.

## Which source is scanned how (honest table)
The system scans these sources ITSELF. Each source has a different degree of automation. No overstating.

| Source | How | Automation |
|---|---|---|
| Hacker News (comments) | `WebFetch` on the `hn.algolia.com` public JSON | **Fully automatic** (no auth, no key) |
| Reddit (posts + comments) | Bash `curl` on the public **RSS** search feed (`search.rss`) | **Fully automatic** (public, no key). Rate limits apply, retry. |
| General web + community forums (industry forums, "looking for X" searches, marketplace and app store reviews) | `WebSearch` | **Fully automatic** |
| X (Twitter) | wants a login, fetch tools are not reliable there | **Semi-automatic.** The system does not pull it; it builds a one-click search link for each X query in `you/02-sources.md` and you look by hand if you want. The main scan runs fine without X. |

> WHY RSS ON REDDIT, WHY NOT `.json`: Reddit closed its keyless `.json` endpoint, which now returns `403`. The public RSS search feed (`search.rss`) is still open and returns `200` without a key. That is why this system uses RSS on Reddit. Both were checked live before shipping.

> Rule: the system writes as a signal ONLY a sentence it ACTUALLY pulled, and puts a source and link on every one. If it cannot reach a source ("reddit is rate-limited in this environment"), it says so plainly and does NOT invent a sentence.

## PHASE 1 · When an automatic scan is requested
Read `you/01-profile.md` (the field you care about) and `you/02-sources.md` (search queries + demand-language patterns). Then, in order:

1. **Hacker News:** for each search query, `WebFetch` this address (turn spaces into `+`):
   `https://hn.algolia.com/api/v1/search?query=<QUERY>&tags=comment&hitsPerPage=30`
   From `comment_text` in the returned JSON, take the sentences carrying demand or money language VERBATIM and save them together with `story_title`. Use `https`, not `http` (plain http answers `301`).
2. **Reddit (RSS · Bash curl):** for each query pull the public RSS search feed with `curl`, giving a descriptive User-Agent. Two shapes:

   ```bash
   # across all of reddit
   curl -s --retry 5 --retry-delay 8 --retry-all-errors \
     -A "idea-miner/1.0 by <your-reddit-or-brand-name>" \
     -o "signals/rss/<QUERY-SLUG>.rss" \
     "https://www.reddit.com/search.rss?q=<QUERY>&sort=relevance&t=year"

   # inside one target subreddit
   curl -s --retry 5 --retry-delay 8 --retry-all-errors \
     -A "idea-miner/1.0 by <your-reddit-or-brand-name>" \
     -o "signals/rss/<SUB>-<QUERY-SLUG>.rss" \
     "https://www.reddit.com/r/<SUB>/search.rss?q=<QUERY>&restrict_sr=1&sort=relevance&t=year"
   ```

   The returned file is Atom XML. Each result is an `<entry>` block; take `<title>`, `<link href="...">` and the demand sentence in `<content>`. **Rate limit (429):** pulling back to back gets you `429`. That is why `--retry` and `--retry-delay` are in the template, and you pull queries one after another, not all at once. If it still fails, write "r/... rate-limited, retry" and move on. Do not invent.
3. **Web + forums:** run `WebSearch` for each query (industry forums, community sites, marketplace and app store reviews, "looking for a tool" searches). Take the real pain and demand sentences in the snippets, and the names of any existing solution or competitor you see (a competitor is valuable for the competition-gap score).
4. **X (semi-automatic):** for each X search in `you/02-sources.md` build the link `https://x.com/search?q=<QUERY>&f=live` (spaces as `%20`, non-ASCII characters URL-encoded). The system does not pull these; it adds them to the report as "look by hand if you want".

Write every signal you collect into `signals/collected-YYYY-MM-DD.md` in this format: source · link · who is saying it (if known) · the pain sentence (verbatim, trimmed) · money language (explicit / indirect loss / none) · in how many sources it repeats · existing solution or competitor. At the end, a one-line summary: how many signals came from which source, and which sources could not be reached.

## PHASE 2 · When scoring and the 5-idea report are requested, read these files IN ORDER (required)
1. `you/01-profile.md` · who you are, which fields you know, what you can build, what your limits are.
2. `you/02-sources.md` · which queries the scan used.
3. `format/criteria.md` · the four criteria and the 1-5 scoring rubric.
4. `format/output-format.md` · the structure you write the 5-idea report in.
5. all files in the `signals/` folder · the collected demand signals to be scored.

Do not produce anything without reading these. When you start, first say "profile + sources + criteria + format + collected signals read".

## Scoring steps (what the system does inside)
1. **Signal to idea:** read every signal in `signals/`. Pull out the real pain underneath it and turn it into a one-sentence SaaS idea ("what, for whom, solving which pain"). MERGE several signals that describe the same pain into ONE idea (a repeating pain is a strong signal).
2. **Read the signal strength:** how many independent signals and sources back an idea. Once, in one source = weak. Repeated by different people in different sources = strong. Explicit money language ("I would pay for this", "we pay $X a month for this") is the strongest; indirect money (lost revenue, the customer who walked) counts too, but not as much as explicit money.
3. **Score the four criteria:** score every idea 1-5 against the `format/criteria.md` rubric: (1) market size, (2) feasibility for you, (3) competition gap, (4) market fit for your region. Write a one-line reason next to every score. Total it out of 20. If the scan surfaced a competitor or existing solution, name it on the competition-gap line.
4. **Filter through the profile:** read `you/01-profile.md`. Ideas in a field the user does not know, or that hit a limit they set ("I will not do this"), are either eliminated or dropped to the bottom with a note "this is outside your field, want to find a partner". The feasibility score is read against the user's own ability to build.
5. **Rank and give the top 5:** sort by total score, write the top 5 ideas in the `format/output-format.md` structure. Mark the top idea with "start here this week".

## Non-negotiable output rules
- **Do NOT invent ideas.** Score only ideas grounded in demand ACTUALLY collected in `signals/`. If there is no signal at all, say "I have no signals, run the PHASE 1 scan first", do not invent an empty report.
- **Do NOT invent signals.** If you could not actually pull a sentence from a source, do not write that signal. Mark an unreachable source as "could not be reached". Source and link are required on every signal.
- **Do NOT inflate scores.** If the signal is weak, the market-size score is low. A one-line reason is required under every score; do not write a score without a reason.
- **Do NOT say "copy it".** If an idea resembles an existing product, do not propose a clone of that product; on the competition-gap criterion write "the existing solution is X, the gap is here" as the POINT OF DIFFERENCE. The output is always "a different angle you could build", never "the same thing as that".
- **Flag the risky field.** For ideas that need a license or regulation (banking, health, legal, personal data), lower the feasibility score and add the note "this field needs permits and compliance". Do not quietly hand out a high score.
- **Region is a variable, not a constant.** Criterion 4 is scored against the region and market the user wrote in `you/01-profile.md` (country, language, payment reality). Do not score it against your own assumed market.
- **Em dash appears NOWHERE in the output:** not in the idea sentence, not in the reason, not in a heading. If you need a separator, use a period, comma, colon, or middle dot (·).
- **No motivational language, no income promises, no hype.** Sentences like "you will get rich", "this will blow up", "do not miss out" are banned. The system speaks like a cool-headed analyst.

## Where the output goes
Write each scoring run as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-idea-report.md`.
Inside the file: (a) the scan summary (how many signals from which source, how many separate ideas they came down to), (b) the full score table (all ideas, four criteria + total), (c) the top 5 idea detail cards, (d) the "start here this week" pick and why, (e) the eliminated and waiting ones, one line each.

## The source list grows, the decision log builds up (persistent memory)
When you notice a new good search query or source, add it to `you/02-sources.md`. When you actually decide to build an idea, or look at one and drop it, write it with the date under the "decision log" section at the bottom of `you/02-sources.md` (which idea, what you decided, why). The system rescans the same queries every week; the query list and the decision log become the persistent memory of your market instinct, and later reports feed from there too.
