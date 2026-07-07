---
title: "Instruction Bloat"
type: concept
tags: [ai-agents, context-window, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/"]
---

# Instruction Bloat

Instruction bloat is what happens when a project's instruction file (`AGENTS.md`/`CLAUDE.md`) occupies a large share — 10-15% — of the model's available context window. A 600-line file can cost 10,000-20,000 tokens before the agent has read any actual code, crowding out the budget needed for real task reasoning.

Bloat isn't caused by any single bad edit — it's the accumulated result of "add a rule" being the easiest response every time an agent fails at something. Each addition is individually reasonable; the file only ever grows, because removing a rule feels riskier than adding one (see Maintenance Decay in [[Lecture 04. Split Instructions Across Files]]). This is why the fix is architectural (splitting into an [[Entry File]] plus topic documents) rather than editorial (writing tighter prose in the same file).

Bloat compounds with [[Lost in the Middle]]: the more the file grows, the more of it sits in the position where the model is least likely to actually use it.

## Related

- [[Entry File]]
- [[Lost in the Middle]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Harness Engineering]]
