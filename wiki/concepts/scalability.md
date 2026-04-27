---
title: "Scalability"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/scalability"]
---

Scalability is the ability of a system to handle growing amounts of work without degrading performance.

## Dimensions (Distributed Systems)

### Size Scalability
Adding more nodes should make the system linearly faster.

### Geographic Scalability
Using multiple data centers to reduce response time.

### Administrative Scalability
Adding more nodes should not increase administrative costs.

## Scaling Strategies (Practical)

### Vertical Scaling (Scale Up)
Add more power to existing machines — CPU, RAM, storage.
- Simple but has limits
- Single point of failure

### Horizontal Scaling (Scale Out)
Add more machines to distribute load.
- Requires stateless services
- Needs load balancer
- Better fault tolerance

### Key Patterns
- **Stateless services** — Store state in shared store (Redis)
- **Load balancing** — Distribute across servers
- **Auto-scaling** — Adjust based on load
- **Database scaling** — Read replicas, sharding
- **Caching** — Reduce DB load