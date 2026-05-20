---
title: "Practical Byzantine Fault Tolerance (pBFT)"
type: concept
tags: [distributed-systems, consensus, byzantine, fault-tolerance]
created: 2026-05-11
updated: 2026-05-20
sources: [medium-consensus-distributed-system]
---

# Practical Byzantine Fault Tolerance (pBFT)

**pBFT** (Castro & Liskov, 1999) is a consensus algorithm designed to reach agreement even when up to 1/3 of nodes act maliciously or arbitrarily ([[Byzantine Failure]]). It was the first BFT algorithm practical enough for real systems, reducing BFT overhead from exponential to polynomial in the number of nodes.

## Assumptions

- Total nodes: `n ≥ 3f + 1` where `f` = max faulty nodes
- Network model: **partially synchronous** (messages eventually delivered; no permanent partition)
- Cryptographic signatures authenticate all messages (prevents forgery)

## Three-Phase Protocol

```
Client → Primary (leader)
            │
            │ PRE-PREPARE (sequence number, value)
            ↓
         Replicas (n-1 backups)
            │
            │ PREPARE (each replica broadcasts to all)
            │ (collect 2f+1 matching PREPARE msgs)
            │
            │ COMMIT (broadcast when prepared)
            │ (collect 2f+1 matching COMMIT msgs)
            ↓
         Execute + Reply to Client
            │
Client waits for 2f+1 matching replies → done
```

| Phase | Who sends | Purpose | Quorum needed |
|-------|----------|---------|---------------|
| Pre-prepare | Primary only | Assign sequence number to request | — |
| Prepare | All replicas | Confirm they received same proposal | 2f+1 |
| Commit | All replicas | Confirm ready to execute | 2f+1 |
| Reply | All replicas | Send result to client | Client waits for 2f+1 matching |

## View Change (Leader Rotation)

If the primary is suspected faulty (timeout), replicas initiate a **view change**:
1. Replicas broadcast `VIEW-CHANGE` messages.
2. When the new primary collects 2f+1 VIEW-CHANGE messages, it sends `NEW-VIEW`.
3. Replicas move to the new view and resume.

This ensures **liveness** — the system makes progress even if the leader is Byzantine.

## Complexity

- **Message complexity**: O(n²) per request — each of n replicas broadcasts to all n replicas in the Prepare and Commit phases.
- **Scalability**: Works for small clusters (n ≤ ~20). Beyond that, communication overhead dominates.

## pBFT vs Modern BFT Protocols

| Protocol | Message complexity | Key improvement |
|----------|--------------------|----------------|
| pBFT | O(n²) | First practical BFT |
| HotStuff (2018) | O(n) with leader aggregation | Linear communication; used in Diem/LibraBFT |
| Tendermint | O(n²) | BFT + PoS; used in Cosmos |
| SBFT | O(n) with collector node | Improved throughput |

## Related Concepts

- [[Byzantine Failure]] — the failure model pBFT tolerates
- [[Consensus Problem]] — the goal: agreement despite faults
- [[Byzantine Generals Problem]] — theoretical foundation
- [[Raft]] — simpler crash-fault-tolerant (non-BFT) alternative
