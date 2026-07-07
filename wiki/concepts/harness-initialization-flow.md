---
title: "Harness Initialization Flow"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Harness Initialization Flow

The harness initialization flow is a pair of explicit routines that `AGENTS.md` should specify to bookend every session:

- **Clock-in**: read the state files (`PROGRESS.md`, [[Decision Log]]), and verify they're actually consistent with the repo's real state before trusting them — this is the check that catches [[Drift]] before it compounds further.
- **Clock-out**: update progress, confirm the state being left behind is accurate, and commit the work as an atomic checkpoint (see [[Agent State ACID Principles]]).

Without an explicit clock-in/clock-out routine, persistence artifacts exist but nothing guarantees a session actually reads or updates them — they decay into stale documentation nobody trusts, which is worse than not having them (a session that distrusts `PROGRESS.md` re-derives everything from scratch anyway, paying full [[Rebuild Cost]]).

## Related

- [[Drift]]
- [[Rebuild Cost]]
- [[Decision Log]]
- [[Agent State ACID Principles]]
- [[Agent State Management]]
