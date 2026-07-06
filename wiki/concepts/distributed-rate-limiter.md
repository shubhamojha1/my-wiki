---
title: "Distributed Rate Limiter"
type: concept
tags: [system-design, rate-limiting, distributed-systems, api-gateway]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Distributed Rate Limiter

A **distributed rate limiter** enforces request quotas across multiple gateway or application instances. Its key challenge is global coordination: every node must make decisions from shared per-client state, otherwise requests spread across nodes can exceed the intended limit.

## Design Shape

The Hello Interview design places the limiter at the [[API Gateway]] or load balancer. This blocks excess requests before they reach application services and avoids an extra rate-limiter service call from the application tier.

The trade-off is limited context. A gateway can inspect the URL/path, headers, query parameters, IP address, API key, and JWT claims, but it cannot cheaply inspect deeper application state unless that state is encoded into the request.

## Core Entities

- [[Rate Limit Rule]]: policy such as "100 requests/minute per user" or "10 search requests/minute per IP".
- Client: user ID, IP address, API key, or a combination.
- Request: the inbound API call carrying the endpoint, client identity, timestamp, and request context.

The basic interface is:

```text
isRequestAllowed(clientId, ruleId) -> {
  passes: boolean,
  remaining: number,
  resetTime: timestamp
}
```

## Shared State

Local memory on each gateway is not enough. If Alice sends 50 requests to Gateway A and 50 to Gateway B, each gateway may think she is still under a 100-request limit even though the global budget is consumed.

The common design uses [[Redis]] as the shared state store. For a [[Token Bucket]], each client bucket stores:

- `tokens`: current number of available tokens.
- `last_refill`: timestamp used to calculate refill since the last request.

The read-calculate-update path must be atomic. `MULTI/EXEC` around only the writes is insufficient if the read happens first; the full read-modify-write should run inside a Redis Lua script.

## Scaling

At high write volume, rate limiting is a write-scaling problem because every request may update counters or bucket state. To reach 1M requests/second, shard state by the same identifier used for enforcement:

- user ID for authenticated users
- IP address for anonymous users
- API key for developer APIs

[[Consistent Hashing]] or [[Redis Cluster]] can route all requests for the same client to the same shard. Splitting a single client's bucket across shards breaks enforcement.

## Failure Mode

When Redis or the limiter backend is unavailable, the system must choose a [[Rate Limiter Failure Mode]]:

- Fail-open preserves API availability but removes protection.
- Fail-closed preserves backend protection but rejects requests that might otherwise be valid.

For a social media API under viral traffic risk, Hello Interview chooses fail-closed because backend overload is worse than brief request rejection.

## Related Concepts

- [[Rate Limiting]]
- [[Token Bucket]]
- [[API Gateway]]
- [[Redis Cluster]]
- [[Dynamic Rate Limit Configuration]]
- [[Rate Limiter Hot Key]]
