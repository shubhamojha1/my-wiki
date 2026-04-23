---
title: "Database Caching"
type: concept
tags: [caching, database, performance]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Database Caching

**Definition:** Caching performed transparently by the database engine, optimizing performance without application code changes.

## How It Works

When you start a database, you get default configuration that:
1. Provides some caching out of the box
2. Is optimized for a generic use case
3. Can be tuned to your specific access patterns

## Tuning Database Caching

A skilled DBA or operational engineer can dramatically improve performance by tuning configuration to match access patterns:

- Adjusting buffer pool sizes
- Configuring query cache settings
- Optimizing row caches (e.g., Cassandra row cache optimization)

## Key Advantage

**Application code gets faster "for free"** — no code changes required.

## Contrast with Application Caching

| Aspect | Database Caching | Application Caching |
|--------|-------------------|---------------------|
| Implementation | Built-in, transparent | Explicit code integration |
| Control | Limited to configuration | Full programmatic control |
| Scope | Per-database | Cross-database patterns |
| Benefit | "Free" performance gains | Handles complex patterns |

## Example: Cassandra Row Cache

Properly configured Cassandra row caches can:
- Dramatically reduce I/O load
- Substantially improve request latencies
- Offload work from application code

## Best Practice

Use both together:
1. Start with database caching for easy wins
2. Add application caching for complex patterns database can't handle
3. Tune database caching first before complex application logic

## Related Concepts

[[Caching]], [[Application Caching]], [[In-Memory Cache]], [[Buffer Pool]]