---
title: "SQL"
type: concept
tags: [database, query-language, relational]
created: 2026-04-22
sources: [cmu_15-445_lec01]
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

## Related

- [[Relational Model]]
- [[Relational Algebra]]
- [[Query Optimization]]