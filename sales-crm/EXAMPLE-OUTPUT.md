# How It Looks (with sample data)

> When you double-click `satis-crm.html`, the system opens with fictional sample data: 6 customers, 3 reps.
> The tables below describe that sample board. Everything is fictional, not real customers or data.
> Note: the interface labels are in Turkish; below they are shown with English glosses.

## Today's call list (morning list)

Customers whose follow-up day falls on today (or earlier) gather here on their own. Overdue ones sit on top with a red tag.

| Customer | Rep | Stage | Next step |
|---|---|---|---|
| Kaya Mobilya | Elif Y. | Teklif (Proposal) | Call to check if the proposal was approved |
| Aydın Petrol | Burak T. | Takipte (Following up) | Ask about budget approval |
| Tuna Lojistik | Deniz K. | Yeni (New) | First call |

## Customer card (opens on click)

```text
Kaya Mobilya · Kaya Mobilya Ltd. · 0555 000 00 01
Rep: Elif Y.        Stage: Proposal
last:  sent the proposal to management, promised to reply Friday
next:  call to check if the proposal was approved

--- call history ---
Jul 01  reached out via website, wants chairs for a 40-person office   (talked)
Jul 06  sent the proposal, will pass to management, replies Friday      (talked)
```

## Dropping a call note (the heart of the system)

After a call the rep writes two lines and picks the outcome and when to call again. The system does the rest.

```text
Call note:   liked the proposal, will ask the boss, replies Wednesday
Outcome:     [ Talked ]  ( No answer )  ( Sale )
Call again:  ( today )  ( tomorrow )  [ 2-3 days ]  ( 1-2 weeks )  ( no need )
                                       → system sets the follow-up day to "today + 2"
```

When the note is saved: the date is stamped automatically, the follow-up day is set, "last discussed" is updated, and when that day arrives the customer surfaces in the morning list. The rep does no date math.

## Month-end panel (manager view)

Pick a month; the table shows each rep's summary for that month, sorted by sales.

| Rep | Calls | Sales | No answer | Conversion |
|---|---|---|---|---|
| Elif Y. | 5 | 1 | 0 | 20% |
| Burak T. | 4 | 1 | 1 | 25% |
| Deniz K. | 2 | 0 | 1 | 0% |

The manager does not ask "who did what today" one by one; it is on the screen.

---

To clear this sample data and start with your own customers: **Settings → Clear sample data**.
