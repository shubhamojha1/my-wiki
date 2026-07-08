---
title: "Evaluator Rubric"
type: concept
tags: [ai-agents, verification, observability, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Evaluator Rubric

An evaluator rubric turns evaluation from subjective judgment into evidence-based structured scoring: quantifiable dimensions (e.g. code correctness, architecture compliance, test coverage) each with an explicit pass/fail threshold, rather than a free-text verdict like "doesn't feel right." [[Lecture 11. Making the Agent's Runtime Observable]] treats this as the concrete mechanism that makes an independent evaluator's judgment actually trustworthy — the missing piece in [[Worker/Checker Separation]] (Lecture 09), which established that separating the worker from the checker helps but didn't specify what makes the checker's judgment *reliable* rather than just *different*.

In the lecture's Anthropic DAW case study (see [[Anthropic]]), the evaluator scored across four dimensions — product depth, functionality, visual design, code quality — each with a hard threshold, using Playwright MCP to interact with the running app like a real user rather than just reading the diff. Early evaluator versions dismissed genuine issues; the fix was analyzing cases where the evaluator's judgment diverged from human judgment and refining the rubric/prompts against that gap, after which scoring became reliable. This is itself an instance of [[Review Feedback Promotion]] applied to the evaluator's own prompts rather than to the code under test.

A rubric citing concrete evidence (e.g. "WCAG AA requires 4.5:1 contrast; measured 2.1:1") rather than a vague objection is what makes evaluation reproducible across different evaluator runs — the process-observability equivalent of [[Completion Evidence]]'s "executable, not subjective" principle.

## Related

- [[Worker/Checker Separation]]
- [[Layered Observability]]
- [[Sprint Contract]]
- [[Completion Evidence]]
- [[Review Feedback Promotion]]
- [[Anthropic]]
