---
title: "Shard Key"
type: concept
tags: [database, sharding, partitioning]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Shard Key

A **shard key** (or partition key) is the column or combination of columns used to determine which shard stores a given row. Every INSERT/UPDATE/DELETE and every routable query passes through the shard key; choosing it correctly is the most consequential sharding decision.

## Requirements for a Good Shard Key

| Requirement | Why | Example |
|-------------|-----|---------|
| **High cardinality** | Many distinct values → even distribution across shards | `user_id` (millions of values) vs `country` (200 values) |
| **Uniform distribution** | Values spread evenly so no shard becomes overloaded | Random UUID or auto-increment; avoid timestamp for write-heavy workloads |
| **Access-pattern aligned** | Frequent queries should include the shard key so they route to one shard | Shard on `tenant_id` if most queries are `WHERE tenant_id = ?` |
| **Immutable** | Changing a key requires migrating the row to a new shard | `user_id` never changes; `email` can change |
| **Co-location friendly** | Related data sharded together avoids cross-shard joins | Shard `orders` on `user_id` if you always query orders by user |

## Examples

| Key | Rating | Reason |
|-----|--------|--------|
| `user_id` | ✓ Good | High cardinality, even distribution, immutable |
| `customer_id` | ✓ Good | Natural tenant boundary for SaaS |
| `(user_id, created_at)` | ✓ Compound | Co-locates user's history; range-friendly within shard |
| `country` | ✗ Bad | Low cardinality (200 values) → hot shards |
| `created_at` | ✗ Bad | All new writes go to the latest shard (hot shard problem) |
| `email` | ✗ Bad | Can change; requires data migration on update |
| `status` | ✗ Bad | Very low cardinality (pending/active/closed) |

## The Hot Shard Problem

When too many rows hash to the same shard (or a range shard receives all new traffic):

```
Shard 0: 5,000 RPS   ← overloaded
Shard 1: 200 RPS
Shard 2: 100 RPS
```

Solution: choose a higher-cardinality key, or add a random suffix to spread load across virtual shards.

A specific case worth naming: the **celebrity problem**, where a single popular entity (a viral post's author, a trending product) generates vastly more traffic than an ordinary key, overloading whichever shard it lands on regardless of how good the overall key choice is. Mitigations beyond the general fixes above:

- **Isolate the hot key to its own dedicated shard** rather than letting it share capacity with ordinary keys.
- **Dynamic shard splitting** — detect the hot shard at runtime and split it further, rather than relying on the original static shard count.

## Composite Shard Keys

Combining columns can achieve better co-location:
- `(region, user_id)` — data stays close to the user's region AND related rows co-locate
- `(tenant_id, entity_id)` — all tenant data together; each entity has a unique ID within the tenant

## Changing the Shard Key

Changing a shard key after deployment is one of the most painful database migrations:
1. All existing data must be read and re-routed to the new shard.
2. Application must dual-write during migration.
3. Migration may take hours or days for large datasets.

Choose carefully before launch.

## Related Concepts

- [[Database Sharding]] — general sharding concepts
- [[Hash-Based Sharding]] — applies hash function to the shard key
- [[Range-Based Sharding]] — uses key range boundaries
- [[Consistent Hashing]] — uses shard key on a hash ring
- [[Cross-Shard Query]] — required when queries don't include the shard key
