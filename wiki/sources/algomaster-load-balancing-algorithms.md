---
title: "Load Balancing Algorithms"
type: source
tags: [system-design, networking, load-balancing]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Load Balancing Algorithms

**Load balancing** distributes incoming traffic across multiple servers to prevent overload and improve performance/availability.

## Algorithms

### Round Robin
- Requests sequentially to each server
- Simple, even distribution
- Use when servers have similar capacity

### Weighted Round Robin
- Servers assigned weights based on capacity
- Higher weight = more requests

### Least Connections
- Routes to server with fewest active connections
- Dynamic, adapts to current load

### Least Response Time
- Routes to server with fastest response time
- Minimizes latency

### IP Hash
- Hash of client IP to determine server
- Enables sticky sessions (same client → same server)

## Health Checks

### Active Health Checks
- Periodic probes (HTTP GET /health)
- Parameters: interval, timeout, healthy/unhealthy thresholds

### Passive Health Checks
- Observe actual traffic
- Detect failures from request patterns

## Layer 4 vs Layer 7

| Feature | L4 (Transport) | L7 (Application) |
|---------|---------------|-----------------|
| OSI Layer | 4 (TCP/UDP) | 7 (HTTP/HTTPS) |
| Inspects | IP, port | URLs, headers, cookies |
| Latency | Very low | 1-5ms overhead |
| SSL Termination | No | Yes |

## Related Concepts

- [[Load Balancing]] — Parent concept
- [[Health Check]] — Server health monitoring
- [[Sticky Session]] — Session persistence

## Source

- AlgoMaster: [Load Balancing Algorithms](https://blog.algomaster.io/p/load-balancing-algorithms-explained-with-code) (June 2024)