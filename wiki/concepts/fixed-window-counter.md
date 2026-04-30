---
title: "Fixed Window Counter"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# Fixed Window Counter

A rate limiting algorithm that divides time into fixed windows and counts requests per window.

## How It Works

1. Time divided into fixed windows (e.g., 1-minute intervals: 12:00–12:01, 12:01–12:02)
2. Each window has a counter starting at zero
3. New requests increment the counter
4. If counter exceeds limit, requests denied until next window

## Boundary Problem

The key weakness: at window boundaries, a client can send up to 2x the allowed rate.

Example: Limit = 100 requests/minute
- At 12:00:50, send 100 requests (uses rest of window 12:00–12:01)
- At 12:01:00, send 100 more requests (uses new window 12:01–12:02)
- Result: 200 requests in ~12 seconds

## Properties

| Aspect | Behavior |
|--------|----------|
| Accuracy | Low (boundary issue) |
| Memory | O(n) where n = number of windows tracked |
| Complexity | Very simple |

## Pros
- Easy to implement and understand
- Clear rate limits per window

## Cons
- Boundary problem allows 2x burst rate
- No smoothing between windows
