---
title: "Capability Gap"
type: concept
tags: [ai-agents, evaluation, machine-learning]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/"]
---

# Capability Gap

The capability gap is the difference between what a model can do on benchmarks and what it can do on real engineering tasks.

Lecture 01 uses SWE-bench Verified pass rates as an example. A score in the 50-60 percent range may look acceptable on paper, but it still means a large share of tasks are not solved. Real projects are harder because requirements are vague, conventions are implicit, and verification is often missing.

[[Lecture 02. What a Harness Actually Is|Lecture 02]] adds a second, more granular data point: a ~20,000-line TypeScript + React project ran the *same model* through four stages of harness improvement — basic README (20% success) → `AGENTS.md` with conventions (60%) → explicit verification commands (80%) → progress-file templates (80-100%). The entire gap closed through harness changes alone, with zero change to the model. See [[Harness Engineering]] and [[Controlled Variable Exclusion Test]] for how to isolate which subsystem is responsible for a given gap.

[[Lecture 03. Making the Repository the Single Source of Truth|Lecture 03]] adds a third data point: a 30-microservice e-commerce platform reduced agent task failure from 70% to much lower purely by centralizing scattered architectural knowledge into standardized repo documentation (`AGENTS.md`/`ARCHITECTURE.md`/`CONSTRAINTS.md`/`PROGRESS.md`) — closing the [[Knowledge Visibility Gap]] rather than changing the model.

[[Lecture 04. Split Instructions Across Files|Lecture 04]] adds a fourth: a SaaS team split a bloated 600-line instruction file into an 80-line [[Entry File]] plus topic documents. Task success rose from 45% to 72%, and — notably the first security-specific metric in this series — security-constraint compliance rose from 60% to 95%, purely from fixing [[Instruction Bloat]] and the [[Lost in the Middle]] effect.

[[Lecture 05. Keeping Context Alive Across Sessions|Lecture 05]] adds a fifth: structured state persistence (`PROGRESS.md` + [[Decision Log]] + verification records) versus a baseline lacking these mechanisms cut rebuild time by 78%, raised feature completion from 58% to 100%, and cut defect rate from 43% to 8%.

[[Lecture 06. Make the Agent Initialize Before Every Work Session|Lecture 06]] adds a sixth, citing Anthropic's long-running application development research directly: projects using a dedicated [[Initialization Phase]] showed 31% higher feature completion rates in multi-session scenarios than projects that mixed setup and implementation.

[[Lecture 07. Draw Clear Task Boundaries for Agents|Lecture 07]] adds a seventh, and the first to compare two *policies* on the same project rather than a before/after harness addition: a REST API project run unconstrained (5 simultaneous features) hit only 37.5% final completion despite ~800 lines written, versus 87.5% final completion with a [[WIP Limit|WIP=1]] policy and ~1200 lines written sequentially. See [[Overreach and Under-finish]].

[[Lecture 08. Use Feature Lists to Constrain What the Agent Does|Lecture 08]] adds an eighth: unstructured task tracking produced 20-minute diagnostic periods per new session and duplicate implementations of already-built functionality; a structured [[Scope Surface|feature list]] cut resume time to 3 minutes with zero rework, and delivered 45% higher feature completion than free-form tracking.

[[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]] adds a ninth: a password-reset feature passed all its unit tests and was declared complete, but the end-to-end flow was never run, the DB migration left the schema inconsistent, and email config was missing. Enforcing [[Three-Layer Termination Validation]] caught all three defects within the session, saving an estimated 5-10x the cost of a post-hoc fix.

[[Lecture 10. Only a Full Pipeline Run Counts as Real Verification|Lecture 10]] adds a tenth, and the sharpest ratio yet: an Electron file-export feature with five component-boundary defects. Unit tests caught zero of five. End-to-end tests caught all five. Test time rose from 2 seconds to 15 — an acceptable cost for catching every defect that would otherwise have shipped.

## Related

- [[SWE-bench]]
- [[Harness Engineering]]
- [[Verification Gap]]
- [[Harness-Induced Failure]]
- [[Controlled Variable Exclusion Test]]
- [[Knowledge Visibility Gap]]
- [[Instruction Bloat]]
- [[Decision Log]]
- [[Initialization Phase]]
- [[Overreach and Under-finish]]
- [[Scope Surface]]
- [[Three-Layer Termination Validation]]
- [[Architectural Boundary Enforcement Rules]]
