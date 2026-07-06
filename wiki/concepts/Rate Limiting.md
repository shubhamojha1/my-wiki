---
title: "Rate Limiting"
type: concept
tags: [api, gateway, rate-limiting]
created: 2026-04-28
sources: ["algomaster-api-gateway", "algomaster-rate-limiting-algorithms", "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Rate Limiting

**Rate limiting** controls how many requests a client can make in a given time window.

In distributed systems, rate limiting is not just an algorithm choice. A [[Distributed Rate Limiter]] must decide where enforcement runs, how clients are identified, where shared state lives, and what happens when the state store is unavailable.

## How It Works

1. Track requests per client (IP or user)
2. Count requests in time window
3. Block when limit exceeded
4. Return 429 Too Many Requests

For interactive APIs, the usual behavior is fail-fast rejection rather than queuing excess requests. A helpful 429 response includes headers such as `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `Retry-After` so clients can back off.

## Distributed Design

Common placement options:

- **In-process**: fastest, but each server only sees local traffic and global limits become inaccurate behind a load balancer.
- **Dedicated service**: centralizes state and can receive rich application context, but adds a network hop and another service dependency.
- **[[API Gateway]] / load balancer**: blocks excess requests at the edge before they reach application servers. This is the common production choice, but it only sees request-visible context such as headers, path, IP address, API key, and JWT claims.

Distributed enforcement needs shared state. [[Redis]] is often used to store per-client counters or [[Token Bucket]] state, while [[Redis Cluster]] or [[Consistent Hashing]] shards that state at high write volume.

## Common Limits

- 10 requests/minute
- 100 requests/hour
- 1000 requests/day

## Use Cases

- Prevent abuse
- DDoS protection
- Protect backend services
- Monetization (paid tiers)

## Client Identification

Rate limits can be keyed by several identifiers:

- User ID from an authorization token for authenticated APIs
- IP address for anonymous traffic, with care for NAT/shared networks
- API key for developer APIs
- Global or endpoint-specific keys for protecting a whole system or costly endpoint

Real systems layer multiple [[Rate Limit Rule]] pages and deny a request when any applicable rule is exhausted.

## Algorithms

### [[Token Bucket]]
- Bucket holds tokens, refilled at fixed rate
- Allows bursts up to bucket capacity
- Simple to implement

### [[Leaky Bucket]]
- Queue-based; requests processed at constant rate
- Smooths out traffic, prevents bursts
- Drops excess requests immediately

### [[Fixed Window Counter]]
- Time divided into fixed windows; counter resets each window
- Boundary problem: allows 2x rate at window edges
- Simplest algorithm

### [[Sliding Window Log]]
- Stores timestamp log per request; removes expired entries
- Most accurate, no boundary issues
- Memory-intensive for high-volume APIs

### [[Sliding Window Counter]]
- Hybrid: weighted sum of current + previous window counts
- Good accuracy, low memory (O(1) per client)
- Trade-off: approximation vs exact accuracy

## Related Concepts

- [[API Gateway]] — Where rate limiting is applied
- [[DDoS Protection]] — Related security concept
