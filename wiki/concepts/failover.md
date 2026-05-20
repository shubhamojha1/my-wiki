---
title: "Failover"
type: concept
tags: [system-design, high-availability, fault-tolerance, reliability]
created: 2026-04-27
updated: 2026-05-20
sources: [druva-failover]
---

# Failover

**Failover** is the automatic or manual switching from a failed primary component to a standby backup, ensuring continuity of service. It is a core mechanism for achieving high availability.

## How It Works

```
[Primary] ←heartbeat→ [Standby]

1. Primary fails (crash, network issue, resource exhaustion)
2. Standby detects missed heartbeats (after timeout T)
3. Standby promotes itself to primary
4. DNS, load balancer, or VIP updated to point to new primary
5. Clients reconnect or are transparently redirected
6. Alert sent; failed node repaired and rejoins as standby
```

## Configurations

### Active-Passive (Hot Standby)

```
[Load Balancer] → [Primary] (serving)
                  [Standby] (idle, synced)
```

- Standby receives replication stream but serves no traffic
- On failure: brief cutover delay (failover time)
- Simpler to implement; standby capacity is "wasted"

### Active-Active

```
[Load Balancer] → [Node 1] (serving)
                  [Node 2] (serving)
```

- Both nodes serve traffic simultaneously
- On failure: remaining node absorbs all traffic
- Zero downtime; requires stateless or session-shared architecture

## Metrics

| Metric | Meaning |
|--------|---------|
| **RTO** (Recovery Time Objective) | Maximum acceptable downtime |
| **RPO** (Recovery Point Objective) | Maximum acceptable data loss |
| **MTTR** | Mean Time to Recover |
| **MTBF** | Mean Time Between Failures |

Faster failover = lower RTO; synchronous replication = lower RPO.

## Common Failover Triggers

- Health check failures (HTTP 5xx, no response)
- Heartbeat timeout
- Resource exhaustion (OOM, disk full)
- Explicit manual override

## Related Concepts

- [[Redundancy]] — providing the backup component
- [[Fault Tolerance]] — broader resilience strategy
- [[High Availability]] — the goal failover supports
- [[Single Point of Failure]] — what failover eliminates
- [[Heartbeat]] — the health detection mechanism
- [[RPO RTO]] — the metrics failover is measured against
