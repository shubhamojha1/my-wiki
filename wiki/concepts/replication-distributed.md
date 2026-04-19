---
title: "Replication (Distributed)"
type: concept
tags: [distributed-systems, data-distribution]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Replication makes copies of the same data on multiple machines, enabling more servers to participate in computation.

## Benefits

### Performance
- Additional computing power and bandwidth applicable
- Reduces distance between client and data

### Availability
- Creates additional copies
- More nodes must fail before system is unavailable

## Problems
- Independent copies must be kept in sync
- Consistency model choice is crucial

## Consistency Models

### Strong Consistency
Allows programming as-if data not replicated. Requires agreement on every operation.

### Weak Consistency
Exposes replication internals. Lower latency, higher availability.

## Patterns

### Synchronous (Eager) Replication
- Write to all N nodes before responding
- Strong guarantees, poor performance
- N-of-N approach

### Asynchronous (Lazy) Replication  
- Respond immediately, replicate later
- Poor durability, high performance
- 1-of-N approach