---
title: "Single Point of Failure (SPOF)"
type: concept
tags: [system-design, fault-tolerance]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/single-point-of-failure-spof"]
---

# Single Point of Failure (SPOF)

A **Single Point of Failure (SPOF)** is any component whose failure would cause the entire system to stop functioning.

## Common SPOFs

| Component | Problem | Solution |
|-----------|---------|----------|
| Single load balancer | LB fails → all traffic stops | Standby LB |
| Single database | DB fails → data unavailable | Replication |
| Single app server | Server fails → app down | Horizontal scaling |
| Single network link | Link fails → no connectivity | Multiple paths |

## How to Identify

Ask for each component: **"What if this fails?"**

If answer = "system stops" → it's a SPOF.

## Strategies to Eliminate

1. **Redundancy** — Multiple backup components
2. **Load balancing** — Distribute + route around failures
3. **Data replication** — Copy across locations
4. **Geographic distribution** — Multi-region
5. **Graceful degradation** — Core functions work

## Related Concepts

[[Redundancy]], [[Fault Tolerance]], [[Load Balancing]], [[Availability]]