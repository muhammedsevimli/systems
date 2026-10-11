# Test result · 10-11 October 2026

The system really ran on this computer (Windows 11, Claude Code 2.1.284, git 2.55) with the fictional Urla Table company (`demo: yes`). The runs used the Turkish version of this system (`ajan-sirketi`); the English version has the same files, rules and steps with English names. Every number below comes from the run log, the git history or the session record.

## How the test was set up

- The package was copied into an empty folder, the folder was turned into a repository and the first commit was made (the first step of `setup` was done by hand; the question-and-answer part was skipped and the demo company was used).
- The CEO was a separate Claude Code session opened in that folder (`claude -p`, non-interactive mode). That is also how you use it: the CEO is the main session you open in the folder. The session running the test did not stand in for the CEO; it only gave the job and measured the result.
- Permissions: file editing on; as commands only git, the log script and a few read commands. There were no permission denials in any run.
- To measure the desks independently, a separate watcher recorded the output of `git worktree list` every second.
- The desks are git worktrees opened by the CEO itself (`git worktree add`). The `isolation: "worktree"` option of Claude Code's Agent tool was not used: it fails with "not in a git repository" when the main session's folder is not a repository, so the package has the CEO open the desk.

## Round 1 · newsletter + Instagram announcement

**The job:** "Write this week's email newsletter for Urla Table." The writer writes the main text itself and gives the Instagram announcement to a helper (1 helper allowance).

| | |
|---|---|
| Workers | 2: writer, auditor |
| Helpers | 1: the writer's helper (Instagram post) |
| Layers | 3: CEO → writer → the writer's helper |
| Desks opened | 2: writer (23:50:08), auditor (23:51:45) |
| Merges | 2, both without conflicts (`8964f89` writer desk, `e8d1a5d` auditor desk) |
| Desks and branches removed | 2/2; at the end `git worktree list` showed only the main folder |
| Log | 16 lines |
| CEO commits | 6 |
| Auditor verdict | PASS, 4 findings (style and approval layout) |
| In approval | `approval/2026-10-10-newsletter-week-41` |
| Sent out | 0 |
| Time | 3 min 50 s (session 23:49:34 → 23:53:24; first log line 23:50:07, last 23:53:07) |
| Tokens (session record, all layers) | 2,175,048: 24,567 written, 1,899,619 read from cache, 250,796 written to cache, 66 new input |
| Tokens (seen by the CEO) | about 133 thousand |
| At list prices | $2.36 (on a subscription this is not billed separately; it comes out of your quota) |

**The watcher's record (`git worktree list`):**
```text
23:50:08  main            be76197 [master]
          desks/writer    be76197 [desk: writer]
23:51:45  main            8964f89 [master]
          desks/auditor   8964f89 [desk: auditor]
23:52:42  main            e8d1a5d [master]
```
The auditor's desk was opened from `8964f89`, so it saw the writer's merged text. The shift order worked.

**What did not work:** the writer opened its helper in the background and returned to the CEO before the helper had finished. The CEO noticed and continued the same writer (SendMessage); the writer waited for the helper and finished the job. The result was correct, but by luck.

**Fix:** a "wait rule" was added to the four workers that can take helpers and to the hiring template (no helper in the background, no returning to the CEO before the helper finishes). The CEO got a step to check the log for the worker's and the helper's `finish` lines before merging. On the auditor's suggestion, the approval file was split into "answer before sending / auditor's notes / texts to publish / internal notes".

## Round 2 · newsletter + Instagram + chalkboard poster (parallel shift)

**The job:** the newsletter and a chalkboard poster for the black-eyed beans. The newsletter and the poster do not wait on each other; the writer gives the Instagram post to a helper.

| | |
|---|---|
| Workers | 3: writer, illustrator, auditor |
| Helpers | 1: the writer's helper |
| Desks open at the same time | 2: writer and illustrator, both open at 23:55:33 |
| Parallel work | writer 23:55:52 → 23:57:13 (81 s), illustrator 23:56:00 → 23:56:56 (56 s), overlapping |
| Merges | 3, all without conflicts (`30eb337` writer, `a7c5e9a` illustrator, `6b4535c` auditor) |
| Auditor desk | opened at 23:57:42 from `a7c5e9a`, saw both merges |
| Waiting for the helper | helper finished 23:56:58, writer 23:57:13; no early return |
| Log | 22 lines |
| Auditor verdict | PASS, 5 findings (style and internal notes) |
| In approval | one file, with a single list of 8 questions at the top |
| Sent out | 0 |
| Time | 5 min 2 s (session 23:54:53 → 23:59:55) |
| Tokens (session record, all layers) | 1,859,645: 31,207 written, 1,546,938 read from cache, 281,442 written to cache, 58 new input |
| Tokens (seen by the CEO) | about 134 thousand |
| At list prices | $2.57 |

**The watcher's record:**
```text
23:55:33  main               e8f385c [master]
          desks/illustrator  e8f385c [desk: illustrator]
          desks/writer       e8f385c [desk: writer]
23:57:33  main               a7c5e9a [master]
23:57:42  main               a7c5e9a [master]
          desks/auditor      a7c5e9a [desk: auditor]
23:59:06  main               6b4535c [master]
```

**Small issues that came up:**
1. The CEO wrote "4 files" in the illustrator's merge line; the right number is 2. It had counted by hand and included the writer's files. The CEO said so itself in its summary. **Fix:** CLAUDE.md now takes the file count from `git diff --shortstat HEAD^1 HEAD`. No new merge run was done after this fix.
2. On the poster, the "Thursday · Friday" text runs over the right edge of its frame (checked by opening the drawing in the browser). The auditor reads the drawing as text, so it could not see this. **Fix:** the illustrator got a text-width calculation and margin rule, the auditor a "visual check: the owner opens it and looks" line. These two rules were not run.
3. The helper wrote its output into the writer's folder instead of its own subfolder and used an unnumbered name in the log. It broke nothing and the merge was clean. Not fixed.

## Round 3 · a new worker with `hire`

**The job:** `hire` a translator (the answers to its questions were given in the message: Turkish to English, for tourists, no helpers), then have it translate round 2's Instagram post into English. It ran in round 2's repository, after the round 2 fixes were committed.

| | |
|---|---|
| Job post | The CEO wrote the translator's job description from the template and added a row to the staff table |
| `.claude/agents/<translator>.md` | **Could not be written.** In non-interactive mode Claude Code refused to write into the `.claude/` folder (the only permission denial in the session record) |
| What the CEO did | Wrote the description as a draft under the company folder, did not work around the permission, and told the owner the two ways forward (grant permission or copy the file) |
| How the translator was opened | As a `general-purpose` worker, with "read the draft first" at the top of the prompt. The auditor is on the staff, so it was opened directly by name |
| Desks and merges | 2 desks, 2 merges (`296db74` translator, `4090fb6` auditor), both removed |
| Log | 14 new lines |
| Auditor verdict | PASS, 4 findings (3 hashtags not in the source, a sign-up call to a Turkish newsletter, one explanation, one style suggestion) |
| In approval | one file, with a list of 4 questions |
| Time | 4 min 41 s (00:00:22 → 00:05:03) |
| Tokens (session record) | 2,074,091 · $1.93 at list prices |

**Result:** the `hire` flow and its fallback worked. In interactive use Claude Code may ask for permission to write into that folder; in this non-interactive test nobody was there to ask, so the write was refused. **Fix:** CLAUDE.md now says "tell your owner to approve if a permission prompt comes up; without permission, write it under `company/staff-drafts/` and use the general worker route". **Not tested:** whether a worker whose file is written under `.claude/agents/` can be opened directly by name in the same session.

## Lookout run · competitor radar (11 October 2026)

**Setup:** the package was copied into an empty folder and made a repository, and the demo company (Urla Table) was used. The CEO was again a separate `claude -p` session. These runs, too, used the Turkish version (`gozcu`, `bin/gozcu_tara.py`); the English scanner `bin/lookout_scan.py` was tested on its own (see the end of this section). Permissions: file edits, git, the log script and Python (`python`, `python3`, `py`). The sources were real and public: the YouTube feeds of 3 food channels (Yemek.com, Nefis Yemek Tarifleri, Refika's Kitchen), the Yemek.com site, Google News searches for "Urla restoran" and "Urla gastronomi", Reddit r/izmir. No key was used.

| | 1. `watch my competitors` | 2. `radar` (with the shift script) | 3. add two sources + `radar` | 4. add a manual link + `radar` |
|---|---|---|---|---|
| How it was given | Answers to the five questions in the message | `bin/radar_vardiya.cmd` run by hand | "add these to the list, then radar" | "add this link with an 'opportunity' note, then radar" |
| Time | 3 min 32 s | 3 min 28 s | 3 min 25 s | 6 min 23 s |
| Sources (read / total) | 7 / 7 | 7 / 7 | 9 / 9 | 10 / 10 |
| Items pulled (last 4 days) | 30 | 30 | 49 | 50 |
| Workers | lookout | lookout | lookout | lookout, auditor |
| Opportunity drafts | 0 | 0 | 0 | 1 (Instagram), auditor PASS, 4 style and timing findings |
| Report length | 63 lines, 1,023 words | 66 lines, 1,231 words | 72 lines, 1,308 words | 88 lines, 1,359 words |
| Log lines | 8 | 7 | 7 | 13 |
| Desks and merges | 1 / 1, no conflict | 1 / 1 | 1 / 1 | 2 / 2 |
| Tokens (session record, CEO and workers) | 1,489,570 | 1,216,553 | 1,516,584 | 2,091,720 |
| Tokens (seen by the CEO) | about 61k | about 68k | not measured | not measured |
| Amount at list price | $1.46 | not printed (the shift script prints no amount) | $1.58 | $2.20 |
| Sent out | 0 | 0 | 0 | 0 |

The scanner itself took 3.4 seconds for 7 sources. The rest of the run time is the lookout writing the report, plus desks and merges.

**What worked:**
- Finding the `channelId` from a YouTube channel URL: all 3 channels were found and their feed addresses were written to the list.
- Traction data: on YouTube items, views, likes, views per hour and the ratio to the channel median went into the report as they were. On news, site and Reddit items the lookout wrote "no view data" every time and made up no numbers.
- Growth between two scans: in run 2 the growth of every video since the previous scan was calculated (for example, a short went from 4,500 to 4,816 in 5 minutes). The gap was under 30 minutes, so hourly growth was not calculated; the lookout said so in the report.
- Opportunity rule: in run 3 one CZN Burak video was fresh and 2.06 times the channel median, but had nothing to do with food. The lookout did not count it, writing "gaining but does not fit us". In run 4 the news link the owner added with an "opportunity" note (a grape harvest festival in Izmir, in 4 different outlets) was read and the lookout wrote an Instagram draft for Saturday breakfast. Menu, phone and the Urla vineyard link were not on the card, so they became `[ASK THE OWNER]`. The auditor audited only the draft, and its verdict went to the top of the approval file.
- Shift: `bin/radar_vardiya.cmd` was run by hand and ran from start to finish with the narrow permissions (file edits, git, log, Python). The Task Scheduler line (`schtasks /create ... /d MON,THU /st 08:30`) was created, `schtasks /query` showed "Days: MON, THU, Next Run Time: 12.10.2026 08:30", and then it was deleted.
- Manual links: the text and date of an X post and the caption of a TikTok video were read without a key. An Instagram link was not read and the owner's note was used. A domain that does not exist was `SKIPPED` and the scan carried on.

**What did not work, or was fixed:**
1. In run 1 the CEO wrote the lookout's hire to the log twice (`watch my competitors` and the first `radar`). **Fix:** CLAUDE.md now skips the second `hire` line on the first scan. Runs 2-4 were their own `radar` jobs, so one line each is correct.
2. A second scan on the same day could not see the previous scan (today's file was left out). **Fix:** the scanner reads the previous file before writing over it. Run 2 ran with this fix.
3. In back-to-back tries Reddit once returned `HTTP 429` (too many requests) and YouTube once dropped the connection. **Fix:** on temporary errors, wait 5 seconds and try once more. The scan after the fix read 7/7. After dozens of tries within minutes, Reddit returned `429` again even after the retry; then only Reddit is skipped and the report comes out with the other sources. Two shifts a week never get near that rate.
4. In run 2 the lookout wrote its own Python command to inspect the raw file; the Windows console failed on an emoji and the lookout recovered. **Fix:** the lookout reads the raw file with the Read tool. No run was made after this rule.
5. A Google News link added by hand only gave the title "Google News". **Fix:** such links count as unreadable and the owner is told to paste the article's own address.
6. The "Urla restoran" and "Urla gastronomi" searches brought off-topic news (cigarette sales, London). The lookout said so in both reports and suggested narrower words. Search quality depends on the words the owner picks; the script cannot fix that.
7. YouTube feed numbers lag: one video's views looked 57 lower after 5 minutes. The lookout called it counter lag; the job description now says "draw no momentum conclusion from negative or zero growth".

**English scanner:** `bin/lookout_scan.py` was run on its own twice with `company/radar/sources.example.md` as the list: 7/7 sources, 29 items, the second run saw the first as the previous scan. A later rerun read 6/7 (Reddit `429`, see item 3). `--find-channel` and `--try` were tried too.

**Not tested in the lookout run:**
- Task Scheduler starting the task at its own time (the task was created and deleted; the script was run by hand).
- Mac: `bin/radar_shift.sh` only passed a syntax check; cron and launchd were not tried.
- Asking the questions one at a time in the chat (the answers were in the message), and the path for a computer without Python.
- A FIX round on an opportunity draft (the auditor said PASS).
- The English package (`agent-company`) run with Claude.
- Hourly growth over a real shift gap (3-4 days); the test scans were 4-6 minutes apart.

## Not tested

- The question-and-answer part of `setup` (tried with the demo company; the step that turns the folder into a repository was done by hand).
- The `shift`, `approve` and `reject` commands.
- A FIX round: the auditor said PASS in both runs, so the fix round never ran.
- Stopping at the token ceiling and the `stopped` event when a limit is passed.
- The composer and researcher roles.
- The whole shift as a workflow ("ultracode").
- The `AGENTS.md` route (Codex and other tools) and Mac.

## Two facts you should know

- **Token count:** the CEO adds up the number it sees when workers return (about 133-134 thousand in both rounds). The real total in the session record was 1.86-2.18 million. Most of the gap is text re-read from the cache; the helper's usage is not visible to the CEO either. That is why the token ceiling applies to the number the CEO sees, and CLAUDE.md has it call that number "visible".
- **Every job means several sessions:** a small newsletter job took 4-5 minutes and about 2 million tokens with two or three workers. You do not need the company for a single post.
