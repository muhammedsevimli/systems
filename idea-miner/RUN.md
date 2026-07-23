# RUN · Two Commands

> Idea mining is two steps. Open this file and copy the relevant command.
> You paste nothing. You write the field you care about into `you/01-profile.md` once; the system scans demand itself.
> Thanks to `CLAUDE.md`, Claude Code will already read the profile + sources + criteria + format files.

## Step 1 · Scan demand (copy)

```
scan the demand in my field.

rules:
- read the field in you/01-profile.md and the search queries in you/02-sources.md.
- scan the sources yourself with your web and shell tools:
  - for hacker news, fetch the hn.algolia.com public json (use https, plain http answers 301).
  - for reddit, pull the public rss search feed with curl: reddit.com/search.rss?q=... and r/<sub>/search.rss?q=...&restrict_sr=1. give a descriptive user-agent. the keyless .json endpoint returns 403, do not use it.
  - on 429 (rate limit), wait and retry with curl --retry --retry-delay, and pull queries one after another.
  - for general web and community forums (industry forums, marketplace and app store reviews), run a web search.
- pull verbatim the real sentences where people say "i wish there was", "i am looking for a solution to this", "i would pay for this", "i do it by hand and i am sick of it". put a source and link on every signal.
- note the names of any existing solution or competitor you see in the scan.
- write the signals you collect into signals/collected-TODAYS-DATE.md. at the end, summarise in one line how many signals came from which source and which one you could not reach.
- do not invent signals. do not write a sentence you did not actually pull, mark what you could not reach as "could not be reached".
```

The system scans the sources itself and writes the real demand sentences into `signals/`. You do not put anything in that folder by hand. How it fills up: `signals/READ-how-this-fills.md`.

## Step 2 · Score and pull out the best 5 ideas (copy)

```
score all the demand signals in the signals folder and give me the best 5 saas ideas.

rules:
- first say in one line that you read the profile + sources + criteria + format + collected signals files.
- turn each signal into a one-sentence saas idea (what, for whom, solving which pain). merge signals describing the same pain into one idea.
- write how many independent signals and sources back each idea (signal strength). mark the signals carrying money language.
- score each idea 1-5 on four criteria: market size, feasibility, competition gap, market fit for my region. a one-line reason under every score. total it out of 20.
- score the region criterion against the region and payment reality written in my profile, not a market you assume.
- if a competitor came out of the scan, name it on the competition-gap line, do not say "copy it", write the point of difference.
- filter through the field and limits in my profile. drop an idea in a field i do not know to the bottom or add a "find a partner" note.
- sort by total score, write the top 5 ideas with detail cards. mark the top one "start here this week".
- do not invent ideas, stand only on the collected signals. do not inflate a score without a reason.
- flag the risky field (license, regulation). do not use em dash, no motivational language, no income promises.
- write the output to the outputs folder as TODAYS-DATE-idea-report.md.
```

## One command (when in a hurry: scan and score together)

```
scan the demand in my field, then score it and pull out the best 5 saas ideas.
scan hacker news, reddit (rss, not json) and the web and forums yourself with your web and shell tools, write the real demand sentences into signals, score the four criteria, put the output in outputs. follow the criteria and profile files, do not invent signals or ideas, justify every score.
```

## Step 3 · When you decide on an idea (copy)
```
i decided <to build / to drop> the <idea name> idea, reason: <short>. add it to the decision log at the bottom of you/02-sources.md with today's date: which idea, what i decided, why. do not propose this idea again in later reports.
```

## Note
The better the search queries you give, the more accurate the scan. The queries live in `you/02-sources.md`; add your own industry words. A strong idea does not come from a single signal; the strong idea is the one whose pain shows up in several sources. The system does not scan X automatically (it wants a login); it builds a one-click search link for it and you look by hand if you want.
