# Example output

> This file shows what a report looks like on the **fictional** data in `data/SAMPLE-DATA.md`. Fictional data, fictional result. It is not a measured run record.
>
> The real run and its real numbers are summarized under "Does it really work" in `README.md`.

This example was deliberately built to land on a different answer than the real run. If the system were rigged for one conclusion, the same role would survive on every dataset. Here a different role stands.

---

# Lead report · short video series · example

Question: why did Episode 7 get 42,300 views when Episode 6 stayed at 4,900.
Run: 5 agents, 2 rounds, parallel sub-agents. Input: `data/SAMPLE-DATA.md`.

| Role | Theory | Round 1 evidence | Round 2 ruling |
|---|---|---|---|
| Marketer | The opening format spread it | The two phone-opening episodes hit 42,300 and 39,700; the talking-to-camera one hit 4,900 | **STANDING** |
| Editor | The edit spread it | Mix -16.2 LUFS, 24 cuts, 0 dropped caption frames | **OUT** |
| Skeptic | The existing audience spread it | 8,400 followers, 520 shares | **OUT** |
| Psychologist | Ownership behavior spread it | Saves 1,460, 2.28x likes; comments 1,180 | **OUT** |
| Mathematician | referee | tested each theory against the numbers | Marketer standing |

**Left standing:** the opening format. The two episodes using the same opening got 42,300 and 39,700 views; the talking-to-camera episode stayed at 4,900. The reach gap is 8.6x and the opening format is the only variable that lines up with it.

**Honesty note:** the behavior the Psychologist read is real, it just does not explain reach. Episode 4 reached 39,700 with weak intent signals (saves at 0.58x likes, saves and comments only 38.3% of total engagement). The same signals explain new follows on Episode 7 (710 against 180), not reach. The two-episode difference rests on two comparisons, and three data points is thin.

---

## From the round 2 files

**`round2_editor.md`**

> OUT
>
> The production measurements across all three episodes are nearly identical: mix between -16.0 and -16.2 LUFS, music separation between 20.5 and 21.0 LU, zero dropped caption frames and zero full black frames in all three, cut count between 22 and 26. Average watch time sits in the same band too: 18.9, 19.4 and 20.1 seconds. A variable that stayed constant cannot produce an 8.6x reach gap. The edit held the ceiling, it did not create the difference.

**`round2_skeptic.md`**

> OUT
>
> On Episode 7 the follower share of unique viewers is 33,800 x 0.076 = 2,569, about a third of the 8,400 follower base. For that group to carry 33,800 unique viewers each one would have to bring 13 viewers; total shares are 520. On Episode 6 follower uniques are 4,150 x 0.419 = 1,739, a comparable base, and the result was 4,900. The base held steady while the result changed.

**`round2_psychologist.md`**

> OUT
>
> Episode 4 cuts me. Saves 340, likes 590, a ratio of 0.58. Saves and comments are only 38.3% of total engagement. It still reached 39,700, close to Episode 7's 42,300. If the ownership signal is weak while reach stays strong, that signal is not carrying reach. What I read explains new follows (710 against 180), not spread.

**`round2_mathematician.md` (referee ruling)**

> **MARKETER: STANDING.** The two phone-opening episodes hit 42,300 and 39,700; the talking-to-camera one hit 4,900. Two observations is thin, but the opening format is the only variable that lines up with the reach gap and no number cuts it.
>
> **EDITOR: OUT.** Production measurements sit in the same band across all three, watch time between 18.9 and 20.1 seconds. A constant variable does not explain 8.6x.
>
> **SKEPTIC: OUT.** Episode 7 follower uniques = 2,569, Episode 6 = 1,739. Comparable base, 8.6x gap.
>
> **PSYCHOLOGIST: OUT.** Episode 4 ran at 0.58 saves per like and a 38.3% intent share and still reached 39,700. Signal weak, reach strong. Note: Episode 7's new-follow count (710) is consistent with that signal, but the question was about reach.
>
> **Data limit:** there are three episodes and no fourth comparison. Opening format and subject both change on Episode 6, so the variable is not fully isolated.
