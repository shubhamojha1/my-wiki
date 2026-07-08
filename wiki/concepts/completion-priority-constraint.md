---
title: "Completion Priority Constraint"
type: concept
tags: [ai-agents, task-scoping, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Completion Priority Constraint

The completion priority constraint is [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]'s ordering rule: verify functional correctness first, then address performance, and only then handle style — with no refactoring permitted until core functionality has actually passed verification.

The lecture names the specific failure this prevents: agents frequently start refactoring, optimizing performance, or polishing style before core functionality is verified. Doing so moves the boundary between verified and unverified code and risks silently breaking previously-working paths — premature optimization becomes a new source of risk instead of an improvement, layered on top of a feature that was never confirmed to work in the first place.

This is a companion rule to [[Three-Layer Termination Validation]]: the layers establish *what* must be checked before declaring done; the completion priority constraint establishes *in what order* work should happen so that "done" isn't a moving target the agent keeps editing underneath its own verification.

## Related

- [[Three-Layer Termination Validation]]
- [[Premature Completion Declaration]]
- [[WIP Limit]]
