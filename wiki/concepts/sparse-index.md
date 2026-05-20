---
title: "Sparse Index"
type: concept
tags: [database, index, structure]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Sparse Index

A **sparse index** stores one entry per data block (or page) rather than one entry per row. Each entry holds the smallest (or first) key in its block and a pointer to that block.

## Dense vs Sparse Comparison

```
Dense index:            Sparse index:
key → exact row ptr     key → block ptr

[1] → row 1             [1]  → block A  (covers rows 1-100)
[2] → row 2
...                     [101]→ block B  (covers rows 101-200)
[99]→ row 99
```

| | Dense | Sparse |
|-|-------|--------|
| Entries | One per row | One per block/page |
| Size | Large | Small (fits in memory easily) |
| Lookup | Direct | Find block, then scan within block |
| Requirement | None | Data must be sorted on the indexed key |

## Lookup Algorithm

1. Binary-search the sparse index for the largest key **≤** search key.
2. Follow the pointer to that data block.
3. Sequential scan within the block to locate the exact record.

The extra block-level scan is cheap when blocks are small (one disk I/O per block).

## When Sparse Indexes Make Sense

- **Clustered / sorted data**: The physical sort order guarantees the target record is within the pointed-to block.
- **Large tables**: A sparse index can fit in RAM even when the dense index would not.
- **LSM-Trees**: Each SSTable (sorted file) has a sparse index at its head to locate data blocks; used in LevelDB, RocksDB, Cassandra.

## Limitations

- Requires sorted storage — cannot be used on heap files with random row order.
- Each lookup incurs an extra within-block scan (typically negligible, but non-zero).

## Related Concepts

- [[Dense Index]] — indexes every row; larger but no within-block scan
- [[Database Index]] — general index concepts
- [[B+Tree]] — leaf level is effectively a dense index over sorted pages
- [[LSM Tree]] — uses sparse indexes over SSTables
