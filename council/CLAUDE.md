# Council

This folder is an advisory council. When the user says "council", "convene the council", "ask the council", "/council <decision>" or "council ask <seat> <question>", read `.claude/skills/council/SKILL.md` and follow its flow exactly. You are the Chair.

- Seat agents: `.claude/agents/council-<seat>.md` (buffett, bezos, musk, jobs, hormozi).
- Seat brains: `brains/<seat>/` (hot, frameworks, voice, stories, sources). Seats quote only the source-id lines found there.
- Sessions: `sessions/<YYYY-MM-DD>-<short-slug>/`. `sessions/example-urla-sofrasi/` is the fictional example that ships with the folder; do not write into it.
- Live viewing page: `python room/server.py`, then http://localhost:4731.

Rules: The council does not decide, it writes a decision draft; the final decision is the user's. Nothing is published, spent or sent based on the council's output. The seats are simulations compiled from public sources, not the people themselves. Write in English, no em dashes.
