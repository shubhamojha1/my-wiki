---
title: "Three-Tier Architecture"
type: concept
tags: [architecture, tier, client-server, web]
created: 2026-05-11
sources: ["algomaster-client-server-architecture"]
aliases: ["3-Tier Architecture"]
---

# Three-Tier Architecture

The most common client-server model for modern web and enterprise applications, introducing a dedicated **Application Layer** (Logic Layer / Middle Tier) between the client and data server.

## The Three Tiers

1. **Presentation Layer (Client)** — the front-end interface (browser or mobile app)
2. **Application Layer (Logic Layer)** — processes requests, applies business rules, interacts with the database
3. **Data Layer (Database Server)** — handles storage, retrieval, and data management

## Characteristics

- Clear separation of concerns between UI, logic, and data
- Centralized business logic — clients remain lightweight
- Each tier can be developed, deployed, and scaled independently

## Example

A web application where the browser (client) interacts with a web server (application server) that queries a database server.

## Tradeoffs

| Pros | Cons |
|------|------|
| Better scalability and maintainability | More complex to set up and manage |
| Centralized logic, lightweight clients | Increased network latency between layers |
| Improved security through abstraction | |

Ideal for web apps, SaaS products, and large internal tools.

## See Also

- [[One-Tier Architecture]]
- [[Two-Tier Architecture]]
- [[N-Tier Architecture]]
- [[Client-Server Architecture]]
