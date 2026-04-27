---
title: "Health Check"
type: concept
tags: [load-balancing, monitoring]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Health Check

**Health checks** detect failed or degraded servers and stop traffic to them.

## Active Health Checks

- Periodic probes (HTTP GET /health endpoint)
- Parameters:
  - **Interval**: Time between checks (5-30 seconds)
  - **Timeout**: Wait for response
  - **HealthyThresholdCount**: Consecutive successes to mark healthy
  - **UnhealthyThresholdCount**: Consecutive failures to mark unhealthy

## Passive Health Checks

- Observe actual traffic and responses
- Cannot be disabled in some systems
- Faster detection from real request patterns

## NGINX Example

```nginx
server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;
```

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Load Balancing]] — Where health checks are used