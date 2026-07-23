# Systems

An open collection of real systems Muhammed Sevimli builds with AI. Each system lives in its own folder and works on its own. They are all simple, most are a single markdown pack, and you do not need to know how to code.

## Systems

| System | What it does | Folder |
|---|---|---|
| Brand Memory | Write your brand once so AI never forgets it. A three-file brand memory that works in Claude Code, Cursor, Codex and 20+ tools. | [brand-memory/](brand-memory/) |
| Sales CRM | A single-file CRM for sales / call-center teams. Every customer on one card, a morning call list, a month-end sales panel. Shared team mode via Google Sheets. | [sales-crm/](sales-crm/) |
| Competitor Tracker | Scans your competitors (site, news, youtube, instagram) weekly and boils it into one Monday report: a summary of each new post + how to adapt it to your brand. | [competitor-tracker/](competitor-tracker/) |
| Second Brain | Write your work into files once so AI already knows the history on every task: projects, decisions, people, resources. It loads only what each task needs. | [second-brain/](second-brain/) |
| Carousel + Hook Generator | Give a topic, get 3 cover hooks and a 7-slide carousel in your brand voice (with image directions + a LinkedIn version). | [carousel-generator/](carousel-generator/) |
| Ad Spy · Competitor Ad Analyzer | Write your competitors, the system builds Meta Ad Library links. Paste the active ads, it extracts the pattern of the ads running for months and writes 10 ad concepts adapted to your brand. | [ad-spy/](ad-spy/) |
| Review Miner · Customer Review Sales Miner | Paste your product's customer reviews, the system extracts the repeating themes, finds the most common objection, and writes a sales angle + objection response + ad hook for each theme. The proof of every angle is the customer's own sentence. | [review-miner/](review-miner/) |
| Ad Concept Factory · 50 Static Ad Concepts | Write your own winning ads and customer reviews, the system produces 50 diverse static ad concepts in your brand voice (automatically every morning or with one command). Rotation of hook type x segment x emotion; each concept is hook + visual direction + rationale. | [ad-concept-factory/](ad-concept-factory/) |
| Client Finder · Prospect Finding + First Message | Write your niche, the system builds Meta Ad Library links. Paste the brands running ads in that niche, and it ranks the prospects by budget signal and the weak point of their ad, then writes each one a tailored first message built on a specific detail from their own ad. | [client-finder/](client-finder/) |
| Trend Radar · Rising Content Angles in Your Niche | Write your niche, and the system pulls the top rising titles of the last week from that niche's Reddit communities via public RSS on its own. It extracts the repeating hook patterns, sorts them hottest to coldest, and writes a "make this week" brief in your brand voice (via frequency + feed order, without inventing a vote count). | [trend-radar/](trend-radar/) |
| Google Ads Auditor · Wasted Ad Spend | Export your Google Ads report once, and the system finds which searches eat money without converting, from your own data. It calculates the total wasted amount line by line, extracts the missing negative keywords, flags the campaign that misallocates the budget, and gives a "fix this week" list (only from the data, no invented multiplier). | [google-ads-auditor/](google-ads-auditor/) |
| Idea Miner · SaaS Idea Scorer | Write the field you care about, and the system scans Hacker News, Reddit, and web and community forums on its own. It turns the real demand where people say "I wish there was" and "I would pay for this" into ideas, scores them on four criteria (market size, feasibility, competition gap, market fit for your region), and ranks the 5 best ideas you could build this week with the reasoning behind each. | [idea-miner/](idea-miner/) |
| Product Plan · Build Plan From a URL | Give the address of a product you like, and the system browses that site itself (home page, features, pricing, docs), takes its logic apart, and writes three files adapted to your business: the product plan, the data schema, and a Claude Code prompt set you paste in order. Not a clone factory; it also writes which feature does not belong in your first version, and why. | [product-plan/](product-plan/) |
| Sales Page + Payment · Single File Page Builder | Write your product into one file and the system writes the sales copy, produces a working single file HTML page, wires in your email form and your ready made payment link, and hands you a launch checklist. If you gave no proof it puts no proof section on the page, and it invents no review. | [sales-page/](sales-page/) |
| Pricing Solver · Pricing Built on Competitor Data | Write your product and your competitors, and the system opens the competitors' public pricing pages itself, pulls the tiers and figures with their sources, builds a feature by tier matrix, picks the value axis with a reason, and proposes three justified tiers. For a competitor who hides their price it invents no figure and keeps them out of every average. | [pricing-solver/](pricing-solver/) |

More systems will be added over time. Each system has its own README that explains setup.

## Install

You can pull any system on its own. For Brand Memory:

```bash
npx degit muhammedsevimli/systems/brand-memory brand-memory
```

The pattern is the same for every system; copy the line you need:

```bash
npx degit muhammedsevimli/systems/sales-crm sales-crm
npx degit muhammedsevimli/systems/competitor-tracker competitor-tracker
npx degit muhammedsevimli/systems/second-brain second-brain
npx degit muhammedsevimli/systems/carousel-generator carousel-generator
npx degit muhammedsevimli/systems/ad-spy ad-spy
npx degit muhammedsevimli/systems/review-miner review-miner
npx degit muhammedsevimli/systems/ad-concept-factory ad-concept-factory
npx degit muhammedsevimli/systems/client-finder client-finder
npx degit muhammedsevimli/systems/trend-radar trend-radar
npx degit muhammedsevimli/systems/google-ads-auditor google-ads-auditor
npx degit muhammedsevimli/systems/idea-miner idea-miner
npx degit muhammedsevimli/systems/product-plan product-plan
npx degit muhammedsevimli/systems/sales-page sales-page
npx degit muhammedsevimli/systems/pricing-solver pricing-solver
```

Or clone the whole repo, or download it with the green **Code → Download ZIP** and use any folder you want.

## Supported tools

File-based systems (e.g. Brand Memory) work the same way across these tools; whichever tool you use reads its own file. Standalone tools (Sales CRM in the browser, Competitor Tracker with Node) have their setup in their own README.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

---

**Muhammed Sevimli** builds these systems. Real sales and growth systems with AI. If you get stuck setting one up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.net/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE)
