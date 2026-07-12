---
title: "Data Modeling"
type: concept
tags: [database, schema-design, interview, methodology]
created: 2026-07-10
sources: ["hellointerview-data-modeling"]
---

# Data Modeling

The process of deciding what entities exist in a system, how they're identified, and how they relate — and, in a system design interview specifically, doing this to a "clear and functional" standard rather than a fully normalized, diagram-complete one.

## Three Factors That Drive Every Schema Decision

Every schema design technique below — choice of keys, normalization, indexing, sharding — exists to serve one of three underlying requirements. Naming which factor is driving a given choice, out loud, is what separates reasoning about a schema from pattern-matching one:

1. **Data volume** — determines whether data can live in one place or must be spread across multiple stores.
2. **Access patterns** — the dominant factor. How data will be queried drives denormalization and indexing decisions far more than volume does. Derive this directly from the API endpoints already designed: "what query does each endpoint need to support?"
3. **Consistency requirements** — how tightly related data must stay coupled. Financial transactions need strong consistency (same database, ACID); a social feed's like count can be eventually consistent, freeing it to live in a separate, differently-optimized store.

Example of tying a choice back to a factor explicitly: *"Since we need to load feeds quickly and likes can be eventually consistent, I'll denormalize like counts into the posts table."*

## Choosing a Database Type

Default to a relational database ([[Relational Model|SQL]], concretely PostgreSQL) unless requirements clearly signal otherwise. The interview failure mode here isn't picking the wrong database — it's reaching for an exotic one to look sophisticated. See each type's dedicated page for full mechanics; this is the interview-selection framing layered on top:

| Type | Reach for it when | Page |
|---|---|---|
| Relational (default) | Almost always — clear entities, relationships, ACID matters | [[Relational Model]] |
| [[Document Database]] | Schema genuinely changes frequently, or records vary wildly in shape — rare in a scoped interview problem | [[Document Database]] |
| [[Key-Value Store]] | Single-identifier lookups, caching, sessions — usually *alongside* SQL, not instead of it (SQL as source of truth, key-value cache in front) | [[Key-Value Store]] |
| [[Wide-Column Store]] | Enormous write volume, time-series/telemetry, append-and-aggregate workloads | [[Wide-Column Store]] |
| [[Graph Database]] | Almost never in interviews — see note below | [[Graph Database]] |

**On graph databases specifically**: they're the most common over-selection mistake. Even Facebook models its social graph in MySQL, and LinkedIn/Twitter use SQL for their core relationship data despite looking like the canonical "social network → graph DB" case. If SQL is good enough for the world's largest social graph, it's very likely good enough for the interview.

## Entities, Keys & Relationships

Map identified entities onto tables/collections with system-generated primary keys (an ID, not business data like an email — business rules change, stable keys shouldn't). Relationships are one-to-many, many-to-many, or (rarely) one-to-one — a 1:1 relationship is often a sign two tables should just be merged. [[Foreign Key|Foreign keys]] enforce referential integrity but cost write-time validation; at large scale, some systems drop them and enforce integrity at the application layer instead, trading a database guarantee for write throughput.

## Supporting Techniques

Each of these exists to serve the three factors above, not as an end in itself:

- **[[Database Index|Indexing]]** — index columns that back your actual query patterns, tied explicitly to specific API endpoints (e.g. "`GET /users/{id}/posts` needs an index on `posts.user_id`").
- **[[Data Denormalization|Normalization vs. denormalization]]** — start normalized; denormalize only for a named reason (read-heavy analytics, audit trails/event logs, search). If you need denormalized speed without giving up a clean source of truth, put a cache with the denormalized shape in front instead of denormalizing the primary schema.
- **[[Database Sharding|Sharding]]** — shard by the primary access pattern so related data stays co-located; avoid time-range shard keys for write-heavy workloads (they concentrate all current writes on one "latest" shard — a hot-shard anti-pattern, see [[Shard Key]]).

## Interview Checklist

When introducing a database component in a high-level design: (1) pick the database type, (2) list the columns each entity needs to satisfy its endpoints, (3) specify primary/foreign keys per relationship, (4) decide which columns need indexes, (5) decide whether denormalization is warranted, (6) decide whether sharding is necessary and, if so, choose a shard key matching the primary access pattern.

## Related Concepts

- [[Relational Model]], [[NoSQL]], [[Document Database]], [[Key-Value Store]], [[Wide-Column Store]], [[Graph Database]] — database type reference pages
- [[Primary Key]], [[Foreign Key]] — key mechanics
- [[Database Index]] — indexing deep dive
- [[Data Denormalization]] — normalization trade-offs
- [[Database Sharding]], [[Shard Key]] — scaling beyond a single instance
- [[ACID Transactions]] — the consistency guarantee that drives the relational default
