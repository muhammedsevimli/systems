# Ad Breakdown Anatomy

> The system splits each ad in `competitor-ads/` into these headings. If the pasted ad has no info for a line, it leaves that line blank, never invents.

## Headings to extract for each ad
1. **Hook:** the ad's first sentence / attention-grabbing opener. The spot where a person stops scrolling. (E.g. a pain sentence, a question, a number, a contrarian take.)
2. **Promise / offer:** what it promises, what the offer is. A discount, a gift, an outcome, a convenience, a guarantee.
3. **Who it speaks to:** who it addresses, judged from its language, choice of pain, examples. Age signal, lifestyle, moment of use.
4. **Format:** video, single image, carousel, or text only. (The type of each ad is visible in the library.)
5. **Proof:** a number, a guarantee, "X people bought", a review screenshot, a celebrity/user demo, an award.
6. **CTA (call):** what it wants. Buy, go to the site, DM, sign up, see the offer.
7. **How long it has been running:** the "started running" date in the library. This is the most valuable signal (below).

## The winning signal (the most important read)
The Meta Ad Library shows the start date of every active ad. The rule:
- **An ad running for months = a winning candidate.** No one pays for a losing ad for months. If it runs long, it converts.
- **An ad running for a few days / weeks = the test phase.** It is not yet clear that it wins, so it is a weak model to copy.
- **If several variations of the same hook are active**, the competitor is putting money behind that hook, so the hook is strong.
The system highlights the long-running and multi-variation hooks; it builds the pattern mainly from these.

## Extracting the pattern (after breaking down each ad)
Once all ads are broken down, the system answers these questions:
- Which hook type repeats (pain / number / contrarian / curiosity / social proof)?
- What is the common offer type (discount / gift / convenience / risk-removal / community)?
- What is the common emotion (relief, fear of missing out, belonging, status, saving)?
- Do they all speak to the same person, or to different segments?
These four answers are "the logic that clearly works". The 10 concepts derive from this logic, not from the competitor's words.

---

## Honest notes about the Meta Ad Library (explain to your audience)
- **It is public and free.** Anyone, without an account, can see a brand's currently running ads at `facebook.com/ads/library`. Meta requires this for transparency.
- **The ad text is visible in the browser:** the top text, the headline, the button, the start date. The system analyzes exactly this text; the hook and the offer are already in it.
- **The system cannot watch video ads on its own.** If something important is in the video you watch (what happens in the first 3 seconds, what is written on screen), you drop a one-line note and the system uses it too. If there is no note it does not invent; it extracts what it can from the text.
- **The free automatic download (API) does not return commercial product ads in most countries.** Meta's official Ad Library API only returns politics/election/social-issue ads; product ads appear only in the browser interface. That is why the "seeing an ad" step is a one-click open-and-paste job, not automatic scraping. The breakdown and generation are automatic.
