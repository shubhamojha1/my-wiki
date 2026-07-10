---
title: "Saga Pattern"
type: concept
tags: [distributed-systems, transaction, sharding, microservices]
created: 2026-07-10
sources: ["hellointerview-sharding"]
---

# Saga Pattern

A way to maintain data consistency across multiple shards or services without a distributed transaction, by breaking one logical operation into a sequence of local transactions — each with a corresponding **compensating transaction** that undoes it if a later step fails.

## Why It Exists

[[Two-Phase Commit (2PC)|Two-Phase Commit]] guarantees atomicity across nodes but is blocking — a coordinator or participant failure can leave the system stuck holding locks until recovery. Sagas trade strict atomicity for availability: each step commits locally and immediately, and failures are handled by rolling forward through compensations rather than blocking until every participant agrees.

## How It Works

```
Step 1: Reserve inventory     (local transaction, commits immediately)
Step 2: Charge payment        (local transaction, commits immediately)
Step 3: Create shipment       (fails)

Compensation, in reverse:
  Undo Step 2: Refund payment
  Undo Step 1: Release inventory
```

Each step's compensating action must be designed up front — this is the real cost of the pattern: business logic has to anticipate failure at every step, not just the transaction coordinator.

## Coordination Styles

- **Choreography** — each service publishes an event on completing its step; the next service reacts to that event. No central coordinator, but the overall flow is implicit and harder to trace.
- **Orchestration** — a central saga coordinator explicitly calls each step and triggers compensations on failure. Easier to reason about and debug, at the cost of a coordinating component.

## Trade-offs vs. 2PC

| | 2PC | Saga |
|---|---|---|
| Atomicity | Strong (all-or-nothing) | Eventual (compensations can lag) |
| Availability during failure | Blocks until recovery | Non-blocking; compensations run async |
| Isolation | True isolation until commit | None — intermediate states are visible to other transactions |
| Complexity | Simpler to reason about atomically | Requires designing a compensating action per step |

## When to Use

Sagas fit multi-shard or multi-service workflows where availability matters more than strict isolation, and where each step's effect can realistically be undone (refund a charge, release a reservation, cancel a shipment). They don't fit operations that can't be compensated after the fact (e.g. sending an email is easy to "undo" by sending a correction, but not truly reversible).

## Related Concepts

- [[Two-Phase Commit (2PC)]] — the alternative this pattern avoids the blocking cost of
- [[Cross-Shard Query]] — the read-side counterpart to this write-side consistency problem
- [[Database Sharding]] — the context where cross-shard transaction consistency becomes a design decision
- [[Eventual Consistency]] — the consistency model sagas implicitly accept between steps
