# Job Application Agent

A system that signs in to LinkedIn for you every morning, finds and scores matching listings, reorders your CV for each listing, writes the cover letter and the form answers, and fills in the Easy Apply form up to the last step. Whether it presses the submit button is your call, with a single line.

**The system runs in your own browser, with your own session, in your own name.** It does not know your password, does not touch your profile, and prepares at most five applications a day.

## What it does

When you are job hunting, most of the day goes into repeating the same work: open the listing feed, read each one to see if it fits, edit your CV for that listing, answer the same five form questions again, note down where you applied. This system finishes that loop before you wake up and leaves a report on your desk.

1. It searches LinkedIn for the roles in `you/TARGET.md` and looks only at Easy Apply listings.
2. It compares each listing with `you/CV.md` and scores it out of 100. It rejects anything that crosses your red lines or falls below the threshold.
3. For the listings that pass, it opens a folder: the listing text, the match breakdown, the CV reordered for the listing (with its PDF), a cover letter, and the form answers.
4. It fills in the Easy Apply form, uploads the CV, and gets to the "Review" screen.
5. With `submit: no` it stops there and saves the draft. With `submit: yes` it submits.
6. It writes the `applications.csv` table and the day's report.

**What it does not do:** it never adds experience, tools or dates your CV does not have. It reorders, emphasizes and summarizes; it does not make things up. It does not fill in listings that redirect to the company site; it prepares the cover letter and leaves the link for you. When it hits a form question it does not know the answer to, it closes the form and asks you.

## Setup

What you need: [Claude Code](https://claude.com/claude-code), Chrome with the [Claude in Chrome](https://claude.com/chrome) extension, Python 3.10+. Signing in to LinkedIn in Chrome once is enough. You do not open or fill in any file; Claude does all of it in chat.

1. Open Claude Code, give it this address and say "set this up for me":

```text
github.com/muhammedsevimli/systems/tree/main/job-application-agent
```

   Claude downloads the folder (with `npx degit`; if you like the command line: `npx degit muhammedsevimli/systems/job-application-agent job-application-agent`).

2. In the folder, type `setup`. Claude asks for your CV (PDF, Word or text) and converts it into `you/CV.md`; asks in chat which roles you want, location, salary floor, red lines and the time; writes `you/TARGET.md`; installs the scheduler. The submit switch starts off.

3. Type `scan` and watch the first scan and the score table. If you like it, type `daily run` or wait for the morning; it runs by itself at the time you gave during `setup`.

4. Read the reports for a few days. Once you trust the system, say "turn submit on" and Claude flips the switch.

The other commands (`scan`, `prepare <link>`, `submit <folder>`, `rehearse <folder>`, `status`) and the details are in `RUN.md`. The `you/CV.md` that ships is the fictional Elif Aydın; `setup` replaces it with yours.

## Does it really work

Yes, with a dry run. All of it is in `TEST-RESULT.md`: it was run on real LinkedIn listings with the fictional Elif Aydın CV and submit turned off. How many listings were scanned, how many were rejected, what was prepared with which score, at which step the form stopped, it is all there. The things that were not measured are written down too.

## What you should know

- LinkedIn's terms of use restrict automated tools. That is why the daily cap is low, there is a wait between clicks, and every application is prepared at human quality. Bulk, fast applications put both your account and your reputation at risk. I do not recommend raising the cap.
- The system runs on your own account. Do not use it on someone else's behalf or in someone else's account.
- For the scheduled run, the computer must be on at that time and Chrome must be reachable. If Chrome is closed, the runner opens it.
- The `reports/log-*.txt` files are raw run logs; do not share them. `.gitignore` already keeps them out.

## Supported tools

| Tool | File it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Codex, Cursor, Windsurf and other tools that read AGENTS.md | `AGENTS.md` (the browser steps need Claude in Chrome) |

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI. If you get stuck setting it up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.com/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
