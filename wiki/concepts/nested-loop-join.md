---
title: "Nested Loop Join"
type: concept
tags: [database, query, join, algorithm]
created: 2026-04-23
---

# Nested Loop Join

**Nested loop join** is a join algorithm that uses nested loops to compare every pair of tuples from two tables.

## How It Works

```
for each tuple t1 in outer table:
    for each tuple t2 in inner table:
        if t1.key == t2.key:
            output (t1, t2)
```

## Variants

### Naive Nested Loop
- O(N × M) comparisons
- Put smaller table outer

### Block Nested Loop
- Load block of outer, scan inner once
- Better cache performance

### Index Nested Loop
- Use index on inner for lookups
- Fast when selective

## Trade-offs

- **Pros**: Simple, works without sorting/index
- **Cons**: Slow for large tables O(N×M)

## Related

- [[Hash Join]] — Usually faster
- [[Sort-Merge Join]] — Alternative
- [[Join]] — General concept