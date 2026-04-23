---
title: "Redundancy"
type: concept
tags: [reliability, fault-tolerance, architecture]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Redundancy

**Definition:** A system property where the loss of a component does not cause system failure; instead, capacity degrades proportionally.

## Ideal Redundancy Property

```
Lost server = decrease capacity by same amount that server added when it was healthy
```

Example: If one machine adds 10% capacity:
- Losing it reduces capacity by 10%
- System continues operating at 90% capacity

## How Redundancy Achieved

### Via Load Balancing
Load balancers detect failed servers and route traffic to healthy ones, masking failures from users.

### Via Replication
- Data replicated across multiple nodes
- Read replicas for read scalability
- Write replication for durability

### Via Stateless Design
Servers can be replaced without data loss if state is externalized (database, cache, etc.).

## Redundancy vs. Vertical Scaling Tension

Vertical scaling concentrates resources on fewer machines, making each more critical:
- One machine failure has larger impact
- Requires sophisticated failover mechanisms
- Often more expensive than distributed alternatives

## Levels of Redundancy

| Level | Description |
|-------|-------------|
| Component | Duplicate critical components |
| Server | Multiple application servers |
| Database | Master-slave or multi-master |
| Datacenter | Geographic distribution |
| Network | Multiple ISPs, redundant paths |

## Related Concepts

[[Horizontal Scalability]], [[Load Balancing]], [[Replication (Distributed)]], [[Fault Tolerance]], [[Availability]]