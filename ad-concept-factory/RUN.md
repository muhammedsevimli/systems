# RUN · One Command

> Producing concepts is one step. Open this file, copy the command, run it.
> Thanks to `CLAUDE.md`, Claude Code will already read the brand + voice + winning memory + format + input files.
> First make sure you filled the three files in the `inputs/` folder (winning ads, customer reviews, liked comments). How to fill them: `inputs/READ-paste-guide.md`.

## Step 1 · Produce 50 concepts (copy)

```
analyze the winning ads, customer reviews, and most-liked comments in the inputs folder and produce 50 static ad concepts for me.

rules:
- first say in one line that you read the brand + voice + winning memory + format + input files.
- break down the winning ads: hook, promise, for whom, emotion, format, proof. collect the repeating pain, praise, and objection from the customer reviews. extract the viral angle from the liked comments.
- summarize the extracted pattern (which hook type landed, common promise, common emotion, frequent objection) in one paragraph.
- dress that logic in my brand and voice and write 50 concepts. each concept is three lines: hook, visual direction, one-line rationale (which winning ad or customer sentence it came from).
- make the 50 concepts truly diverse: follow the rotation grid in concept-format.md (hook type + segment + emotion). do not write the same hook again with the words swapped.
- do not invent a number/discount/guarantee i do not have, leave a placeholder. do not invent reviews, take them from the real input.
- do not use the banned words in 02-voice.md, do not use em dashes.
- write the output to the outputs/ folder as YYYY-MM-DD-theme.md. at the end, give a "morning shortlist" note (the first 5 concepts to try) and a LinkedIn measured-register note.
```

## Short version (when in a hurry)
```
analyze the winning ads + reviews in inputs, extract the pattern, write 50 diverse static concepts in my brand voice (hook + visual + rationale), write the output to outputs. follow the voice and format files, do not invent numbers or reviews, no em dashes.
```

## Step 2 · When a concept lands (copy)
When a concept truly works in an ad (a sale, a click, a save), write it into the system's memory:
```
<write the concept name> landed. add it to the winning memory with today's date: which hook type it was, why it landed, make this angle primary in later rounds. write it into 03-winning-memory.md.
```

## Want it automatic every morning?
You can set up a task that runs the Step 1 command on its own every morning (it works while you sleep, and in the morning 50 concepts are ready). Step-by-step setup: `automation/SETUP-automation.md`. If you do not want that, you run the command by hand whenever you like; both give the same output.

## Note
The richer the input, the clearer the pattern. At least 3-4 winning ads, 8-10 customer reviews, 3-5 liked comments is a good start. A strong pattern does not come from a single ad and two reviews; the system will still produce, but the material will be thin.
