---
title: "Over-fetching"
type: concept
tags: [api, rest, graphql, performance]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-rest-vs-graphql"]
---

# Over-fetching

**Over-fetching** occurs when an API returns more data than the client needs for a given operation. The client receives and must deserialize a large payload but uses only a small fraction of it.

## Concrete Example

A mobile app displays a user's name in a header. The REST endpoint returns the full user object:

```json
GET /users/42
{
  "id": 42,
  "name": "Alice",          ← only this is needed
  "email": "alice@...",
  "phone": "555-...",
  "address": { ... },
  "createdAt": "2023-...",
  "preferences": { ... },
  "billingInfo": { ... }    ← 7 unnecessary fields
}
```

The client uses only `name` but receives and processes the entire object on every render.

## Why It Matters

- **Bandwidth waste** — especially costly on mobile networks or for high-traffic APIs
- **Increased latency** — larger payloads take longer to serialize, transmit, and deserialize
- **Unnecessary processing** — client must allocate memory and parse unused fields
- **Backend load** — server queries and returns data that is immediately discarded

## In REST

REST endpoints return fixed response shapes defined by the server. All clients receive the same structure regardless of their actual data needs.

Mitigations (partial):
- `?fields=name,email` query parameters (non-standard; requires custom implementation)
- Dedicated endpoint per client type (BFF — Backend For Frontend pattern)
- Response projection parameters (GraphQL-like approach added to REST)

## In GraphQL

Client specifies exactly which fields it needs:

```graphql
query {
  user(id: 42) {
    name
  }
}
```

Server returns only `{ "user": { "name": "Alice" } }`.

## Related Concepts

- [[REST API]] — the primary source of over-fetching problems
- [[GraphQL]] — eliminates over-fetching by design
- [[Under-fetching]] — the complementary problem (too little data per request)
