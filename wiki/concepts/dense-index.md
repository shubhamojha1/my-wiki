---
title: "Dense Index"
type: concept
tags: [database, index, structure]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Dense Index

A **dense index** has an entry for every search key value in the table. Each distinct key appears in the index.

## Characteristics

- **Every key indexed**: One index entry per search key value
- **Fast lookups**: Direct pointer to the row for any key
- **Larger size**: More entries means more storage
- **Best for**: Tables with few distinct key values or when fast individual record access is needed

## Comparison

| Aspect | Dense | [[Sparse Index]] |
|--------|-------|-----------------|
| Entries | Every key | Some keys |
| Lookup | Direct | Requires scan to nearest entry |
| Storage | Larger | Smaller |
| Write overhead | Higher | Lower |

## Related

- [[Sparse Index]] — Only indexes some keys
- [[Database Index]] — General concept
