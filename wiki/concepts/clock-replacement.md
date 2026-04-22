---
title: "Clock Replacement"
type: concept
tags: [database, storage, cache, eviction]
created: 2026-04-23
---

# Clock Replacement

**Clock** (or CLOCK) is an efficient approximation of [[LRU]] that uses a reference bit and circular scanning.

## How It Works

1. Each page has a **reference bit** (accessed flag)
2. On access, set reference bit to 1
3. On eviction, scan circularly:
   - If bit is 1: clear it and move on
   - If bit is 0: evict this page

## Why "Clock"?

The algorithm resembles a clock hand sweeping around a circular buffer of pages.

## Trade-offs

- **Pros**: O(1) per operation, no need to update timestamps
- **Cons**: Less accurate than true LRU, can keep recently-scanned pages

## Usage

Most production DBMSs use CLOCK or similar because it's faster than true LRU while providing similar performance.

## Related

- [[LRU]] — True least-recently-used (more accurate, slower)
- [[Buffer Pool]] — Where clock is commonly used
- [[Cache Eviction Policy]] — General category