---
title: "Lateral Join"
type: concept
tags: [database, sql, join]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# Lateral Join

A join where the right side can reference columns from the left side. Enables correlated subqueries in FROM clause.

## Syntax

```sql
SELECT * FROM table AS t1
LATERAL (subquery referencing t1.column) AS t2;
```

## Use Case

When you need to run a correlated subquery for each row of the left table.

## Example: Student Count per Course

```sql
SELECT * FROM course AS c
LATERAL (
    SELECT COUNT(*) AS cnt 
    FROM enrolled 
    WHERE enrolled.cid = c.cid
) AS t1,
LATERAL (
    SELECT AVG(gpa) AS avg_gpa 
    FROM student s
    JOIN enrolled e ON s.sid = e.sid
    WHERE e.cid = c.cid
) AS t2;
```

## How It Works

Think of it like a for-loop: for each row in the left table, execute the right-side subquery, passing in the left row's values.

## Benefits

- More expressive than correlated subqueries in SELECT
- Can return multiple columns/rows per left row
- Cleaner than JOIN with complex WHERE conditions

## Related

- [[SQL]]
- [[CTE]]