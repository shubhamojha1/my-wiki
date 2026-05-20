---
title: "GraphQL"
type: concept
tags: [api, graphql, query-language]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-api", "algomaster-rest-vs-graphql"]
---

# GraphQL

**GraphQL** is a query language for APIs and a runtime for executing those queries, developed by Facebook in 2012 and open-sourced in 2015. Clients specify exactly the data they need; the server returns only that.

## Core Ideas

- **Declarative data fetching** — client describes the shape of the response it wants
- **Single endpoint** — all operations go through one URL (typically `POST /graphql`)
- **Strongly typed schema** — the API is described by a type system; introspection is built in
- **Hierarchical** — query structure mirrors the data graph

## Operations

| Operation | Purpose | Analogy |
|-----------|---------|---------|
| `query` | Read data | HTTP GET |
| `mutation` | Write or modify data | HTTP POST/PUT/DELETE |
| `subscription` | Real-time push via WebSocket | SSE / WebSocket |

## Example

```graphql
query {
  user(id: "42") {
    name
    email
    posts(last: 3) {
      title
      createdAt
    }
  }
}
```

The server returns only `name`, `email`, and the last 3 `posts` with `title` and `createdAt` — nothing more.

## vs REST

| Aspect | REST | GraphQL |
|--------|------|---------|
| Endpoints | Many (one per resource) | One |
| Response shape | Fixed by server | Defined by client |
| Over-fetching | Common | Eliminated |
| Under-fetching (N+1) | Common | Eliminated via nested queries |
| Versioning | URL-based (`/v2/`) | Schema evolution with deprecation |
| Caching | HTTP cache works naturally | Requires custom cache keys |
| File upload | Easy | Requires multipart extensions |

## Strengths

- Eliminates [[Over-fetching]] and [[Under-fetching]]
- Excellent for mobile clients with bandwidth constraints
- Introspection enables auto-generated documentation and tooling
- One round trip fetches deeply nested, related data

## Weaknesses

- Harder to cache than REST (no per-URL caching out of the box)
- N+1 database query problem requires DataLoader or batching
- Not ideal for simple CRUD APIs
- File upload is non-standard

## When to Use

- Complex, interconnected data graphs (social networks, e-commerce)
- Multiple clients (web, mobile, third-party) with different data needs
- Aggregating data from multiple microservices into one call

## Related Concepts

- [[REST API]] — Primary alternative
- [[Over-fetching]] — Problem GraphQL solves
- [[Under-fetching]] — Problem GraphQL solves
- [[gRPC]] — Alternative for internal service communication
- [[API Gateway]] — GraphQL gateway can aggregate multiple services
