---
title: "Weighted Round Robin"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Weighted Round Robin

**Weighted Round Robin** assigns weights to servers based on capacity.

## How It Works

1. Each server has a weight (processing power)
2. Higher weight = proportionally more requests

## Example

- Server1 weight: 5
- Server2 weight: 1
- Server3 weight: 1

Server1 receives 5x the traffic.

## Use Cases

- Servers have different capacities
- Heterogeneous server fleet

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Round Robin]] — Basic version without weights