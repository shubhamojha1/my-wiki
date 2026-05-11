---
title: "Materialized View"
type: concept
tags: [database, query, optimization]
created: 2026-05-11
sources: [algomaster-scaling-database]
---

# Materialized View

A **materialized view** is a pre-computed, disk-stored result set of a query. Unlike regular views (virtual, computed on-the-fly), materialized views physically store the results for fast retrieval.

## Characteristics

- **Pre-computed**: Query runs once, results stored
- **Disk-stored**: Physical table-like storage
- **Staleable**: Data becomes stale until refreshed
- **Refreshable**: Can be scheduled (cron) or triggered

## Example

```sql
CREATE MATERIALIZED VIEW daily_sales_summary AS
SELECT date, product_id,
       SUM(quantity) AS total_quantity,
       SUM(amount) AS total_amount
FROM sales
GROUP BY date, product_id;
```

Refresh schedule:
```sql
REFRESH MATERIALIZED VIEW daily_sales_summary;  -- manual
-- or via scheduler (cron every 1 day)
```

## Use Cases

- Daily/weekly sales reports and dashboards
- Aggregated analytics on large datasets
- Pre-computed joins across multiple tables
- Data warehouse ETL pipelines

## Trade-offs

| Pro | Con |
|-----|-----|
| Blazing fast read queries | Stale data between refreshes |
| Offloads expensive computation | Storage overhead |
| Simplifies application queries | Refresh can be resource-intensive |

## Related

- [[SQL]] — Query language for defining views
- [[Caching]] — Similar idea (pre-computed for speed)
- [[OLAP]] — Typical workload for materialized views
