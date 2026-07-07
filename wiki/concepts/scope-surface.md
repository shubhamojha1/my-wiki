---
title: "Scope Surface"
type: concept
tags: [ai-agents, task-scoping, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/"]
---

# Scope Surface

A scope surface is a DAG (directed acyclic graph) of a project's work units, externalized into a machine-readable repo file (JSON or Markdown), tracking each task through four possible states. [[Lecture 07. Draw Clear Task Boundaries for Agents]] recommends this so a fresh session can immediately see what's done, in progress, or blocked without re-deriving it from conversation or code inspection.

This is related to but distinct from `PROGRESS.md`/[[Decision Log]] from [[Agent State Management]]: those capture narrative progress and reasoning ("what happened and why"), while the scope surface is specifically the structured dependency graph of *tasks and their states* — the artifact a [[WIP Limit]] policy checks against to decide whether a new task is allowed to start.

## Related

- [[WIP Limit]]
- [[Completion Evidence]]
- [[Overreach and Under-finish]]
- [[Agent State Management]]
- [[System of Record]]
