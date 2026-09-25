# Test result · 25 September 2026

The system was run on real LinkedIn with the fictional Elif Aydın CV that ships with the setup and the `demo: yes` setting. No human started the run; `tools/daily_run.py` was run the way the scheduler would call it, and it used the open LinkedIn session in Chrome. Company names are not written here; the listings were real and public. The test ran on the Turkish version of this system, so the searches used the Turkish role titles; the steps and rules are the same.

## Numbers

| | |
|---|---|
| Roles searched | 3 (Digital Marketing Specialist · Performance Marketing Specialist · Growth Marketing Specialist) |
| Search results (Easy Apply + last 24 hours) | 31 + 4 + 19 |
| New listings after deduplication | 22 |
| Detail pages read | 8 |
| Rejected | 15 (5 red line: agency and internship · 5 on score · 1 location · 4 from list data) |
| Passed the threshold (70) | 2 (75 and 74 points) |
| Folders prepared | 2 (listing, match, tailored CV and PDF, cover letter, answers, preview) |
| Forms that reached the "Review" screen | 2 |
| Submitted | 0 |
| Drafts left in the account | 0 (Jobs tracker → Drafts: no matches) |
| Left for tomorrow without scoring | 7 |
| Duration | 27 minutes (10:58 → 11:25) |

## Behaviors that worked correctly

1. **The red line came before the score.** The listing with the highest role overlap of the run (Google Ads, Meta Ads, GA4, Looker Studio, Kartal and hybrid; everything matched) was rejected without scoring because the listing text mentioned "agency culture" and "agency experience". `you/TARGET.md` said "no agencies".
2. **The score breakdown was written item by item.** In the 75-point listing, the degree mismatch (the listing asks for Statistics or Industrial Engineering, the CV says Business Administration) cost 8 points under mandatory requirements and was also written as a "weakest gap".
3. **Not a single made-up line was added to the CV.** In the tailored CV the summary paragraph was rewritten for the listing, the Klaviyo flow and A/B test bullets moved to the top, and the ad budget bullet moved down. Experience, dates and numbers are identical to `you/CV.md`.
4. **The cover letter was tied to a concrete item in the listing.** The first sentence took two separate items from the listing ("building customer journeys" and "continuous A/B testing") and matched them with two measured results from the CV. 148 words, no stock phrases.
5. **It did not make up an answer it did not know; it asked.** Six "ASK OWNER" lines came out: the listing's "must live on the Anatolian side" requirement (the CV had no district), a conflict on years of experience (the CV says 5 years 3 months, the target file said 4 years; the agent went with the CV and reported the conflict), the marketing automation tool, SQL, an exception on office location, and salary relative to the title.
6. **It filled in the form to the last step and did not submit.** In a three-step form, the additional questions (commute, hybrid, net salary) were filled in from `you/TARGET.md`; the "Review" screen was saved to `preview.md`; the "Submit application" button was not pressed; "Discard" was chosen when closing. After the run, the Drafts tab in LinkedIn's own Jobs tracker is empty, and the newest entry in the Applied tab is from three months ago.
7. **It reported its own decision.** In demo mode it did not upload the fictional CV to the form; the reason is that a resume uploaded to LinkedIn stays permanently in the account. This decision was later turned into a rule (`CLAUDE.md`, demo mode).
8. **The cap was reached, the rest was left for tomorrow.** The daily cap was 2 in this run; after the two listings that passed the threshold, 7 listings were written to the table as `candidate`, and tomorrow's run looks at them first.

## Measured weaknesses

- **The listing detail panel is slow.** The `/jobs/view/<id>/` address did not load the text at all for some listings; it took clicking the card on the search page and waiting 8-10 seconds. Reading one listing text took 4-5 rounds, which is why only 8 of the 22 listings could be read. This path and the "no more than three attempts" rule were added to step 2 of `CLAUDE.md`.
- **The IDs of two listings in the list could not be captured.** Two listings seen while scrolling, whose `job_id` could not be taken, could not be written to the table; they will show up again the next day, no harm done.
- **Single-step forms do not surface the conflict.** The second listing's form had no additional questions; the "fully on-site, European side" mismatch never showed up in the form. The system caught it in scoring (location item 2/15) and in the "ASK OWNER" list, not in the form.
- **LinkedIn is retiring classic job search.** The search page shows a notice that classic job search is being phased out gradually from September. The address parameters worked in this run. If it goes away, step 1 falls back to searching through the interface (written in `CLAUDE.md`), and a new test is needed.

## Not tested

- Real submission with `submit: yes`. It could not be submitted with the demo person; do the first few runs with your own CV on `submit: no`, then turn it on.
- Uploading a real CV file to the form (`file_upload`). Deliberately skipped in demo mode; the tool exists and the rule is written, but it was not seen in a run.
- A listing that redirects to the company site ("external"). None came up in this run.
- Closing the form with "question pending". It was not triggered because the questions could be answered from the target file.
- The scheduler triggering by itself. `tools/setup.py` installs the task; in this test the run was started by hand.
- The interview rehearsal (`rehearse`) command.
