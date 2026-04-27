---
title: "REST vs GraphQL"
type: source
tags: [system-design, api, rest, graphql]
created: 2026-04-28
sources: ["algomaster-rest-vs-graphql"]
---

# REST vs GraphQL

**REST** and **GraphQL** are two popular API architectural styles.

## REST

- **Multiple endpoints** (one per resource)
- **HTTP methods**: GET, POST, PUT, DELETE
- **Over-fetching**: Returns more data than needed
- **Under-fetching**: Multiple requests for related data
- **Versioning**: Often via URL (/v1, /v2)
- **Caching**: Leverages HTTP caching natively

## GraphQL

- **Single endpoint** (/graphql)
- **Client decides** what data to fetch
- **Queries**: Fetch data
- **Mutations**: Modify data
- **Subscriptions**: Real-time updates
- **Strong typing**: Schema-defined types
- **No versioning**: New fields additive

## Comparison

| Aspect | REST | GraphQL |
|--------|------|---------|
| Endpoints | Multiple | Single |
| Data control | Server | Client |
| Caching | HTTP native | POST-based |
| Real-time | Polling/WebSockets | Subscriptions |

## When to Use

- **REST**: Simple APIs, third-party integrations, need HTTP caching
- **GraphQL**: Multiple clients, flexible queries, real-time needed
- **Hybrid**: Both for different use cases

## Related Concepts

- [[REST API]] — REST architectural style
- [[GraphQL]] — Query language for APIs

## Source

- AlgoMaster: [REST vs GraphQL](https://blog.algomaster.io/p/rest-vs-graphql) (March 2025)