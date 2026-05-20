---
title: "Hash Table"
type: concept
tags: [database, data-structure, index, algorithms]
created: 2026-04-23
updated: 2026-05-20
sources: [cmu_15-445_lec05]
---

# Hash Table

A **hash table** is a data structure that maps keys to values using a [[Hash Function]] to compute array indices. It provides O(1) average-case lookup, insert, and delete — the fastest possible for point lookups.

## How It Works

```
key → hash_function → index → array slot → value
```

1. Apply `h(key)` to get an index `i`
2. Store or retrieve the value at `array[i]`
3. Handle collisions (when two keys map to the same index)

## Collision Resolution

| Strategy | Mechanism | Pros | Cons |
|----------|-----------|------|------|
| **[[Chained Hashing]]** | Each slot holds a linked list | Simple; handles high load factor | Pointer overhead; poor cache locality |
| **[[Linear Probe Hashing]]** | Probe next slots linearly | Cache-friendly; no pointers | Clustering degrades performance |
| **Robin Hood Hashing** | Evict rich (low PSL) elements | Reduced variance in probe lengths | More complex |
| **Cuckoo Hashing** | Two hash functions; displace old | Worst-case O(1) lookup | Complex insert |

## Performance

| Operation | Average Case | Worst Case (many collisions) |
|-----------|-------------|------------------------------|
| Lookup | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case is rare; avoided by keeping load factor < 0.75 and using good hash functions.

## Database Uses

| Use Case | Hash Table Role |
|----------|----------------|
| Buffer pool page table | `page_id → frame_id` mapping |
| Table catalog | `table_name → table_metadata` |
| [[Hash Index]] | `key → tuple pointer(s)` |
| [[Hash Join]] | Build phase: inner table keyed by join attribute |

## Limitations

- **No ordered operations** — cannot do range scans (use [[B-Tree]] instead)
- **Worst-case O(n)** — with many collisions or poor hash function
- **Resize cost** — resizing requires rehashing all entries

## Related Concepts

- [[Hash Function]] — the function that maps keys to slots
- [[Chained Hashing]] — separate chaining collision resolution
- [[Linear Probe Hashing]] — open addressing collision resolution
- [[Extendible Hashing]] — dynamically resizable hash table
- [[Hash Index]] — database index built on a hash table
- [[B-Tree]] — ordered alternative supporting range queries
