---
title: "Under-fetching"
type: concept
tags: [api, rest, graphql, performance]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-rest-vs-graphql"]
---

# Under-fetching

**Under-fetching** occurs when a single API call doesn't return enough data, forcing the client to make multiple sequential requests to assemble the information it needs.

## The N+1 Problem

The classic manifestation is the **N+1 query problem**:

```
1. GET /users/42           → { id: 42, name: "Alice", postIds: [1, 2, 3] }
2. GET /posts/1            → { title: "Hello World" }
3. GET /posts/2            → { title: "Second Post" }
4. GET /posts/3            → { title: "Third Post" }
```

Displaying a user's profile with their posts requires **4 HTTP round trips**: 1 for the user, then N more for each post. With many posts (or many users on a list page), this multiplies quickly.

## Why It Happens in REST

REST is resource-oriented — each endpoint represents one resource type. Related resources live at different URLs. There is no standard way to fetch nested or related data in a single call without building custom composite endpoints.

## Consequences

- **High latency** — sequential round trips compound; 4 requests × 50ms each = 200ms minimum
- **Mobile impact** — worse on high-latency or metered connections
- **Backend load** — multiple lightweight calls may be less efficient than one structured query
- **Complex client code** — clients must orchestrate multi-step fetch sequences

## Mitigations in REST

- **Composite endpoints** — custom endpoints that bundle related data (e.g., `GET /users/42?include=posts`)
- **BFF (Backend For Frontend)** — a dedicated API layer per client type that pre-aggregates data
- **Response embedding** — `_embedded` resources in HAL/JSON:API formats

## In GraphQL

A single GraphQL query fetches a user and their posts in one round trip:

```graphql
query {
  user(id: 42) {
    name
    posts {
      title
    }
  }
}
```

Returns all data in one response. No N+1.

## Related Concepts

- [[REST API]] — the primary source of under-fetching
- [[GraphQL]] — eliminates under-fetching by design
- [[Over-fetching]] — the complementary problem (too much data per request)
