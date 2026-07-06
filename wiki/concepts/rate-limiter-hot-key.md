---
title: "Rate Limiter Hot Key"
type: concept
tags: [rate-limiting, redis, sharding, hot-key]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Rate Limiter Hot Key

A **rate limiter hot key** occurs when one client identifier, such as a user ID, IP address, or API key, receives enough requests to overload the Redis shard that owns its rate-limit state.

## Causes

- Abuse or DDoS traffic from one source.
- Misconfigured bots or clients.
- Legitimate high-volume integrations such as analytics pipelines.
- Many users sharing an IP through corporate NAT, public WiFi, or carrier-grade NAT.

## Mitigations

For legitimate high-volume clients:

- Encourage client-side rate limiting that respects `X-RateLimit-*` and `Retry-After` headers.
- Provide batching endpoints to reduce check volume.
- Offer premium tiers or dedicated infrastructure for high-throughput clients.

For abuse:

- Temporarily block IPs or API keys after repeated limit violations.
- Use upstream DDoS protection such as Cloudflare or AWS Shield.
- Filter malicious traffic before it reaches the [[Distributed Rate Limiter]].

## Design Note

IP-based rate limits should account for shared IPs. Authenticated user or API-key limits are usually more precise than IP-only enforcement.

## Related Concepts

- [[Rate Limiting]]
- [[Distributed Rate Limiter]]
- [[Redis Cluster]]
- [[DDoS Protection]]
