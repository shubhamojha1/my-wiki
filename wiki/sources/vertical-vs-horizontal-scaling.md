---
title: "System Design: Vertical vs Horizontal Scaling"
type: source
tags: [system-design, scaling, architecture, algomaster]
created: 2026-05-12
sources: []
---

# System Design: Vertical vs Horizontal Scaling

An AlgoMaster article by Ashish Pratap Singh (Apr 2024) explaining vertical scaling (scale up) and horizontal scaling (scale out), their trade-offs, and when to use each.

## Core Concepts

### Vertical Scaling (Scaling Up)

Adding more power to an existing machine — upgrading CPU, RAM, storage.

**Pros**: Simplicity, lower latency (no inter-server communication), cost-effective initially, no major code changes.

**Cons**: Limited ceiling, single point of failure, downtime for upgrades, expensive at high-end.

### Horizontal Scaling (Scaling Out)

Adding more servers to the pool with a load balancer distributing traffic.

**Pros**: Near-limitless scalability, fault tolerance, commodity hardware cost.

**Cons**: Distributed system complexity, inter-server latency, higher initial setup cost, app may need code changes.

### Decision Factors

- Cost (initial hardware vs long-term operational)
- Workload type (CPU-bound, memory-bound, distributable?)
- Architectural complexity (can the app handle distribution?)
- Future growth (how much scaling is realistically needed?)

### Combining Both Strategies

- Vertically-scaled clusters: powerful machines as nodes in a horizontally-scaled cluster
- Database sharding: partition data across servers (horizontal), each server vertically scaled
- Common pattern: start vertical, switch to horizontal when hitting limits

## Source

- AlgoMaster: [System Design: Vertical vs Horizontal Scaling](https://blog.algomaster.io/p/system-design-vertical-vs-horizontal-scaling) (Apr 2024)
