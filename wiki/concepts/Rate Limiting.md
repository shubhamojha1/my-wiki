---
title: "Rate Limiting"
type: concept
tags: [api, gateway, rate-limiting]
created: 2026-04-28
sources: ["algomaster-api-gateway"]
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

- **Token Bucket**: Tokens refill over time
- **Leaky Bucket**: Fixed rate processing
- **Fixed Window**: Reset count each window
- **Sliding Window**: Smooth rate distribution

## Related Concepts

- [[API Gateway]] — Where rate limiting is applied
- [[DDoS Protection]] — Related security concept