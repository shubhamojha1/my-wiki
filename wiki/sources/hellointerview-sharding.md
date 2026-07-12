---
title: "Sharding in System Design Interviews"
type: source
tags: [system-design, sharding, database, interview]
created: 2026-07-10
sources: ["https://www.hellointerview.com/learn/system-design/core-concepts/sharding"]
---

# Sharding in System Design Interviews

Source: [[Hello Interview]] core-concepts guide.

## Framing

Consistent with the companion [[API Design for System Design Interviews]] and [[Caching for System Design Interviews]] guides, this article treats sharding as an interview-scoped decision rather than a full reference, and opens with an explicit caution against reaching for it too early: "a well-tuned single database can get you surprisingly far." Its recommended interview sequence: establish a specific bottleneck (storage capacity, write throughput, or read throughput), propose a shard key aligned with actual access patterns, pick a distribution strategy, and name the trade-offs — chiefly expensive cross-shard queries.

Most of the mechanics here (shard key selection, hash/range/directory-based strategies, hot shards, cross-shard query cost) are already documented at equal or greater depth in this wiki, via [[Database Sharding]], [[Shard Key]], [[Hash-Based Sharding]], [[Range-Based Sharding]], [[Directory-Based Sharding]], and [[Cross-Shard Query]] — folded the interview framing and few genuinely new pieces into those pages rather than duplicating them here.

## New Ground: Partitioning vs. Sharding Terminology

The article draws a clean scope distinction this wiki hadn't stated explicitly: **partitioning** splits a table within a single database instance (horizontally by row, or vertically by column); **sharding** extends that across multiple independent machines. Folded into both [[Partitioning]] and [[Database Sharding]].

## New Ground: Cross-Shard Transaction Consistency

The existing [[Cross-Shard Query]] page covers the *read* side of spanning shards (scatter-gather, joins, aggregation). This article's "Consistency Issues" section is a distinct *write*-side problem: a transaction touching multiple shards can't use a normal local database transaction. It names three responses — design to avoid cross-shard transactions, use [[Two-Phase Commit (2PC)|Two-Phase Commit]] (already documented as a general distributed-systems entity, now cross-linked into the sharding context), or implement **sagas**. Sagas weren't previously documented anywhere in this wiki, so [[Saga Pattern]] is a new concept page.

## New Ground: The Celebrity Problem

The article's name for a specific hot-shard case: a single popular entity (not just an unlucky key distribution) overwhelms its shard. Two mitigations not previously captured on [[Shard Key]]'s Hot Shard Problem section: isolating the hot key to its own dedicated shard, and dynamic shard splitting at runtime. Folded in.

## New Ground: Auto-Sharding Systems

The article names Vitess (MySQL sharding middleware) and Citus (PostgreSQL sharding extension) alongside Cassandra, DynamoDB, and MongoDB as systems that automate sharding. Vitess and Citus weren't mentioned anywhere in this wiki before; added as a comparison table on [[Database Sharding]] rather than standalone entity pages, matching the one-line depth the source article gives them.

## Related Pages

- [[Database Sharding]]
- [[Shard Key]]
- [[Hash-Based Sharding]]
- [[Range-Based Sharding]]
- [[Directory-Based Sharding]]
- [[Cross-Shard Query]]
- [[Partitioning]]
- [[Saga Pattern]]
- [[Two-Phase Commit (2PC)]]
- [[API Design for System Design Interviews]]
- [[Caching for System Design Interviews]]
- [[Hello Interview]]
