---
title: "Lecture 11. Making the Agent's Runtime Observable"
type: source
tags: [ai-agents, harness-engineering, coding-agents, observability]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Lecture 11. Making the Agent's Runtime Observable

Source: [[Learn Harness Engineering]] by [[Walking Labs]]. Eleventh in the series, following [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]].

## Thesis

Without observability into runtime state, agents make decisions under uncertainty. Observability has to be built into the harness architecture itself, not left for agents to improvise — echoing but going deeper than Lecture 02's Feedback Subsystem (see [[Harness Engineering]]).

## Why Agents Can't Self-Solve Observability

1. Agents don't know which signals they should even be recording.
2. Log formats drift inconsistent across sessions, blocking systematic analysis.
3. Process observability (contracts, rubrics — see below) needs harness-level support; it isn't something more agent logging can produce on its own.

## The Real Cost of Missing Observability

1. **Correctness vs. appearance** — code review shows what was written; runtime tracing shows what actually executed. Boundary-condition errors only surface through execution traces.
2. **Evaluation becomes subjective** — without scoring rubrics and acceptance criteria, different evaluators reach contradictory conclusions about the same output, making quality non-reproducible.
3. **Retries become blind** — when failure reasons are opaque, an agent retries randomly, sometimes "fixing" unrelated code while the actual root cause goes untouched. Wastes tokens and time.
4. **Session handoff inefficiency** — Anthropic observed incomplete work handed to a new session costs 30-50% of that session's time on redundant re-diagnosis of system state.

## Layered Observability

Two layers, designed together rather than bolted on separately:

- **Runtime observability** — system-level signals (logs, traces, process events, health checks) answering "what did the system do."
- **Process observability** — harness decision artifacts (plans, scoring rubrics, acceptance criteria) answering "why should this change be accepted."

See [[Layered Observability]].

## Core Artifacts

- **[[Task Trace]]**: a complete decision-path record from start to completion — explicitly analogous to distributed-systems request tracing (the lecture cites Google's Dapper paper, Sigelman et al., as the foundational reference).
- **[[Sprint Contract]]**: a pre-coding agreement specifying task scope, verification standards, and exclusions, negotiated before implementation starts.
- **[[Evaluator Rubric]]**: turns evaluation from subjective judgment into evidence-based structured scoring across named dimensions with explicit thresholds — the mechanism that makes [[Worker/Checker Separation]] (Lecture 09) actually reliable rather than just "a second opinion."

## Building It: Four Steps

1. **Runtime signal collection**: app lifecycle states (startup/ready/running/shutdown), feature-path execution records with entry points and checkpoints, data flow between components, resource utilization, full error context.
2. **Sprint contracts**: structured pre-task negotiation of scope, verification standards, exclusions.
3. **Evaluator rubrics**: quantifiable scoring (e.g. code correctness, architecture compliance, test coverage) with explicit pass/fail thresholds.
4. **OpenTelemetry standardization**: a trace per session, a span per task, sub-spans per verification step, using standard attributes so tools like Jaeger and Zipkin can consume them directly.

## Illustrative Scenario: Dark Mode

Without observability: a planner-generator-evaluator workflow flounders on vague requirements, the evaluator rejects with unmeasured objections ("doesn't feel right"), and blind retries burn 45 minutes for a barely-acceptable result. With a sprint contract (which components to modify, verification standard per component, explicit exclusions) plus runtime traces plus an evaluator rubric citing evidence ("WCAG AA requires 4.5:1 contrast; measured 2.1:1"), the same task finishes in 15 minutes at high quality — a 3x efficiency difference with observability as the single variable.

## Case Study: Anthropic's Three-Agent DAW Experiment (March 2026)

**This is a distinct experiment from the 2D-game-editor case study already in this wiki from [[Lecture 01. Strong Models Don't Mean Reliable Execution|Lecture 01]] and [[Lecture 09. Preventing Agents from Declaring Victory Too Early|Lecture 09]]** — different task, different roles, different numbers. Building a browser-based DAW (Digital Audio Workstation) using the Web Audio API, with three specialized roles:

- **Planner** — expands a 1-4 sentence requirement into a full product spec, staying at product-context level rather than jumping to premature technical detail.
- **Generator** — implements feature by feature, negotiating a sprint contract before each sprint, self-evaluating before handoff.
- **Evaluator** — uses Playwright MCP to interact with the running app like a real user, scoring across four dimensions (product depth, functionality, visual design, code quality), each with a hard pass/fail threshold.

| Phase | Time | Cost |
|---|---|---|
| Planner | 4.7 min | $0.46 |
| Build round 1 | 2 hr 7 min | $71.08 |
| QA round 1 | 8.8 min | $3.24 |
| Build round 2 | 1 hr 2 min | $36.89 |
| QA round 2 | 6.8 min | $3.09 |
| Build round 3 | 10.9 min | $5.88 |
| QA round 3 | 9.6 min | $4.06 |
| **Total** | **3 hr 50 min** | **$124.70** |

Early evaluator versions dismissed real issues prematurely; the fix was analyzing logs where the evaluator's judgment diverged from human judgment, then refining the QA prompts against that gap — after which evaluator scoring became reliable. Sample evidence-backed QA feedback: "Visually impressive but DAW features are presentational only — clips can't be dragged, no instrument UI panel, no visual effects editor." An eleventh capability-gap data point. See [[Capability Gap]] and [[Anthropic]].

## Related Pages

- [[Harness Engineering]]
- [[Layered Observability]]
- [[Task Trace]]
- [[Sprint Contract]]
- [[Evaluator Rubric]]
- [[Worker/Checker Separation]]
- [[Anthropic]]
- [[Capability Gap]]
- [[Learn Harness Engineering]]
- [[Walking Labs]]
- [[Lecture 10. Only a Full Pipeline Run Counts as Real Verification]]
