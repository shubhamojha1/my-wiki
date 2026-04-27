---
title: "Least Connections"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Least Connections

**Least Connections** routes to the server with fewest active connections.

## How It Works

1. Track active connections per server
2. New request goes to server with least connections

## Use Cases

- Varying request durations
- Similar server capabilities

## Pros

- Dynamic load distribution
- Adapts to current server load

## Cons

- Requires tracking active connections

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Least Response Time]] — Response time-based version