# Trend Radar · Rising Content Angles in Your Niche · Auto-Read Rule (AGENTS.md)

> This file is the universal AGENTS.md open standard. Codex, Google Antigravity, Windsurf, Kilo and 20+ AI tools read it automatically while working in this folder.
> For Claude Code the same rule is in `CLAUDE.md`, for Cursor in `.cursor/rules/trend-radar.mdc`.
> The goal: end the weekly blank-screen problem. Write your niche once, then with one command pull the titles that rose the most in that niche's Reddit communities over the last week, extract the repeating hooks and angles, and get a "make this week" brief.

## What the system does (two phases)
1. **Reddit scan (AUTOMATIC, REAL):** it pulls the top rising titles of the last week for the subreddits in `target/01-niche.md` from Reddit's public RSS feed. This STEP IS REAL and fully automatic: Reddit's `top/.rss?t=week` feed is free, needs no account or key, and has no setup. You do not even click, no manual pasting.
2. **Angle extraction + brief (AUTOMATIC):** it reads the pulled titles (and, if you want, the YouTube/TikTok/Reels examples you paste by hand), extracts the repeating HOOK patterns, angles, formats, and topics. Output: a "make this week" brief. For each angle: which hook works, its proof (how many titles repeated it, where it sits in the feed, which community), how it maps to your niche, a sample title, and a format suggestion.

> WHY RSS, WHY NOT .json: Reddit closed its keyless `.json` endpoint, which now returns `403`. But the public RSS feed (`top/.rss?t=week`) is still open and returns `200` without a key. That is why the system uses RSS. RSS has no vote (upvote) COUNT; but the `/top/?t=week` feed is ALREADY sorted (the top one is the post that landed most that week), so ORDER is a signal. An optional OAuth path for advanced users who also want the vote count is at the bottom of this file.

## PHASE 1 · When a Reddit scan is requested (automatic pull · RSS + curl)
Read `target/01-niche.md`. For EACH subreddit there, build and pull this address:

```text
https://www.reddit.com/r/<SUBREDDIT>/top/.rss?t=week
```

- **Use `curl` to pull, with a descriptive User-Agent.** Web-fetch tools may be blocked on Reddit; curl with a descriptive UA returns `200`. Command template (saves to a file, does not flood the screen):

  ```bash
  curl -s --retry 5 --retry-delay 6 --retry-all-errors \
    -A "trend-radar/1.0 by <your-reddit-or-brand-name>" \
    -o "data/rss/<SUBREDDIT>.rss" \
    "https://www.reddit.com/r/<SUBREDDIT>/top/.rss?t=week"
  ```

- **Rate limit (429):** if you pull too fast back to back, Reddit may return `429`. So use `--retry` + `--retry-delay` (in the template above) and pull subreddits one after another, not all at once. On `429` the retry waits and tries again; if it still fails, write "r/... rate-limited, retry".
- The returned file is Atom XML. Each post is an `<entry>` block. From each `<entry>` TAKE: `<title>` (title = hook), `<link href="...">` (link), `<published>` (date). RSS has NO vote/comment count, do not invent one.
- **Order is a signal:** the `top/.rss?t=week` feed is sorted from the most-landed of the week downward for that subreddit. Keep a title's ORDER in the feed (1 = top = strongest). Do not reorder it, write it in the order it came.
- Write the result to `data/reddit-YYYY-MM-DD.md` in a table: subreddit · order · title · date · link. Keep the feed order within each subreddit.
- **NO inventing:** write only the titles you ACTUALLY pulled. If a subreddit comes back empty or hits a rate limit, write "r/... could not be pulled (reason)", do not invent a title. If no data comes at all, say "first add a working subreddit to target/01-niche.md" and stop.
- When the pull is done, say in one line: "reddit data pulled (X titles, Y subreddits, HTTP 200). now run the 2nd command."

## PHASE 2 · When a brief is requested, read these files IN ORDER (required)
1. `brand/01-brand.md` · who you are, what you make, what you are NOT, which platform.
2. `brand/02-voice.md` · how you write, how you address, banned words.
3. `target/01-niche.md` · niche, language/country, subreddits, search terms.
4. `format/trend-analysis.md` · how you extract hook patterns + the brief structure.
5. all files in the `data/` folder · the pulled Reddit data + (if any) hand-pasted YouTube/TikTok/Reels examples.

Do not produce anything without reading these. When you start, first say "brand + voice + niche + format + data read".

## Angle extraction steps (what the system does inside)
1. **Group:** cluster the titles in `data/` by topic/pattern. Put titles that repeat the same problem, format, or angle together. If at least 2 titles repeat, it is a pattern; a single title is not a pattern.
2. **Name the hook pattern:** for each cluster, name the repeating hook in one sentence (from the hook types in `format/trend-analysis.md`). Write the pattern SHOWING IT FROM THE DATA: which titles, how many, which subreddits. No generic talk.
3. **Read the heat (with the RSS signal):** RSS has no vote count, so read heat from two signals: (a) **frequency** = how many titles repeat the same hook (the more, the hotter), (b) **order** = are those titles near the top of the feed (top/.rss is sorted; the top one landed most that week). The cluster that both repeats most and sits at the top of the feed is the hottest angle. Do not invent numbers; count frequency and order from the `data/` file.
4. **Map to the niche:** turn each angle into your work via `brand/01-brand.md`. Say "this hook maps to this in your niche", concrete. Mark any angle that hits a "what you are NOT" line in `brand/01-brand.md` with ELIMINATE, "this is not your work, skip" (with the reason).
5. **Write sample titles:** for each landing angle, suggest 1-2 sample titles/hooks in the brand's VOICE (in the tone of `brand/02-voice.md`, without banned words). Add a format suggestion (reel, carousel, short video, long video).

## Non-negotiable output rules
- NEVER use the BANNED words in `brand/02-voice.md`. When you see a banned pattern, rewrite the title from scratch.
- Never contradict the "what you are NOT" lines in `brand/01-brand.md`. Do not suggest "make this" for a trend outside your niche; write what you saw but why you skipped it.
- **NO invented trends.** Draw conclusions only from titles that ACTUALLY exist in `data/`. Do NOT invent the vote/comment count that RSS does not give; read heat from frequency + feed order. If data is thin, say "data is thin, add this subreddit or paste an example", do not invent an angle.
- **Repeat threshold:** to call an angle a "trend" it must appear in at least 2 titles (or 1 Reddit + 1 pasted example). A single title goes to a separate section with a "maybe" note, not the main list of the brief.
- Reddit is English-heavy; titles may be in English. You extract the pattern and write a sample title in your niche's language; do not copy the English title as is, take the pattern UNDERNEATH it.
- Em dash appears NOWHERE in the output: not in a title, not in the brief, not in a note. If you need a separator, use a period, comma, colon, or middle dot (·).

## Where the output goes
Write each run as a single file in the `outputs/` folder: `outputs/YYYY-MM-DD-brief.md`.
Inside the file: (a) a data summary (how many titles, which subreddits, the standout titles sitting at the top of the feed), (b) a HOTTEST-TO-COLDEST ordered angle list (with frequency + order proof), (c) a "make this week" short list (top 3-4 angles + sample title + format), (d) the skipped ones (angles that hit "what you are NOT" or have thin data, with the reason).

## Persistent memory (the system improves every week)
When you actually produce an angle and it lands (or does not), write it with the date under the "angles that landed" section at the bottom of `target/01-niche.md` (which hook, which format, what happened). Later briefs feed from there too; every week the system gets closer to the angle that truly works for you. When you notice a new subreddit or search term, add it to `target/01-niche.md`.

## Optional advanced box · if you also want the vote count (OAuth)
RSS is the default, setup-free path and is enough for most people (order + frequency carry the signal). If you also want to see the vote/comment COUNT, Reddit's official API gives it, and setup is one-time:
1. Open `reddit.com/prefs/apps`, "create another app", pick type **script**.
2. It gives you a `client_id` (the short code under the app name) and a `secret`.
3. Get a token with them: send `grant_type=client_credentials` with Basic Auth (client_id:secret) to `https://www.reddit.com/api/v1/access_token`. (If you get `401` while testing, the endpoint works, fix the credential.)
4. With the token, pull `https://oauth.reddit.com/r/<SUBREDDIT>/top?t=week&limit=25`; in the JSON, `data.children[].data.ups` and `num_comments` give the vote and comment COUNT.
This path wants deeper signal; RSS works with zero setup. Both feed the same brief, the only difference is the vote count becoming visible.
