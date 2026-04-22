---
title: "Hash Function"
type: concept
tags: [database, data-structure, hash]
created: 2026-04-23
---

# Hash Function

A **hash function** maps a key to an index in a hash table array.

## Properties

- **Deterministic**: Same key → same index
- **Uniform distribution**: Keys spread evenly across slots
- **Fast**: Should be O(1)

## Database Considerations

- **Not cryptographic**: Don't need secure hash functions
- **Common functions**: MurmurHash, xxHash, CityHash
- **Integer keys**: Can use identity or simple modular arithmetic

## Collision

When `h(k1) = h(k2)`, we have a **collision**. Must be handled by the hashing scheme.

## Related

- [[Hash Table]] — Data structure using hash function
- [[Collision]] — When hash function produces same index
- [[Linear Probe Hashing]] — Collision resolution scheme