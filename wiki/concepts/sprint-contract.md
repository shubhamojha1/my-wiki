---
title: "Sprint Contract"
type: concept
tags: [ai-agents, task-scoping, observability, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Sprint Contract

A sprint contract is a pre-coding agreement specifying a task's scope, the verification standards it will be judged against, and explicit exclusions — negotiated *before* implementation starts, not inferred afterward. [[Lecture 11. Making the Agent's Runtime Observable]] frames this as the concrete artifact behind **process observability** in [[Layered Observability]]: it answers "why should this change be accepted" in advance, rather than leaving that question to be litigated at evaluation time.

This is related to but distinct from [[Scope Surface]] (Lecture 07) and [[Completion Evidence]] (Lecture 07): a scope surface tracks task *state* as work progresses, and completion evidence proves a task *is* done — a sprint contract is negotiated *before either exists*, fixing what "done" will mean and what's explicitly out of scope so the generator and evaluator aren't relitigating the boundary mid-task.

In the lecture's dark-mode example, the difference between having and not having a sprint contract was the single variable behind a 3x efficiency gain (45 minutes of blind, vague-requirement retries vs. 15 minutes with a contract specifying exactly which components to modify, the verification standard per component, and what was explicitly excluded).

## Related

- [[Layered Observability]]
- [[Scope Surface]]
- [[Completion Evidence]]
- [[Evaluator Rubric]]
