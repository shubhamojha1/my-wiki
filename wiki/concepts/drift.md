---
title: "Drift"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Drift

Drift is the growing gap between what an agent believes about a repository's state and what's actually true. It compounds across session boundaries: each session that restarts from a stale or incomplete artifact inherits the previous session's inaccuracies and adds its own, and nothing forces a correction unless the harness explicitly checks for it.

This is why [[Lecture 05. Keeping Context Alive Across Sessions]] treats "verify consistency" as a required step of the clock-in half of the [[Harness Initialization Flow]] — reading `PROGRESS.md` isn't enough on its own; the session also needs to confirm the repo actually matches what the file claims before trusting it. Unchecked drift is also what makes [[Rebuild Cost]] creep upward over time even when the persistence artifacts themselves haven't changed.

## Related

- [[Rebuild Cost]]
- [[Harness Initialization Flow]]
- [[Agent State ACID Principles]]
- [[System of Record]]
