---
title: "Hash Join"
type: concept
tags: [database, query, join, algorithm]
created: 2026-04-23
---

# Hash Join

**Hash join** is a join algorithm that uses a hash table to find matching tuples efficiently.

## How It Works

1. **Build phase**: Hash outer table into hash table
2. **Probe phase**: Scan inner table, probe hash table for matches

## Complexity

- O(N + M) if hash table fits in memory
- Use smaller table as build (outer)

## Variants

### In-Memory Hash Join
- Entire build table in memory
- Fast, O(N+M)

### Grace Hash Join
- Partition both tables
- Handle partition pairs separately
- Handles large tables that don't fit in memory

## Trade-offs

- **Pros**: Fast for equijoin O(N+M)
- **Cons**: Only equijoin, needs memory

## Related

- [[Nested Loop Join]] — Simpler
- [[Sort-Merge Join]] — Alternative
- [[Grace Hash Join]] — Partitioned version