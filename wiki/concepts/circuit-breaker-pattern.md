---
title: "Circuit Breaker Pattern"
type: concept
tags: [microservices, fault-tolerance, resilience]
created: 2026-05-11
sources: [medium-circuit-breaker]
---

# Circuit Breaker Pattern

The **Circuit Breaker** pattern prevents cascading failures in microservices by detecting failures and failing fast instead of waiting for timeouts, giving downstream services time to recover.

## States

### Closed
Normal operation. Requests pass through to the service. The circuit breaker monitors failure rates.

### Open
When failures exceed a threshold, the circuit **trips** to open. Requests return immediately with an error — no attempt to reach the failing service. This prevents thread pool exhaustion and queue buildup.

### Half-Open
After a timeout period, the circuit transitions to half-open and allows a limited number of test requests through:
- **Success**: Circuit resets to closed — normal traffic resumes
- **Failure**: Circuit returns to open — timeout restarts

```
Closed → [failures > threshold] → Open
Open → [timeout expires] → Half-Open
Half-Open → [test succeeds] → Closed
Half-Open → [test fails] → Open
```

## How It Works

1. A proxy wraps calls to the downstream service
2. The proxy monitors response times and failure rates
3. When response time exceeds threshold (e.g., 200ms) for significant percentage of requests (e.g., 75%), circuit trips
4. During open state, requests fail fast with no queuing
5. Background pings probe the service; when it recovers, circuit resets

## Benefits

- **Fail fast**: No waiting for timeouts on known-bad services
- **No cascading failures**: One slow service doesn't flood the system
- **Graceful degradation**: Fallbacks can serve cached/default responses
- **Self-healing**: Automatic recovery detection via probe requests

## Related

- [[Cascading Failure]] — The problem circuit breakers prevent
- [[Retry Pattern]] — Often used together with circuit breakers
- [[Bulkhead Pattern]] — Isolates failures by resource pool
- [[API Gateway]] — Often hosts circuit breaker logic
- [[Health Check]] — Probes used for half-open state testing
