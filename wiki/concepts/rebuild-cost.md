---
title: "Rebuild Cost"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/"]
---

# Rebuild Cost

Rebuild cost is the time a new agent session needs to reach an executable, correctly-oriented state after a previous session ends — reading state files, verifying they match reality, and reconstructing enough understanding to keep working safely. [[Lecture 05. Keeping Context Alive Across Sessions]] targets compressing this from roughly 15 minutes down to about 3.

Rebuild cost is the concrete, measurable form of the abstract "losing continuity" problem: it's what you actually pay every time a session restarts. Good `PROGRESS.md`/[[Decision Log]] artifacts and an explicit [[Harness Initialization Flow]] are the direct levers for lowering it; unmanaged [[Drift]] is what makes it creep back up over time.

[[Lecture 06. Make the Agent Initialize Before Every Work Session|Lecture 06]] names a companion, first-time-only version of this metric: "time from start to first passing test," measured against a project's [[Initialization Phase]] rather than against a mid-project session restart. That lecture's case study found 20 minutes spent on dedicated initialization recovered itself and cut total rebuild time by 60% versus skipping straight to implementation.

## Related

- [[Drift]]
- [[Harness Initialization Flow]]
- [[Decision Log]]
- [[Agent State Management]]
- [[Compaction vs. Reset]]
- [[Initialization Phase]]
