---
title: "Caching for System Design Interviews"
type: source
tags: [system-design, caching, interview]
created: 2026-07-10
sources: ["https://www.hellointerview.com/learn/system-design/core-concepts/caching"]
---

# Caching for System Design Interviews

Source: [[Hello Interview]] core-concepts guide.

## Framing

Like the companion [[API Design for System Design Interviews]] guide, this article treats its topic as one interview phase rather than a comprehensive reference: introduce caching only after identifying a specific database bottleneck with concrete metrics, then walk through identifying what to cache, choosing an architecture, setting an eviction policy, and naming the downsides it introduces. Its framing principle: "caches make reads faster and reduce load on whatever is behind them, but they introduce complexity around staleness and invalidation." The concrete latency number it opens with — Redis reads at ~1ms vs. a database at ~50ms, "a 50x improvement" — is the headline justification for reaching for caching at all.

Most of this article's mechanics (cache-aside, write-through, write-behind, read-through, LRU/LFU/FIFO eviction, cache stampede) are already documented in this wiki in more depth, via [[Caching]], [[Cache-Aside]], [[Cache Eviction Policy]], and [[Cache Stampede]]. This summary focuses on what's new rather than re-deriving ground those pages already cover.

## New Ground: Cache Locations

The article's four-location framing is coarser than this wiki's existing per-location pages, but names two categories not previously captured:

- **[[In-Process Caching]]** — local memory inside an application process (config, feature flags). "Blazing fast, but it comes with obvious limitations" since each server holds its own independent copy, unshared across instances.
- **Client-Side Caching** — data cached on user devices or within client libraries, offering "limited control from the backend" and staleness challenges distinct from the protocol-level mechanics [[Browser Caching]] already documents (this wiki treats client-side caching as effectively covered by Browser Caching's HTTP-protocol detail plus this note, rather than a separate page).

Its other two locations — External Caching (Redis/Memcached) and CDN — map directly onto this wiki's existing [[In-Memory Cache]] and [[CDN]] pages. One CDN detail worth noting: the article states modern CDNs cache "much more than static files," including API responses and full HTML pages, not just images/CSS/JS.

## New Ground: Hot Keys

The article names cache hot keys as a distinct problem from cache stampede — see [[Cache Hot Key]] for the concept page, created because it parallels the wiki's existing [[Rate Limiter Hot Key]] page (same phenomenon, different domain) closely enough to warrant the same treatment. Mitigations named: replication, a local fallback cache, and rate limiting as a backstop.

## Everything Else

Cache architectures (cache-aside, write-through, write-behind, read-through), eviction policies (LRU/LFU/FIFO/TTL), and cache consistency/stampede are all already covered at equal or greater depth by existing pages — no changes needed there.

## Related Pages

- [[Caching]]
- [[Cache-Aside]]
- [[Cache Eviction Policy]]
- [[Cache Stampede]]
- [[In-Process Caching]]
- [[Cache Hot Key]]
- [[In-Memory Cache]]
- [[CDN]]
- [[Browser Caching]]
- [[Rate Limiter Hot Key]]
- [[API Design for System Design Interviews]]
- [[Hello Interview]]
