---
title: "Harness Primitive"
type: concept
tags: [ai-agents, harness-engineering, architecture]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/"]
---

# Harness Primitive

A harness primitive is a machine-readable artifact that other harness components — not just humans — read from and depend on to function. [[Lecture 08. Use Feature Lists to Constrain What the Agent Does]] draws the line sharply: "documents are for humans to read; primitives are for systems to execute." A `PROGRESS.md` narrative is a document. A feature list with a fixed schema that a scheduler, verifier, and progress tracker all parse is a primitive.

The distinction matters because a primitive can't be quietly bypassed the way a prose convention can — it behaves more like a database-level constraint than a linted style rule. A feature can't silently become "done" if nothing but a passing verification command is allowed to flip its state (see [[Scope Surface]] and [[Completion Evidence]]).

## The Feature List as a Primitive

The lecture names four harness components that depend directly on the feature list, not on any other artifact:

1. **Scheduler** — selects the next `not_started` feature.
2. **Verifier** — runs verification commands and approves state transitions.
3. **Handoff reporter** — generates session summaries automatically from feature states.
4. **Progress tracker** — measures project health metrics.

This is why the feature list must be a single source of truth: if any of these four components read scope information from somewhere else (a comment, a chat message, a stale doc), they can silently diverge from each other.

## Related

- [[Scope Surface]]
- [[Completion Evidence]]
- [[System of Record]]
- [[WIP Limit]]
- [[Harness Engineering]]
