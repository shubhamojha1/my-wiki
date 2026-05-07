---
title: "SQL"
type: concept
tags: [database, query-language, relational]
created: 2026-04-22
sources: [cmu_15-445_lec01, "https://algomaster.io/learn/system-design/sql-vs-nosql"]
---

# SQL

Structured Query Language - the standard declarative language for relational database management systems.

## Classification

SQL is a **declarative** language: users specify what data they want, not how to retrieve it. The DBMS's query optimizer determines the execution plan.

## Core Operations (CRUD)

- **SELECT**: Query data
- **INSERT**: Add new rows
- **UPDATE**: Modify existing rows
- **DELETE**: Remove rows

## DDL (Data Definition)

- **CREATE TABLE**: Define schema
- **ALTER TABLE**: Modify schema
- **DROP TABLE**: Remove table
- **CREATE INDEX**: Create index

## Example Queries

```sql
-- Select with filter
SELECT name, email FROM users WHERE age > 21;

-- Join two tables
SELECT a.title, ar.name 
FROM Albums a 
JOIN Artists ar ON a.artist_id = ar.id;

-- Aggregation
SELECT COUNT(*), AVG(price) FROM products;
```

## SQL vs NoSQL

| Dimension | SQL | [[NoSQL]] |
|-----------|-----|-----------|
| Data Model | Relational (tables, rows, columns, foreign keys) | Key-value, document, column-family, graph |
| Schema | Fixed, defined upfront, enforced | Flexible, schema-less |
| Scalability | Vertical (scale-up) | Horizontal (scale-out) |
| Transactions | Full [[ACID Transactions\|ACID]] | BASE (eventual consistency) |
| Performance | Optimized for complex queries, joins | High-throughput at scale |

### When to Choose SQL

- Structured data with clear relationships
- Complex queries requiring joins and aggregations
- ACID transactions (financial, inventory, booking)
- Stable, well-defined schema
- Strong consistency requirements

## Related

- [[Relational Model]]
- [[Relational Algebra]]
- [[Query Optimization]]
- [[NoSQL]]
- [[ACID Transactions]]