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

---

# Example output · the lookout, competitor radar

> Everything in this section is the real output of the lookout test run (run 4, 11 Oct 2026). The run used the Turkish version of this system (`ajan-sirketi`), so the log and the report were produced in Turkish; they are translated into English here. The "What they did" list is shortened (Reddit and two news items left out); nothing else is changed. The company is fictional. The sources are real and public; none of them is a competitor of Urla Table, they were picked for the demo. Folder paths specific to the test computer and long Google News links are shortened.

## The job given

```text
Add a link to the list by hand: https://www.haberege.com.tr/izmirde-buyuk-efes-bag-bozumu-festivali-bugun-basliyor-1791633184-4310742
note: 'opportunity: grape harvest week in Izmir, let's tie it to Urla's vineyards and remind people of Saturday breakfast'. Then radar.
```

## The lookout's list (`company/radar/sources.md`)

```text
days: 4
python: python
opportunity_channel: Instagram

| Name | Type | Address | Note |
|---|---|---|---|
| Yemek.com · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCWA2nh0yrIMC6uG0hfbucRQ | @yemekcom |
| Nefis Yemek Tarifleri · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCeh3XQszWO6lLdKz_SZmm1Q | @nefisyemektarifleri |
| Refika's Kitchen · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCO3MaQR-Vh6cgBZRlD44jWg | @refikaninmutfagi |
| CZN Burak · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCUcfej7lPDoeqTlferD2mcw | @CZNBurak |
| Yemek.com · site | site | https://yemek.com | feed: https://yemek.com/rss.xml |
| News: Urla restaurant | news | Urla restoran | Google News search |
| News: Urla gastronomy | news | Urla gastronomi | Google News search |
| News: Izmir gastronomy | news | İzmir gastronomi | Google News search |
| Reddit: r/izmir | reddit | r/izmir | eating out questions in the city |
| Haber Ege: Grape Harvest Festival | link | https://www.haberege.com.tr/izmirde-buyuk-efes-bag-bozumu-festivali-bugun-basliyor-1791633184-4310742 | opportunity: grape harvest week in Izmir... |
```

## Log (13 lines from this run)

```json
{"t":"2026-10-11T19:47:37+03:00","who":"ceo","event":"hire","detail":"lookout: radar-2026-10-11 (fourth scan)"}
{"t":"2026-10-11T19:47:51+03:00","who":"ceo","event":"desk","detail":"lookout: company/desks/lookout (desk/radar-2026-10-11-lookout)"}
{"t":"2026-10-11T19:48:13+03:00","who":"lookout","event":"start","detail":"radar-2026-10-11"}
{"t":"2026-10-11T19:48:13+03:00","who":"lookout","event":"desk","detail":".../company/desks/lookout"}
{"t":"2026-10-11T19:50:32+03:00","who":"lookout","event":"finish","detail":"10/10 sources, 50 items, 1 draft: company/approval/radar-2026-10-11.md"}
{"t":"2026-10-11T19:51:01+03:00","who":"ceo","event":"merge","detail":"lookout: 2 files came into the main branch"}
{"t":"2026-10-11T19:51:02+03:00","who":"ceo","event":"hire","detail":"auditor: radar-2026-10-11 opportunity draft"}
{"t":"2026-10-11T19:51:02+03:00","who":"ceo","event":"desk","detail":"auditor: company/desks/auditor (desk/radar-2026-10-11-auditor)"}
{"t":"2026-10-11T19:51:18+03:00","who":"auditor","event":"start","detail":"radar-2026-10-11 opportunity draft audit"}
{"t":"2026-10-11T19:51:19+03:00","who":"auditor","event":"desk","detail":".../company/desks/auditor"}
{"t":"2026-10-11T19:52:13+03:00","who":"auditor","event":"finish","detail":"verdict: PASS, 4 findings (style); company/outputs/radar-2026-10-11/auditor/audit.md"}
{"t":"2026-10-11T19:52:53+03:00","who":"ceo","event":"merge","detail":"auditor: 1 file came into the main branch"}
{"t":"2026-10-11T19:52:54+03:00","who":"ceo","event":"approval_request","detail":"company/approval/radar-2026-10-11.md"}
```

## Approval file (`company/approval/radar-2026-10-11.md`)

> # Waiting for approval: Competitor radar · 2026-10-11
> - Status: WAITING FOR APPROVAL
> - Prepared by: lookout, auditor (no helper)
> - Auditor's verdict: PASS (only the opportunity draft was audited; 4 style and timing notes below)
> - Where it goes: the report itself is an internal document. Opportunity drafts are for Instagram (your owner does the sending).
>
> ## To answer before sending
> - Timing note: in the article the festival runs only 10-11 October (two days), at Swissôtel Büyük Efes Izmir, Oval Garden. Today is its last day. "Grape harvest week" from the owner's note is not in the article. So the draft mentions the festival in the past tense and reminds people of next Saturday (17 October). Is the draft fine like this? (Draft 1)
> - [ASK THE OWNER: Is there a concrete link between the vineyards of Urla and your table (grapes, molasses, an ingredient from a vineyard or a producer)? It is not on the company card. If not, this sentence comes out.] (Draft 1)
> - [ASK THE OWNER: Is Saturday breakfast on 17 October open, still 09:00-13:00? The card has it under "this week's information".] (Draft 1)
> - [ASK THE OWNER: What is on the table at Saturday breakfast? The card has no breakfast menu.] (Draft 1)
> - [ASK THE OWNER: Which phone number should go in the post for bookings?] (Draft 1, part 3 idea 1)
> - [ASK THE OWNER: Are the Çeşme black-eyed beans on Thursday and Friday this week too, and in which dish?] (Part 3, idea 2)
>
> ## Auditor's notes
> Verdict PASS. No red line broken and no unsourced number; the hours, phone bookings and closed on Sunday are on the company card, the festival dates and venue match the article.
> - The Urla vineyard question is worded differently in two places. To clarify: if there is no link, the sentence that comes out is "Our minds went to the vineyards too." The first sentence that stays is "Grape harvest was the talk of Izmir at the weekend."
> - If the answer is "no link", the grape harvest hook is weak; the post becomes a plain Saturday breakfast reminder.
> - "At the weekend" means last weekend (10-11 October). The post should go out by 13 October at the latest, or the first sentence will be misread.
> - The closing ("plan your weekend around Saturday") is an imperative, a little sharp for the friendly voice; it could be softened.
>
> ## Scan
> 10 of 10 sources read, 50 items in the last 4 days. Previous scan: company/radar/raw-2026-10-11.json (today's 19:42 local version; overwritten under the same name, the third version is in the git history, commit dce10d8).
>
> Scan time: 2026-10-11 19:48 (local). About 6.5 minutes between the two scans. The gap is under 30 minutes, so hourly growth was not calculated and no momentum conclusion was drawn from `growth_since_last_scan`. CZN Burak's videos showed 0 growth: YouTube counter lag. The newly added manual link (Haber Ege) was read.
>
> ## 1. What they did
> - **Yemek.com · YouTube** · 2026-10-11 16:30 · [Olive and Halloumi Bun](https://www.youtube.com/shorts/ezbygMmCwDU) · 5,226 views, 270 likes, 1,582.6 views per hour, 0.19 of the channel median (3.3 hours ago)
> - **Yemek.com · YouTube** · 2026-10-11 11:33 · [How to Cook Basmati Rice](https://www.youtube.com/shorts/e_xeGSE8H-Y) · 15,161 views, 398 likes, 1,837.8 per hour, 0.54 of the median (8.2 hours ago)
> - **Nefis Yemek Tarifleri · YouTube** · 2026-10-08 14:44 · [Yogurt Cake Recipe](https://www.youtube.com/watch?v=kRpV_E4l9js) · 70,020 views, 895 likes, 908.5 per hour, 1.16 of the median (77.1 hours ago)
> - **Refika's Kitchen · YouTube** · no video in the last 4 days.
> - **Yemek.com · site** · 2026-10-11 08:30 · [Menu of the Day, 11 October 2026](https://yemek.com/11-ekim-2026-gunun-menusu/) · no view data
> - **CZN Burak · YouTube** · 2026-10-10 13:37 · [Dubai Vs Hasbulla UFC Dagestan](https://www.youtube.com/shorts/gyjejyGWEww) · 233,827 views, 5,292 likes, 7,746.8 per hour, 2.06 of the median (30.2 hours ago)
> - **News: Izmir gastronomy** · 2026-10-10 22:32 · [Büyük Efes Grape Harvest Festival starts today](<Google News link>) (basingazetesi.net) · no view data; the same story in 4 different outlets
> - **Haber Ege: Grape Harvest Festival** (manual) · 2026-10-10 14:53 · [Büyük Efes Grape Harvest Festival starts today in Izmir](https://www.haberege.com.tr/izmirde-buyuk-efes-bag-bozumu-festivali-bugun-basliyor-1791633184-4310742) · no view data. From the article: 10-11 October, Swissôtel Büyük Efes Izmir Oval Garden, vineyard producers, food stops, music. Owner's note: "opportunity".
>
> **What took off:**
> 1. CZN Burak "Dubai Vs Hasbulla UFC Dagestan": 233,827 views, 7,746.8 per hour, 2.06 of the channel median (30.2 hours ago). Not food content.
> 2. Büyük Efes Grape Harvest Festival: the same story in 4 different outlets, 21.3 to 28.9 hours ago; the owner added it by hand as an "opportunity".
> 3. Yemek.com "Çat Kapı 2026" episode: 57,589 views, 2.04 of the median. But 49.8 hours ago, above the 48-hour limit.
>
> ## 2. The angle that fits us
> - **Grape Harvest Festival:** the card's audience includes "people from Izmir who come at the weekend". Vineyards and food were the talk of Izmir this weekend; a hook to remind people coming to Urla at the weekend of Saturday breakfast (09:00-13:00, phone bookings). Channel: Instagram. Limit: the festival ends today, and "Urla's vineyards" is not on the card, so the owner was asked.
> - **CZN Burak Hasbulla video:** gaining, but no link to food, Urla or our audience. No angle can be written, so it is not an opportunity.
> - **GastroShow 2026** (two outlets): nothing on the card to connect it to.
>
> ## 3. What we should make today
> 1. **Saturday breakfast reminder with the grape harvest hook** · channel: Instagram · based on: Büyük Efes Grape Harvest Festival (4 outlets, owner's note) · first line: "Grape harvest was the talk of Izmir at the weekend." To post on Monday 12 October. Draft 1 below.
> 2. **Thursday black-eyed bean board** · channel: the chalkboard in the restaurant · based on: Yemek.com black-eyed bean salad (22,997 views) and the Çeşme beans on the card · first line: "Fresh black-eyed beans from Çeşme on Thursday and Friday." Written on Thursday 15 October morning, if the beans come that week too.
> 3. **Newsletter box: "For those coming to Urla on Saturday"** · channel: weekly email newsletter · based on: the Izmir day-trip news story · first line: "If you are coming to Urla on Saturday, breakfast is 09:00 to 13:00, and we are closed on Sunday."
>
> ## Opportunity drafts
> ### Draft 1: Instagram · Büyük Efes Grape Harvest Festival
> - Why now: the festival ran on 10-11 October, the story is in 4 different outlets (21.3 to 28.9 hours ago), the owner marked it as an "opportunity" by hand. The festival ends today, so the text is in the past tense and aims at Saturday breakfast on 17 October.
> - Channel: Instagram
>
> Grape harvest was the talk of Izmir at the weekend. Our minds went to the vineyards too. [ASK THE OWNER: Is there a concrete link between the vineyards of Urla and your table? If so, which vineyard or producer, which ingredient? If not, keep only the first sentence instead of these two.]
>
> We'll be waiting for you at breakfast this Saturday. We're open 09:00 to 13:00. [ASK THE OWNER: Same hours on 17 October?]
>
> What's on the table: [ASK THE OWNER: breakfast menu]
>
> We take bookings by phone: [ASK THE OWNER: phone number]. We're closed on Sunday, so plan your weekend around Saturday.
>
> ## Internal notes (not published)
> - Raw file: company/radar/raw-2026-10-11.json
> - Audit report: company/outputs/radar-2026-10-11/auditor/audit.md
> - Sources that could not be read: none.
> - The festival and hotel names are not in the draft: the festival will be over, and the hotel is not our business. Price, menu and phone are not on the card, so they were not written.
> - Yemek.com Çat Kapı (2.04 of the median) was 1.8 hours over the 48-hour limit, so it was not counted as an opportunity.

## What this example shows

- **No made-up numbers:** views exist only on YouTube items. Every news, site and link item says "no view data".
- **The opportunity rule worked:** CZN Burak's video was fresh and 2.06 times the channel median, but had no angle that connects to the company; it was not counted. The Çat Kapı episode was 1.8 hours over the 48-hour limit, so it was not counted either.
- **The draft stayed on the card:** breakfast hours, phone bookings and closed on Sunday come from the company card. Menu, phone number and the Urla vineyard link were not on the card, so they became `[ASK THE OWNER]` and were gathered at the top of the list.
- **The auditor looked only at the draft:** the rest of the report is an internal document. The auditor said PASS, added the timing note ("should go out by 13 October at the latest") and did not rewrite the text.
