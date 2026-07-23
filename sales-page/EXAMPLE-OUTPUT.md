# Example Output · One Full Run

> This is the output of a real run. Input: `you/EXAMPLE-01-product.md` and the example values in `you/02-links.md`.
> Fictional business: Wheelhouse Studio, a small pottery studio running a four week beginner course.
> Every run writes THREE files into `outputs/`. Two of them are below: the sales copy and the launch checklist. The third one, the page itself, sits in `outputs/beginner-pottery-course-sales-page.html` and opens on a double click.
> Note the proof section: the proof field in the product file was left EMPTY, so no proof section was put on the page and no review was invented. That is the anti invention rule working.

---
---

# FILE 1 · `outputs/beginner-pottery-course-copy.md`

# Sales Copy · Beginner Pottery Course (Wheelhouse Studio)

> Read: `you/EXAMPLE-01-product.md` + `you/02-links.md` + `format/page-format.md`.
> This copy is the source of `outputs/beginner-pottery-course-sales-page.html`. Change a sentence here, say "rebuild the html", and the page updates.

## Brand line
Wheelhouse Studio

## Title
A four Saturday pottery course for people who have never touched clay

## Subtitle
Four Saturday mornings, in a group of eight, you throw your own mug and bowl on the wheel and take them home fired.

## Price box
- Price: 240 dollars
- Price note: one off payment, materials and firing included, tax included
- Button: book my place · 240 dollars

## Who it is for
- adults who have never made ceramics and want to make something with their hands
- people who work at a screen all week and want a screen free weekend
- couples and friends who want to come as a pair, a two person booking is open

Who it is not for:
- participants under 14, because of kiln and wheel safety
- people who want to work at an advanced level, this is a beginner course

## What you are dealing with right now
You said "I will pick up a hobby" months ago and you still do not know where to begin. You go to one off workshops, they are pleasant, but a week later you have neither a piece in your hand nor anything you learned. And doing it on your own means dealing with clay, a wheel and a kiln, which is a job of its own.

## What we do
Four Saturdays in a row, same group, same wheel. In the first week you learn to centre the clay, in the following weeks you throw a mug and a bowl, and in the last week you glaze. Materials, tools and firing are ours; you just turn up. Your pieces are fired and handed over to you.

## What is included
- 4 weeks, every Saturday 10:00 to 13:00, 12 studio hours in total
- a group of 8, a wheel each
- clay, glaze and firing included, 6 kilos of clay per person
- your pieces fired and handed over within two weeks
- apron, tools and cleaning materials ready at the studio

## Proof
(the section was NOT PUT on the page · the proof field in the product file is empty)

## Frequently asked
- **I have no experience at all, is that alright?** The course starts from zero. The first week is spent centring clay. No experience is expected.
- **What if I miss a week?** You can move a missed week once, into the same week of the next run.
- **When do I get my pieces?** Firing takes two weeks after the last session, and we let you know when they are ready.
- **Is there parking?** There is paid street parking, the studio has no car park of its own.

## Email block
- Title: tell me when the next dates open
- Note: i only write to you with the next start date, nothing else
- Button: let me know

## Footer
- Refund: Cancel up to 7 days before the course starts and you get a full refund. Cancel inside the last 7 days and you can send someone else in your place, but there is no refund. If you come to the first week and decide not to continue, the remaining 3 weeks are refunded.
- Contact: hello@wheelhousestudio.example · Unit 4, Foundry Lane
- Seller: Wheelhouse Studio

---

## Note · the empty fields and what you need to do

1. **The proof field is empty.** That is why no proof section was put on the page. No invented review and no sentence like "300 people attended" was written. When you get one sentence from a participant at the end of the first run, with their permission, write it into the proof field in `you/01-product.md` and have the page rebuilt; the proof section is added right above the frequently asked block.
2. **The payment link is an example link.** The `PAYMENT_LINK` line in `you/02-links.md` is a test link right now. Replace it with your live link and say "i updated the links".
3. **The form endpoint is an example code.** The `EXAMPLECODE` in the `FORM_ACTION` line has to become your own Formspree code.
4. **The contact address is an example domain.** Write your real email address in.
5. **The legal line.** Add your own trading name and any registration or tax details you have to show into the legal note in `you/01-product.md`, and they drop into the footer of the page. What is required differs by region, so check the rules where you sell.
6. **The "what it is not" list was applied.** Certificates, one to one private lessons, selling materials and open studio access are implied nowhere on the page.

---
---

# FILE 2 · `outputs/beginner-pottery-course-launch-checklist.md`

# Launch Checklist · Beginner Pottery Course (Wheelhouse Studio)

> Before you go live, REALLY test these and tick them off. Do not share the page until all of them are ticked.

## A · Does the page open
- [ ] Double clicking `beginner-pottery-course-sales-page.html` opens it in your browser, with no broken boxes and no empty areas.
- [ ] Open it on your phone. Nothing overflows, the button fits the screen, there is no horizontal scrolling.
- [ ] Toggle your phone's dark mode on and off. The text is readable in both modes.
- [ ] The browser tab reads "A four Saturday pottery course for people who have never touched clay · Wheelhouse Studio".

## B · Does the payment really work (the most critical)
- [ ] Tap the "book my place · 240 dollars" button. It goes to your own Stripe page.
- [ ] Does that page say Beginner Pottery Course.
- [ ] Does that page say 240 dollars, exactly as the page does. If it is different, fix it before you start selling.
- [ ] The link currently in the file is a TEST link. Switch it to the live link, and do not go live with the test one.
- [ ] Make one real payment yourself, or try the Stripe test card. See the payment land in your account.
- [ ] See for yourself, once, what the buyer receives after paying (the confirmation email and the first session details).

## C · Does the email form really deliver mail
- [ ] Type your own email into the "tell me when the next dates open" form and submit.
- [ ] Did the record reach your inbox through Formspree. Check the spam folder too.
- [ ] See for yourself, once, what the user sees after submitting.
- [ ] The form endpoint currently reads `EXAMPLECODE`. Until you put your own code in, the page is NOT READY to publish.

## D · Is the information on it correct
- [ ] 240 dollars is correct, the currency is correct, and the note says tax is included.
- [ ] The refund terms are on the page (full refund up to 7 days before, a substitute inside the last 7 days, the remaining 3 weeks refunded if you leave after the first session) and they are the terms you will really honour.
- [ ] hello@wheelhousestudio.example is really your address. Replace the example domain.
- [ ] The seller name Wheelhouse Studio is on the page.
- [ ] There is no invented review, no invented number and no invented badge on the page. The proof field is empty, so there is no proof section either. Correct.
- [ ] The 10:00 to 13:00 hours, the 4 week length and the 8 person capacity match the run you are actually opening.
- [ ] Check what the rules where you sell require on the page (seller details, tax information, cancellation rights) and add any line that is missing.

## E · Going live
- [ ] Drag the file onto a free static host (Netlify Drop, Cloudflare Pages, GitHub Pages). You have an address.
- [ ] Open the address on another device, it works.
- [ ] Send the address to a friend and ask whether they can tell in one sentence what is being sold. If they cannot, fix the title.
- [ ] Write the page address into the publish log in `you/02-links.md`.

## F · The first 48 hours
- [ ] Reply to the first record that comes through the form.
- [ ] On the first booking, confirm that the confirmation email really goes out.
- [ ] Note the questions that come in. If two people ask the same thing (for example "can I bring my own clay"), add it to the frequently asked block and have the page rebuilt.
