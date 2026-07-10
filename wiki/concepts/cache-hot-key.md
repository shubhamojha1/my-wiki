---
title: "Cache Hot Key"
type: concept
tags: [caching, performance, failure-mode]
created: 2026-07-10
sources: ["hellointerview-caching"]
---

# Cache Hot Key

A single cache key receiving disproportionately high traffic relative to other keys, concentrating load onto whichever cache node holds it and creating a bottleneck even though the overall cache cluster has capacity to spare.

## Why It Happens

Cache data is typically distributed across nodes by key (see [[Consistent Hashing]] / [[Hash-Based Sharding]]), so total cluster capacity assumes traffic spreads roughly evenly across keys. A single viral post, celebrity profile, or trending product can violate that assumption — one key absorbs a disproportionate share of requests, and the single node holding it becomes the bottleneck regardless of how many other nodes are idle.

## Mitigations

- **Replication** — copy the hot key's value to multiple nodes so requests for it can be spread across replicas instead of hammering one.
- **Local fallback cache** — an [[In-Process Caching|in-process]] cache layer in front of the shared cache absorbs repeated reads for the same hot key without a network hop at all.
- **Rate limiting** — cap request volume for a given key as a backstop, trading strict correctness for protecting the node from overload (see [[Rate Limiting]] and the analogous [[Rate Limiter Hot Key]] problem in the rate-limiting domain).

## Related Concepts

- [[Rate Limiter Hot Key]] — the same underlying phenomenon (one identifier overwhelming one shard) in the rate-limiting domain
- [[Caching]] — parent concept; hot spots are listed there as a general challenge
- [[Cache Stampede]] — a related but distinct failure mode: stampede is many keys' concurrent misses overwhelming the *backend*, hot key is one key's traffic overwhelming a *cache node*
- [[Consistent Hashing]] — the distribution mechanism whose even-traffic assumption hot keys violate
