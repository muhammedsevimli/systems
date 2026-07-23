# Sales Page · Copy Format and Writing Rules

> The system writes the sales copy in this order and by these rules. The order does not change, and an empty section is not invented.

## Section order (top to bottom)

1. **Brand line** · one word or a short brand name. No decoration.
2. **Title (H1)** · says what the product is and who it is for in one sentence. 12 words at most. Not a tagline, a description.
   - good: "A four Saturday pottery course for people who have never touched clay"
   - bad: "Set your creativity free" (it is not clear what is being sold)
3. **Subtitle** · one sentence, concrete. Says what you get and what you go home with. Numbers and durations belong here.
4. **Price box (top)** · price, one line price note, payment button. It sits high on the page so someone who has decided can buy without scrolling.
5. **Who it is for** · 2 to 4 items. Then the "who it is not for" items (if they are in the file). Ruling the wrong person out makes selling easier.
6. **What you are dealing with right now (the pain)** · one paragraph of 2 to 4 sentences. Talk in the reader's own words. No fear pumping, no drama, no exaggeration.
7. **What we do (the solution)** · 2 to 4 sentences. Plainly explains how the product works. Step by step if there is a process.
8. **What is included** · a concrete list. Duration, quantity, what is covered, delivery. Every item says something measurable.
9. **Proof** · if there IS proof in the file: a real review (with the person's permission), a real number, real past work. If there is NO proof in the file, this section does not go on the page at all. Invented reviews, invented percentages and invented attendee counts are banned.
10. **Frequently asked** · the real questions from the file. At least one of them should be an objection question ("what if I cannot make it", "will it work", "I have no experience").
11. **Price box (bottom)** · the same box again. A reader who scrolled down does not have to scroll back up.
12. **Email block** · a one line offer for the person who is not buying today (next dates, restock, waiting list). Write honestly what you will send.
13. **Footer** · refund or cancellation terms, contact, seller name. All three are mandatory.

## Writing rules

- Plain English, like talking, in the second person. No corporate language ("our firm", "we provide our customers with").
- Short sentences. One idea per sentence.
- **No em dash.** Use a full stop, a comma, a colon, a middle dot (·).
- **No inflated promises:** guarantees, certain results, "your life will change", "do not miss out", fake urgency ("only 3 spots left" when that is not true) are banned.
- **No motivational language.** The page sells, it does not give a pep talk.
- **No "it is not X, it is Y" contrast pattern.**
- No piling up adjectives: words like "unique", "amazing", "revolutionary" are cut.
- No trashing competitors, no comparison by name.
- No information that is not in the file gets into the copy.
- Nothing from the "what it is NOT" list is implied.
- In health, finance and legal, no outcome promise is written; add an "for information only" note if it is needed.

## Length

It does not fit on one screen, and it does not run long either. The target is 350 to 600 words in total. A paragraph that says nothing gets deleted.

## The copy file output

`outputs/<slug>-copy.md` is written with the section headings so the user can fix any sentence by hand and have the page rebuilt. A "note" section is added at the very end of the copy: which section was left off the page because which field was empty, and what the user needs to add.
