---
title: "Partitioning"
type: concept
tags: [distributed-systems, data-distribution]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Partitioning divides a dataset into smaller, independent sets across multiple nodes.

## Purpose
- Reduce impact of dataset growth (each partition is a subset)
- Enable parallel processing

## Benefits

### Performance
- Limits amount of data to examine
- Locates related data in same partition

### Availability
- Partitions can fail independently
- Requires multiple nodes to fail before system unavailable

## Characteristics
- Application-specific (depends on access patterns)
- Focus on defining partitions based on expected access patterns
- Handle cross-partition access inefficiencies

## Common Approaches
- Range-based partitioning
- Hash-based partitioning
- Directory-based lookup

## Partitioning vs. Sharding

Scope is the distinguishing factor: partitioning divides a table into smaller pieces *within a single database instance*, either horizontally (splitting rows) or vertically (splitting columns — see [[Vertical Partitioning]]). [[Database Sharding]] extends the same idea *across multiple independent machines*. Sharding is a form of partitioning; not all partitioning involves sharding.

## Related

- [[Database Sharding]] — Horizontal scaling via partitioned databases
- [[Vertical Partitioning]] — Column-based partitioning within a single instance
- [[Hash-Based Sharding]] — Hash-based data distribution
- [[Range-Based Sharding]] — Range-based data distribution