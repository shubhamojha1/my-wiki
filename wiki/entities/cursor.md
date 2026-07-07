---
title: "Cursor"
type: entity
tags: [ai-agents, coding-assistant, ide]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# Cursor

Cursor is an AI-assisted code editor discussed in [[Lecture 02. What a Harness Actually Is]] as part of the lecture's tool survey. It uses `.cursorrules` files for the [[Harness Engineering|Instruction Subsystem]] and can read project structure and lint configuration for context.

Its named weakness is the [[Agent State Management|State Subsystem]]: closing the IDE loses accumulated session context, so state is not durably preserved across sessions the way the lecture recommends (e.g. via a `PROGRESS.md`).

## Related

- [[Harness Engineering]]
- [[Codex]]
- [[AutoGPT]]
- [[Lecture 02. What a Harness Actually Is]]
