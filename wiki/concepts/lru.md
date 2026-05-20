---
title: "LRU"
type: concept
tags: [database, storage, cache, eviction, algorithms]
created: 2026-04-23
updated: 2026-05-20
sources: [cmu_15-445_lec06]
---

# LRU

**LRU** (Least Recently Used) is a cache eviction policy that evicts the item accessed furthest in the past when the cache is full. It exploits temporal locality: recently accessed items are likely to be accessed again soon.

## How It Works

Maintain a doubly-linked list ordered by recency:

```
Most Recent ←→ B ←→ A ←→ D ←→ E ←→ Least Recent
```

- **Access item A** → move A to the front (most recent)
- **Cache full, insert F** → evict E (least recently used), add F to front

Standard implementation: **HashMap + Doubly-Linked List**
- HashMap: O(1) lookup by key
- Linked list: O(1) move-to-front and remove-from-tail

## Complexity

| Operation | Time |
|-----------|------|
| Lookup | O(1) |
| Insert | O(1) |
| Evict | O(1) |
| Space | O(capacity) |

## Variants

| Variant | Key Idea | Advantage |
|---------|----------|-----------|
| **LRU-1** (basic) | Evict least recently used | Simple |
| **LRU-K** | Use last K accesses (not just 1) | More robust to sequential scans |
| **2Q** | Separate hot and cold queues | Resists one-time-access pollution |
| **[[Clock Replacement]]** | Reference bit + clock hand | O(1) approximate LRU, cache-friendly |

## Vulnerability: Sequential Scans

A sequential scan (full table scan) can completely evict the working set:
- Pages A, B, C, D, E are hot
- Scan loads F, G, H, I, J — each evicts a hot page
- After scan: A–E all evicted; cache polluted with scan pages

**Fix**: LRU-K or 2Q; or mark scan pages as "not recently used" from the start.

## Use in Databases

The DBMS buffer pool uses LRU (or variants) to decide which disk pages to evict from RAM when a new page must be read in. Database-specific optimizations: **LRU-K** is common in production (PostgreSQL uses clock sweep, InnoDB uses a modified LRU list).

## Related Concepts

- [[Buffer Pool]] — the DB cache that uses LRU
- [[Cache Eviction]] — the general category
- [[Clock Replacement]] — efficient approximation
- [[ARC]] — adaptive algorithm combining LRU + LFU
