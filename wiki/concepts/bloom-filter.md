---
title: "Bloom Filter"
type: concept
tags: [data-structure, probabilistic, set-membership]
created: 2026-05-11
sources: [algomaster-bloom-filters]
---

# Bloom Filter

A **Bloom filter** is a probabilistic data structure that tests whether an element **might be** in a set, using far less memory than a hash table. It can produce **false positives** but never **false negatives**.

## Structure

- **Bit array** of size `m`, all bits initially 0
- **k independent hash functions**, each maps an element to a position `[0, m-1]`

## Operations

### Insert
1. Pass element through each of k hash functions → k positions
2. Set all k bits to 1

### Membership Check
1. Pass element through k hash functions → k positions
2. If **any bit is 0**: element **definitely not** in set
3. If **all bits are 1**: element **probably** in set (false positive possible)

## Properties

| Property | Guarantee |
|----------|-----------|
| False negatives | **None** — "not present" is definitive |
| False positives | **Possible** — controlled by m, k, and number of inserted elements |
| Deletions | **Not supported** in standard form |
| Memory | **O(1)** — fixed-size bit array regardless of element count |

## Tuning

False positive rate `p` depends on:
- `m` — bit array size (larger = fewer collisions)
- `k` — number of hash functions (more = lower p, up to a point)
- `n` — number of inserted elements

Optimal `k ≈ (m/n) × ln(2)`

## Real-World Uses

- **Web caching** (Apache): Check if URL probably cached
- **Spam filtering**: Quick spam address check
- **Databases**: Cassandra, HBase, Redis use Bloom filters to skip disk lookups for missing keys
- **Recommendations**: Netflix avoids re-recommending watched content
- **Social networks**: Facebook avoids suggesting existing friends
- **Blockchain**: Bitcoin SPV nodes use Bloom filters for transaction filtering

## Related

- [[Counting Bloom Filter]] — Variant supporting deletions via counters
- [[Hash Table]] — Exact but memory-intensive alternative
- [[Caching]] — Common application domain
