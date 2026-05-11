---
title: "Two-Tier Architecture"
type: concept
tags: [architecture, tier, client-server]
created: 2026-05-11
sources: ["algomaster-client-server-architecture"]
aliases: ["2-Tier Architecture"]
---

# Two-Tier Architecture

A client-server model split into two parts:
- **Client** — handles the **presentation layer** (UI)
- **Server** — handles both **business logic** and **data storage**

The client communicates directly with the server, which runs the logic and interacts with the database.

## Characteristics

- Direct client-to-server communication
- Server handles both application logic and data management
- Simpler deployment than 3-tier

## Example

A desktop application that connects directly to a central database to retrieve and display data.

## Tradeoffs

| Pros | Cons |
|------|------|
| Centralized data management | Poor scalability as clients increase |
| Simpler than 3-tier | Performance bottlenecks on the server |
| | Difficult to update logic across client versions |

Suitable for internal tools or apps with a small user base and limited traffic.

## See Also

- [[One-Tier Architecture]]
- [[Three-Tier Architecture]]
- [[N-Tier Architecture]]
- [[Client-Server Architecture]]
