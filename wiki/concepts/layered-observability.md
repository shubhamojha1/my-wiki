---
title: "Layered Observability"
type: concept
tags: [ai-agents, observability, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Layered Observability

Layered observability is [[Lecture 11. Making the Agent's Runtime Observable]]'s architectural split into two layers, designed together rather than bolted on separately:

- **Runtime observability** — system-level signals (logs, traces, process events, health checks) that answer "what did the system do." This is the same territory as [[Runtime Feedback Signals]] from Lecture 09, generalized into a named architectural layer.
- **Process observability** — harness decision artifacts (plans, scoring rubrics, acceptance criteria) that answer "why should this change be accepted." This is new: it's not about what the code did, but about the reasoning behind whether the result counts as good.

The lecture argues both layers are essential and neither substitutes for the other: runtime observability alone tells you what happened but not whether it should count as success (the [[Verification Gap]] problem — code that ran without producing the right result); process observability alone (a well-written contract or rubric) tells you the standard but not whether reality met it without runtime evidence. See [[Task Trace]], [[Sprint Contract]], and [[Evaluator Rubric]] for the concrete artifacts in each layer.

This extends the [[Harness Engineering|Feedback Subsystem]] from Lecture 02 with a reason *why* agents specifically can't build this themselves: they don't know what signals to record, their logging drifts inconsistent across sessions, and process observability needs harness-level structure beyond whatever an agent chooses to log on its own.

## Related

- [[Task Trace]]
- [[Sprint Contract]]
- [[Evaluator Rubric]]
- [[Harness Engineering]]
- [[Verification Gap]]
