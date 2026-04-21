---
title: "Window Function"
type: concept
tags: [database, sql, analytics]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# Window Function

SQL function that performs calculations across a set of rows related to the current row, without collapsing them into groups.

## How It Works

1. Partition rows (PARTITION BY)
2. Sort within partition (ORDER BY in OVER)
3. For each row, compute over its "window" of related rows

## Aggregation Window Functions

Standard aggregates work as window functions:
- `AVG()`, `COUNT()`, `SUM()`, `MIN()`, `MAX()`

## Special Window Functions

- **ROW_NUMBER()**: Sequential number for each row in partition
- **RANK()**: Position with gaps for ties
- **DENSE_RANK()**: Position without gaps
- **LAG()**: Value from previous row
- **LEAD()**: Value from next row

## Syntax

```sql
SELECT 
    column,
    AGGREGATE_FUNC(column) OVER (PARTITION BY col ORDER BY col),
    ROW_NUMBER() OVER (PARTITION BY col ORDER BY col)
FROM table;
```

## Example

```sql
-- Find student with second highest grade per course
SELECT * FROM (
    SELECT *, RANK() OVER (PARTITION BY cid ORDER BY grade) AS rank
    FROM enrolled
) AS ranking
WHERE rank = 2;
```

## Key Properties

- Does NOT collapse rows (unlike GROUP BY)
- ORDER BY in OVER ensures deterministic results
- RANK computed after window function; ROW_NUMBER computed before

## Related

- [[GROUP BY]] — Collapses rows into groups
- [[SQL]]