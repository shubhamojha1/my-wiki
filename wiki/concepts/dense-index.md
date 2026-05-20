---
title: "Dense Index"
type: concept
tags: [database, index, structure]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Dense Index

A **dense index** has one entry for every search key value in the indexed relation — typically one entry per row. Each entry holds the key plus a direct pointer (page ID + slot) to the corresponding row.

## Structure

```
Table rows:          Dense index:
row 1  key=5    →   [5]  → (page 1, slot 1)
row 2  key=12   →   [12] → (page 1, slot 2)
row 3  key=18   →   [18] → (page 2, slot 1)
row 4  key=31   →   [31] → (page 2, slot 2)
```

A lookup for key K requires only one index traversal (O(log n) in the B-tree) followed by one page fetch — no within-block scan.

## Dense vs Sparse

| Aspect | Dense | Sparse |
|--------|-------|--------|
| Entries | One per row | One per data block |
| Lookup | Direct pointer to row | Pointer to block + scan |
| Index size | Large | Small |
| Data sort required | No | Yes (data must be sorted) |
| Typical use | Heap files, secondary indexes | Clustered/sorted files |

## When Dense Indexes Are Used

- **Secondary indexes**: Because the data is not sorted by the secondary key, there's no locality to exploit — every key needs its own pointer. Dense index is the only option.
- **Non-clustered indexes** (SQL Server terminology) always dense.
- **B+tree leaf level**: The leaves of a B+tree are a dense index — one entry per unique key in the data.

## Trade-offs

- **Size**: For a 1-billion-row table with an 8-byte key + 6-byte pointer, the dense index is ~14 GB. May not fit in memory.
- **Write amplification**: Every INSERT/DELETE requires an index entry update. For secondary indexes this multiplies write cost.
- **Solution**: Partial indexes (index only a subset of rows) reduce size while keeping lookup directness.

## Related Concepts

- [[Sparse Index]] — one entry per block; requires sorted data
- [[Database Index]] — general index concepts
- [[Secondary Index]] — always dense (no sort order to exploit)
- [[B+Tree]] — its leaf level is a dense index
- [[Partial Index]] — dense over a row subset
