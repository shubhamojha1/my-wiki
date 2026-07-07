---
title: "System of Record"
type: concept
tags: [ai-agents, documentation, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/"]
---

# System of Record

The repository as system of record means the repo is the final authority on project decisions, architecture, execution state, and verification standards — not merely the place the code happens to live. This sharpens Lecture 02's "the repo IS the spec" framing (see [[Harness Engineering]]) into an explicit ownership claim: if a decision matters to how the agent should behave, it belongs in a repo-tracked file, not in a side channel.

The recommended structure for realizing this:

- `AGENTS.md` at the repo root — project overview, commands, constraints.
- `ARCHITECTURE.md` per module directory — design context located next to the code it describes.
- `CONSTRAINTS.md` — hard constraints called out on their own.
- `PROGRESS.md` — status tracking, feeding [[Agent State Management]].

Four principles keep this structure from rotting: knowledge lives adjacent to the code it describes, standardized entry files enable fast orientation, documentation stays minimal but complete, and updates are synchronized with code changes so the [[Knowledge Visibility Gap]] doesn't quietly reopen.

## Related

- [[Knowledge Visibility Gap]]
- [[Fresh Session Test]]
- [[Harness Engineering]]
- [[Agent State Management]]
- [[Agent State ACID Principles]]
