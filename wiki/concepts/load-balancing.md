---
title: "Load Balancing"
type: concept
tags: [infrastructure, scalability, distribution]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Load Balancing

**Definition:** Distributing requests across multiple resources according to some metric while monitoring health and availability.

## Goals

### Horizontal Scalability
Linear capacity increase with added hardware:
- 1 machine → 2 machines = capacity doubles
- 3 machines → 4 machines = +33% capacity

### Redundancy
Graceful degradation when servers fail:
- Lost server = decrease capacity by same amount it added
- System continues functioning without disruption

## Load Balancing Layers

A moderately large system balances load at three layers:

```
[User] --layer 1--> [Web Servers] --layer 2--> [Platform] --layer 3--> [Database]
```

1. **User to web servers** — external traffic distribution
2. **Web servers to platform** — internal service routing
3. **Platform to database** — data layer distribution

## Implementation Approaches

### 1. Smart Clients
- Load-balancing embedded in database/service client
- Handles host pools, health detection, failover
- **Pros**: No additional infrastructure
- **Cons**: Complex to implement correctly, hard to maintain

### 2. Hardware Load Balancers
- Dedicated appliances (e.g., Citrix NetScaler)
- **Pros**: Highest performance, handles many edge cases
- **Cons**: Very expensive, complex configuration

### 3. Software Load Balancers (Recommended)
- Runs locally on each box (e.g., HAProxy)
- Each service bound to localhost port
- **Pros**: Flexible, cost-effective, easy setup
- **Cons**: Requires configuration

## Health Checks

Load balancers must:
- Detect downed hosts and avoid routing requests
- Detect recovered hosts and re-add to pool
- Handle adding new hosts dynamically

## Related Concepts

[[Horizontal Scalability]], [[Redundancy]], [[Software Load Balancer]], [[Hardware Load Balancer]], [[Smart Client]], [[HAProxy]]