---
title: "Task Trace"
type: concept
tags: [ai-agents, observability, research, harness-engineering]
created: 2026-07-08
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/"]
---

# Task Trace

A task trace is a complete decision-path record from the start of a task to its completion. [[Lecture 11. Making the Agent's Runtime Observable]] draws the analogy explicitly to distributed-systems request tracing, citing Google's Dapper paper (Sigelman et al.) as the foundational reference — the same kind of real external citation as Guo et al. (2017) for [[Confidence Calibration Bias]] and Liu et al. (2023) for [[Lost in the Middle]].

The lecture recommends standardizing this with OpenTelemetry conventions: a trace per session, a span per task, sub-spans per verification step, using standard attributes so existing distributed-tracing tools (Jaeger, Zipkin) can consume the output directly rather than needing a bespoke viewer.

A task trace is the concrete artifact underlying **runtime observability** in [[Layered Observability]] — it's what makes "what did the system actually do" answerable after the fact instead of reconstructed from memory.

## Related

- [[Layered Observability]]
- [[Runtime Feedback Signals]]
- [[Three-Layer Termination Validation]]
- [[Harness Engineering]]
