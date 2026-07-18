# RUN · Two Commands

> Finding trends is two steps. Open this file and copy the relevant command, then run it.
> Thanks to `CLAUDE.md`, Claude Code will already read the brand + voice + niche + format files.
> The Reddit side is fully automatic: the system pulls the RSS itself, you paste nothing.

## Step 1 · Scan your niche's reddit communities (copy)

```
scan my niche's reddit communities.

rules:
- for each subreddit in target/01-niche.md, pull https://www.reddit.com/r/<sub>/top/.rss?t=week.
- pull with curl, give a descriptive user-agent. use curl, not web-fetch (reddit returns 200 to curl).
- if you get 429 (rate limit), wait and retry with curl --retry --retry-delay, pull subreddits one after another.
- take the title, link, and date from each entry. keep the feed order (the top one landed most that week).
- rss has no vote count, do not invent one. order is the signal.
- write the result to data/reddit-TODAYS-DATE.md in a table: subreddit, order, title, date, link.
- if a subreddit cannot be pulled, do not invent, write "could not be pulled (reason)".
- at the end, say how many titles from how many subreddits and the http code in one line.
```

The system pulls each subreddit's RSS feed itself and writes the top rising titles into the `data/` folder. You do not click. (If you want, after this step you can hand-paste a few standout examples from YouTube/TikTok/Reels: `data/READ-paste-guide.md`. Not required, the system works with Reddit alone.)

## Step 2 · Get your "make this week" brief (copy)

```
analyze the titles in the data folder and write me a "make this week" brief.

rules:
- first say in one line that you read the brand + voice + niche + format + data files.
- group titles by topic and hook pattern. call something a "trend" if it repeats in at least 2 titles.
- for each pattern, name the repeating hook and show it from the data: which titles, how many, which subreddits.
- rate each angle by heat: rss has no votes, so heat = how many titles repeat it (frequency) + is it near the top of the feed (order). do not invent numbers.
- map each angle to my niche: what does this hook mean in my work, say it concretely.
- do not suggest making an angle that hits a "what you are not" line, write what you saw but why you skipped it.
- for each landing angle, write 1-2 sample titles in my voice and a format suggestion (reel/carousel/short video).
- do not use em dash. do not use the banned words in 02-voice.md.
- write the output to the outputs/ folder as TODAYS-DATE-brief.md: data summary, hottest-to-coldest angle list, "make this week" top 3-4, skipped ones.
```

## Short version (when in a hurry)
```
group the titles in data by hook pattern, sort hottest to coldest (frequency + feed order), write the top 3-4 angles in my voice with a sample title as "make this week", skip anything that hits "what you are not", put the output in outputs. do not invent, there is no vote count, read from order and repeat count.
```

## Step 3 · When you produce an angle and see its result (copy)
```
i produced and published the <angle name> angle, result: <landed / did not land, short>. add it to the "angles that landed" section of target/01-niche.md with today's date: which hook, which format, what happened. factor this into later briefs.
```

## Note
The more and the more accurate the subreddits you add, the sharper the scan. 3-5 subreddits is a good start. Pick the community that fits your niche exactly: a broad community (e.g. a general topic) brings a lot of noise, a narrow niche-specific community gives a cleaner signal. If you also want to see the vote COUNT, check the optional OAuth box at the bottom of `CLAUDE.md`; RSS works with zero setup.
