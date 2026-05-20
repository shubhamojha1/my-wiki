---
title: "Hash Index"
type: concept
tags: [database, index, hash]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Hash Index

A **hash index** stores key → row-pointer mappings in a hash table. Given a key, the index applies a hash function to compute a bucket address, then follows the bucket's chain of pointers to find the matching row(s).

## Structure

```
hash(key) → bucket

key = 42  →  h(42) = 7  →  bucket[7] → [(42, page5, slot2), ...]
key = 99  →  h(99) = 3  →  bucket[3] → [(99, page2, slot1), ...]
key = 55  →  h(55) = 7  →  bucket[7] → [(42, page5, slot2), (55, page8, slot3)]  (collision)
```

## Lookup Characteristics

| Query type | Hash index | B+Tree index |
|------------|-----------|-------------|
| Exact equality (`col = 5`) | O(1) average | O(log n) |
| Range (`col BETWEEN 5 AND 10`) | Full scan required | O(log n + k) |
| Order by / sorted output | Not supported | Natural |
| Prefix search (`LIKE 'abc%'`) | Not supported | Supported |

## Collision Handling

- **Chaining**: Each bucket holds a linked list; all keys that hash to the same bucket are chained.
- **Open addressing**: Probe adjacent buckets on collision (linear/quadratic probing, double hashing).
- **Extendible hashing**: Doubles the directory when a bucket overflows; avoids full rehash.
- **Linear hashing**: Splits individual buckets incrementally; better for disk-based storage.

## In-Memory vs On-Disk

| Variant | Where | Examples |
|---------|-------|---------|
| In-memory hash index | RAM only | PostgreSQL hash index (historically in-memory then WAL-logged since v10), MySQL Memory engine |
| On-disk hash | Disk | Oracle hash clusters, older PostgreSQL hash |
| Hybrid | Memory + overflow pages | InnoDB adaptive hash index (auto-built on hot B-tree pages) |

**InnoDB Adaptive Hash Index**: InnoDB automatically builds a hash index on top of its B+tree for B-tree pages that are accessed repeatedly. This is transparent and cannot be manually created.

## When to Choose a Hash Index

- Workload is almost entirely equality lookups (e.g., session store, primary key fetch).
- Keys are uniformly distributed (avoids bucket hotspots).
- Range queries and sorted access are not needed.

## Related Concepts

- [[Hash Table]] — the underlying data structure
- [[B+Tree]] — supports range queries; preferred general-purpose index
- [[Database Index]] — general index concepts
- [[Hash Function]] — determines bucket placement and collision rates
