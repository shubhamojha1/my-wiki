---
title: "Redlock"
type: concept
tags: [redis, locking, distributed-systems]
created: 2026-05-11
sources: [kleppmann-distributed-locking]
---

# Redlock

**Redlock** is a distributed lock algorithm built on Redis, designed by Salvatore Sanfilippo (antirez). It attempts to achieve fault-tolerant locking by requiring a majority of 5 Redis nodes to agree on lock ownership.

## Algorithm

1. Client gets current time in milliseconds
2. Acquires lock on all N (typically 5) Redis nodes sequentially with a short timeout
3. Computes elapsed time = current_time - start_time
4. Lock is acquired if client got locks on **majority** (≥ N/2 + 1) of nodes AND elapsed time < lock TTL
5. Effective lock TTL = original TTL - elapsed time

## Criticisms (Kleppmann, 2016)

| Problem | Detail |
|---------|--------|
| **No fencing tokens** | No monotonically increasing token, so stale holders can write unsafely |
| **Clock dependency** | Uses `gettimeofday` (non-monotonic), vulnerable to clock jumps |
| **Synchronous assumptions** | Assumes bounded network delay, bounded pauses, bounded clock error |
| **Safety vs liveness** | Safety depends on timing, not just liveness |

## Recommendation

- For **efficiency** locks: single Redis node (SET NX) — simpler, cheaper
- For **correctness** locks: use [[ZooKeeper]]/[[etcd]] with [[Fencing Token|fencing tokens]]

## Related

- [[Distributed Lock]] — General locking concept
- [[Fencing Token]] — Missing feature in Redlock
- [[Redis]] — Platform Redlock is built on
