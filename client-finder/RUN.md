# RUN · Two Commands

> Finding clients takes two steps. Open this file, copy the relevant command, and fill in the `<...>` parts for yourself.
> Thanks to `CLAUDE.md`, Claude Code will already read the service + voice + niche + format files.

## Step 1 · Build the ad library links for your niche (copy)

```
build the meta ad library links for my niche.

rules:
- give a separate link for each search term in target/01-niche.md.
- build the links with the country code from the file and with active_status=active.
- url-encode non-ascii characters.
- write which term each link belongs to next to it.
- at the end, tell me in one line what to do next (click the link, paste the brands).
```

The system gives you a link for each search term. Click the link, and in the Meta Ad Library page that opens you see the brands **currently running ads** in that niche. If they are running ads, they have a budget. Paste the name, the ad text, and the "started running on" date of the brands you see into a file in the `prospects/` folder. How to paste: `prospects/READ-paste-guide.md`.

## Step 2 · Rank the prospects and write the messages (copy)

```
analyze the brands in the prospects folder, give me a ranked prospect list and a tailored first message for each one.

rules:
- first say in one line that you read the service + voice + niche + format + raw prospect files.
- break down each prospect: what they sell, to whom, how long they have been running ads, how many different ads, format, weak point.
- mark the one running ads for months as "has budget" and write why.
- write each prospect's weak point by showing it from their ad (weak hook / unclear offer / single format / no social proof).
- score and rank the prospects: budget signal + how solvable the weakness is with my service + fit with my price range.
- write a tailored first message for each prospect: what you noticed (a specific detail from that brand's ad), what you suggest, one clear question.
- the messages must be tailored, not copy-paste templates. do not use bulk-send language.
- do not invent a number, example, or reference i do not have, leave a placeholder. do not invent anything about the prospect.
- do not use the banned words in 02-voice.md, keep the tone. do not use em dashes.
- write the output into the outputs/ folder as YYYY-MM-DD-niche.md. at the end, add a note on the register for linkedin and email.
```

## Short version (when you are in a hurry)
```
analyze the brands in prospects, rank them by budget signal and weak point, write a tailored first message for each, put the output in outputs. follow the voice and format files, do not invent anything.
```

## Step 3 · When a message gets a reply (copy)
```
the message i sent to <brand name> got a reply. add it with today's date to the "angles that got replies" section in target/01-niche.md: which weak point it was, which sentence landed, make this angle primary in the next messages.
```

## Note
The more brands and ads you paste, the more accurate the ranking. At least 4-5 brands, with 1-2 active ads per brand, is a good start. You cannot find a weak point from a single ad.
