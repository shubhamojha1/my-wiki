---
title: "Sort-Merge Join"
type: concept
tags: [database, query, join, algorithm]
created: 2026-04-23
updated: 2026-05-20
---

# Sort-Merge Join

**Sort-merge join** (SMJ) first sorts both input tables on the join key, then merges them in a single linear scan — two sorted pointers advance together, matching equal keys.

## Algorithm

```
1. SORT phase:
   Sort R on join_key (if not already sorted)
   Sort S on join_key (if not already sorted)

2. MERGE phase:
   i = 0, j = 0
   while i < len(R) and j < len(S):
     if R[i].key == S[j].key:
       output all matching pairs (handle duplicates)
     elif R[i].key < S[j].key:
       i++
     else:
       j++
```

For duplicate keys, one side must be "marked" and rewound — this is the **mark/restore** optimization.

## Complexity

| Phase | Time |
|-------|------|
| Sort (if needed) | O(N log N + M log M) — external sort if > memory |
| Merge | O(N + M) — single linear pass |
| **Total** | **O(N log N + M log M)** |

If both inputs are already sorted (pre-indexed by join key), sort is O(1) and join is O(N + M).

## When SMJ is Preferred

| Condition | Why SMJ wins |
|-----------|-------------|
| Both tables sorted on join key (index) | Sort phase free → O(N+M) |
| Data too large for hash table in memory | Sort uses sequential I/O; hash join spills randomly |
| Range joins (`R.a BETWEEN S.b AND S.c`) | Only SMJ and NLJ support non-equijoins efficiently |
| ORDER BY join key after join | SMJ produces sorted output; avoids a sort later |

## Hash Join vs Sort-Merge Join

| Aspect | Hash Join | Sort-Merge Join |
|--------|----------|----------------|
| Equijoin only | Yes | No (supports ranges) |
| Memory | Build hash table of smaller table | Buffers for sort |
| Best case | O(N + M) if build table fits in RAM | O(N + M) if pre-sorted |
| Worst case (spill) | O(N + M + partition I/O) | O(N log N + M log M) sequential |
| Output sorted? | No | Yes (sorted by join key) |
| Parallelism | Easy (partition by hash) | Easy (merge-sort of sorted runs) |

## Example: Pre-Sorted Merge

```sql
-- Both tables have index on customer_id → B-tree already sorted
SELECT o.order_id, c.name
FROM orders o JOIN customers c ON o.customer_id = c.customer_id;
-- Planner chooses index scan + merge join → O(N + M)
```

## Related Concepts

- [[Hash Join]] — usually faster for equijoins when tables fit in memory
- [[Nested Loop Join]] — O(N×M); good for small inner table or indexed lookup
- [[External Sort]] — the on-disk sort used when data exceeds memory
- [[Clustered Index]] — pre-sorts data by the key; enables O(N+M) merge join
