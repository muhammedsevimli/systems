# Example output

Taken from the 27 September 2026 demo run. The listing and the 12 CVs are fictional (there is no company called Derin Kozmetik, and the candidates are not real people); the rest is as the agent wrote it. The demo run was done on the Turkish original of this system; the excerpts below are its English translation. The full report is produced in the `reports/2026-09-27.md` format; it holds candidate data, so it never goes into the repo.

## reports/2026-09-27.md (excerpt)

> **DEMO · Daily report · 27 September 2026**
> CVs read 12 (5 md, 3 txt, 3 pdf, 1 docx) · Unreadable 0 · Rejected by a red line 2 · Rejected by the threshold 4 · Above the threshold 6 · Shortlist 5 (1 question pending) · Backup 1 · Invite drafts 5 · Rejection drafts 6 · Sent 0 (demo)

**Shortlist**

| Rank | Candidate | Score | Why they were picked | Status |
|---|---|---|---|---|
| 1 | Burak Yazıcı | 96 | Ran ads and CRM together on the cosmetics side; Braze flows, influencer measurement and A/B tests match four of the listing's five job items one to one. | invite-ready |
| 2 | Selin Karaca | 91 | Does the same job in fashion e-commerce with measured results; raised the CRM share of revenue from 11 percent to 19 percent with Insider flows. | invite-ready |
| 3 | Deniz Aksoy | 79 | Has all four must-haves; ran ads, the GA4 setup and the email flow alone. Industry is tourism. | invite-ready |
| 4 | Oya Kılıç | 76 | Has ads and Klaviyo flow experience. English level contradicts itself within the CV, ASK THE OWNER 1. | question-pending |
| 5 | Mert Oral | 74 | Strong in Meta, Google and TikTok Ads, two years on the brand side. No CRM flow experience. | invite-ready |

**Rejected**

| Candidate | Score | Reason |
|---|---|---|
| Irmak Şahin | - | Red line 1: all experience on the agency side, no brand side experience. In the CV: "Five years on the agency side..." |
| Kaan Uysal | - | Red line 2: lives in İzmir, the CV says "I have no plans to relocate; I only apply for fully remote positions." The listing asks for 3 days a week in the office. |
| Can Demir | 68 | 2 points below the threshold. Two must-haves missing: has not built a CRM flow (email was a separate team), English A2. |
| Hakan Önal | 53 | 14 years of experience, outside the 3-6 year band; spent the last six years as a team manager. |
| Zeynep Er | 50 | Role is content and social media. The ad budget management and CRM flow must-haves are missing. |
| Ayşe Nur Polat | 39 | 11 months of full-time experience (internship not counted), band 3-6 years. |

> **Fields not scored:** age, marital status, photo (present in 2 CVs, not taken into account) · military service status (present in 1 CV, not taken into account).

**ASK THE OWNER**

1. **Oya Kılıç, English level.** The summary says "I have worked in multinational teams with fluent English", the languages section says "English (B1)". With the reading in her favor she scored 76 and is 4th on the shortlist. If B1 is right, a must-have is missing, the score drops to 68, she leaves the shortlist and Ece Tunç (70) takes her place. The same CV shows two full-time jobs running as "present" in the same period; if you call her in, ask about that too.
2. **Is the English B2 must-have really required?** Can Demir scored 68, 2 points below the threshold; one of his gaps is English (A2). If this must-have becomes a preference, Can scores 76 and makes the shortlist.
3. **Is there a minimum time for "has worked on the brand side"?** The listing gives no length. I applied the red line as "no brand side experience at all".

## invites/selin-karaca.md

```
To: selin.karaca@example.com
Subject: Derin Kozmetik · Marketing Specialist interview invitation
---
Hello Selin Karaca,

Thank you for applying for the Marketing Specialist (Performance and CRM) position at Derin Kozmetik. In your CV we saw that the welcome, cart abandonment and win-back flows you built on Insider raised the CRM channels' share of revenue from 11 percent to 19 percent. In this position, the same person will run both ads and CRM.

We would like to have a 45-minute video call (Google Meet) with you. In the call we will talk about your recent work, the team and the working arrangement (3 days a week at the Ataşehir office). If you reply to this email with a time that suits you next week on Tuesday or Thursday, between 10:00 and 12:00, we will send you the link.

Derin Kozmetik Human Resources
hr@derinkozmetik.example.com
```

*(The candidate is addressed by full name, with no "Mr." or "Ms.": the agent does not infer gender from a name. The score, the ranking and the other candidates are not in the email.)*

## rejections/kaan-uysal.md

```
To: kaan.uysal@example.com
Subject: Derin Kozmetik · Your Marketing Specialist application
---
Hello Kaan Uysal,

Thank you for applying for the Marketing Specialist (Performance and CRM) position at Derin Kozmetik and for sharing your CV with us. We have reviewed the applications and decided to move forward with other candidates for this position.

Your CV was used only to assess this position and will be deleted once the process is over.

We wish you all the best.

Derin Kozmetik Human Resources
hr@derinkozmetik.example.com
```

*(Kaan was rejected by a red line, but the rejection email gives no reason. The reason lives only in the owner's report.)*

## screen-me/2026-09-27-lila-moda.md (candidate mode, excerpt)

The fictional Elif Aydın CV (the demo person of the Job Application Agent) and a fictional "Senior CRM Specialist" listing pasted into the chat:

> **You would be rejected regardless of your score.** The listing says "at least 3 years of experience with Insider is required"; Insider does not appear anywhere in your CV. For reference: without this line your score would be 78 and you would pass the threshold.
>
> **Your summary pushes you out of the band.** The listing asks for 5-8 years; your summary says "For four years". The dates add up to 5 years, but someone reading the summary, or a crude filter, counts you as 4 years and drops you out of the band.
>
> **What your CV is missing (you have it, but it does not show):** the Klaviyo and HubSpot items sit between the ad items. For listings like this one, the CRM items should move to the top.
>
> **You really do not have it (never goes into the CV):** Insider, Braze, BigQuery, team management.

The same CV scored 98 on the demo listing (Derin Kozmetik): "You would not be rejected for this listing; the only serious point that could hold you back is the years sentence in your summary."
