---
title: "Vertical Partitioning"
type: concept
tags: [database, partitioning, optimization]
created: 2026-05-11
sources: [algomaster-scaling-database]
---

# Vertical Partitioning

**Vertical partitioning** splits a database table into smaller tables, each containing a subset of the columns from the original.

## How It Works

Columns are grouped by access frequency:
- **Hot columns**: Frequently accessed (e.g., ID, name, price) go in one table
- **Warm columns**: Less frequent (e.g., description, specs) in another
- **Blob columns**: Large binary data (e.g., images, videos) in a third

## Example

An e-commerce `product` table split into:
- `core_product` (id, name, price, category)
- `product_details` (description, specifications)
- `product_media` (images, videos)

## Benefits

- Reduces amount of data read per query
- Improves cache efficiency for hot columns
- Enables different storage/compression per table
- Better I/O for selective column access

## Trade-offs

| Pro | Con |
|-----|-----|
| Faster queries on hot columns | More complex joins across partitions |
| Better cache utilization | Transactional overhead |
| Independent scaling of partitions | Application must manage multiple tables |

## Related

- [[Partitioning]] — General partitioning concept
- [[Database Sharding]] — Horizontal splitting (by rows)
- [[Column Store]] — Extreme vertical partitioning
