---
title: "Learn Harness Engineering"
type: entity
tags: [ai-agents, education, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Learn Harness Engineering

`Learn Harness Engineering` is a lecture series about making coding agents reliable through better task framing, repository conventions, validation, and state management.

Lecture 01 argues that model capability is only one input to success — the harness around the model determines whether the agent can understand the task, execute it cleanly, and prove that it is finished. Lecture 02 follows up with a precise structural definition: a harness is exactly five subsystems (instruction, tool, environment, state, feedback), and a project can be audited against that model directly. Lecture 03 sharpens the Instruction and State subsystems further, arguing the repo must be an authoritative [[System of Record]], not just code storage, and giving concrete tools ([[Fresh Session Test]], [[Agent State ACID Principles]]) to check that it actually is. Lecture 04 zooms into the Instruction Subsystem specifically: why instruction files balloon over time ([[Instruction Bloat]]), why that's actively harmful rather than just wasteful ([[Lost in the Middle]]), and how to split one giant file into an [[Entry File]] plus topic documents. Lecture 05 zooms into the State Subsystem: why bigger context windows can't fix cross-session continuity loss, why compaction preserves the "what" of a decision but drops the "why" ([[Decision Log]]), and what an explicit [[Harness Initialization Flow]] looks like. Lecture 06 argues initialization deserves its own dedicated phase entirely separate from implementation ([[Initialization Phase]]) — distinct from Lecture 05's per-session clock-in/clock-out routine — because mixing setup and feature work weakens both. Lecture 07 turns to task scoping within a session: why agents overreach and under-finish ([[Overreach and Under-finish]]), and how a [[WIP Limit]] of one, backed by executable [[Completion Evidence]] and an externalized [[Scope Surface]], fixes it. Lecture 08 sharpens that same scope surface into a precise state machine and names the broader principle behind it: a [[Harness Primitive]] is a machine-enforced artifact, not a document a human merely reads. Lecture 09 turns to why agents declare victory too early ([[Premature Completion Declaration]]), grounding it in real research on [[Confidence Calibration Bias]] and fixing it with [[Three-Layer Termination Validation]] and [[Worker/Checker Separation]]. Lecture 10 extends that same validation with a fourth blind-spot category (resource lifecycle issues) and argues end-to-end testing doesn't just catch more defects, it changes how the agent codes — backed by executable [[Architectural Boundary Enforcement Rules]] like OpenAI's [[Layered Domain Architecture]], and strengthened over time via [[Review Feedback Promotion]]. Lecture 11 deepens the Feedback Subsystem into [[Layered Observability]] — a runtime layer ([[Task Trace]]) and a process layer ([[Sprint Contract]], [[Evaluator Rubric]]) — and supplies the missing reliability mechanism for [[Worker/Checker Separation]]: an evaluator is only as good as the rubric it scores against.

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
- [[Initialization Phase]]
- [[Startup Readiness Checklist]]
- [[Overreach and Under-finish]]
- [[WIP Limit]]
- [[Completion Evidence]]
- [[Scope Surface]]
- [[Harness Primitive]]
- [[Premature Completion Declaration]]
- [[Confidence Calibration Bias]]
- [[Worker/Checker Separation]]
- [[Three-Layer Termination Validation]]
- [[Verification-Validation Dual Gate]]
- [[Completion Priority Constraint]]
- [[Architectural Boundary Enforcement Rules]]
- [[Review Feedback Promotion]]
- [[Layered Domain Architecture]]
- [[Layered Observability]]
- [[Task Trace]]
- [[Sprint Contract]]
- [[Evaluator Rubric]]

## Related

- [[Walking Labs]]
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]]
- [[Lecture 02. What a Harness Actually Is]]
- [[Lecture 03. Making the Repository the Single Source of Truth]]
- [[Lecture 04. Split Instructions Across Files]]
- [[Lecture 05. Keeping Context Alive Across Sessions]]
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]]
- [[Lecture 07. Draw Clear Task Boundaries for Agents]]
- [[Lecture 08. Use Feature Lists to Constrain What the Agent Does]]
- [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]
- [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]]
- [[Lecture 11. Making the Agent's Runtime Observable]]
