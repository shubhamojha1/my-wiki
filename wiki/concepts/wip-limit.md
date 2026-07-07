---
title: "WIP Limit"
type: concept
tags: [ai-agents, task-scoping, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/"]
---

# WIP Limit

A WIP (work-in-progress) limit is the Kanban principle of capping how many tasks can be active simultaneously. [[Lecture 07. Draw Clear Task Boundaries for Agents]] argues WIP=1 is the safe default for agents: only one task active at a time, and the next one starts only after the current one passes end-to-end verification (see [[Completion Evidence]]).

The mechanism that makes this work is **completion pressure**: a WIP limit is a constraining force that requires finishing before starting anything new, which directly counters [[Overreach and Under-finish]] rather than just asking the agent to be more disciplined about scope. In the lecture's case study, a REST API project run with WIP=1 wrote *more* total code (~1200 lines vs. ~800) than the unconstrained version and finished more than twice as much work (87.5% vs. 37.5% final completion) — the constraint didn't slow output, it redirected it toward finishing.

## Related

- [[Overreach and Under-finish]]
- [[Completion Evidence]]
- [[Scope Surface]]
- [[Capability Gap]]
