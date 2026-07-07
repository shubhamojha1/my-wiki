---
title: "AutoGPT"
type: entity
tags: [ai-agents, coding-assistant, cautionary-example]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/"]
---

# AutoGPT

AutoGPT is used in [[Lecture 02. What a Harness Actually Is]] as a cautionary example of a missing [[Agent State Management|State Subsystem]]. Without structured state management, context accumulates without bound during long-running tasks, producing loops and eventual failure.

The lecture is explicit that this is a harness architecture problem, not evidence of a weaker model — the same framing it uses throughout: attribute the failure to the missing subsystem, not to the model.

## Related

- [[Harness Engineering]]
- [[Agent State Management]]
- [[Context Anxiety]]
- [[Lecture 02. What a Harness Actually Is]]
