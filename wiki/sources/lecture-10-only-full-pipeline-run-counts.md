---
title: "Lecture 10. Only a Full Pipeline Run Counts as Real Verification"
type: source
tags: [ai-agents, harness-engineering, coding-agents]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Lecture 10. Only a Full Pipeline Run Counts as Real Verification

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Tenth in the series, following [[Lecture 09. Preventing Agents from Declaring Victory Too Early]].

## Thesis

An agent finishes an Electron app's file-export feature with all unit tests passing. Real usage reveals five component-boundary defects anyway — file path format errors, an unresponsive progress bar, memory leaks. "Problems surface the moment they are wired together." This is the same taxonomy already in this wiki from [[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]] (`[[Three-Layer Termination Validation]]`), with one addition: **Resource Lifecycle Issues** — file handles, connections, and sockets leaking across component boundaries — folded into the existing page rather than restated as new. Interface Mismatch, State Propagation Errors, and Environment Dependency are the same three categories Lecture 09 already named.

## E2E Testing Changes Behavior, Not Just Detection

The lecture's sharper point: end-to-end testing doesn't just *catch* more defects, it changes how an agent codes in the first place. With E2E in the loop, agents start considering component interactions rather than isolated functions, start respecting architectural boundaries instead of working around them, and handle error paths more thoroughly — because they know the check that will run actually crosses those boundaries.

## Architectural Boundaries Come First

OpenAI's experience is cited directly: architectural constraints have to be established "on day one," because agents copy whatever pattern already exists in the repository — a weak initial pattern propagates. OpenAI's own answer is a **Layered Domain Architecture**: fixed layers (Types → Config → Repo → Service → Runtime → UI) with strictly forward dependencies only. See [[Layered Domain Architecture]] and [[OpenAI]]/[[Codex]]. The guiding principle, echoing Lecture 02's "constrain through rules, not micromanagement": **enforce invariants, don't micromanage implementation**.

## Architectural Boundary Enforcement Rules

A boundary documented in prose can be silently violated. The fix is converting the architecture doc into an *executable* check — e.g. a grep pattern that fails the build if a renderer process directly calls a Node.js API, rather than a comment asking developers (or agents) not to. See [[Architectural Boundary Enforcement Rules]]. This is the same "documents vs. primitives" logic from [[Harness Primitive]] (Lecture 08), applied specifically to architecture rules instead of feature lists.

## Validation Hierarchy (Testing Adequacy Gradient)

The lecture frames its required levels in test-pyramid terms rather than Lecture 09's syntax/runtime/system-level naming, but it's the same underlying gradient: Level 1 unit tests (required), Level 2 integration tests (required), Level 3 end-to-end tests (required specifically for cross-component changes). Detection capability increases at each level — see the addition to [[Three-Layer Termination Validation]].

## Agent-Oriented Error Messages

Refines Lecture 09's "actionable error feedback" into a concrete three-part structure: **what** went wrong, **why** it matters, and a concrete **how to fix** it — e.g. "Move this call to `preload/file-ops.ts` and invoke via `window.api`" rather than just "call failed here."

## Review Feedback Promotion

Each new defect category a human catches in code review gets promoted into a permanent automated check — an architectural rule, a new E2E scenario, whatever catches that class of bug going forward — so the harness gets measurably stronger over time instead of relying on the same reviewer catching the same mistake indefinitely. See [[Review Feedback Promotion]].

## Case Study

Electron file-export feature, three components, five defects (interface mismatch, state propagation via IPC, resource leak, permission issue in the packaged environment, error propagation from service layer to UI). Unit tests caught **zero** of the five. End-to-end tests caught **all five**. Test time rose from 2 seconds to 15 seconds — judged an acceptable trade for catching defects that would otherwise ship. A tenth capability-gap data point. See [[Capability Gap]].

## Related Pages

- [[Harness Engineering]]
- [[Three-Layer Termination Validation]]
- [[Architectural Boundary Enforcement Rules]]
- [[Review Feedback Promotion]]
- [[Layered Domain Architecture]]
- [[Harness Primitive]]
- [[OpenAI]]
- [[Codex]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 09. Preventing Agents from Declaring Victory Too Early]]
