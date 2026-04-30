---
title: "Rate Limiting"
type: concept
tags: [api, gateway, rate-limiting]
created: 2026-04-28
sources: ["algomaster-api-gateway", "algomaster-rate-limiting-algorithms"]
---

# Rate Limiting

**Rate limiting** controls how many requests a client can make in a given time window.

## How It Works

1. Track requests per client (IP or user)
2. Count requests in time window
3. Block when limit exceeded
4. Return 429 Too Many Requests

## Common Limits

- 10 requests/minute
- 100 requests/hour
- 1000 requests/day

## Use Cases

- Prevent abuse
- DDoS protection
- Protect backend services
- Monetization (paid tiers)

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