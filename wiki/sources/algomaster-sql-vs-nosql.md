---
title: "SQL vs NoSQL"
type: source
tags: [database, sql, nosql, system-design]
created: 2026-05-08
sources: ["https://algomaster.io/learn/system-design/sql-vs-nosql"]
---

# SQL vs NoSQL

**Source:** AlgoMaster.io by Ashish Pratap Singh (Updated Oct 2025)

Compares relational (SQL) and non-relational (NoSQL) databases across seven dimensions.

## The 7 Key Differences

| Dimension | SQL | NoSQL |
|-----------|-----|-------|
| Data Model | Relational (tables, rows, columns, foreign keys) | Non-relational (key-value, document, column-family, graph) |
| Schema | Fixed, defined upfront, enforced | Flexible, schema-less, dynamic attributes |
| Scalability | Vertical (scale-up) | Horizontal (scale-out) |
| Query Language | SQL standard (SELECT, JOIN, GROUP BY) | Proprietary APIs, query languages specific to each DB |
| Transactions | Full ACID | BASE (Basically Available, Soft state, Eventual consistency) |
| Performance | Optimized for complex queries, joins, aggregations | Optimized for high-throughput reads/writes at scale |
| Use Cases | Structured data, complex relationships, ACID needs | Unstructured data, high scale, rapid iteration |

## When to Choose SQL

- Structured data with clear relationships
- Complex queries requiring joins and aggregations
- ACID transactions (financial systems, inventory, booking)
- Stable, well-defined schema
- Strong consistency requirements

## When to Choose NoSQL

- Rapid iteration with evolving data models
- Massive scale with horizontal distribution
- Unstructured or semi-structured data (JSON, logs, events)
- High-throughput read/write workloads
- Eventual consistency is acceptable

## Related Pages

- [[SQL]], [[NoSQL]], [[ACID Transactions]], [[Relational Model]], [[Document Database]], [[Key-Value Store]]
