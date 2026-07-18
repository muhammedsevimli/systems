# Google Ads Auditor · Wasted Ad Spend 🔍

Export your Google Ads report once, and the system finds which searches are eating money without converting, straight from your own data. It calculates the total wasted amount line by line, extracts the missing negative keywords, flags the campaign that misallocates the budget, and hands you a "fix this week" list. A no-code Google Ads auditor that works in Claude Code, Cursor, Codex and any tool that reads `AGENTS.md`.

A system that saves you from logging into the account every month and eliminating search terms one by one asking "where is my money going". You paste the report once; the system separates the relevant searches from the wasted ones, sums the wasted amount from the cost column in your data, and tells you what to do in priority order. You start not from a guess but from your own number.

## What it does

In Google Ads, money leaks most as "clicks on searches that are not relevant to your business": someone searches "how to clean", clicks your ad, you pay, and that person never buys. This system finds that leak in your report and puts it in front of you with a number. It reads two reports:

1. **Search terms report** (the main source): which searches actually triggered your ads, and how many clicks, how much cost, and how many conversions each one brought. The wasted money is hidden here.
2. **Campaigns report** (if available): cost, conversions, conversion value, ROAS per campaign. It shows where the budget is misallocated.

Then it runs five audits: wasted spend, missing negative keywords, wrong match type, budget misallocation, low CTR / high cost signals. Output: the total wasted amount (calculated from your data, never invented) + a prioritized fix list + estimated savings.

Honest limit: this system does not connect to your account. Google Ads has an official API, but it requires a developer token and OAuth setup, which is a technical job. So the main path is: export the report from the panel, paste it into the `data/` folder. Reading, calculation, and the fix list are fully automatic; you make the changes in the account. The system tells you what to do, it does not touch the account.

## What you need

- **Claude Code, Cursor, Codex** or another AI tool that reads `AGENTS.md`. No terminal required.
- A folder and 15 minutes. You are not learning anything new, just describing your account in a file and pasting the report.
- Access to your Google Ads account (to export the report). If you have conversion tracking set up, the audit is more accurate.

## Supported tools

The same read rule lives in three separate files, and whichever tool you use reads the right one. You do not have to do anything.

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/google-ads-auditor.mdc` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (universal open standard) |

## Install

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/google-ads-auditor google-ads-auditor
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "set it up".** The easiest option. Open this folder in Claude Code / Cursor / Codex and say "set up this Google Ads auditor for my account". It fills in the account file with you.

These are the files the system reads. Fill in the account part with your own:

- `account/01-account.md`: what you sell, for whom, target ROAS/CPA, what you are NOT (which searches are wasted)
- `format/audit-anatomy.md`: the five audits and the rule for calculating the wasted amount (comes ready)
- `format/output-format.md`: the structure of the audit report (comes ready)
- `data/`: you paste the Google Ads reports here (the export guide is inside the folder)

`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/` and `RUN.md` stay as they are, no need to change them.

Then one command. First prepare the report (how: `data/READ-data-export-guide.md`), then audit:

> audit my google ads account. find my wasted ad spend and produce a prioritized fix list

The system classifies each search term, calculates the wasted amount by summing line costs, and produces the fix list. For the full command, see `RUN.md`.

## Does it really work? Test it in 30 seconds

- **Number:** did it show which line costs it summed to get the wasted amount. If it did, it passed.
- **Separation:** did it put a relevant-but-not-converting term in the "watch" bucket, or count all of them as wasted. If it separated them, it passed.
- **Invention:** did it use a multiplier that is not in the data ("doubles it", "grows your revenue"), or speak only from the data. If it spoke only from the data, it passed.
- **Suggestion voice:** did it say "I paused that campaign", or "cut this, add that negative". If it stayed in the suggestion voice, it passed.

## Your account grows · let the system sharpen with you

When you apply a fix (added a negative, cut a campaign), tell the system "I did this". It writes it with the date in the "applied fixes" section at the bottom of `account/01-account.md`. Next month, when it audits the new report, it reads this: it will not suggest the same leak twice, and it compares whether the fix worked. Your account's memory accumulates.

## Example output

`EXAMPLE-OUTPUT.md` has a full audit the system produced for a fictional business ("Oak Handcrafted Wood"): the summary box, the breakdown of the wasted lines, the prioritized fix list, and the watch bucket. The only input was a fictional search terms and campaigns report. (All examples are fictional; there are no real brands, accounts, customers, or numbers.)

## Who it is for

Anyone who spends money on Google Ads: e-commerce brands, service businesses, performance marketers, agencies, founders, small teams, local shops. Anyone who manages their own account but wants a clear answer to "where is my money going". No technical knowledge or code required; the system reads your report, calculates the number, and tells you what to do, and you apply the change.

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI. If you get stuck setting it up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.net/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
