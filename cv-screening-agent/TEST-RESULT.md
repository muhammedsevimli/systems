# Test result · 27 September 2026

The system was run on this computer (Windows 11, Python 3.11) with the fictional Derin Kozmetik listing that ships with the setup (`demo: yes`) and the 12 fictional CVs in `candidates/samples/`. The test ran on the Turkish version of this system, so the CVs and the listing were in Turkish; the steps, the scoring and the rules are the same, and the samples here are their English translations. Two separate screening runs were done:

1. **Full flow (daily run, folder mode).** The Claude session that built the system ran in the agent role: it copied the CVs, read them with the CV reading tool, scored them, and wrote `candidates.csv`, the report, 5 invite drafts and 6 rejection drafts.
2. **Independent `screen` run.** The session that wrote the sample CVs knew what should happen to each candidate, so its scoring cannot count as neutral. To measure this, `claude -p "screen"` ran as a separate session on a clean copy of the system; that session saw only `CLAUDE.md`, `you/JOB.md` and the CVs.

Candidate mode (`screen me`) was run separately with two listings.

## Numbers (full flow)

| | |
|---|---|
| CVs read | 12 (5 md, 3 txt, 3 pdf, 1 docx) |
| Unreadable | 0 |
| Rejected by a red line | 2 (Irmak Şahin: agency experience only · Kaan Uysal: İzmir, not relocating, fully remote only) |
| Rejected by the threshold (70) | 4 (Can Demir 68 · Hakan Önal 53 · Zeynep Er 50 · Ayşe Nur Polat 39) |
| Above the threshold | 6 |
| Shortlist | 5: Burak Yazıcı 96 · Selin Karaca 91 · Deniz Aksoy 79 · Oya Kılıç 76 (question pending) · Mert Oral 74 |
| Backup | 1 (Ece Tunç 70) |
| ASK THE OWNER | 3 |
| Invite drafts | 5 (Oya Kılıç's is waiting for the ASK THE OWNER answer) |
| Rejection drafts | 6 |
| Emails sent | 0 |
| Time | full flow 3 minutes (23:47 → 23:50) · independent `screen` 4 minutes 18 seconds (23:50:15 → 23:54:33) |

**Fields not scored:** age, marital status, photo (present in 2 CVs, not taken into account) · military service status (present in 1 CV, not taken into account). One of them is a strong candidate (Burak Yazıcı, PDF), the other a mid-range one (Deniz Aksoy). Both made the shortlist; these fields appear in no score item, no reason, no candidate row of the report and no draft. The independent run wrote the same line on its own ("present in 3 CVs, not taken into account").

**ASK THE OWNER questions:**
1. Oya Kılıç: the summary says "fluent English", the languages section "B1". With the reading in her favor she scored 76; if B1 is right she drops to 68 and Ece Tunç from the backups takes her place. The same CV shows two full-time jobs running as "present" in the same period.
2. Is the English B2 must-have really required? Can Demir scored 68, 2 points below the threshold, and one of his gaps is English.
3. Is there a minimum time for "has worked on the brand side"? The listing gives no length.

## Behaviors that worked

1. **PDF, Word and text were read on the same line.** 3 PDFs (printed with headless Chrome), 1 Word file (.docx) and 8 md/txt files were converted to text with the CV reading tool; the "Age · Marital status · Photo" line in the PDF also came through as text, so the agent saw this information and still did not score it.
2. **The red line came before the score.** Irmak Şahin's CV was one of the highest in the pool on role overlap (cosmetics, Klaviyo, TikTok Ads, SQL, 3 million TL a month); both of her jobs were at agencies, so she was rejected without being scored. Kaan Uysal was rejected because he wrote "I have no plans to relocate"; no rejection was made on a guess.
3. **Years of experience were calculated from the dates.** Ayşe Nur Polat's 4-month internship was not counted (11 months). Oya Kılıç's two overlapping jobs were counted once (3 years 8 months). The "for X years" sentences in the summaries did not go into the score.
4. **A contradiction did not reject, it became a question.** Oya Kılıç stayed on the shortlist with the reading in her favor, her status became `question-pending`, and "BEFORE SENDING: ASK THE OWNER 1" was written at the top of her invite draft.
5. **No reason in the rejection emails.** The 6 rejection drafts are the same polite text; even the email to Kaan, rejected by a red line, does not mention location. The invites contain no score, rank or other candidates; the greeting uses the full name, and no gender was inferred from a name.
6. **Deduplication.** After the run, the CV reading tool was run on the inbox again: all 12 of 12 files "read", 0 new CVs.
7. **The independent run made the same decisions.** The 5 candidates on the shortlist are the same, in the same order (Burak, Selin, Deniz, Oya, Mert). The two red lines are the same, the bottom three rejections are the same. The `screen` command followed its rule and wrote no drafts. It applied the demo rule on its own: the inbox was empty, it copied the samples, and it did not open Chrome.
8. **The fair screening refusal is written down.** The sample dialogue in `CLAUDE.md` shows the agent refusing "make under 30 a red line" during `setup` and proposing the experience band instead.

## Candidate mode (`screen me`)

The fictional Elif Aydın CV (the demo person of the Job Application Agent) was read with the CV reading tool and scored against two listings:

- **Derin Kozmetik (the published text of the demo listing): 98/100, would not be rejected.** The report found the single serious risk: the summary says "for four years", the dates say 5 years; the hiring side's system flags this as a contradiction. The SMS flow the listing asks for is not in the CV (1 point). Strengths: the Klaviyo cart abandonment and repeat purchase flow (a one-to-one match with the listing), the same budget scale, influencer measurement and A/B testing.
- **Lila Moda, Senior CRM Specialist (a fictional listing pasted into the chat): would be rejected regardless of score.** The listing says "at least 3 years of experience with Insider is required", and Insider is not in the CV. Without the line she would score 78. The "for four years" sentence could drop her out of the 5-8 year band.
- Both reports have "what your CV is missing" in two separate lists: things she has that do not show (how to write them so they show) and things she really does not have (never written into the CV). Not a single line suggests writing experience that does not exist.

## Measured weaknesses

- **Scores move ±5 from run to run.** On the same CVs the independent run gave Selin 95 (91), Deniz 83 (79), Oya 81 (76), Mert 75 (74), Ece 74 (70), Can 70 (68), Zeynep 55 (50), Hakan 49 (53), Ayşe Nur 40 (39). The difference is largest in the role item (the only item that needs judgment). The result: **Can Demir was rejected with 68 in one run and went to the backups with 70 in the other.** Decisions within two or three points of the threshold are not final. That is why the report puts these candidates on ASK THE OWNER and the rejection email waits for the next run.
- **For Oya Kılıç, the outcome of the contradiction changed between runs.** In the full flow the B1 reading takes her below the threshold (68); in the independent run it does not (73). Both runs asked the right question and weighed the answer differently.
- **A must-have does not act as a rejection gate, it only lowers the score.** The independent run wrote this to ASK THE OWNER on its own: Mert Oral is on the shortlist without ever having built a CRM flow. By design each missing one costs 8 points; if the owner says "anyone missing it should be rejected", that must-have becomes a red line.
- **Em dash.** The independent run's report had 29 em dashes. A writing rule was added to the Limits section of `CLAUDE.md`; it was not run again after the rule.

## Tool tests

| Tool | Test | Result |
|---|---|---|
| CV reading tool | 3 PDF, 1 DOCX, 5 MD, 3 TXT | 12/12 read |
| CV reading tool | scanned (empty) PDF, old .doc, broken .docx | all three gave a clear "UNREADABLE" message, exit code 3 |
| CV reading tool | as if pypdf and pdfminer were missing | "Run this: py -m pip install pypdf" |
| CV reading tool, list mode | after the run | 12/12 "read" (with sha and file name) |
| Scheduler setup | Windows Task Scheduler | the task was installed, next run 28.09.2026 09:00, status Ready; removed with the remove flag, the query came back empty |
| Runner, dry run | print the command | in folder + demo mode, `claude -p ... "daily run"` without Chrome |
| Cleanup | on a separate copy | 26 files listed in dry mode; 26 files deleted with the confirm flag, `candidates.csv` back to its header, the 12 sample CVs and `you/JOB.md` kept; the second run said "No personal data to delete" |
| 4 Python files | `ast.parse` syntax | passed |

For the English port, the four tools in `tools/` were checked again: `ast.parse` passed on all four, `tools/read_cv.py` read all 12 English samples (including the 3 PDFs and the Word file), `tools/daily_run.py --dry-run` printed the command, and `tools/cleanup.py` listed nothing to delete on the clean folder.

## Not tested

- **The Gmail label path** (`source: gmail`): the label search with Chrome, moving the attachments from the Downloads folder into `candidates/inbox/`. This path does not exist in demo mode; the rule is written, it was not seen in a run.
- **Real email sending** (`send: yes`): composing, replying and the "Message sent" confirmation in Gmail. Sending is off in demo mode. Holding the rejection email until the next run was not seen with a real second run either.
- **The scheduler's own trigger.** The setup tool installed and removed the task; the task was not seen running by itself at 09:00. The runner did not run with a real `claude -p` call (its command was checked with the dry run; the independent `screen` run used the same `claude -p` path by hand).
- **The `setup` flow itself**: reading a listing link with Chrome, asking the questions in chat, refusing "under 30" in a real conversation. The rule and the sample dialogue are written; a live conversation was not run.
- **The `inspect`, `invite`, `reject`, `status` commands on their own.** The invite and rejection drafts were written inside the full flow; the commands were not called one by one.
- **The macOS (launchd) and Linux (cron) schedulers.** Tried only on Windows.
- **Real CVs.** All the CVs are fictional and cleanly formatted. In real life the text order can break in PDFs with tables, two columns or images; the CV reading tool reads them, but if the order gets mixed up, the scoring is affected.
