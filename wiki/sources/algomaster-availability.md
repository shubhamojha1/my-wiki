---
title: "AlgoMaster: Availability"
type: source
tags: [system-design, availability]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/availability"]
author: Ashish Pratap Singh
---

# Availability

**Source:** AlgoMaster.io System Design — Availability Chapter

## Definition

**Availability** measures how often a system is operational and accessible to users.

> **Important**: Availability is not the same as reliability. A system can be highly available but unreliable.

| Concept | Question | Example |
|---------|----------|---------|
| Availability | Is the system responding? | HTTP 200 |
| Reliability | Is the response correct? | Correct balance |

---

## Availability Tiers (Nines)

| Availability | Downtime/Year | Example |
|--------------|---------------|---------|
| 99% | 3.6 days | Personal apps |
| 99.9% | 8.7 hours | Business |
| 99.99% | 52 minutes | HA systems |
| 99.999% | 5 minutes | Telecom |

---

## Core Concept: Redundancy

> If you have one of something and it fails, you have zero. If you have two and one fails, you still have one.

Redundancy means having backup components that take over when primary components fail.

---

## Patterns for High Availability

### Pattern 1: Active-Active vs Active-Passive

**Active-Active**: Multiple nodes handle traffic simultaneously.
- Requires stateless services
- Best utilization

**Active-Passive**: One active, one standby.
- Simpler
- Lower cost

### Pattern 2: Load Balancer

Distributes traffic across multiple servers, routes around failures.

### Pattern 3: Multi-Layer Redundancy

A chain is only as strong as its weakest link.
- App servers + load balancer + database + cache
- All need redundancy

### Pattern 4: Queues for Slow Responses

When downstream can't handle peak load, use a queue to buffer.

### Pattern 5: Circuit Breaker

Prevent cascading failures by cutting off failing services.

---

## Key Takeaways

1. **Redundancy everywhere** — Every layer needs backup
2. **Assume failure** — Design for components to fail
3. **Use multiple zones** — Distribute across data centers
4. **Circuit breakers** — Prevent cascade
5. **Monitor** — Detect failures early