---
title: "DDoS Protection"
type: concept
tags: [security, availability, rate-limiting]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# DDoS Protection

**DDoS protection** detects and filters malicious distributed traffic before it overwhelms application infrastructure. It complements [[Rate Limiting]] but usually runs earlier in the request path, often at the edge network, CDN, WAF, or cloud provider.

## Relationship To Rate Limiting

[[Distributed Rate Limiter]] systems protect backend services from excessive client traffic, but they can themselves become a target. A single abusive IP, API key, or botnet can create [[Rate Limiter Hot Key]] pressure by forcing many checks against the same shard.

DDoS protection helps by blocking malicious traffic before it reaches the API gateway or Redis-backed limiter. The Hello Interview rate limiter breakdown names Cloudflare and AWS Shield as examples of upstream protection services.

## Related Concepts

- [[Rate Limiting]]
- [[Rate Limiter Hot Key]]
- [[WAF]]
- [[Availability]]
