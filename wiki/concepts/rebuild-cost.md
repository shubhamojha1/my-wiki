---
title: "Rebuild Cost"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Rebuild Cost

Rebuild cost is the time a new agent session needs to reach an executable, correctly-oriented state after a previous session ends — reading state files, verifying they match reality, and reconstructing enough understanding to keep working safely. [[Lecture 05. Keeping Context Alive Across Sessions]] targets compressing this from roughly 15 minutes down to about 3.

Rebuild cost is the concrete, measurable form of the abstract "losing continuity" problem: it's what you actually pay every time a session restarts. Good `PROGRESS.md`/[[Decision Log]] artifacts and an explicit [[Harness Initialization Flow]] are the direct levers for lowering it; unmanaged [[Drift]] is what makes it creep back up over time.

## Related

- [[Drift]]
- [[Harness Initialization Flow]]
- [[Decision Log]]
- [[Agent State Management]]
- [[Compaction vs. Reset]]
