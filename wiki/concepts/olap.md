---
title: "OLAP"
type: concept
tags: [database, workload, analytical]
created: 2026-04-23
---

# OLAP

**OLAP** (Online Analytical Processing) is a database workload characterized by complex, read-heavy queries that aggregate and analyze large datasets.

## Characteristics

- **Complex queries**: Multi-way joins, aggregations, subqueries
- **Full table scans**: Often need to scan large portions of data
- **Historical data**: Analysis over time periods
- **Column-oriented storage**: Better for column aggregations

## Examples

- Business intelligence dashboards
- Sales reporting
- Financial analysis
- Data mining

## Comparison with OLTP

| Aspect | OLAP | OLTP |
|--------|------|------|
| Query complexity | Complex (aggregations) | Simple (point queries) |
| Data size | TB/PB | GB |
| Updates | Batch load | Frequent |
| Latency tolerance | Higher | Low |
| Storage | Column-oriented | Row-oriented |

## Related

- [[OLTP]] — Transaction processing
- [[Column Store]] — Better suited for OLAP
- [[Data Warehouse]] — Storage system for OLAP
- [[Aggregation]] — Common OLAP operation