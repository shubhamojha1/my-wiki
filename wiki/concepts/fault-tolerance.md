---
title: "Fault Tolerance"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "cockroachlabs.com/blog/what-is-fault-tolerance"]
---

# Fault Tolerance

**Fault tolerance** is a system's ability to continue operating correctly — possibly at reduced capacity — in the presence of failures. A fault-tolerant system defines what class of faults it expects, then engineers redundancy and recovery to survive them.

## Fault vs Failure

- **Fault**: A defect in a component (crashed process, dropped packet, corrupted byte).
- **Error**: A fault that propagates into incorrect system state.
- **Failure**: The system no longer meets its specification (a visible outage).

Fault tolerance is about preventing faults from becoming failures.

## Types of Faults

| Type | Description | Examples |
|------|-------------|---------|
| **Crash-fail** | Node halts and stops responding | Power loss, OOM kill, hardware failure |
| **Network partition** | Nodes can't communicate | Switch failure, routing misconfiguration |
| **Slow / gray failure** | Node responds slowly or intermittently | GC pauses, disk saturation |
| **Byzantine** | Node sends arbitrary/malicious messages | Hardware bit-flip, compromised node |
| **Correlated** | Multiple nodes fail simultaneously | Datacenter power outage, bad deploy |

## Core Mechanisms

| Mechanism | How it helps |
|-----------|-------------|
| **Replication** | Multiple copies of data; no single copy is critical |
| **Quorum** | Write/read majority → survive minority failures |
| **Heartbeats** | Detect node failures quickly |
| **Automatic failover** | Promote a replica when primary dies |
| **Idempotent retries** | Safely retry failed operations |
| **Circuit breaker** | Stop sending to a failing downstream, give it time to recover |
| **Bulkhead** | Isolate failure domains so one failure doesn't cascade |

## Quorum Formula

To tolerate `f` crash failures with replication factor `n`:

```
n ≥ 2f + 1    (minimum replicas needed)
quorum = f + 1 = ⌊n/2⌋ + 1

Examples:
  3 replicas → tolerate 1 failure  (quorum = 2)
  5 replicas → tolerate 2 failures (quorum = 3)
  7 replicas → tolerate 3 failures (quorum = 4)
```

## Fault Tolerance vs High Availability

| Concept | Focus |
|---------|-------|
| **Fault tolerance** | Continue with no interruption despite faults (zero downtime goal) |
| **High availability** | Minimize downtime; may have brief interruption during failover |
| **Reliability** | Correct results over time; related but not identical |

## Levels of Fault Tolerance

- **Component-level**: RAID for disk, ECC for RAM, redundant PSUs.
- **Node-level**: Multiple processes on multiple servers.
- **Rack-level**: Replicas on different racks (avoid one network switch failure).
- **AZ-level**: Replicas in different availability zones.
- **Region-level**: Geographic replication for disaster recovery.

## Related Concepts

- [[Redundancy]] — the duplication mechanism enabling fault tolerance
- [[Failover]] — the action of switching to a replica when primary fails
- [[High Availability]] — the availability guarantee fault tolerance enables
- [[Quorum (Distributed)]] — the voting mechanism for consistent decisions
- [[Byzantine Failure]] — the hardest fault model to tolerate
