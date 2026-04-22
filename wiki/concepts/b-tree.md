---
title: "B+Tree"
type: concept
tags: [database, storage, index, btree]
created: 2026-04-23
---

# B+Tree

A **B+Tree** is a self-balancing tree data structure that maintains sorted data and allows efficient insertion, deletion, and search. It is the most common index structure in database systems.

## Structure

- **Root**: Top node, may have children
- **Internal Nodes**: Store keys and child pointers (not data)
- **Leaf Nodes**: Store actual data (or pointers to data) and linked list
- **All leaves at same level** — balanced height

## Properties

- **Sorted**: Keys in order, enables range scans
- **Balanced**: All paths from root to leaf have same length
- **Fan-out**: High branching factor (hundreds of children)
- **Height**: Typically 2-4 levels for large tables

## Operations

- **Search**: O(log N) — traverse from root
- **Insert**: Find leaf, insert key (split if full)
- **Delete**: Find leaf, remove key (merge if underfull)
- **Range scan**: Start at first key, follow leaf links

## Variants

- **B-Tree**: Internal nodes can store data (not just keys)
- **B+Tree**: Only leaves store data, internal nodes store keys only

## Related

- [[Index-Organized Table]] — Uses B+Tree to store data
- [[Database Page]] — B+Tree nodes are stored in pages
- [[Primary Key]] — Often the B+Tree key
- [[Clustered Index]] — Table ordered by index key