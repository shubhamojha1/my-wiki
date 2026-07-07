---
title: "Overreach and Under-finish"
type: concept
tags: [ai-agents, task-scoping, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/"]
---

# Overreach and Under-finish

Overreach is activating more tasks than optimal within a single session — the classic case is being asked for one feature and instead touching database schema, routes, components, and middleware all at once. It's quantified concretely: zero end-to-end passing tests despite substantial code written. Under-finish is the resulting low ratio of passing tasks to activated tasks.

[[Lecture 07. Draw Clear Task Boundaries for Agents]] treats these as a single cyclically-amplifying failure, not two separate problems: the more tasks an agent activates at once, the less of its finite attention each one gets (context capacity C divided across k simultaneous tasks means each gets only C/k), so more tasks finish partially, which produces more under-finish, which often reads to the agent as "there's still more to touch," inviting further overreach.

Two outside references anchor this: **Little's Law** (L = λ × W) — more work-in-progress increases lead time, and longer-lived unfinished work has a higher chance of failing before completion — and Steve McConnell's *Rapid Development*, which names scope creep as the single leading cause of project failure, independent of AI agents specifically.

The fix is structural rather than a plea for discipline: see [[WIP Limit]].

## Related

- [[WIP Limit]]
- [[Completion Evidence]]
- [[Scope Surface]]
- [[Context Anxiety]]
- [[Capability Gap]]
