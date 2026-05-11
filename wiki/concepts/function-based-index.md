---
title: "Function-Based Index"
type: concept
tags: [database, index, function]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Function-Based Index

A **function-based index** is created on the result of a function or expression applied to one or more columns. Also called an expression-based index.

## Characteristics

- **Pre-computed**: Stores the result of the function, not raw column values
- **Query acceleration**: Speeds up queries using the same expression in WHERE
- **Flexible**: Any deterministic function can be indexed

## Examples

```sql
-- Index on UPPER for case-insensitive search
CREATE INDEX idx_upper_name ON employees (UPPER(last_name));

-- Index on computed expression
CREATE INDEX idx_total ON orders (quantity * unit_price);
```

## Related

- [[Database Index]] — General concept
