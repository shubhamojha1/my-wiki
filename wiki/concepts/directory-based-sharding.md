---
title: "Directory-Based Sharding"
type: concept
tags: [database, sharding, lookup]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Directory-Based Sharding

**Directory-based sharding** uses a lookup table (directory) that directly maps each shard key to the shard where its data resides.

## How It Works

1. A lookup table stores `key → shard` mappings
2. On query, look up the key in the directory
3. Route the query to the mapped shard

## Pros and Cons

| Pro | Con |
|-----|-----|
| Maximum flexibility — any key to any shard | Directory is a single point of failure / bottleneck |
| Easy to add/remove shards without reshuffling | Lookup adds latency on every query |
| No data movement during reconfiguration | Directory must be replicated for HA |

## Use Cases

- Small to medium datasets where shard mapping changes frequently
- Multi-tenant systems with varying tenant sizes
- Custom routing logic needed per tenant

## Related

- [[Database Sharding]] — General concept
- [[Hash-Based Sharding]] — No lookup needed (deterministic)
