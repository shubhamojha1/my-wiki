---
title: "Stateless Architecture"
type: concept
tags: [architecture, stateless, scalability, rest]
created: 2026-05-12
sources: ["stateful-vs-stateless-architecture"]
---

# Stateless Architecture

A system design where the server does not preserve client-specific data between requests. Each request is treated as independent — the server processes it using only the information provided in that request, then discards any temporary data.

## Common Patterns

### Token-Based Authentication (JWT)
1. Client authenticates once; server issues a signed [[JWT]]
2. Client includes token in every request via `Authorization: Bearer <token>` header
3. Server validates token signature and claims (user ID, expiry) — no server-side session storage needed

### Idempotent APIs
Operations produce the same result regardless of how many times they're executed (e.g., `PUT /users/123` with the same payload). Essential for reliability in distributed systems where retries are common.

## Advantages
- **Horizontal scalability** — any server can handle any request; add servers effortlessly
- **Resilience** — server failure doesn't disrupt user sessions (no per-server state)
- **Simplicity** — no session synchronization or sticky session configuration
- **Lower memory footprint** — no server-side session storage
- **Cacheable** — responses depend only on request parameters, enabling [[CDN]] and caching layers

## Challenges
- **Less context** — personalization requires external effort (cookies, tokens)
- **Client-side complexity** — client must manage and transmit tokens; losing them means re-authentication
- **Larger payloads** — each request must carry all necessary information

## Use Cases
- [[Microservices]] — services handle requests independently via shared data stores
- [[REST API]] / [[GraphQL]] — stateless by design; clients send auth tokens per request
- Mobile apps — tokens stored locally, sent with each API call
- [[CDN]] / caching layers — responses cacheable since they depend only on request params

## Related
- [[Stateful Architecture]] — The contrasting design
- [[Session Management]] — Externalizing state to keep app servers stateless
- [[REST API]] — The canonical stateless API style
- [[System Design Trade-Offs]] — Trade-off #10: Stateful vs Stateless
