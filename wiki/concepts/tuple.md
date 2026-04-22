---
title: "Tuple"
type: concept
tags: [database, storage, data]
created: 2026-04-23
---

# Tuple

A **tuple** (or row) is a collection of attribute values that represents a single record in a relational database table.

## Characteristics

- **Fixed-length attributes**: Integers, floats (stored directly)
- **Variable-length attributes**: Strings, blobs (stored with offset)
- **Null values**: Often represented with a bitmap

## Storage in Pages

- [[Slotted Page]]: Tuples stored sequentially, slot array tracks offsets
- [[Index-Organized Table]]: Tuples stored in B+Tree leaf nodes
- [[Heap File]]: Tuples stored without particular order

## Tuple Header

- **Transaction ID**: For concurrency control
- **Commit identifier**: Visibility info
- **Null bitmap**: Which attributes are null
- **Record length**: Size of tuple

## Related

- [[Database Page]] — Container for tuples
- [[Slotted Page]] — Organization scheme
- [[Index-Organized Table]] — Alternative storage
- [[Schema]] — Defines tuple structure