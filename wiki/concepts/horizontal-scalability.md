---
title: "Horizontal Scalability"
type: concept
tags: [scalability, architecture]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Horizontal Scalability

**Definition:** The ability to increase system capacity linearly by adding more machines to the system.

## Contrast with Vertical Scalability

| Aspect | Horizontal | Vertical |
|--------|------------|----------|
| Growth method | Add machines | Add resources to existing machine |
| Capacity gain | Linear (2x machines = 2x capacity) | Sub-linear (diminishing returns) |
| Ceiling | Theoretical unlimited | Hardware limits (RAM, CPU slots) |
| Cost curve | Linear | Exponential at high end |
| Redundancy | Natural (multiple machines) | Complex failover required |

## Why Horizontal is Preferred

Vertical scaling becomes undesirable because:
1. **Cost efficiency** — Adding resources to one machine is eventually more expensive than adding another machine
2. **Redundancy conflict** — Vertical scaling and redundancy can be at odds
3. **Hardware ceiling** — Bounded by available slots for RAM, CPUs, disks

## Key Requirement: Statelessness

Horizontal scalability requires:
- No server-side session state (sessions in shared cache/database)
- No local file dependencies
- Deterministic request handling across machines

## Enabling Technologies

- [[Load Balancing]] — Distributes requests across machines
- [[Caching]] — Enables better resource utilization
- [[Database Sharding]] — Partition data across nodes
- [[Message Queues]] — Decouple processing for parallel workers

## When to Choose Horizontal Over Vertical

| Scenario | Choose Horizontal | Choose Vertical |
|----------|------------------|-----------------|
| Growth rate | Rapid, unpredictable | Limited, predictable |
| Availability needs | High (fault tolerance critical) | Moderate (downtime tolerable) |
| App distribution | Easy to partition | Tight coupling, legacy code |
| Architecture | Microservices | Monolithic |
| Budget preference | Commodity hardware, operational expense | Single powerful machine, capital expense |
| Latency requirements | Tolerates inter-server communication | Latency-critical (single machine) |

## Combining with Vertical

Many systems use both: powerful individual machines (vertical) as nodes in a horizontally-scaled cluster (horizontal). Example: [[Database Sharding]] partitions data across horizontally-scaled DB servers, while each server is vertically scaled for performance.

## Related Concepts

[[Scalability]], [[Redundancy]], [[Load Balancing]], [[Caching]], [[Database Sharding]]