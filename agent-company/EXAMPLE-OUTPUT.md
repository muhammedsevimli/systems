# Example output · Urla Table, weekly newsletter

> Everything in this file is the real output of a test run (round 1, 10 Oct 2026). The run used the Turkish version of this system (`ajan-sirketi`), so the log and the texts were produced in Turkish; they are translated into English here, nothing else is changed. The company is fictional: it has nothing to do with any real business. Folder paths specific to the test computer are shortened.

## The job given

```text
Write this week's email newsletter for Urla Table.
The writer writes the main newsletter text itself and gives a short Instagram post announcing
the newsletter to a helper (1 helper allowance in this job).
```

## The CEO's job description (`company/jobs/newsletter-week-41.md`, shortened)

**Finished state:** Urla Table's email newsletter for this week (with two subject line options) and a short Instagram post announcing it; both in the company card's voice, using only the card's information, through the auditor and sitting in the approval folder.

| # | Need | Who |
|---|---|---|
| 1 | Main text of the email newsletter (including two subject line options) | writer |
| 2 | Short Instagram post announcing the newsletter | the writer's helper |
| 3 | Audit report: PASS / FIX | auditor |

**Shift order:** writer → writer's desk merged → auditor (sees the writer's output) → approval.

## Log (16 lines)

The Turkish log uses the field names `kim` / `olay` / `detay`; the English version uses `who` / `event` / `detail`. Shown here with the English names:

```json
{"t":"2026-10-10T23:50:07+03:00","who":"ceo","event":"hire","detail":"writer: newsletter main text (+1 helper allowance: Instagram announcement)"}
{"t":"2026-10-10T23:50:07+03:00","who":"ceo","event":"hire","detail":"auditor: newsletter-week-41 audit"}
{"t":"2026-10-10T23:50:08+03:00","who":"ceo","event":"desk","detail":"writer: desks/writer (desk/newsletter-week-41-writer)"}
{"t":"2026-10-10T23:50:23+03:00","who":"writer","event":"start","detail":"newsletter-week-41"}
{"t":"2026-10-10T23:50:23+03:00","who":"writer","event":"desk","detail":".../desks/writer"}
{"t":"2026-10-10T23:50:28+03:00","who":"writer","event":"helper","detail":"helper-1: short Instagram post announcing the newsletter (instagram.md)"}
{"t":"2026-10-10T23:50:45+03:00","who":"writer-helper-1","event":"start","detail":"newsletter-week-41 instagram announcement"}
{"t":"2026-10-10T23:51:09+03:00","who":"writer-helper-1","event":"finish","detail":"outputs/newsletter-week-41/writer/helper-1/instagram.md"}
{"t":"2026-10-10T23:51:29+03:00","who":"writer","event":"finish","detail":"outputs/newsletter-week-41/writer/copy.md (newsletter + Instagram announcement), helper-1/instagram.md"}
{"t":"2026-10-10T23:51:45+03:00","who":"ceo","event":"merge","detail":"writer: 2 files came into the main branch"}
{"t":"2026-10-10T23:51:45+03:00","who":"ceo","event":"desk","detail":"auditor: desks/auditor (desk/newsletter-week-41-auditor)"}
{"t":"2026-10-10T23:51:57+03:00","who":"auditor","event":"start","detail":"newsletter-week-41 audit"}
{"t":"2026-10-10T23:51:57+03:00","who":"auditor","event":"desk","detail":".../desks/auditor"}
{"t":"2026-10-10T23:52:28+03:00","who":"auditor","event":"finish","detail":"verdict: PASS, 4 findings (outputs/newsletter-week-41/auditor/report.md)"}
{"t":"2026-10-10T23:52:42+03:00","who":"ceo","event":"merge","detail":"auditor: 1 file came into the main branch"}
{"t":"2026-10-10T23:53:07+03:00","who":"ceo","event":"approval_request","detail":"approval/2026-10-10-newsletter-week-41.md"}
```

The `shift` command turns this into:

| Worker | Desk | Started | Finished | Helpers | Status |
|---|---|---|---|---|---|
| writer | desks/writer | 23:50:23 | 23:51:29 | 1 | merged |
| writer-helper-1 | the writer's desk | 23:50:45 | 23:51:09 | - | finished |
| auditor | desks/auditor | 23:51:57 | 23:52:28 | 0 | merged |

Waiting for approval: `company/approval/2026-10-10-newsletter-week-41.md`

## The approval file

> # Waiting for approval: Urla Table weekly email newsletter, week 41
> - Status: WAITING FOR APPROVAL
> - Made by: writer (newsletter text), writer-helper-1 (Instagram announcement, reviewed by the writer), auditor
> - Auditor verdict: PASS (4 suggestions, notes below)
> - Where it goes: email newsletter + Instagram post (your owner sends it)
>
> ## Answer before sending
>
> 1. [ASK THE OWNER: What is the phone number for bookings and takeaway? Should it go into the newsletter and the Instagram post?]
> 2. [ASK THE OWNER: How are takeaway orders placed, by phone or some other way?]
> 3. [ASK THE OWNER: What address and whose name should go at the bottom of the newsletter?]
> 4. [ASK THE OWNER: Is the newsletter sign-up link in the Instagram bio?]
>
> ## Auditor's style suggestions (optional)
>
> - Newsletter, paragraph 2: the speed claim in "if you are after a **quick** plate at lunchtime" is not on the card. Suggestion: "if you are after a plate at lunchtime, our door is open."
> - Instagram, closing line: "We'll write again next week" belongs to the newsletter. Suggestion: just "See you at the table."
>
> ## 1. Email newsletter
>
> **Subject line option 1:** Çeşme black-eyed beans on Thursday and Friday
> **Subject line option 2:** This week's lunch menu and Saturday breakfast
>
> Hello,
>
> This week's lunch menu is the same Monday to Friday: lentil soup, olive-oil artichokes, oven-roasted vegetables and rice pudding for dessert. If you are after a quick plate at lunchtime, our door is open. We do takeaway too. [ASK THE OWNER: How are takeaway orders placed, by phone or some other way? Should the number go into the text?]
>
> What's new this week is black-eyed beans. Fresh beans are coming from Çeşme, and they will be on the table on Thursday and Friday. Only those two days, just so you know.
>
> Saturday breakfast is between 09:00 and 13:00. We take bookings by phone. If you are coming over from Izmir at the weekend, we suggest calling ahead. [ASK THE OWNER: What is the booking phone number?]
>
> We are closed on Sunday.
>
> We'll write again next week.
>
> Urla Table
> [ASK THE OWNER: What address and whose name should go at the bottom of the newsletter?]
>
> ## 2. Instagram post
>
> This week's newsletter is out. Here is what's happening in the kitchen this week, in short.
>
> Our lunch menu Monday to Friday: lentil soup, olive-oil artichokes, oven-roasted vegetables and rice pudding.
>
> What's new this week is black-eyed beans. Fresh from Çeşme, only on Thursday and Friday.
>
> Our Saturday breakfast runs 09:00 to 13:00. Give us a call to book a table. [ASK THE OWNER: Should the phone number go into the post, and if so, what is it?]
>
> We are closed on Sunday.
>
> Sign up to read the full newsletter: [ASK THE OWNER: Is the newsletter sign-up link in the bio?]
>
> We'll write again next week, see you at the table.
>
> #Urla #UrlaTable #Çeşme #blackeyedbeans #oliveoilartichokes
>
> ## Internal notes (not published) · shortened
>
> - Sources: all information comes from "This week" (lunch menu, Çeşme beans Thursday-Friday, Saturday breakfast 09:00-13:00, closed Sunday) and "Company" in `company/COMPANY.md`. No prices, campaigns, health claims or customer names.
> - Audit report: `company/outputs/newsletter-week-41/auditor/report.md`

## What this example shows

- **Nothing invented:** the company card had no phone number or address. The writer did not make one up; it put `[ASK THE OWNER]` in four places, and the CEO gathered them into one list at the top of the approval file.
- **The auditor decided and did not rewrite:** it flagged "quick plate" as a small claim that is not on the card and left the fix to the owner.
- **The helper is in the log:** the writer's helper never went through the CEO, yet the moment it was hired and the moment it finished are both in the log.
- **The desks merged:** the writer's desk was merged before the auditor started, which is why the auditor's desk could see the writer's text.
