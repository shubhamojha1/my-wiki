---
title: "OLTP"
type: concept
tags: [database, workload, transaction]
created: 2026-04-23
---

# OLTP

**OLTP** (Online Transaction Processing) is a database workload characterized by many short, concurrent transactions that perform simple reads and writes.

## Characteristics

- **Short transactions**: Individual operations complete quickly
- **High concurrency**: Many simultaneous users
- **Simple queries**: Point queries, single-row updates
- **Strong consistency**: ACID compliance critical
- **Row-oriented storage**: Better for point updates

## Examples

- Bank transfers
- E-commerce orders
- Inventory management
- User authentication

## Comparison with OLAP

| Aspect | OLTP | OLAP |
|--------|------|------|
| Transaction length | Short | Long |
| Query complexity | Simple | Complex |
| Data size | GB | TB/PB |
| Updates | Frequent | Batch load |
| Storage | Row-oriented | Column-oriented |

## Related

- [[OLAP]] — Analytical processing
- [[Row Store]] — Better suited for OLTP
- [[ACID]] — Transaction properties
- [[Transaction]] — Unit of work