# Cost

Five agents run at once and each one carries its own context. You are producing five answers to a single question, plus a second round on top. This does not cost what asking one agent costs.

## The real run

| | |
|---|---|
| Agents | 5 |
| Rounds | 2 |
| Model | top tier for all five |
| Total tokens | roughly 570k |
| Wall clock | about 4 minutes |

The input was four source files. If your data grows, tokens grow with it, because every agent reads the data separately. Five agents reading the same 50k-token dataset counts as 250k.

## Start with three agents

Five roles is the full team. Your first run does not need it.

**Three agents is enough:** two theories plus the Mathematician. You will see whether the system works at this size, at less than half the cost. If both theories stay standing, add roles.

**Four agents is a good balance:** three theories plus the Mathematician. Enough for most questions.

**Five agents** is worth it when the theories are genuinely different from each other. If two roles argue the same thing in different words, the second one is burning money.

## Cheap model for cheap work

The roles do not all need the same model. Change the `model` line in each role file.

| Role | Suggested | Why |
|---|---|---|
| Mathematician | top tier | The system rests on this. If the arithmetic is wrong, the whole debate collapses. |
| Theory roles, round 1 | mid tier | Writing a theory and pulling three numbers out of a file is not heavy work. |
| Theory roles, round 2 | mid tier | The ruling is one word and the reasoning is 80 words. |
| Lead | top tier | It is your session and it runs the debate. |

Dropping the four theory roles to mid tier takes out most of the cost and leaves the referee at full strength.

## When not to run it

- **No data.** The system runs on numbers. With no numbers all five agents tell stories and the referee marks every one "cannot be separated". You pay for nothing.
- **You already know the answer.** Opening five agents for confirmation is an expensive way to agree with yourself.
- **The question is not tied to one outcome.** "Why are we not selling" is not a question. "Why did last month's campaign bring 40 orders when the previous ones brought 120" is.

The system pays off most when you have the data and still cannot tell the causes apart.
