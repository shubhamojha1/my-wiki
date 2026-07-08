---
title: "Scope Surface"
type: concept
tags: [ai-agents, task-scoping, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/"]
---

# Scope Surface

A scope surface is a DAG (directed acyclic graph) of a project's work units, externalized into a machine-readable repo file (JSON or Markdown), tracking each task through four possible states. [[Lecture 07. Draw Clear Task Boundaries for Agents]] recommends this so a fresh session can immediately see what's done, in progress, or blocked without re-deriving it from conversation or code inspection.

This is related to but distinct from `PROGRESS.md`/[[Decision Log]] from [[Agent State Management]]: those capture narrative progress and reasoning ("what happened and why"), while the scope surface is specifically the structured dependency graph of *tasks and their states* — the artifact a [[WIP Limit]] policy checks against to decide whether a new task is allowed to start.

## The Four States (Lecture 08)

[[Lecture 08. Use Feature Lists to Constrain What the Agent Does|Lecture 08]] names the concrete state machine underlying the scope surface: each unit of work moves through `not_started` → `active` → `blocked` → `passing`. Two rules make the machine trustworthy rather than aspirational:

- **Pass-state gating**: only a successful verification command (see [[Completion Evidence]]) can move a unit to `passing`. The agent cannot set its own state directly — this is what makes the scope surface a [[Harness Primitive]] rather than just a document.
- **Single source of truth**: all scope information for the project comes from this one structure, not from scattered comments, chat, or stale docs.

Four harness components read directly from it: a scheduler (picks the next `not_started` unit), a verifier (runs checks, approves transitions), a handoff reporter (auto-generates session summaries from current states), and a progress tracker (project health metrics).

## Related

- [[WIP Limit]]
- [[Completion Evidence]]
- [[Overreach and Under-finish]]
- [[Agent State Management]]
- [[System of Record]]
- [[Harness Primitive]]
