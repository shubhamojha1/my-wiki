---
title: "One-Tier Architecture"
type: concept
tags: [architecture, tier, monolithic]
created: 2026-05-11
sources: ["algomaster-client-server-architecture"]
aliases: ["1-Tier Architecture", "Monolithic Model"]
---

# One-Tier Architecture

The simplest client-server model where the **user interface**, **business logic**, and **data storage** all reside in a single application or system. The user interacts directly with the data without any intermediary.

## Characteristics

- No network communication overhead
- Tight coupling of all concerns
- Single application handles everything

## Examples

Microsoft Excel, personal finance tools that store and compute everything locally.

## Tradeoffs

| Pros | Cons |
|------|------|
| Simple to build and deploy | Not scalable |
| No network communication overhead | No separation of concerns |
| Fast for single-user | Unsuitable for multi-user environments |

Best suited for small, standalone, offline applications.

## See Also

- [[Two-Tier Architecture]]
- [[Three-Tier Architecture]]
- [[N-Tier Architecture]]
- [[Client-Server Architecture]]
