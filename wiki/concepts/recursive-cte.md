---
title: "Recursive CTE"
type: concept
tags: [database, sql, recursion]
created: 2026-04-22
sources: [cmu_15-445_lec02]
---

# Recursive CTE

A Common Table Expression that references itself, enabling recursive query execution. Makes SQL Turing-complete.

## Syntax

```sql
WITH RECURSIVE cte_name AS (
    -- Base case: initial row(s)
    SELECT ...
    UNION [ALL]
    -- Recursive case: references cte_name
    SELECT ... FROM cte_name WHERE ...
)
SELECT * FROM cte_name;
```

## Example: Number Sequence

```sql
WITH RECURSIVE counter AS (
    SELECT 1 AS n
    UNION
    SELECT n + 1 FROM counter WHERE n < 10
)
SELECT * FROM counter;
```

## Execution Model

1. **Base case**: Evaluate initial SELECT
2. **Recursive case**: Use previous iteration's results
3. **Repeat**: Until no new rows generated
4. **Union**: Combine all iterations

## Use Cases

- Hierarchical data (org charts, file systems)
- Graph traversal
- Generating sequences
- Path finding

## Safety

Most systems have a recursion depth limit (e.g., PostgreSQL's `max_recursive_iterations`).

## Related

- [[CTE]]
- [[SQL]]