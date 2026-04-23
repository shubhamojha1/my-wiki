---
title: "Software Load Balancer"
type: concept
tags: [infrastructure, load-balancing]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Software Load Balancer

**Definition:** Load balancing software that runs on servers rather than dedicated hardware, distributing traffic across a pool of machines.

## Key Example: HAProxy

HAProxy runs locally on each server machine, providing load balancing without dedicated infrastructure:

```
┌─────────────────────────────────────────────┐
│ Server 1: localhost:9000 → platform pool    │
│ Server 2: localhost:9000 → platform pool    │
│ Server 3: localhost:9000 → platform pool    │
└─────────────────────────────────────────────┘
         │
         ▼
    [HAProxy routes to healthy servers]
```

## How It Works

1. Each service bound to a localhost port
2. HAProxy listens on a virtual IP/port
3. Performs health checks on backend machines
4. Routes requests only to healthy instances
5. Automatically adds/removes hosts from pool

## Example Setup

```conf
listen app
    bind *:8000
    balance roundrobin
    server app1 10.0.1.1:9000 check
    server app2 10.0.1.2:9000 check
    server app3 10.0.1.3:9000 check
```

## Advantages

- **No hardware cost** — runs on commodity servers
- **Flexible** — easily reconfigured
- **Transparent** — appears as single endpoint to clients
- **Health-aware** — removes sick hosts automatically
- **Cost-effective** — open-source options available

## Comparison

| Type | Cost | Performance | Flexibility |
|------|------|-------------|-------------|
| Software (HAProxy) | Free | High | High |
| Smart client | Free | High | Low (per-app) |
| Hardware | $$$$ | Highest | Low |

## Recommended Starting Point

For most systems, start with software load balancing and move to smart clients or hardware only with deliberate need.

## Related Concepts

[[Load Balancing]], [[HAProxy]], [[Hardware Load Balancer]], [[Smart Client]], [[Horizontal Scalability]]