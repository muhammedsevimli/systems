# Agent Company

A template that runs Claude Code like a company. Claude is the CEO. You give it a job; it works out what the job needs, hires a worker for each need, gives everyone their own desk and sets up the shift order. The finished work lands in your approval folder. Nothing goes out until you approve it.

You are the board.

## What it does

When you tell a single chat "write this week's newsletter, write the Instagram announcement too, then check it", everything happens in one place, in one line, tangled together. This template splits the work the way a company does:

1. **Needs list.** The CEO reads the job, writes its finished state in one sentence and lists the needs.
2. **Hiring.** It picks someone from the staff for each need: a writer for text, an illustrator for visuals, an auditor for checking. If no role fits, it writes a new worker from the hiring template.
3. **A desk for everyone.** Every worker works in their own copy of the files. Nobody steps on anyone else's files. When the work is done, the copies are merged into the main folder.
4. **Shift order.** Workers who do not wait on each other work at the same time. A worker who needs someone else's output starts when that one finishes. The auditor goes last.
5. **Workers who take helpers.** If the writer's job splits, it takes a helper on its own. It does not ask you; you only get the finished work. Every helper still goes into the log.
6. **Log.** Who was hired when, which desk they worked at, when they finished: all of it sits line by line in a single log file.
7. **Approval gate.** The finished work lands in `company/approval/`. Email, posts, publishing, payments: Claude does none of them.

## Staff

| Worker | What it does | Takes helpers |
|---|---|---|
| Writer | Newsletters, posts, page copy, scripts, email drafts. | Yes |
| Illustrator | Covers, posters, scene plans, diagrams. A brief and a drawing that opens in the browser for every visual. | Yes |
| Composer | A music and sound plan for a video or ad, and the brief to give a music generator. | Yes |
| Researcher | Competitor, price and trend research. Every fact with its source link. | Yes |
| Lookout | Competitor radar. Scans the list you give it two mornings a week, writes who posted what and what took off, and tells you what to make today. | No |
| Auditor | Checks every output that will leave the company against the company card and the red lines. Says PASS or FIX. | No |

You can add any role you want: just type `hire translator`.

## Setup · from the chat

What you need: [Claude Code](https://claude.com/claude-code). You do not need to open or fill in any file.

1. Open Claude Code, give it this address and say "set this up for me":

```text
github.com/muhammedsevimli/systems/tree/main/agent-company
```

2. In the folder, type:

```text
setup
```

Claude asks at most five questions to get to know your company: its name, what it does, who it sells to, which channels it publishes on, two or three rules that describe its voice, and your red lines. It writes the company card from your answers. It also prepares the folder so everyone can work at their own desk; if your computer is missing the small tool this needs, it tells you.

If you want to try it first, give it a job without typing `setup`. The folder comes with a fictional example company: **Urla Table**, a small home-cooking restaurant in Urla.

## Three commands

```text
setup
```
First-time setup. Once.

```text
hire <role>
```
Adds a new worker to the staff. Example: `hire translator`. Claude asks three questions, writes the worker's job description and shows it to you. If Claude Code asks for permission to save the file, you approve it.

```text
shift
```
Shows the board of the last job: who was hired, who is at which desk, who finished, what is waiting for approval.

Apart from these, you give the job in plain words:

```text
Write this week's email newsletter for Urla Table, and the Instagram announcement too.
```

Once you have read the job in the approval folder, type `approve <file>` or `reject <file> <your note>`. If you reject it, the CEO passes your note to the right worker and has it fixed.

## Competitor radar: the lookout

A second job you can give the company: watching your competitors. The CEO hires a lookout for it and gives it the list to watch. The lookout scans the list and leaves you a three-part report on every shift:

1. **What they did:** who posted what in the last few days, and what took off.
2. **The angle that fits us:** where that content connects to your company.
3. **What we should make today:** three concrete ideas, each for a channel.

If the lookout sees something fresh that is gaining views fast, it also writes a reply or post draft. The draft goes through the auditor and lands in the approval folder. Nothing is sent unless you approve it.

**Setup.** Give Claude Code this system's GitHub address, type `setup` in the folder, then type:

```text
watch my competitors
```

The CEO asks at most five questions: who to watch (YouTube channel, site, blog), which words to search for in the news, any links you want to add by hand, how many days to scan, which channel the opportunity drafts are for. It writes the list itself and runs the first scan. After that, for every new report:

```text
radar
```

**What it reads.** All free, no keys:

| Source | How | Traction data |
|---|---|---|
| YouTube channel | The channel's public feed | Views and likes |
| Site or blog | The site's feed, or its sitemap if there is no feed | None |
| News | Google News search | None |
| Reddit | Community or search feed | None |
| A link you add by hand | The text of X and TikTok posts, the title of other pages | None |

Following X and Instagram accounts on a schedule is not in this version: these sites do not give a list without a key. If you add the link of a post you saw, the lookout reads it too. An Instagram link needs a login, so it is not read; the note you write next to it is used. Where there is no view data, the lookout makes up no numbers; it writes "no view data".

**Fixed shift.** If you like, the lookout runs on its own two mornings a week (for example Monday and Thursday at 08:30). Just say "set up the lookout's shift"; the CEO adds a line to Task Scheduler on Windows or to cron on a Mac. Your computer has to be on at that time. It is optional; you can also run it by typing `radar`.

**What you need.** Python 3 on your computer. Most Macs have it; on Windows, if it is missing, the CEO tells you how to install it from python.org. The CEO runs the scan; you do not need to open a terminal.

## Limits

- At most 5 workers and at most 2 helpers in total per job. A helper cannot take a helper.
- A job's token ceiling is 1.5 million. If it would be passed, the CEO stops and asks you. You can change both on the company card. The CEO adds up the token counts it can see, and that number stays below the real usage (more in `TEST-RESULT.md`).
- Nothing goes out: no email, post, message, publishing or payment. Even when you say `approve`, you do the sending.
- No number, price or campaign that is not on the company card goes into an output. Missing information is marked `[ASK THE OWNER]`.

## Does it really work

Yes, with real runs. All of it is in `TEST-RESULT.md`.

- **Round 1, weekly newsletter:** the CEO hired the writer and the auditor, and the writer took a helper for the Instagram post. Two desks were opened, both merged without conflicts, and the job landed in the approval folder. 16 log lines, 3 minutes 50 seconds.
- **Round 2, newsletter and chalkboard poster:** the writer and the illustrator worked at their own desks at the same time, and the auditor started after both had merged. 3 workers, 1 helper, 3 merges, 22 log lines, 5 minutes.
- **The lookout, competitor radar:** four runs with real public sources (3 food channels, a food site, Google News, Reddit). `watch my competitors` took 3 minutes 32 seconds: 7 of 7 sources read, 30 items from the last 4 days, a 63-line report. The lookout did not count a fresh video that did not fit the company as an opportunity; it wrote an Instagram draft from a news story the owner added with an "opportunity" note, and the auditor said PASS. The shift script ran from start to finish on Windows when started by hand.
- **Sent out:** zero in every run.

The issues that came up in the test and the commands that were not tested are in the same file.

The output itself is in `EXAMPLE-OUTPUT.md`.

## What you should know

- Every worker runs like a separate Claude session, so it uses more tokens than a single chat. You do not need the company for a small job (a single post).
- If your Claude Code has a multi-stage batch run feature, the CEO can run the same shift order in one go. It is optional.
- Step-by-step usage is in `RUN.md`.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` and `.claude/agents/` |
| Codex, Google Antigravity, Windsurf, Kilo and 20+ tools | `AGENTS.md` (in a tool that cannot open sub-agents, the CEO plays the roles one after another) |

---

**Muhammed Sevimli** builds these systems. Real sales and growth systems with AI. If you get stuck setting one up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- X: https://x.com/_msevimli
- Instagram: https://instagram.com/msevimli_
- Threads: https://threads.com/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

🧩 Built with Claude Code.

## License

[MIT](LICENSE)
