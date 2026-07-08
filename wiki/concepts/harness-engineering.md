---
title: "Harness Engineering"
type: concept
tags: [ai-agents, software-engineering, automation]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Harness Engineering

Harness engineering is the practice of making a model usable by building the surrounding system correctly. The harness is everything in the engineering infrastructure outside the model weights: task specification, tool access, environment setup, verification, and state management. [[Lecture 01. Strong Models Don't Mean Reliable Execution|Lecture 01]] treats it as the main lever for turning capable models into reliable agents; [[Lecture 02. What a Harness Actually Is|Lecture 02]] gives it a precise, checkable structure.

## Core Framing

- **"The repo IS the spec"**: all necessary context should live in the repository — structured instruction files, explicit verification commands, clear directory organization — not in a developer's head or a chat thread.
- **"Anything the agent cannot see, for all practical purposes, does not exist."** This is the sharper, operational form of the same idea.
- **[[Lecture 03. Making the Repository the Single Source of Truth|Lecture 03]]** sharpens this further into [[System of Record]]: the repo is the *authority*, not just the code's home. It names the gap directly as [[Knowledge Visibility Gap]] — knowledge that lives only in people's heads or side channels — and gives a concrete way to check for it, the [[Fresh Session Test]].

## Recommended Repository Structure (Lecture 03)

- `AGENTS.md` at the repo root — project overview, commands, constraints.
- `ARCHITECTURE.md` per module directory — design context located next to the code it describes.
- `CONSTRAINTS.md` — hard constraints called out on their own.
- `PROGRESS.md` — status tracking, feeding [[Agent State Management]].

Four principles keep this from rotting: knowledge lives adjacent to the code it describes; standardized entry files enable fast orientation; documentation stays minimal but complete; and updates stay synchronized with code changes, or the Knowledge Visibility Gap quietly reopens (Lecture 03 calls this rising "Knowledge Decay Rate"). Discovery Cost — the context an agent burns hunting for something that should have been immediately visible — is the everyday symptom of getting this structure wrong.

## Instruction File Architecture (Lecture 04)

`AGENTS.md` itself tends to balloon over time via "add a rule every time something fails" — see [[Instruction Bloat]]. That growth actively hurts: it eats context budget, and because LLMs attend to mid-document content worse than to the start or end ([[Lost in the Middle]], Liu et al. 2023), the constraints that get buried in the middle of a long file are the ones most likely to be ignored regardless of how important they are.

The fix is architectural, not editorial — split into an [[Entry File]] (50-200 lines: overview, first-run commands, max 15 hard constraints, links to topic docs with applicability conditions) plus topic documents (50-150 lines each, in `docs/`) pulled in only when relevant. Every instruction should carry its source, applicability condition, and expiry condition so audits can track [[Instruction Signal-to-Noise Ratio]] and prune what's stale, rather than letting the file only ever grow.

## The Five Subsystems (Lecture 02)

A complete harness needs all five; missing any one produces an incomplete harness:

1. **Instruction Subsystem** — a doc (`AGENTS.md`/`CLAUDE.md`) with project overview, tech stack + versions, first-run commands, hard constraints, links to deeper docs.
2. **Tool Subsystem** — least-privilege tool access. Too little access (e.g. no shell) blocks the agent from doing the work at all, not just from doing it well.
3. **Environment Subsystem** — self-describing environment state: dependency locks (`pyproject.toml`/`package.json`), runtime pins (`.nvmrc`/`.python-version`), Docker/devcontainers for reproducibility.
4. **State Subsystem** — a `PROGRESS.md` tracking completed work, in-progress items, blockers; updated before a session ends, reviewed when the next begins. See [[Agent State Management]] and [[Agent State ACID Principles]] for a structured way to reason about what "well-managed state" means.
5. **Feedback Subsystem** — explicit verification commands (tests, type check, lint, a combined check target). Lecture 02 calls this the subsystem with typically the highest ROI. See [[Verification Gap]] and [[Definition of Done]]. [[Lecture 11. Making the Agent's Runtime Observable|Lecture 11]] deepens this subsystem into [[Layered Observability]] — a runtime layer ("what did the system do," via [[Task Trace]]) and a process layer ("why should this change be accepted," via [[Sprint Contract]] and [[Evaluator Rubric]]) — and explains why agents can't build this observability themselves: they don't know what to record, their logging drifts inconsistent across sessions, and process artifacts need harness-level structure.

(Lecture 01's "five layers" — task specification, context provision, execution environment, verification feedback, state management — describe the same territory at a slightly different cut; Lecture 02's subsystem model is the more operational version and supersedes it for planning purposes.)

## Guiding Principles

- **Provide maps, not manuals**: `AGENTS.md` should function as a directory (~100 lines), not an encyclopedia — push depth into a `docs/` folder.
- **Constrain through rules, not micromanagement**: enforce invariants with executable rules rather than enumerating individual instructions.
- **Remove one component at a time**: ablate subsystems sequentially, holding the model fixed, to measure each one's marginal contribution. See [[Controlled Variable Exclusion Test]].

## Why It Matters

Weak harnesses produce avoidable failures even when the model is strong. A better harness changes the agent's behavior more than a model swap often does — demonstrated twice: Anthropic's and OpenAI's case studies in Lecture 01, and the 20% → ~100% staged rollout (same model throughout) in Lecture 02. See [[Capability Gap]].

## Related

- [[Capability Gap]]
- [[Harness-Induced Failure]]
- [[Verification Gap]]
- [[Diagnostic Loop]]
- [[Definition of Done]]
- [[Agent State Management]]
- [[Context Anxiety]]
- [[Controlled Variable Exclusion Test]]
- [[Knowledge Visibility Gap]]
- [[System of Record]]
- [[Fresh Session Test]]
- [[Agent State ACID Principles]]
- [[Instruction Bloat]]
- [[Lost in the Middle]]
- [[Instruction Signal-to-Noise Ratio]]
- [[Entry File]]
- [[Codex]]
- [[Cursor]]
- [[AutoGPT]]
- [[Layered Observability]]
- [[Task Trace]]
- [[Sprint Contract]]
- [[Evaluator Rubric]]
- [[Learn Harness Engineering]]
