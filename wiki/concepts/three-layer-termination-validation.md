---
title: "Three-Layer Termination Validation"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Three-Layer Termination Validation

Three-layer termination validation is [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]'s concrete structural fix for [[Premature Completion Declaration]]: a layered sequence of checks, none of which can be skipped, that replaces the agent's subjective sense of "done" with objective, executed evidence.

1. **Layer 1 — Syntax and Static Analysis**: cheapest to run, least informative, but mandatory — get the spelling right before reading further.
2. **Layer 2 — Runtime Behavior Verification**: the application actually starts, critical paths execute. This is the core evidence that a feature is *runnable*, not just written.
3. **Layer 3 — System-Level Confirmation**: end-to-end testing, integration validation, real user-scenario simulation. The last line of defense — proof the feature is *correct*, not just runnable.

[[Lecture 10. Only a Full Pipeline Run Counts as Real Verification|Lecture 10]] frames the same gradient in test-pyramid terms instead — Level 1 unit tests (required), Level 2 integration tests (required), Level 3 end-to-end tests (required for cross-component changes) — calling it the **testing adequacy gradient**: detection capability increases at each level. It's the same structure as Layers 1-3 above, not a competing one.

The lecture's reasoning for why Layer 2 alone (passing unit tests) isn't enough: unit tests isolate units and mock dependencies, so they structurally cannot catch **component boundary defects** — cross-component problems that only surface once pieces are wired together. Four named categories:

1. **Interface Mismatch** — components expect different data formats (e.g. relative vs. absolute path expectations between a renderer and a preload script) but pass isolated tests anyway.
2. **State Propagation Errors** — cross-layer inconsistencies, e.g. a DB migration changes schema but an ORM cache still holds the old shape.
3. **Resource Lifecycle Issues** (Lecture 10) — file handles, connections, or sockets leaking across component boundaries; nothing in an isolated unit test exercises the full lifecycle.
4. **Environment Dependency** — code that works in a mocked environment but fails in production due to configuration, latency, or service-availability differences.

Lecture 10's case study: an Electron file-export feature with five defects across these categories. Unit tests caught zero of five; end-to-end tests caught all five. Test time rose from 2 seconds to 15 — judged an acceptable trade. Critically, the lecture argues E2E testing doesn't just *detect* more defects, it *changes how the agent codes*: with E2E in the loop, agents start considering component interactions, respecting architectural boundaries, and handling error paths more thoroughly, because they know the check that runs will actually cross those boundaries.

Termination judgment should be **externalized**, not made by the agent — the harness independently runs this validation using [[Runtime Feedback Signals|runtime signals]] (app reached ready state, critical paths executed, DB writes/file ops/side effects correct, temp resources cleaned up), and only advances between layers on a pass.

Layer 3 also enforces the **completion priority constraint** — see [[Completion Priority Constraint]] — and both the spec-correctness and system-requirements halves of the check are sometimes called the **verification-validation dual gate** — see [[Verification-Validation Dual Gate]].

**Agent-oriented error messages**: failures should carry repair instructions, not just a failure state, structured as three explicit parts — what went wrong, why it matters, and a concrete how-to-fix. Lecture 09's example: "Test failed: POST /api/reset-password returned 500. Check that the email service config exists in environment variables. The template file should be at templates/reset-email.html." Lecture 10's example, for an architectural-boundary violation rather than a test failure: "Move this call to `preload/file-ops.ts` and invoke via `window.api`." Either way, specific enough that the agent can self-correct instead of guessing.

New defect categories caught in code review should be promoted into a permanent automated check rather than relying on a reviewer catching the same thing twice — see [[Review Feedback Promotion]]. And the boundaries this whole validation enforces need to exist before implementation starts, not be retrofitted — see [[Architectural Boundary Enforcement Rules]] and [[Layered Domain Architecture]].

## Related

- [[Premature Completion Declaration]]
- [[Verification-Validation Dual Gate]]
- [[Completion Priority Constraint]]
- [[Completion Evidence]]
- [[Definition of Done]]
- [[Confidence Calibration Bias]]
- [[Architectural Boundary Enforcement Rules]]
- [[Review Feedback Promotion]]
- [[Layered Domain Architecture]]
