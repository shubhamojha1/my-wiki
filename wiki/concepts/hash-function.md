---
title: "Hash Function"
type: concept
tags: [database, data-structure, hash, algorithms]
created: 2026-04-23
updated: 2026-05-20
sources: [cmu_15-445_lec05]
---

# Hash Function

A **hash function** maps an arbitrary input key to a fixed-range output index (typically an integer), enabling O(1) average-case lookup in a [[Hash Table]]. For database use, speed and distribution matter more than cryptographic security.

## Properties of a Good Hash Function

- **Deterministic**: same key always produces the same output
- **Uniform distribution**: outputs spread evenly across the range to minimize collisions
- **Fast**: O(1) computation regardless of key size
- **Avalanche effect**: small change in input produces very different output

## Database Hash Functions (Non-Cryptographic)

| Function | Speed | Quality | Notes |
|----------|-------|---------|-------|
| **MurmurHash3** | Very fast | Very good | Widely used; not cryptographic |
| **xxHash** | Fastest | Excellent | Often default in modern DBs |
| **CityHash** | Fast | Very good | Google's hash for strings |
| **FNV** | Fast | Good | Simple, portable |
| **MD5 / SHA** | Slow | Excellent | Cryptographic; overkill for indexes |

For integer keys, identity (`h(k) = k`) or simple modular arithmetic (`k mod N`) often suffices.

## Collision

A **collision** occurs when `h(k1) = h(k2)` for `k1 ≠ k2`. Collisions are inevitable (pigeonhole principle) when the key space is larger than the table. Collision resolution strategies:

- **[[Linear Probe Hashing]]** — scan to next empty slot
- **[[Chained Hashing]]** — linked list at each slot
- **[[Extendible Hashing]]** / **[[Linear Hashing]]** — dynamically resize to reduce collisions

## Load Factor

`α = n / m` (number of keys / number of slots). As α approaches 1, collision probability rises and performance degrades. Most hash tables resize when `α > 0.7–0.8`.

## Related Concepts

- [[Hash Table]] — the data structure that uses hash functions
- [[Linear Probe Hashing]] — open addressing collision scheme
- [[Chained Hashing]] — separate chaining collision scheme
- [[Extendible Hashing]] — dynamic hash table design
- [[Cryptographic Hash]] — hash functions designed for security, not speed
