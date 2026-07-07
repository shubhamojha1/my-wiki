---
title: "Agent State Management"
type: concept
tags: [ai-agents, state-management, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/"]
---

# Agent State Management

Agent state management is the part of harness engineering that preserves useful work across sessions.

Lecture 01 treats the repository as the system of record. Notes, architectural decisions, and partially completed work should live somewhere persistent so a fresh session does not have to rediscover the same facts from scratch.

[[Lecture 03. Making the Repository the Single Source of Truth|Lecture 03]] gives this a concrete structure: a `PROGRESS.md` tracking completed work, in-progress items, and blockers as part of the [[System of Record]], plus [[Agent State ACID Principles]] as a checklist for whether that state is actually durable, isolated, consistent, and atomically updated.

## Related

- [[Harness Engineering]]
- [[Diagnostic Loop]]
- [[Context Anxiety]]
- [[Codex]]
- [[System of Record]]
- [[Agent State ACID Principles]]
