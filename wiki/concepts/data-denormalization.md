---
title: "Data Denormalization"
type: concept
tags: [database, optimization, schema-design]
created: 2026-05-11
sources: [algomaster-scaling-database]
---

# Data Denormalization

**Data denormalization** is the process of intentionally introducing redundancy into a database schema to optimize read performance — typically by combining tables or adding redundant columns to avoid complex joins.

## How It Works

Instead of normalized tables with joins:
```sql
-- Normalized: 3 tables, needs JOIN
SELECT * FROM users u
JOIN posts p ON u.user_id = p.user_id
JOIN comments c ON u.user_id = c.user_id;
```

Denormalize by storing related data inline:
```sql
-- Denormalized: embedded JSON
CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    posts JSON,
    comments JSON
);
```

## Trade-offs

| Pro | Con |
|-----|-----|
| Faster reads (no joins) | Write amplification (update many copies) |
| Simpler query patterns | Increased storage |
| Better read scalability | Data inconsistency risk |

## When to Use

- **Read-heavy** workloads (social media feeds, product catalogs)
- **Aggregated data** (pre-joined for dashboards)
- **Caching-like patterns** (embed hot related data)
- Can be combined with [[Caching]] for further read offload

## When to Avoid

- Write-heavy workloads (update costs outweigh read benefits)
- Strong consistency requirements (redundant copies may diverge)
- Complex update logic needed across denormalized fields

## Related

- [[Caching]] — Similar performance motivation
- [[Materialized View]] — Pre-computed query results
- [[Normalization]] — Opposite design philosophy
