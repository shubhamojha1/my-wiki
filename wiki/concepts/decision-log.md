---
title: "Decision Log"
type: concept
tags: [ai-agents, documentation, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/"]
---

# Decision Log

A decision log (`DECISIONS.md`) records design decisions with their rationale: what was chosen, why the alternatives were rejected, and what constraints shaped the choice. It's the direct fix for [[Lecture 05. Keeping Context Alive Across Sessions|Lecture 05]]'s what/why loss — the observation that compaction and plain code diffs preserve *what* was built but not *why*, so a fresh session can see a decision without its justification and quietly undo it.

It complements `PROGRESS.md` rather than replacing it: `PROGRESS.md` tracks *where things stand* (commit hash, test status, next steps), while the decision log tracks *why things stand there* — the reasoning a new session needs to avoid re-litigating settled questions or reversing deliberate trade-offs.

## Related

- [[Rebuild Cost]]
- [[Compaction vs. Reset]]
- [[Agent State Management]]
- [[System of Record]]
- [[Agent State ACID Principles]]
