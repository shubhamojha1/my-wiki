---
title: "Hardware Load Balancer"
type: concept
tags: [infrastructure, load-balancing]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Hardware Load Balancer

**Definition:** Dedicated network appliance designed specifically for load balancing traffic across servers.

## Examples

- **Citrix NetScaler** — Industry standard enterprise load balancer
- **F5 Big-IP** — High-end application delivery controller
- **Cisco ACE** — Data center load balancer

## Characteristics

| Aspect | Description |
|--------|-------------|
| Performance | Highest throughput, lowest latency |
| Cost | Very expensive (tens of thousands+) |
| Complexity | Requires specialized knowledge |
| Purpose | First point of contact for external traffic |

## Typical Usage Pattern

Large companies with substantial budgets use hardware load balancers:
1. As the **single entry point** from external users
2. For the **first tier** of load balancing only
3. Combined with other mechanisms for internal traffic

## Limitations

- **Cost barrier** — prohibitive for smaller organizations
- **Configuration complexity** — steep learning curve
- **Inflexibility** — harder to adapt to changing needs
- **Vendor lock-in** — dependent on specific hardware

## Cost-Performance Tradeoff

Hardware load balancers are the most expensive but offer highest performance. For most systems, software solutions provide sufficient capability at a fraction of the cost.

## Hybrid Approach

Many organizations use a hybrid:
```
[User] → [Hardware LB] → [Software LB pool] → [Internal services]
```

## Related Concepts

[[Load Balancing]], [[Software Load Balancer]], [[Horizontal Scalability]]