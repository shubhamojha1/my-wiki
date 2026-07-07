---
title: "Compaction vs. Reset"
type: concept
tags: [ai-agents, context-window, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Compaction vs. Reset

Compaction and reset are two different strategies for continuing work once a session's context is running out, with different failure modes:

- **Compaction** summarizes the current session's context in place, staying within the same session. It's cheap, but risks losing the *why* behind decisions — compaction strategies typically compress down to final code (the "what"), discarding the intermediate reasoning that justified it. See the what/why loss described in [[Lecture 05. Keeping Context Alive Across Sessions]].
- **Reset** ends the session and starts a fresh one that reconstructs its understanding entirely from persisted artifacts (`PROGRESS.md`, [[Decision Log]], git history). This is architecturally cleaner — no risk of a bad in-session summary — but its quality is a direct function of how good those persisted artifacts are. A reset with a weak `PROGRESS.md` is worse than a good compaction.

Neither is a strictly better default: compaction is the pragmatic in-session fallback, while reset is only as reliable as the [[Harness Engineering|State Subsystem]] backing it. Choosing well means investing in persistence artifacts good enough that reset is the safe option, rather than leaning on compaction to paper over missing state.

## Related

- [[Rebuild Cost]]
- [[Drift]]
- [[Decision Log]]
- [[Context Anxiety]]
- [[Agent State Management]]
