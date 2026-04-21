---
title: "GROUP BY"
type: concept
tags: [database, sql, aggregation]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# GROUP BY

SQL clause that partitions rows into groups based on specified columns, enabling aggregate computations per group.

## Syntax

```sql
SELECT column, AGGREGATE_FUNC(column)
FROM table
GROUP BY column;
```

## Example

```sql
SELECT cid, AVG(gpa)
FROM enrolled
JOIN student ON enrolled.sid = student.sid
GROUP BY cid;
```

## Rules

- Non-aggregated columns in SELECT must appear in GROUP BY
- Each group produces one output row
- GROUP BY columns define canonical value for each group

## Related Extensions

- **GROUPING SETS**: Multiple groupings in one query
- **ROLLUP**: Hierarchical aggregation (e.g., by year, quarter, month)
- **CUBE**: All combinations of groupings

## Related

- [[HAVING]] — Filter groups after aggregation
- [[SQL]]
- [[Window Functions]]