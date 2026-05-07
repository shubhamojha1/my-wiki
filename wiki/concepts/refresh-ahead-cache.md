---
title: "Refresh-Ahead Cache"
type: concept
tags: [caching, pattern, proactive]
created: 2026-05-08
sources: ["https://github.com/donnemartin/system-design-primer#cache"]
---

# Refresh-Ahead Cache

**Definition:** A caching pattern where the cache proactively refreshes recently accessed entries before they expire, reducing latency for subsequent reads.

## Flow

```
1. [App reads key] → cache hit
2. [Cache detects TTL near expiry]
3. [Cache asynchronously re-fetches from DB]
4. [TTL extended, entry stays fresh]
```

## How It Works

The cache tracks access patterns and preemptively refreshes entries that are:
- Frequently accessed (hot)
- Nearing their TTL expiration
- Likely to be requested again soon

## Characteristics

| Aspect | Description |
|--------|-------------|
| Read latency | Very low (always fresh) |
| Write path | Configurable (write-through or write-behind) |
| Prediction dependency | Requires accurate forecasting |
| Complexity | Higher than passive strategies |

## Advantages

- **Reduced read latency** — avoids blocking on cache miss
- **Smoother performance** — refreshes happen in background, not on critical path
- **Better user experience** — no latency spikes from TTL expiration

## Disadvantages

- **Wasted refreshes** — predicting wrong items wastes resources
- **Increased load** — background refreshes add load to DB even for idle entries
- **Prediction complexity** — hard to implement well

## When to Use

- Access patterns are predictable (e.g., trending content, leaderboards)
- Latency sensitivity is high
- Cost of cache miss exceeds cost of proactive refresh

## Related Pages

- [[Caching]], [[Cache-Aside]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Read-Through Cache]]
