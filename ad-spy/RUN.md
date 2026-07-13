# RUN · Two Commands

> Cracking competitor ads is two steps. Open this file and copy the relevant command, filling in the `<...>` parts for yourself.
> Thanks to `CLAUDE.md`, Claude Code will already read the brand + voice + competitors + format files.

## Step 1 · Generate your competitors' ad links (copy)

```
generate the meta ad library links for my competitors.

rules:
- give a separate link for each competitor in 03-competitors.md.
- build the links with country set to my market and active_status=active.
- write the competitor's name next to each link.
- at the end, tell me in one line what to do next (click the link, paste the active ads).
```

The system gives you a link for each competitor. Click the link, and on the Meta Ad Library page that opens you will see that competitor's **currently running (active)** ads. Copy the text of the visible ads (the top text, the headline, the "running since" date, the button text) and paste it into a file named after the competitor in the `competitor-ads/` folder. How to paste: `competitor-ads/READ-paste-guide.md`.

## Step 2 · Analyze and produce 10 concepts (copy)

```
analyze all the ads in the competitor-ads folder and produce 10 ad concepts for me.

rules:
- first say in one line that you read the brand + voice + competitors + format + raw ads files.
- break down each competitor ad: hook, promise, for whom, format, proof, cta, how long it has been running.
- mark the ad running for months as a "winning candidate" and write why.
- summarize the repeating pattern (common hook, common offer type, common emotion) in one paragraph.
- dress that logic in my brand and voice and write 10 concepts. each concept: hook, format suggestion, offer/promise, cta, "which competitor logic it came from", "why it can land".
- do not invent a number/discount/guarantee i do not have, leave a placeholder.
- do not use the banned words in 02-voice.md, keep the tone. do not use em dashes.
- write the output to the outputs/ folder as YYYY-MM-DD-theme.md. at the end, give a LinkedIn measured-register note.
```

## Short version (when in a hurry)
```
analyze the ads in competitor-ads, extract the pattern, write 10 concepts adapted to my brand, write the output to outputs/. follow the voice and format files, do not invent numbers.
```

## Note
The more competitors and ads you paste, the clearer the pattern comes out. At least 2 competitors, 2-3 active ads per competitor, is a good start. A pattern does not come from a single ad.
