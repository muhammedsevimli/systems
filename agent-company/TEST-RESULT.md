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
