---
title: "Round Robin"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Round Robin

A **Round Robin** load balancing algorithm that sequentially distributes requests across servers.

## How It Works

1. Request goes to first server
2. Next request goes to second server
3. Loops back to first after last server

## Use Cases

- All servers have similar capacity
- Simple, stateless workloads

## Pros

- Simple to implement
- Even distribution

## Cons

- Doesn't consider server load
- Inefficient for different server capacities

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Weighted Round Robin]] — Capacity-aware version