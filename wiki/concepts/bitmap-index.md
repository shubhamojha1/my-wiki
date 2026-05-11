---
title: "Bitmap Index"
type: concept
tags: [database, index, bitmap, analytics]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Bitmap Index

A **bitmap index** uses a bitmap (binary array) to represent the presence or absence of a key value in each row. Each bit corresponds to a row.

## Characteristics

- **Low cardinality**: Best for columns with few distinct values (e.g., gender, status)
- **Bitwise operations**: AND, OR, NOT performed efficiently on bitmaps
- **Compact**: Very space-efficient for low-cardinality columns
- **Analytics-friendly**: Ideal for complex queries with multiple conditions

## Use Cases

- Data warehousing and OLAP
- Columns with enumerated types (e.g., order status, region)
- Queries involving multiple WHERE conditions combined with AND/OR

## Related

- [[Database Index]] — General concept
- [[B+Tree]] — More common for high-cardinality columns
