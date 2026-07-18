# data/ folder · what is here, what you paste

This folder holds two kinds of files (and one subfolder):
1. **reddit-YYYY-MM-DD.md** · the system creates this AUTOMATICALLY on the 1st command. You do not touch it.
2. **rss/** · the raw RSS files the system downloads with curl (one `.rss` per subreddit). Intermediate files, you do not look at them.
3. **(optional) paste-*.md** · a file where you HAND-paste standouts from YouTube/TikTok/Reels.

## The Reddit side is fully automatic
When you run the 1st command, the system pulls the public RSS feed (`top/.rss?t=week`) of the subreddits in `target/01-niche.md` with Bash curl and writes the `reddit-YYYY-MM-DD.md` file itself (subreddit · order · title · date · link). No key, no account, no setup, no clicking. Since RSS gives no vote count, the system reads heat from feed order + repeat count; if you also want the vote COUNT, see the optional OAuth box in `CLAUDE.md`.

## YouTube / TikTok / Reels paste (optional · 3 minutes)
Not required. The system works with Reddit alone. But if there are 3-5 short videos/reels blowing up in your niche in the last week, pasting them makes the brief sharper (it catches current format trends that are not on Reddit).

### How to paste
1. Search your niche on YouTube/TikTok/Instagram, filter to "this week" or the last few days, look at the most-viewed/liked.
2. Open a file named `paste-YYYY-MM-DD.md` in this folder.
3. Fill in the block below for each video. If you cannot see a number, leave it blank, do not invent; the system does not use invented numbers.

### Template (one block per video)
```text
## <video title or first sentence>
Platform: <YouTube Shorts / TikTok / Reels>
Views/likes: <a number if you can see one, otherwise blank>
Format: <talking head / screen recording / before-after / list / voiceover>
What the first 3 seconds say: <the hook sentence>
Topic: <one sentence>
Note: <what caught your eye. blank if none.>
```

## Tips
- The first 3 seconds (the hook) is the most valuable data. The system takes the hook pattern, not the topic.
- Do not fix the text, paste it as is.
- Leave a number you are unsure of blank. If it is blank the system says blank, it does not invent.
- 3-5 examples is a good start. A pattern does not come from a single example.
