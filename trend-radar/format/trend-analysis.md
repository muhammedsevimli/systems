# Trend Analysis · Hook Patterns + Brief Structure

The system turns the pulled titles into angles with the steps described here.

## What a hook pattern means
The OUTSIDE of a title is the topic (that plant, that product, that tool). The INSIDE is the hook pattern: the psychological angle that lifts the title. You take the pattern, not the topic; the same pattern is dressed onto another topic in your niche. Example: "My plant is dying, what should I do" has the topic "plant" and the pattern "rescue/diagnosis". The same pattern lands in food, finance, or software niches too.

## Frequently repeating hook patterns (pick from here when naming a cluster)
1. **Rescue / diagnosis:** "this broke, what should I do". Explodes comments (everyone helps/diagnoses). High comment signal.
2. **Before/after transformation:** "it got to this state in 6 weeks". Broad reach, shows proof (photo/before-after).
3. **Cheap / free / no-buy:** "I did this without spending money". Gets saved, gets shared.
4. **Beginner mistake:** "if you do this, stop, I used to too". Broad audience, sees themselves.
5. **With few resources / constraint:** "for those with a north-facing window", "in 10 minutes", "with one ingredient". Practical, actionable.
6. **Comparison / choice:** "X or Y", "the best/worst I bought". Sparks debate.
7. **List / roundup:** "5 that are impossible to kill", "3 things for beginners". Clickable, saveable.
8. **Counter-take / myth-busting:** "everyone gets this wrong, here is the truth" (PROVE it, not a hollow claim).
9. **Personal story / turning point:** "the thing I learned after 1 year". Builds connection.
10. **Result/number reveal:** "it became this much, here is how". Concrete, builds trust.

## Reading heat (proof · with the RSS signal)
RSS has NO vote (upvote) or comment COUNT. So you read heat from two other signals, both visible in the `data/` file:
- **Frequency (how much it repeated):** how many titles the same hook pattern appears in. A cluster repeating in 8 titles is hotter than 2. The most-discussed problem of the week is the one that repeats most.
- **Feed order (how near the top):** the `top/.rss?t=week` feed is already sorted, the top post landed most that week in that community. A cluster concentrated in the upper feed rows is hotter than one scattered in the lower rows.
- **The hottest:** the cluster that both repeats a lot and sits at the top of the feed. Lots of repeats but always at the bottom = "broad but weak"; few titles but always at the top = "narrow but strong".
No invented numbers, and the vote count is not invented either (RSS does not give it). If a cluster has a single title, do not call it a "trend", call it a "single signal". (If you also want the vote COUNT, the optional OAuth box at the bottom of `CLAUDE.md` adds it; RSS is the default setup-free path.)

## Mapping to the niche (the most critical step)
Turn each landing pattern into your work via `brand/01-brand.md`:
1. Take the pattern (not the topic).
2. What does this pattern map to in your niche, write it concretely in one sentence.
3. Check against "what you are NOT" in `brand/01-brand.md`. If it hits, ELIMINATE it, write why you skipped it in the "skipped" section of the brief.
4. Write 1-2 sample titles in the tone of `brand/02-voice.md`. No banned words, no em dash.
5. Suggest a format: which format the pattern sits well in (rescue/diagnosis reel; list carousel; before/after short video; counter-take long video or thread).

## Brief structure (outputs/YYYY-MM-DD-brief.md)
1. **Data summary:** how many titles, which subreddits, scan date, the standout 3 titles sitting at the top of the feed.
2. **Hottest-to-coldest angle list:** for each angle: name · hook pattern · proof (titles + repeat count + feed order) · niche mapping · sample title(s) · format.
3. **Make this week (top 3-4):** the hottest, niche-fitting, producible angles. For each: one sample title + format + why this week.
4. **Skipped:** angles that hit "what you are NOT" (with the reason) + thin single signals.

## HONEST LIMIT · access model
- **Reddit:** the public RSS feed (`top/.rss?t=week`) is free and keyless, needs no setup. The system pulls the titles REALLY and automatically (Bash curl + descriptive User-Agent). It collects no personal data, does no login or scraping; it reads only the public post title, link, and date. Reddit closed its keyless `.json` endpoint (403); RSS is still open (200), so the system uses RSS. RSS gives no vote count (see reading heat: frequency + feed order). An optional OAuth path for those wanting the vote count is at the bottom of `CLAUDE.md`.
- **YouTube / TikTok / Reels:** there is no free, reliable, automatic path. Official APIs demand quota/approval and are weak for trend discovery; scraping hits terms of service and is fragile. So these platforms are an optional "open and paste" layer (the same logic as the honesty of the Meta Ad Library or similar manual steps). The system does not invent trends; it draws conclusions only from what it pulled from Reddit or what you pasted.
