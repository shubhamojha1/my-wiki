---
title: "Distributed Lock"
type: concept
tags: [distributed-systems, locking, consensus]
created: 2026-05-11
sources: [kleppmann-distributed-locking]
---

# Distributed Lock

A **distributed lock** ensures that among several nodes trying to do the same piece of work, only one actually does it at any given time.

## Efficiency vs Correctness

| Use Case | Failure Cost | Tolerance | Approach |
|----------|-------------|-----------|----------|
| **Efficiency** | Redundant work, extra cost | Forgiving | Single-node Redis SET NX |
| **Correctness** | Data corruption, safety violation | Zero tolerance | Consensus system + [[Fencing Token]] |

## The Process Pause Problem

A client holding a lock may pause (GC, page fault, network delay) long enough for the lock lease to expire, then resume and act as if still holding the lock:

1. Client acquires lock
2. Client pauses (GC for seconds/minutes)
3. Lock lease expires
4. Another client acquires the lock
5. Original client resumes, unaware the lock was lost
6. Both clients believe they hold the lock → corruption

## Requirements for Correctness

- **Fencing**: monotonically increasing tokens that resource servers validate
- **Fault-tolerant storage**: consensus-based registry ([[ZooKeeper]], [[etcd]], [[Raft]])
- **Leases**: time-bound locks so crashed clients don't hold locks forever

## Related

- [[Fencing Token]] — Monotonically increasing numbers for safe lock usage
- [[Redlock]] — Redis-based distributed lock algorithm (controversial)
- [[Consensus]] — Required for fault-tolerant lock services
- [[ZooKeeper]] — Popular lock service with fencing support
