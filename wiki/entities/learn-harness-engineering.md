---
title: "Learn Harness Engineering"
type: entity
tags: [ai-agents, education, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Learn Harness Engineering

`Learn Harness Engineering` is a lecture series about making coding agents reliable through better task framing, repository conventions, validation, and state management.

Lecture 01 argues that model capability is only one input to success — the harness around the model determines whether the agent can understand the task, execute it cleanly, and prove that it is finished. Lecture 02 follows up with a precise structural definition: a harness is exactly five subsystems (instruction, tool, environment, state, feedback), and a project can be audited against that model directly. Lecture 03 sharpens the Instruction and State subsystems further, arguing the repo must be an authoritative [[System of Record]], not just code storage, and giving concrete tools ([[Fresh Session Test]], [[Agent State ACID Principles]]) to check that it actually is. Lecture 04 zooms into the Instruction Subsystem specifically: why instruction files balloon over time ([[Instruction Bloat]]), why that's actively harmful rather than just wasteful ([[Lost in the Middle]]), and how to split one giant file into an [[Entry File]] plus topic documents. Lecture 05 zooms into the State Subsystem: why bigger context windows can't fix cross-session continuity loss, why compaction preserves the "what" of a decision but drops the "why" ([[Decision Log]]), and what an explicit [[Harness Initialization Flow]] looks like.

## What It Covers

- [[Harness Engineering]]
- [[Capability Gap]]
- [[Verification Gap]]
- [[Diagnostic Loop]]
- [[Definition of Done]]
- [[Context Anxiety]]
- [[Agent State Management]]
- [[Controlled Variable Exclusion Test]]
- [[Knowledge Visibility Gap]]
- [[System of Record]]
- [[Fresh Session Test]]
- [[Agent State ACID Principles]]
- [[Instruction Bloat]]
- [[Lost in the Middle]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Entry File]]
- [[Rebuild Cost]]
- [[Drift]]
- [[Compaction vs. Reset]]
- [[Decision Log]]
- [[Harness Initialization Flow]]

## Related

- [[Walking Labs]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 02. What a Harness Actually Is]]
- [[Lecture 03. Making the Repository the Single Source of Truth]]
- [[Lecture 04. Split Instructions Across Files]]
- [[Lecture 05. Keeping Context Alive Across Sessions]]
