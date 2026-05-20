---
title: "Health Check"
type: concept
tags: [load-balancing, monitoring]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-load-balancing-algorithms"]
---

# Health Check

A **health check** is a mechanism used by load balancers, orchestrators (Kubernetes), and service meshes to detect failed or degraded instances and route traffic away from them automatically.

## Active vs Passive Health Checks

| Type | How it works | Detect speed | Overhead |
|------|-------------|-------------|---------|
| **Active** | Load balancer periodically probes the endpoint | Slow (waits for interval) | Probe traffic added |
| **Passive** | Observe real request failures/timeouts | Fast (real traffic) | None |
| **Hybrid** | Both active + passive | Fastest | Both |

Most production systems use hybrid: passive detection for fast failure response, active probes for recovery detection.

## Active Health Check Parameters

```
Interval:              10s   (how often to probe)
Timeout:               3s    (max wait for response)
HealthyThreshold:      2     (consecutive successes → healthy)
UnhealthyThreshold:    3     (consecutive failures → unhealthy)

State machine:
  HEALTHY → failure × 3 → UNHEALTHY → success × 2 → HEALTHY
```

## Health Check Endpoints

A `/health` endpoint should check:
- Application is running (liveness)
- Dependencies are reachable (readiness — database, cache)
- Not overloaded (optional)

```
HTTP 200 OK    → healthy
HTTP 503       → unhealthy (overloaded, dependency down)
TCP connect OK → layer-4 check (does not verify app logic)
```

## Kubernetes Probes

Kubernetes distinguishes:
- **Liveness probe**: Is the app alive? If fails → restart container.
- **Readiness probe**: Is the app ready to serve? If fails → remove from Service endpoints (no traffic).
- **Startup probe**: Has the app finished initializing? Delays liveness checks.

## Configuration Examples

**NGINX (passive)**:
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 10.0.0.2:8080 max_fails=3 fail_timeout=30s;
}
```

**AWS ALB (active)**:
```
HealthCheckPath: /health
HealthCheckIntervalSeconds: 15
HealthyThresholdCount: 2
UnhealthyThresholdCount: 3
```

## Related Concepts

- [[Load Balancing]] — routes traffic based on health check state
- [[Circuit Breaker]] — application-level health check pattern
- [[Failover]] — the action taken when a health check determines a node is down
