---
title: "HAVING"
type: concept
tags: [database, sql, aggregation]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# HAVING

SQL clause that filters groups after aggregation (unlike WHERE which filters rows before).

## Syntax

```sql
SELECT column, AGGREGATE_FUNC(column)
FROM table
GROUP BY column
HAVING AGGREGATE_FUNC(column) > value;
```

## Example

```sql
SELECT cid, AVG(gpa) AS avg_gpa
FROM enrolled
JOIN student ON enrolled.sid = student.sid
GROUP BY cid
HAVING AVG(gpa) > 3.9;
```

## Key Difference

- **WHERE**: Filters individual rows before grouping
- **HAVING**: Filters groups after aggregation

## Related

- [[GROUP BY]] — Partition rows into groups
- [[SQL]]