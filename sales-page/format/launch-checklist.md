# Launch Checklist · template

> The system fills this list in for your product and writes it to `outputs/<slug>-launch-checklist.md`. Before you go live you REALLY test the items and tick them off. Do not share the page until all of them are ticked.

## A · Does the page open
- [ ] Double clicking the `.html` file opens it in your browser, with no broken boxes and no empty areas.
- [ ] Open it on your phone. Nothing overflows, the button fits the screen, there is no horizontal scrolling.
- [ ] Toggle your phone's dark mode on and off. The text is readable in both modes.
- [ ] The page title (the text on the browser tab) is correct.

## B · Does the payment really work (the most critical)
- [ ] Tap the payment button. It goes to your own payment provider's page.
- [ ] Is the PRODUCT NAME correct on the page that opens.
- [ ] Is the PRICE on that page exactly the same as the one on your page. If it is different, fix it before you start selling.
- [ ] If the provider is in test mode, switch it to live. Do not go live with a test link.
- [ ] Make one real payment yourself, or try the provider's test card. See the payment land in your account.
- [ ] See for yourself, once, what the buyer receives after paying (email, delivery link, booking).

## C · Does the email form really deliver mail
- [ ] Type your own email into the form and submit.
- [ ] Did the record reach you (your inbox for Formspree, the sheet for Google Form, the list for Klaviyo or Mailchimp). Check the spam folder too.
- [ ] See for yourself, once, what the user sees after submitting (a thank you page or a message).
- [ ] If the form endpoint still reads `FORM_ACTION_HERE`, the page is NOT READY to publish.

## D · Is the information on it correct
- [ ] The price is correct, the currency is correct, and the tax situation is stated (whether tax is included).
- [ ] The refund and cancellation terms are on the page and they are the terms you will really honour.
- [ ] A way to make contact is on the page, and that address or number is really yours.
- [ ] The seller name is on the page.
- [ ] There is no invented review, no invented number and no invented badge on the page. If you have no proof, there is no proof section either.
- [ ] Dates, durations and capacity match today's reality.
- [ ] Check what the rules where you sell require on the page (seller details, tax information, cancellation rights) and add any line that is missing.

## E · Going live
- [ ] Drag the file onto a free static host (Netlify Drop, Cloudflare Pages, GitHub Pages). You have an address.
- [ ] Open the address on another device, it works.
- [ ] Send the address to a friend and ask whether they can tell in one sentence what is being sold. If they cannot, fix the title.
- [ ] Write the page address into the publish log in `you/02-links.md`.

## F · The first 48 hours
- [ ] Reply to the first record that comes through the form.
- [ ] On the first payment, confirm that delivery really works.
- [ ] Note the questions that come in, add the repeating one to the FAQ and have the page rebuilt.
