---
title: "Sliding Window Log"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# Sliding Window Log

A rate limiting algorithm that maintains a log of request timestamps and checks against a sliding time window.

## How It Works

1. Maintain a sorted log of request timestamps per client
2. On new request, remove entries older than the window size
3. Count remaining entries
4. If count < limit: allow request, add timestamp to log
5. If count >= limit: deny request

## Properties

| Aspect | Behavior |
|--------|----------|
| Accuracy | Perfect (no boundary issues) |
| Memory | O(n) where n = requests in window (high for busy APIs) |
| Complexity | Simple but memory-intensive |

## Example
Window: 60 seconds, Limit: 100 requests
- Request at T=10s → log: [10]
- Request at T=50s → log: [10, 50]
- Request at T=65s → remove entries < 5s → log: [10, 50] → count=2, allow

## Pros
- Very accurate, no rough edges
- Works well for low-volume APIs

## Cons
- Memory-intensive for high-volume APIs
- Requires storing and searching timestamps
