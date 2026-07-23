# 02 · Links (form endpoint + payment link)

> These are the two lines the system wires into the page. The system opens no account, sets up no payment provider, and asks you for no password or API key. You paste your ready made link and the system wires it to the form and the button on the page.
> The values below are EXAMPLES. Write over them with your own.

---

## Email collection · form endpoint

One line, the address the form posts to. If you do not fill it in, the system leaves `FORM_ACTION_HERE` and puts a visible warning on the page.

```text
FORM_ACTION: https://formspree.io/f/EXAMPLECODE
```

Where to get one (starting from the free tier):

| Route | What you do | What you get |
|---|---|---|
| Formspree | open a free account on formspree.io, create a new form | a `https://formspree.io/f/xxxxxxx` address. Every submission lands in your inbox |
| Google Form | open a Google Form, one question "email", Send, take the embed code from the `<>` icon | an embedded form. In that case paste the embed code into the `FORM_EMBED` line |
| Klaviyo / Mailchimp | take the embed code of your list | an embed code. Same, into the `FORM_EMBED` line |

If you are going to use a Google Form or a Klaviyo embed code, leave the `FORM_ACTION` line empty and paste the embed code here:

```text
FORM_EMBED: (empty)
```

Form field labels:

```text
FORM_TITLE: tell me when the next dates open
FORM_NOTE: i only write to you with the next start date, nothing else
FORM_BUTTON: let me know
```

---

## Payment · the ready made payment link

One line, the address the button goes to. If you do not fill it in, the system leaves the button as a visible warning reading `PAYMENT_LINK_HERE`.

```text
PAYMENT_LINK: https://buy.stripe.com/test_EXAMPLE_LINK
PAYMENT_BUTTON: book my place · 240 dollars
```

Where to get one (the system opens none of these for you, you open one once):

| Provider | What it suits | How to get the link |
|---|---|---|
| Stripe Payment Link | cards, digital products and services | in the Stripe dashboard go to Payment links, enter the product and price, copy the link |
| Gumroad | digital products, templates, ebooks | create the product, copy the product page link |
| Lemon Squeezy | digital products, subscriptions | create the product, copy the checkout link |
| Paddle | digital products and software, with tax handled for you | create the product, copy the checkout link |

If you already sell through your own store, the product or checkout link of that store works the same way. Whatever you use, check which providers and payment methods are available where you and your customers are, because that differs by region.

> The system does not touch the money flow. Collection, fees, refunds and invoicing all run in your own provider account. The page only takes the user to that link.

---

## Look (optional)

```text
ACCENT_COLOUR: #b4552f
BRAND_LINE: Wheelhouse Studio
```

If you give no colour, the template default stays.

---

## Publish log (write here as you put pages live)

| Date | Page address | Note |
|---|---|---|
| (example) 2026-07-25 | wheelhousestudio.example/pottery | first publish, title leads with "four Saturdays" |
