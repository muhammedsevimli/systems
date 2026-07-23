# Collected Demand Signals · 2026-07-24 · Automatic Scan Output

> This file was produced automatically by the system. Field: local appointment businesses + small ecommerce.
> The sources were REALLY scanned with Claude Code's web and shell tools (WebFetch + Bash curl + WebSearch) on 24 July 2026. Every signal carries its source and link.
> Hacker News answered `200` over `hn.algolia.com` (plain `http` answers `301`, so `https` was used). Reddit's keyless `.json` endpoint answered `403`, so the public RSS search feed was used, which answered `200`. One subreddit pull came back `429` (rate limit) and went through on the retry.
> No usernames or personal data were carried over from the pulled posts.

## Signal 1
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=appointment+scheduling+small+business&tags=comment
Who is saying it: an operator talking about small business software
Pain sentence: "scheduling is a big pain point for these tiny businesses but no one addresses it in a humane way"
Money language: indirect (an unsolved pain in a paid category)
In how many sources: the appointment pain repeats across several comments and on Reddit
Existing solution / competitor: none named in the comment ("no one addresses it")

---

## Signal 2
Source: Hacker News (Show HN thread)
Link: https://hn.algolia.com/api/v1/search?query=appointment+scheduling+small+business&tags=comment
Who is saying it: the founder of an appointment reminder tool, describing the target audience
Pain sentence: "Anyone that books client/customer appointments and wants to avoid no-shows"
Money language: indirect (a no-show is lost revenue; the Show HN targets paying users)
In how many sources: the no-show pain shows up in Hacker News, Reddit, and web reviews
Existing solution / competitor: Remindr.co (SMS and email reminder tool), Leadmonk (booking tool with a free tier)

---

## Signal 3
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=appointment+scheduling+small+business&tags=comment
Who is saying it: someone evaluating a new reminder product
Pain sentence: "do you expect your users to manually input their appointments into two separate systems?"
Money language: none
In how many sources: the double-entry pain also appears in a Reddit booking software complaint
Existing solution / competitor: existing booking systems, but they sit apart from the reminder layer

---

## Signal 4
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=appointment+scheduling+small+business&tags=comment
Who is saying it: someone who has worked on online booking for practices
Pain sentence: "you're always going to run into problems with conflicting appointments", and practices dislike reserving fixed online slots
Money language: indirect (a conflicting appointment burns a slot)
In how many sources: also confirmed by a Reddit complaint about double-booked slots
Existing solution / competitor: ZocDoc style slot reservation

---

## Signal 5
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=respond+to+reviews+small+business&tags=comment
Who is saying it: an observation about local businesses
Pain sentence: "Every small business who cares about their Google Maps standing responds to bad reviews"
Money language: none stated (but map ranking feeds revenue)
In how many sources: the review response pain repeats across several comments
Existing solution / competitor: Revumatic (an SMB tool that drafts review responses with AI) came up in the same scan

---

## Signal 6
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=respond+to+reviews+small+business&tags=comment
Who is saying it: someone working at a review platform
Pain sentence: businesses want to "respond publicly to individual review's"
Money language: none
In how many sources: one comment, pointing the same way as Signal 5
Existing solution / competitor: the review platforms themselves, but the drafting work stays manual

---

## Signal 7
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=ecommerce+returns+refund+manual&tags=comment
Who is saying it: an ecommerce operator
Pain sentence: "Only if things like returns are automated can you actually scale the business", said next to "the manual process that most smaller ecommerce players labour under"
Money language: indirect (the returns process caps growth)
In how many sources: several comments in the same thread
Existing solution / competitor: the returns modules of the large platforms, heavy for a micro seller

---

## Signal 8
Source: Hacker News comment
Link: https://hn.algolia.com/api/v1/search?query=ecommerce+returns+refund+manual&tags=comment
Who is saying it: someone who ran the operations side of a small shop
Pain sentence: at a few hundred packages "the only option was to do it manually", and integrating an API to "print the labels automatically" was never done
Money language: indirect (hours of manual work per day)
In how many sources: one comment, its own topic
Existing solution / competitor: shipping label platforms exist, but they are aimed at higher volume

---

## Signal 9
Source: Reddit (r/smallbusiness · public RSS search)
Link: https://www.reddit.com/r/smallbusiness/comments/1tz6m53/how_do_you_reduce_noshows_for_service/
Who is saying it: the owner of a small service business
Pain sentence: "when someone books a slot and does not show up, that time is hard to recover. It also blocks another cus[tomer]", asked without wanting to pressure customers
Money language: indirect (an unrecoverable slot)
In how many sources: no-show threads repeat across the same community
Existing solution / competitor: none named

---

## Signal 10
Source: Reddit (r/smallbusiness · public RSS search)
Link: https://www.reddit.com/r/smallbusiness/comments/1uqg9ua/how_much_you_are_losing_to_cancelled_bo
Who is saying it: someone whose relative just opened a salon
Pain sentence: the biggest problem is "people cancelling the appointment in the last minute or no show up"
Money language: indirect (the thread is literally about how much is being lost)
In how many sources: the same pain in several posts in the community
Existing solution / competitor: none named

---

## Signal 11
Source: Reddit (r/smallbusiness · public RSS search)
Link: https://www.reddit.com/r/smallbusiness/comments/1rsfh5w/we_stopped_calling_patients_to_confirm/
Who is saying it: an appointment based practice that changed its confirmation process
Pain sentence: mornings went to voicemails "that nobody listened to"; after switching to text confirmations "people actually respond"
Money language: indirect (half a morning of staff time)
In how many sources: supports the reminder channel choice in Signals 2, 9, 10
Existing solution / competitor: none named. Note: this one is a healthcare practice, which matters for the profile limit

---

## Signal 12
Source: Reddit (r/smallbusiness · public RSS search)
Link: https://www.reddit.com/r/smallbusiness/comments/1so93tp/salon_booking_software_advice/
Who is saying it: a skin care clinic owner of 7-8 years
Pain sentence: the booking system became "a HUGE headache", with "appointments disappearing from my calendar or appointments being shown as booked multiple times"
Money language: indirect (paying for a tool that loses appointments)
In how many sources: overlaps with Signals 3 and 4 (double entry, conflicting slots)
Existing solution / competitor: Vagaro (named in the post as the tool being used)

---

## Signal 13
Source: Web + review sites (WebSearch snippet)
Link: https://www.g2.com/products/daysmart-salon
Who is saying it: a salon owner reviewing booking software
Pain sentence: the system is "expensive to begin with" and has "constant added costs", including being charged separately for SMS reminders
Money language: explicit (an existing tool is already being paid for, and the reminder feature is charged on top)
In how many sources: the same complaint pattern shows up across several booking tool review pages
Existing solution / competitor: DaySmart Salon, Vagaro, Zenoti, Reservio, TimeToBook, Appointible (the category is crowded)

---

## Look by hand (semi-automatic · X, not pulled by the system)
- `https://x.com/search?q=%22no%20show%22%20%22appointment%22%20losing&f=live`
- `https://x.com/search?q=%22I%20wish%20there%20was%20an%20app%22%20small%20business&f=live`
(X wants a login, so the system did not pull these; add signals here by hand if you want.)

---

## Scan summary
- Hacker News (fully automatic, WebFetch on the `hn.algolia.com` JSON, HTTP 200): 8 signals across 6 queries. Real, quoted verbatim.
- Reddit (fully automatic, Bash curl on the public RSS search feed, HTTP 200 after one 429 retry): 4 signals from r/smallbusiness. The keyless `.json` endpoint answered `403` and was not used.
- Web + review sites (fully automatic, WebSearch): 1 strong signal with explicit money language, plus 6 competitor names in the booking category.
- X (semi-automatic): not pulled, one-click links produced.
- Total: 13 signals, coming down to 5 separate ideas. The most repeated pain: appointment no-shows and last-minute cancellations. The clearest money language: Signal 13, a salon owner already paying for a booking tool and being charged extra for reminders.
