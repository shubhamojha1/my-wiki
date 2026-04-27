---
title: "AlgoMaster: Reliability"
type: source
tags: [system-design, reliability]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/reliability"]
author: Ashish Pratap Singh
---

# Reliability

**Source:** AlgoMaster.io System Design — Reliability Chapter

## Definition

**Reliability** is the probability that a system will perform its intended function correctly over a given period of time.

A reliable system performs its intended function correctly and consistently, even in the face of faults.

---

## Availability vs Reliability

| Concept | Question It Answers | Example |
|--------|-------------------|---------|
| Availability | Is the system responding? | HTTP 200 |
| Reliability | Is the response correct? | Correct balance |
| Fault Tolerance | Does it keep working when components fail? | Works with 1 DB down |
| Durability | Is data preserved despite failures? | Data survives disk failure |

A system can be available but unreliable:
- Payment system that charges twice = available but unreliable

---

## Reliability Techniques

### 1. Redundancy

Having backup components that can take over if one fails.

### 2. Failover

Automatic switching to redundant component when failure detected.

### 3. Load Balancing

Distributes traffic, prevents single points of failure.

### 4. Monitoring

Track health and performance, alert on issues.

### 5. Graceful Degradation

Keep core functionality working when parts fail.

- Reduced service vs complete failure
- Example: Read-only mode during write DB failure

### 6. Circuit Breakers

Detect failing service, temporarily cut off requests to prevent cascade.

---

## Key Takeaways

1. **Available ≠ Reliable** — System can respond but respond incorrectly
2. **Redundancy** — Have backup components
3. **Failover** — Automatic switching
4. **Graceful degradation** — Core functions work even if parts fail
5. **Circuit breakers** — Prevent cascade failures