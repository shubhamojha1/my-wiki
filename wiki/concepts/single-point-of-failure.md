---
title: "Single Point of Failure (SPOF)"
type: concept
tags: [system-design, fault-tolerance]
created: 2026-04-27
updated: 2026-05-20
sources: ["algomaster.io/learn/system-design/single-point-of-failure-spof"]
---

# Single Point of Failure (SPOF)

A **Single Point of Failure (SPOF)** is any component in a system whose failure causes the entire system (or a critical function) to stop working. Eliminating SPOFs is a core goal of high-availability system design.

## Identifying SPOFs

The test: **"What happens if this component fails right now?"**

- **SPOF**: system stops entirely or a critical function is unavailable
- **Non-SPOF**: system degrades but continues; other nodes handle the load

Useful technique: draw a failure mode diagram — trace every request path and mark any single node that can block the flow.

## Common SPOFs and Mitigations

| Component | SPOF Scenario | Mitigation |
|-----------|--------------|-----------|
| **Load balancer** | LB crashes → all traffic stopped | Active-passive LB pair; anycast; multiple LBs with DNS failover |
| **Database (primary)** | Primary fails → writes unavailable | Replication + automatic failover (Sentinel, Patroni); multi-primary |
| **DNS server** | Single DNS server → name resolution fails | Multiple nameservers; TTL caching |
| **Message broker** | Single broker → queue unavailable | Cluster replication (Kafka ISR, RabbitMQ mirrored queues) |
| **Application server** | Single instance → app down | Horizontal scaling; multiple AZs |
| **Network link** | Single switch/cable | Redundant links; ECMP routing; multi-homed BGP |
| **Authentication service** | Auth service down → no one can log in | Multi-region auth; fallback token validation |
| **External dependency** | Third-party API → blocks all operations | Circuit breaker; graceful degradation; caching of last response |

## Levels of SPOF Elimination

```
Level 1: Component redundancy (second LB, second DB replica)
Level 2: Rack redundancy    (different racks within a DC)
Level 3: AZ redundancy      (multiple availability zones in same region)
Level 4: Region redundancy  (active-active or active-passive geo replication)
Level 5: Provider redundancy (multi-cloud for critical services)
```

Higher levels provide more availability but add cost and complexity. Determine the required SLA before choosing a level.

## Hidden SPOFs

Some SPOFs are not obvious:
- **Shared config service**: If all services depend on a single etcd/Consul instance with no replication.
- **Deployment pipeline**: If CI/CD is the only path to deploy hotfixes.
- **Monitoring system**: SPOF for your SPOF detection — monitor the monitor.
- **Human process**: On-call person is the SPOF for incident response if there's no runbook.

## Related Concepts

- [[Redundancy]] — the mechanism that eliminates SPOFs
- [[Fault Tolerance]] — the broader system property SPOF elimination supports
- [[Load Balancing]] — distributes load and routes around failures
- [[Failover]] — the recovery action when a SPOF fails despite mitigation
- [[Availability]] — the metric SPOF elimination improves
