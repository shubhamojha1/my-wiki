---
title: "Sliding Window Counter"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# Sliding Window Counter

A hybrid rate limiting algorithm that combines [[Fixed Window Counter]] efficiency with [[Sliding Window Log]] accuracy.

## How It Works

1. Track request counts for current and previous window
2. Calculate weighted estimate based on overlap with sliding window:
   ```
   estimated_count = (overlap_ratio * previous_window_count) + current_window_count
   ```
3. If `estimated_count + 1 > limit`: deny request
4. Otherwise: allow and increment current window counter

## Example

Window: 1 minute, Limit: 100 requests
- At 30 seconds into current window (50% overlap):
  - Previous window had 80 requests
  - Current window has 40 requests
  - Estimated = (50% × 80) + 40 = 40 + 40 = 80
  - Next request would make 81 → allowed (81 < 100)

## Properties

| Aspect | Behavior |
|--------|----------|
| Accuracy | Good (approximation of sliding window) |
| Memory | O(1) per client (just 2 counters) |
| Complexity | Moderate |

## Pros
- More accurate than [[Fixed Window Counter]]
- More memory-efficient than [[Sliding Window Log]]
- Smooths out boundary issues between windows

## Cons
- Slightly more complex to implement
- Approximation, not exact like [[Sliding Window Log]]
