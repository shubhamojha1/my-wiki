---
title: "Three-Layer Termination Validation"
type: concept
tags: [ai-agents, verification, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/"]
---

# Three-Layer Termination Validation

Three-layer termination validation is [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]'s concrete structural fix for [[Premature Completion Declaration]]: a layered sequence of checks, none of which can be skipped, that replaces the agent's subjective sense of "done" with objective, executed evidence.

1. **Layer 1 — Syntax and Static Analysis**: cheapest to run, least informative, but mandatory — get the spelling right before reading further.
2. **Layer 2 — Runtime Behavior Verification**: the application actually starts, critical paths execute. This is the core evidence that a feature is *runnable*, not just written.
3. **Layer 3 — System-Level Confirmation**: end-to-end testing, integration validation, real user-scenario simulation. The last line of defense — proof the feature is *correct*, not just runnable.

The lecture's reasoning for why Layer 2 alone (passing unit tests) isn't enough: unit tests isolate units and mock dependencies, so they structurally cannot catch cross-component problems like an interface mismatch (relative vs. absolute path expectations between a renderer and a preload script), state propagation errors (a DB migration changes schema but an ORM cache still holds the old shape), or environment-dependent failures (works in test, breaks in the real environment's config/network/service availability).

Termination judgment should be **externalized**, not made by the agent — the harness independently runs this validation using [[Runtime Feedback Signals|runtime signals]] (app reached ready state, critical paths executed, DB writes/file ops/side effects correct, temp resources cleaned up), and only advances between layers on a pass.

Layer 3 also enforces the **completion priority constraint** — see [[Completion Priority Constraint]] — and both the spec-correctness and system-requirements halves of the check are sometimes called the **verification-validation dual gate** — see [[Verification-Validation Dual Gate]].

A related tactic for making failures actionable: error messages should include repair instructions, not just a failure state. Instead of "Test failed," give the agent something like "Test failed: POST /api/reset-password returned 500. Check that the email service config exists in environment variables. The template file should be at templates/reset-email.html" — specific enough that the agent can actually self-correct instead of guessing.

## Related

- [[Premature Completion Declaration]]
- [[Verification-Validation Dual Gate]]
- [[Completion Priority Constraint]]
- [[Completion Evidence]]
- [[Definition of Done]]
- [[Confidence Calibration Bias]]
