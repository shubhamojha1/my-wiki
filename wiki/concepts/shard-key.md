---
title: "Shard Key"
type: concept
tags: [database, sharding, partitioning]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Shard Key

A **shard key** (or sharding key) is a unique identifier used to determine which shard a particular piece of data belongs to. It can be a single column or a combination of columns.

## Requirements

- **High cardinality** — many distinct values for even distribution
- **Access-pattern aligned** — queried frequently to enable targeted routing
- **Stable** — values should not change (or change rarely)

## Examples

| Key | Good? | Reason |
|-----|-------|--------|
| `user_id` | Yes | High cardinality, even distribution |
| `customer_id` | Yes | Natural fit for tenant-based data |
| `country` | No | Low cardinality causes hot shards |
| `order_date` | Mixed | Can work for range but may cause skew |

## Impact

A poor shard key causes **hot spots** (one shard overloaded), frequent **rebalancing**, and inefficient **cross-shard queries**.

## Related

- [[Database Sharding]] — General concept
- [[Hash-Based Sharding]] — Uses hash of the key
- [[Range-Based Sharding]] — Uses key ranges
