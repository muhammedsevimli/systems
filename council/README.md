# Council

An advisory council that Claude sets up for you. You put a business decision in front of a five-seat council: Warren Buffett, Jeff Bezos, Elon Musk, Steve Jobs and Alex Hormozi. Each seat reads its own brain, writes its card, and in the second round objects to the others. At the end Claude builds the score table and writes a decision draft labeled GO / CONDITIONAL GO / NO GO. The final decision is yours.

The seats are simulations compiled from these people's public sources (shareholder letters, books, interviews, talks); they are not the people themselves.

## What it does

When you ask a single chat "should I open a second location?", one voice answers, and it usually drifts toward what you want to hear. The council tests the same question from five angles that do not look alike:

| Seat | The question it owns |
|---|---|
| Warren Buffett · Capital and risk | How does this decision use the money, is there a risk of permanent loss, will it still make sense in 10 years? |
| Jeff Bezos · Customer and systems | Does the customer really want this, is it a setup that keeps running on its own or a one-off effort? |
| Elon Musk · Speed and engineering | Is there a way to do this 10x faster or 10x cheaper, which step is unnecessary? |
| Steve Jobs · Product and focus | What does this change in a person's life, what are we saying no to? |
| Alex Hormozi · Offer, pricing and sales | Will people pay for this, how much, does the cash from the first 30 days pay for the next customer? |

The flow:

1. **Brief.** Claude turns your decision into one question, options (A, B, C, "do nothing") and a success metric.
2. **Seal.** Before calling the council, Claude writes its own opinion and seals it. The seats never see it.
3. **Round one.** The five seats write their cards at the same time: position, strongest reason (with a source number), biggest risk, a question for you, a score for each option.
4. **Round two.** Each seat reads the other cards, objects to at least one seat by name, accepts a point where someone is right, and gives a final score.
5. **Decision.** Scores are averaged. An option that any seat calls a high ruin risk cannot go above 6.0. If the seats are 4 or more points apart on an option, the label is at most CONDITIONAL. The report also writes down the difference between the seal and the council, so Claude audits the council instead of just going along with it.

## Setup

All you need is the Claude desktop app. If you use ChatGPT, do the same steps in Codex.

1. Open the Claude desktop app and start a new chat in the Code tab. Paste this address and say "download this for me and work in this folder":

```text
github.com/muhammedsevimli/systems/tree/main/council
```

Claude handles the rest. If it needs to install something, it asks you first and you approve.

2. Type your decision:

```text
convene the council: should I open a second location?
```

If something is missing, Claude asks at most three questions, then convenes the council. It takes a few minutes. You get the short decision in the chat, and the full report stays in the folder.

3. If you want to watch the room live, type in the same chat:

```text
open the room
```

Claude starts the page and gives you an address to click. As each card arrives that seat speaks, its words flow into a speech bubble, objection and agreement arrows are drawn in round two, and the decision band opens at the end. Hover over a seat and it repeats its last words.

To watch a finished session again card by card (for a screen recording), type "replay the room". Each card stays on screen for 4 seconds; press R to restart, C to go back to live.

The page only reads the session folder and connects to nothing else. The first time you open it, it shows the fictional example session that ships with the folder; when you convene your own council it switches to yours on its own.

## Modes

All of them are plain sentences you type in the chat:

| What you type | What happens |
|---|---|
| `convene the council: <decision>` | Full council: 5 seats, 2 rounds |
| `quick council: <decision>` | Quick council: 3 seats picked for the decision, 1 round |
| `convene the council: <decision>, with Buffett, Jobs and Hormozi` | You pick the seats |
| `council ask hormozi: <question>` | A short question to a single seat, no scores. The answer lands in `sessions/questions/` |

## Example

`sessions/example-urla-sofrasi/` is a real council run for a fictional business: a 40-seat home-cooking restaurant in Urla, Turkey, asking "should I open a second location?" with four options. It holds the brief, the sealed opinion, every card from both rounds and the decision report. Every number about the business is made up.

## Folders

```text
council/
  brains/<seat>/             each seat's sources, frameworks, voice and stories
  brains/BRAIN-TEMPLATE.md   template for adding a new seat
  sessions/                  every council opens a folder here
  room/                      live viewing page
```

To add a new seat, type "add a new seat to the council: <person>, their question is <question>". Claude writes the brain folder from the template, sets up the seat and adds it to the list; it shows you the sources and asks for your approval.

## Honesty

- The seats are not the people. The last line of every card says so.
- Seats only quote the source-numbered lines in their brain folder (like `S3`; every number's source is in `sources.md`). Everything else is that seat's own reasoning. The brains are kept short: about 2,300 words per seat.
- The council does not decide, it writes a decision draft. Nothing is published, spent or signed automatically based on its output.
- You provide the numbers. The council does not invent missing numbers; it asks, or writes the assumption down openly.
- The seat busts are stylized drawings derived from openly licensed photos; licenses and credits are in `room/portrait/SOURCES.md`. Hormozi has no openly licensed photo, so his bust was drawn from a written description only, with no photo.

## Supported tools

The Claude desktop app (Code tab) runs the council at its best: all five seats write at the same time. Codex in ChatGPT, Google Antigravity, Windsurf, Kilo and 20+ other tools understand the same folder; in a tool that cannot run the seats at the same time, the assistant plays them one after another.

## Advanced

This section is only for people who want to set things up by hand; the flow above needs none of it.

- Download as ZIP: on the [repository page](https://github.com/muhammedsevimli/systems), green Code button → Download ZIP. Unzip it and pick the `council` folder inside in Claude's Code tab.
- If you know the command line: `npx degit muhammedsevimli/systems/council council`
- Start the room by hand: `python room/server.py` in the folder, then http://localhost:4731 (replay: http://localhost:4731/?play=1&step=4).
- Instructions the assistant reads: `CLAUDE.md` (Claude), `AGENTS.md` (Codex and others); the flow and the seats live in `.claude/skills/council/` and `.claude/agents/`.

---

**Muhammed Sevimli** builds these systems. Real sales and growth systems with AI. If you get stuck setting one up or want a step-by-step guide, reach out:

- Web: https://muhammedsevimli.com
- X: https://x.com/_msevimli
- Instagram: https://instagram.com/msevimli_
- Threads: https://threads.com/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

🧩 Built with Claude Code.

## License

Code and text: [MIT](LICENSE). Seat busts: under the license of their source photos (CC BY / CC BY-SA, details in `room/portrait/SOURCES.md`). Font: SIL Open Font License (`room/fonts/OFL.txt`).
