---
title: "LRU"
type: concept
tags: [database, storage, cache, eviction]
created: 2026-04-23
---

# LRU

**LRU** (Least Recently Used) is a cache [[Cache Eviction Policy]] that evicts the page that was accessed longest ago when the cache is full.

## How It Works

1. Track access time for each item
2. On eviction, select item with oldest access time
3. On access, update access time to "now"

## Variants

- **LRU-K**: Considers last K accesses, more robust to scan workloads
- **Clock**: Approximate LRU using reference bits (more efficient)
- **2Q**: Differentiates between resident and recycled pages

## Trade-offs

- **Pros**: Good hit rate for temporal locality
- **Cons**: Expensive to maintain exact ordering; vulnerable to scans

## Related

- [[Cache Eviction Policy]] — General category
- [[Buffer Pool]] — Where LRU is commonly used
- [[Clock Replacement]] — Efficient LRU approximation
- [[ARC]] — Adaptive Replacement Cache (LRU + LFU)