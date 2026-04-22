---
title: "Secondary Index"
type: concept
tags: [database, index]
created: 2026-04-23
---

# Secondary Index

A **secondary index** is an index that is not the clustered index. It provides an alternate access path to data.

## Characteristics

- **Multiple per table**: Can have many secondary indexes
- **Contains pointers**: Leaf nodes store row IDs, not data
- **Unique or non-unique**: Can enforce uniqueness constraint
- **Covering index**: Can satisfy query without table access

## How It Works

1. Query uses secondary index
2. Index returns row pointers (RIDs)
3. Table/clustered index accessed to get actual data
4. **Covering**: If all needed columns in index, skip table access

## Trade-offs

- **Pros**: Fast alternate access paths, can index any columns
- **Cons**: Additional storage, maintenance overhead on writes

## Related

- [[Clustered Index]] — The primary/index table order
- [[Index Scan]] — Access method
- [[Covering Index]] — Query answered from index alone