---
title: "How to Do Distributed Locking"
type: source
tags: [distributed-systems, locking, redis, redlock]
created: 2026-05-11
sources: [kleppmann-distributed-locking]
---

# How to Do Distributed Locking

**Author:** Martin Kleppmann
**URL:** https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
**Published:** February 8, 2016

## Summary

A seminal critique of Redlock (Redis distributed locking algorithm) and a thorough analysis of distributed locking fundamentals — efficiency vs correctness, the process pause problem, fencing tokens, and the importance of system model assumptions.

## Key Concepts Covered

- **Two reasons for locks**: efficiency (saving cost, approximate) vs correctness (preventing corruption)
- **Process pause problem**: GC pauses, page faults, network delays can cause lock leases to expire while a client still believes it holds the lock
- **Fencing tokens**: monotonically increasing token per lock acquisition; storage server rejects writes with stale tokens
- **Redlock critique**: no fencing token facility, relies on synchronous timing assumptions, clock jumps can break safety
- **Synchronous model assumptions**: bounded network delay, bounded process pauses, bounded clock error — not realistic in practice
- **Recommendation**: single Redis for efficiency locks; ZooKeeper/etcd with fencing tokens for correctness locks
