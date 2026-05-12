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
Add more power to existing machines — CPU, RAM, storage (or faster SSDs).

**Pros**: Simple, lower latency (no inter-server communication), minimal code changes, cost-effective at small scale.

**Cons**: Hardware ceiling (finite CPU/RAM/storage slots), single point of failure, downtime during upgrades, disproportionately expensive at high-end.

**Good for**: Small-to-medium apps with limited growth, legacy apps with tight coupling, latency-sensitive workloads, budget-constrained projects.

### Horizontal Scaling (Scale Out)
Add more machines to distribute load behind a load balancer.

**Pros**: Near-limitless scalability, fault tolerance (node failure doesn't bring down system), cost-effective via commodity hardware.

**Cons**: Distributed system complexity (consistency, networking, coordination), inter-server latency, higher initial setup cost, may require code changes for distributed operation.

**Good for**: Rapidly growing apps, high-availability requirements, microservices architectures, workloads easily partitioned across nodes.

### Combining Both Strategies

Many successful systems combine both approaches:
- **Vertically-scaled clusters** — Powerful individual machines form the nodes of a horizontally-scaled cluster
- **Database sharding** — Data partitioned across multiple DB servers (horizontal), each server vertically scaled
- **Common pattern** — Start with vertical scaling for simplicity, switch to horizontal when hitting single-machine limits

### Decision Factors

When choosing between vertical and horizontal:
- **Cost** — Initial hardware costs vs long-term operational expenses
- **Workload** — CPU-bound, memory-bound, or distributable across nodes?
- **Architectural complexity** — Can the application code handle distributed workloads?
- **Future growth** — How much scaling is realistically anticipated?

### Key Patterns
- **Stateless services** — Store state in shared store (Redis)
- **Load balancing** — Distribute across servers
- **Auto-scaling** — Adjust based on load
- **Database scaling** — Read replicas, sharding
- **Caching** — Reduce DB load