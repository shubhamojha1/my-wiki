---
title: "Hash Index"
type: concept
tags: [database, index, hash]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Hash Index

A **hash index** uses a hash function to map keys to specific bucket locations in a hash table. Each bucket contains pointers to rows.

## Characteristics

- **O(1) lookups**: Constant-time for exact match queries
- **No ordering**: Does not support range queries or sorting
- **Collision handling**: Multiple keys may hash to the same bucket
- **Fixed or dynamic**: Can use extendible or linear hashing for growth

## Trade-offs

| Pro | Con |
|-----|-----|
| Fastest for equality queries (`WHERE id = 5`) | No range scan support (`WHERE id > 5`) |
| Simple implementation | Poor for ORDER BY |
| Good for primary key lookups | Rebuilds expensive under updates |

## Related

- [[Hash Table]] — Underlying data structure
- [[B+Tree]] — Better for range queries
- [[Database Index]] — General concept
