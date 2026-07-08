---
title: "WIP Limit"
type: concept
tags: [ai-agents, task-scoping, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/"]
---

# WIP Limit

A WIP (work-in-progress) limit is the Kanban principle of capping how many tasks can be active simultaneously. [[Lecture 07. Draw Clear Task Boundaries for Agents]] argues WIP=1 is the safe default for agents: only one task active at a time, and the next one starts only after the current one passes end-to-end verification (see [[Completion Evidence]]).

The mechanism that makes this work is **completion pressure**: a WIP limit is a constraining force that requires finishing before starting anything new, which directly counters [[Overreach and Under-finish]] rather than just asking the agent to be more disciplined about scope. In the lecture's case study, a REST API project run with WIP=1 wrote *more* total code (~1200 lines vs. ~800) than the unconstrained version and finished more than twice as much work (87.5% vs. 37.5% final completion) — the constraint didn't slow output, it redirected it toward finishing.

[[Lecture 08. Use Feature Lists to Constrain What the Agent Does|Lecture 08]] names the same pressure from the feature-list side as **back-pressure**: any unresolved (`not_started`, `active`, or `blocked`) entry in the [[Scope Surface]] creates pressure against starting new work until it's resolved. It's the same enforcement mechanism described from two angles — the WIP policy is the rule, back-pressure is what that rule feels like from inside the state machine.

## Related

- [[Overreach and Under-finish]]
- [[Completion Evidence]]
- [[Scope Surface]]
- [[Capability Gap]]
- [[Harness Primitive]]
