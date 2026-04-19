---
title: "Consistency Model"
type: concept
tags: [distributed-systems, consistency]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

A consistency model is a contract between programmer and system, guaranteeing predictable results if specific rules are followed.

## Strong Consistency Models

### Linearizable Consistency
All operations appear to execute atomically in global real-time order.

### Sequential Consistency
All operations appear to execute atomically in some order consistent across all nodes. Distinguishable from linearizable only with full timing observability.

## Weak Consistency Models

### Client-Centric
Guarantees about single client's view (e.g., never see older values).

### Causal Consistency
Ordering respects causal relationships.

### Eventual Consistency
If no new updates, all replicas eventually agree. Without additional constraints, this is trivial/useless.

## Choice Tradeoffs
- Strong consistency = high latency, low availability during partition
- Weak consistency = low latency, high availability