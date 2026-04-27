---
title: "CockroachDB: Fault Tolerance"
type: source
tags: [system-design, fault-tolerance, distributed-systems]
created: 2026-04-27
sources: ["cockroachlabs.com/blog/what-is-fault-tolerance"]
---

# Fault Tolerance

**Source:** CockroachDB Blog — What is Fault Tolerance

## Definition

**Fault tolerance** describes a system's ability to handle errors and outages without any loss of functionality. It's critical in cloud computing where reliability and uptime are paramount.

---

## Key Concepts

### Fault Tolerance vs High Availability

| Aspect | Fault Tolerance | High Availability |
|--------|---------------|-------------------|
| Goal | Zero downtime, zero data loss | Minimal downtime |
| Approach |冗余 across nodes/AZs | Automatic recovery |

### Quorum Requirement

- Data replicated across multiple nodes
- Must have **quorum** (majority) to commit writes
- 3 replicas = can tolerate 1 node failure
- 5 replicas = can tolerate 2 node failures

**Formula**: `max failures = (replication factor - 1) / 2`

---

## Replication Strategies

### Single Region (3 AZs)
- 3x replication
- Tolerates: 1 node failure, 1 AZ failure
- RPO: 0 seconds

### Multi-Region
- 3 regions, 3x replication
- Tolerates: 1 node, 1 AZ, 1 region failure
- RPO: 0 seconds

### Disaster Recovery
- Cross-region replication
- Tolerates: Region failures
- RPO: 10s of seconds

---

## How It Works (CockroachDB)

1. **Sync replication** — Data copied to multiple nodes
2. **Raft consensus** — Quorum required to commit
3. **Automatic recovery** — When node fails, re-replicate to healthy nodes
4. **Rebalancing** — When nodes recover, redistribute data

---

## Fault Tolerance Goals

| Goal | Replication Factor | What Survives |
|------|-------------------|---------------|
| 1 node | 3 | 1 node failure |
| 1 AZ | 3 | 1 availability zone |
| 2 nodes | 5 | 2 node failures |
| 1 region | 5 | 1 region failure |

---

## Key Takeaways

1. **Replicate data** — Multiple copies across nodes
2. **Quorum-based commits** — Need majority for writes
3. **Automatic recovery** — System heals itself
4. **Survival goals** — Define what failures to tolerate