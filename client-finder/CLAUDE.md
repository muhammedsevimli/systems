# Client Finder · Prospect Finding + First Message · Auto-Read Rule

> This file is read automatically at the START of every Claude Code session you open in this folder.
> You do nothing. Claude Code loads it on its own while working in this folder.
> The goal: never restate your service from scratch every time; write your niche once, then get a ranked prospect list + a first message tailored to each prospect with one command.

## What the system does (two phases)
1. **Link generation (automatic):** from the niche and country in `target/01-niche.md`, it builds Meta Ad Library (the public ad archive) search links. You click the link and see the brands running ads in that niche RIGHT NOW. If they are running ads, they have a budget.
2. **Breakdown + ranking + message (automatic):** you paste the brands and their ads you saw in the library into the `prospects/` folder. The system breaks down each prospect (what they sell, how long they have been running ads, the weak point of their ad), RANKS the prospects by fit with your service, then writes a TAILORED first message for each one.

> HONEST LIMIT: the Meta Ad Library is public, but there is no free automatic download (API) for commercial product ads; the ad text is visible in the browser. So the step of SEEING a brand in the library is a one-click manual "open and paste" step. The breakdown, ranking, and message generation are fully automatic. Details: bottom of `format/prospect-breakdown.md`.

## PHASE 1 · When a link is requested
Read `target/01-niche.md`. For each niche term, build the Meta Ad Library link with this template and write them one by one:

```text
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<NICHE>&search_type=keyword_unordered&media_type=all
```

- Put the niche term in place of `<NICHE>` (replace spaces with %20: "dental clinic" -> "dental%20clinic"). URL-encode non-ASCII characters.
- Use the country code from `target/01-niche.md` instead of `country=US` (TR, DE, NL...). If the file has no country, assume US and say so in one line.
- If `target/01-niche.md` has more than one search term, build a SEPARATE link for EACH of them. Try synonyms and the word the audience actually uses, one by one; one term means one list, and variety increases the number of prospects.
- After giving the links, tell the user in one line: "click the link, paste the brands and ad texts you see into `prospects/<niche>.md`, then run command 2."

## PHASE 2 · When a prospect list + messages are requested, read these files IN ORDER (required)
1. `brand/01-service.md` · what you sell, to whom, price range, what you are NOT.
2. `brand/02-voice.md` · how you write, how you address, banned words.
3. `target/01-niche.md` · which niche, which country you are prospecting in.
4. `format/prospect-breakdown.md` · the headings you split each prospect into + the ranking score.
5. `format/message-format.md` · the structure you write the first message in.
6. all files in the `prospects/` folder · the raw prospects to be broken down.

Do not produce anything without reading these. When you start, first say "service + voice + niche + format + raw prospects read".

## Breakdown steps (what the system does inside)
1. **Break down:** split each brand in `prospects/` into the headings in `format/prospect-breakdown.md` (what they sell, to whom, how long they have been running ads, how many different ads, format, weak point).
2. **Read the budget signal:** mark a brand that has been running ads for months as "has budget". A long-running ad is running because money is being spent on it. A brand that just started may be in the test phase, so its budget signal is weak.
3. **Find the weak point:** which of these four is missing in each ad: weak hook (the first sentence does not stop anyone), unclear offer (you cannot tell what you get), single format (all the same type of visual, no testing), no social proof (no testimonial, number, or review). Write the weak point BY SHOWING IT FROM THE AD, do not make generic remarks.
4. **Rank:** rank with the score in `format/prospect-breakdown.md`: budget signal + how solvable the weakness is with your service + fit with the price range in `brand/01-service.md`. The one at the top is the prospect most likely to reply.
5. **Write the message:** a TAILORED first message for each prospect in the structure of `format/message-format.md`. What you noticed (specific to that brand, from their ad), what you suggest, one clear question.

## Non-negotiable output rules
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite the message from scratch.
- Never contradict the "what I am NOT" lines in `brand/01-service.md`. Do not offer work you do not do.
- **The message must be tailored, not a copy-paste template.** Every message must contain a SPECIFIC detail from that brand's ad. If there is no detail, do not write the message: say "not enough information for this prospect, paste 1-2 more ads from the library".
- **One question rule:** there is exactly one clear question at the end of the message. No two questions, no three options, no "what do you think" pile.
- NO made-up numbers, fake promises, or non-existent references. If your number/work is not in `brand/01-service.md`, leave a `[put your own example/number here]` placeholder, never invent.
- Do not invent information about the prospect's name or industry. Rely only on what is written in `prospects/`. If you are not sure, do not write it.
- **This is not spam:** the message is short, tailored, one question, no sales pressure. Bulk-send language ("hello, I would like to introduce our services") is BANNED.
- Em dash (long dash) appears NOWHERE in the output: not in the message, not in a heading, not in a note line. If you need a separator, use a period, comma, colon, or middle dot (·).

## Where the output goes
Write each run as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-<niche>.md`.
Inside the file: (a) the prospect breakdown table, (b) the RANKED prospect list (score + why it is in that position), (c) a tailored first message for each prospect, (d) the platform note (DM/Instagram: direct and casual; LinkedIn/email: a more measured register).

## The prospect list grows (persistent memory)
When you notice a new niche or search term, add it to `target/01-niche.md`. When a message actually gets a reply, write it with the date under the "angles that got replies" section at the bottom of `target/01-niche.md` (which weak point, which sentence landed). Later runs feed from there too; the system gets closer to your work with every round.
