# 02 · Sources and Automatic Search Queries

> The system scans demand ITSELF. This file tells it which queries to scan with.
> What follows is a fictional example (local appointments + small ecommerce). Change it for your own field, and add queries as you find good ones.
> The principle: look where people OPENLY use asking or complaining language for a solution. The most valuable signal is the sentence "I would pay for this".

## Demand-language patterns (what the system looks for)
The sentence types the system hunts for, whatever the source:
- "I wish there was an app / tool that"
- "I am looking for a solution to this", "does something like this exist"
- "I do it by hand every month and I am sick of it", "we do this manually"
- "I hate <tool>", "<tool> is too expensive / too complicated"
- "we pay $X a month for this", "I would pay for this"
- "there is no version of this for my country", "it does not work here"

## Hacker News queries (fully automatic · hn.algolia.com)
The system fetches `https://hn.algolia.com/api/v1/search?query=<QUERY>&tags=comment` for each query. Add your own field words.
- `appointment scheduling small business`
- `no-show appointments deposit`
- `respond to reviews small business`
- `ecommerce returns refund manual`
- `someone should build` (general demand hunting)
- `I would pay for` (money-language hunting)

## Reddit queries (fully automatic · public RSS search · curl)
The system pulls `https://www.reddit.com/search.rss?q=<QUERY>&sort=relevance&t=year` for each query, or `https://www.reddit.com/r/<SUB>/search.rss?q=<QUERY>&restrict_sr=1&sort=relevance&t=year` for a target community. On `429` it waits and retries; queries go one after another, not all at once. (The keyless `.json` endpoint returns `403`, which is why RSS is used.)
- `r/smallbusiness` · `no show appointments`, `booking software frustration`
- `r/ecommerce` · `returns manual spreadsheet`
- `r/msp` or your own industry community · `we do this manually`
- across all of reddit · `"I wish there was an app" small business`, `"I would pay for" tool`

> Tip: a narrow, field-specific community gives a cleaner signal; a very broad community brings noise. Mix them: 1-2 broad + 2-3 narrow.

## Web + forum queries (fully automatic · web search)
The system scans these with a web search (industry forums, community sites, marketplace and app store reviews, "looking for" searches).
- `<industry> forum "I wish there was an app"`
- `<job> "looking for software"`, `<job> "software recommendation"`
- Marketplace product pages near your field: the 1 and 2 star reviews.
- App Store / Google Play: the low-star reviews of similar apps ("it does not have this feature", "it does not work in my country").
- Community sites where your customers actually hang out (a trade association board, a Discord announcement page, an industry subforum).

## X (Twitter) searches (semi-automatic · wants a login)
The system does not pull these; it builds a one-click search link for each and you look by hand if you want.
| Search pattern | What you are looking for |
|---|---|
| `"I wish there was an app"` | demand that made it into words |
| `"is there a tool that"` | a user hunting for a solution |
| `<your field word> "doing it manually"` | the manual pain |
| `"appointment" "no show"` | the pain of appointment-taking businesses |

## Decision log (the system fills it, or you do)
When you decide to build an idea, or drop one, write it here with the date. Later reports read this and do not propose the same idea again.
- (none yet)
