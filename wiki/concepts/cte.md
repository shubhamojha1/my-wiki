---
title: "CTE (Common Table Expression)"
type: concept
tags: [database, sql, query]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# CTE (Common Table Expression)

A named temporary result set defined within the scope of a single SQL statement, using the WITH clause.

## Syntax

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;
```

## Example

```sql
WITH recent_students AS (
    SELECT * FROM student WHERE age < 21
)
SELECT * FROM recent_students WHERE gpa > 3.5;
```

## Benefits

- Improves readability by naming subqueries
- Reusable within a single query
- Alternative to nested queries
- Can bind column names before AS

```sql
WITH cteName (col1, col2) AS (
    SELECT 1, 2
)
SELECT col1 + col2 FROM cteName;
```

## Multiple CTEs

```sql
WITH 
    cte1 AS (SELECT 1),
    cte2 AS (SELECT 2)
SELECT * FROM cte1, cte2;
```

## Recursive CTE

Adding RECURSIVE enables self-referencing queries:
- SQL becomes Turing-complete
- Used for hierarchies, graphs, sequences

See [[Recursive CTE]].

## Related

- [[SQL]]
- [[Recursive CTE]]
- [[Window Functions]]