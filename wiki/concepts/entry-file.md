---
title: "Entry File"
type: concept
tags: [ai-agents, documentation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/"]
---

# Entry File

An entry file is a short (50-200 line) top-level instruction document — `AGENTS.md`/`CLAUDE.md` — whose job is to route an agent to detail, not contain the detail itself. It should hold only:

- A one- or two-sentence project overview.
- First-run commands (e.g. `make setup && make test`).
- A maximum of 15 global hard constraints.
- One-line links to topic documents, each with an applicability condition stating when that doc matters.

Everything else — API patterns, database rules, testing standards — belongs in topic documents (50-150 lines each, typically under `docs/`), pulled in only when relevant ("Reveal on Demand"). Information that's naturally expressed in code (type definitions, interface comments) should live there instead of being duplicated into prose.

This is the concrete implementation of Lecture 02's "maps, not manuals" principle (see [[Harness Engineering]]) and directly counters [[Instruction Bloat]]: an entry file that stays small keeps its most important lines out of the [[Lost in the Middle]] danger zone and keeps its [[Instruction Signal-to-Noise Ratio]] high.

## Related

- [[Instruction Bloat]]
- [[Lost in the Middle]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Harness Engineering]]
- [[System of Record]]
