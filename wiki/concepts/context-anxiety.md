---
title: "Context Anxiety"
type: concept
tags: [ai-agents, context-window, software-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Context Anxiety

Context anxiety is the behavior some agents show when their available context is running low. They rush toward closure, skip verification, and prefer the simplest apparent fix over the best one.

Lecture 01 presents it as a real operational failure mode rather than a vague feeling. Long-running tasks need better session structure, checkpoints, and preserved state so the agent does not panic at the end of the window.

[[Lecture 05. Keeping Context Alive Across Sessions|Lecture 05]] (citing the same Anthropic research) makes the underlying constraint explicit: this isn't a problem model upgrades solve. Even a 1M-token window still gets exhausted by a sufficiently complex task, so the fix has to be structural persistence ([[Rebuild Cost]], [[Decision Log]], [[Harness Initialization Flow]]) rather than waiting for bigger windows.

## Related

- [[Verification Gap]]
- [[Agent State Management]]
- [[Harness Engineering]]
- [[Diagnostic Loop]]
- [[Rebuild Cost]]
- [[Compaction vs. Reset]]
