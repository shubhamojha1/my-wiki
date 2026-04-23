---
title: "HAProxy"
type: entity
tags: [tool, infrastructure, load-balancer]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# HAProxy

**Type:** Software load balancer  
**Website:** [haproxy.1wt.eu](http://haproxy.1wt.eu/)

## Overview

HAProxy is a free, open-source software load balancer that provides high availability and load distribution for TCP/HTTP applications. It is the recommended starting point for load balancing in most systems.

## How It Works

HAProxy runs locally on each server machine. Services are bound to localhost ports, and HAProxy:
1. Listens on a virtual IP or port
2. Performs health checks on backend servers
3. Routes requests to available servers
4. Handles failover automatically

## Example Configuration

```
# Platform machines accessible via localhost:9000
# Database read pool at localhost:9001
# Database write pool at localhost:9002
```

Each service has a locally bound port; HAProxy manages:
- Health checks to detect failed hosts
- Adding/removing hosts from pools
- Load distribution across all machines

## Advantages

- **No special hardware required** — runs on commodity servers
- **Easy to configure** — declarative configuration language
- **Health checking** — automatic detection of failed hosts
- **Flexibility** — supports Layer 4 and Layer 7 load balancing
- **Cost-effective** — open-source with no licensing fees

## Comparison with Alternatives

| Approach | Pros | Cons |
|----------|------|------|
| HAProxy (recommended) | Flexible, free, easy setup | Requires configuration |
| Smart clients | No infrastructure | Complex, hard to maintain |
| Hardware (NetScaler) | High performance | Expensive, complex setup |

## Related Concepts

[[Load Balancing]], [[Software Load Balancer]], [[Horizontal Scalability]], [[Redundancy]]