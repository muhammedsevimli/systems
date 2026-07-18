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

More systems will be added over time. Each system has its own README that explains setup.

## Install

You can pull any system on its own. For Brand Memory:

```bash
npx degit muhammedsevimli/systems/brand-memory brand-memory
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
