---
title: "Agent State ACID Principles"
type: concept
tags: [ai-agents, state-management, harness-engineering]
created: 2026-07-07
sources: ["https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/", "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/"]
---

# Agent State ACID Principles

The lecture borrows the database [[ACID Transactions|ACID]] model as an analogy for managing agent state — not a claim that agent state is a database transaction, but a mapping onto the same four concerns:

| Property | Database meaning | Agent state meaning |
|---|---|---|
| Atomicity | All-or-nothing transaction execution | One git commit per logical operation — no half-applied changes left in the repo |
| Consistency | Valid state before/after, integrity constraints hold | Verification predicates confirm the repo is actually in the state the agent claims |
| Isolation | Concurrent transactions don't interfere | Separate progress files or branches so concurrent agent sessions don't race on the same state |
| Durability | Committed data survives failures | Critical knowledge is persisted in git-tracked files, not ephemeral session memory |

This gives [[Agent State Management]] a concrete checklist instead of a vague "preserve progress" mandate: does state survive a crash (durability), does concurrent work collide (isolation), can you verify the claimed state is real (consistency), and is each update atomic enough to not leave the repo half-updated (atomicity)?

[[Lecture 12. Leave a Clean Handoff at the End of Every Session|Lecture 12]] names the same atomicity property again from the session-boundary angle as **session integrity**: a session either leaves all five [[Harness Initialization Flow|clean-state conditions]] true, or it's treated as incomplete — no partial credit, the same all-or-nothing framing as atomicity above, just applied to an entire session rather than a single commit.

## Related

- [[ACID Transactions]]
- [[Agent State Management]]
- [[System of Record]]
- [[Harness Engineering]]
- [[Harness Initialization Flow]]
