---
title: "Harness Initialization Flow"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/"]
---

# Harness Initialization Flow

The harness initialization flow is a pair of explicit routines that `AGENTS.md` should specify to bookend every session:

*Not to be confused with the [[Initialization Phase]] from Lecture 06 — that's a one-time (or per-major-task) setup investment that happens before any sessions start; this is the lightweight routine every individual session repeats.*

- **Clock-in**: read the state files (`PROGRESS.md`, [[Decision Log]]), and verify they're actually consistent with the repo's real state before trusting them — this is the check that catches [[Drift]] before it compounds further.
- **Clock-out**: update progress, confirm the state being left behind is accurate, and commit the work as an atomic checkpoint (see [[Agent State ACID Principles]]).

Without an explicit clock-in/clock-out routine, persistence artifacts exist but nothing guarantees a session actually reads or updates them — they decay into stale documentation nobody trusts, which is worse than not having them (a session that distrusts `PROGRESS.md` re-derives everything from scratch anyway, paying full [[Rebuild Cost]]).

## Clean State: What "Confirm the State" Actually Means (Lecture 12)

[[Lecture 12. Leave a Clean Handoff at the End of Every Session|Lecture 12]] gives clock-out a concrete, checkable definition: a session doesn't count as ending cleanly unless all five of these hold —

1. Build passes (CI-verified).
2. All tests pass, including pre-existing ones.
3. Progress recorded in machine-readable artifacts.
4. No stale artifacts left behind (debug logs, commented-out code, TODO markers).
5. Startup path still functional for whoever runs the next session.

Skipping this isn't neutral — Lehman's laws of software evolution predict that systems under continuous change grow more complex by default, so a session that leaves state "close enough" is actively contributing to decay, not just deferring cleanup. A 12-week case study found a project without an enforced clean-state check degraded from 100% build/test pass and a 5-minute startup in week 1 to 68%/61%/60+ minutes by week 12, versus 97%/95%/9 minutes with the check enforced. See [[Cleanup Loop]] and [[Quality Document]] for the ongoing maintenance this feeds into.

## Related

- [[Drift]]
- [[Rebuild Cost]]
- [[Decision Log]]
- [[Agent State ACID Principles]]
- [[Agent State Management]]
- [[Initialization Phase]]
- [[Cleanup Loop]]
- [[Quality Document]]
