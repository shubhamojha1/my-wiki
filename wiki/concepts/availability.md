---
title: "Availability"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/availability"]
---

Availability is the proportion of time a system is in a functioning condition.

## Definition
`Availability = uptime / (uptime + downtime)`

## Availability vs Reliability

| Concept | Question | Example |
|---------|----------|---------|
| Availability | Is system responding? | HTTP 200 |
| Reliability | Is response correct? | Correct balance |

A system can be highly available but unreliable (e.g., charges twice).

## Availability Tiers

| Availability | Downtime/Year |
|--------------|---------------|
| 99% | ~4 days |
| 99.9% | ~9 hours |
| 99.99% | ~1 hour |
| 99.999% | ~5 minutes |

## Patterns

- **Redundancy** — Backup components take over
- **Active-Active** — All nodes handle traffic
- **Active-Passive** — Standby waits
- **Circuit Breaker** — Prevent cascade failures

## Fault Tolerance
Distributed systems build reliable systems from unreliable components through redundancy.