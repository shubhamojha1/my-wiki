---
title: "Data Modeling for System Design Interviews"
type: source
tags: [system-design, database, schema-design, interview]
created: 2026-07-10
sources: ["https://www.hellointerview.com/learn/system-design/core-concepts/data-modeling"]
---

# Data Modeling for System Design Interviews

Source: [[Hello Interview]] core-concepts guide.

## Framing

Consistent with the companion API design, caching, and sharding guides in this series, the article scopes data modeling to interview standards: "clear, functional, and aligned with your system's requirements," not a fully normalized schema diagram. It surfaces twice in the interview's delivery framework — core entities during requirements gathering, then a basic schema (fields, relationships, indexing/partitioning notes) during high-level design.

This wiki already has deep reference coverage of every database type and schema-design mechanic the article touches — [[Relational Model]], [[NoSQL]], [[Document Database]], [[Key-Value Store]], [[Wide-Column Store]], [[Graph Database]], [[Primary Key]], [[Foreign Key]], [[Database Index]], [[Data Denormalization]], [[Database Sharding]] all cover their topics in more depth than this article does. What the article adds isn't new mechanics but an interview-specific *methodology* layered on top — captured in the new [[Data Modeling]] page rather than duplicated across the existing reference pages.

## New Ground: The Default-to-SQL Framework

The article's sharpest point: the interview failure mode isn't choosing the wrong database, it's over-selecting an exotic one to look sophisticated. Its concrete corrective — even Facebook models its social graph in MySQL, and LinkedIn/Twitter use SQL for core relationship data — directly counters the temptation the wiki's own [[Graph Database]] page could otherwise encourage by presenting graph traversal as strictly superior for social-network-shaped problems. Folded as an "Interview Caution" section onto [[Graph Database]] and an "Interview Default" section onto [[NoSQL]].

## New Ground: Three-Factor Schema Design Driver

Data volume, access patterns, and consistency requirements — named as the three things every schema technique (keys, normalization, indexing, sharding) ultimately serves. This is a genuinely new organizing framework, not previously stated anywhere in the wiki; it's the core of the new [[Data Modeling]] page.

## New Ground: Dropping Foreign Keys at Scale

Not previously on [[Foreign Key]]: at very large scale, some systems drop FK constraints and enforce referential integrity at the application layer instead, trading a database-level guarantee for write throughput. Folded in as a "Cost at Scale" section.

## New Ground: Interview Checklist

A concrete 6-step sequence for introducing a schema in a high-level design (database type → columns per entity → keys → indexes → denormalization decision → sharding decision). Captured in [[Data Modeling]]'s Interview Checklist section.

## Related Pages

- [[Data Modeling]]
- [[Relational Model]]
- [[NoSQL]]
- [[Graph Database]]
- [[Document Database]]
- [[Key-Value Store]]
- [[Wide-Column Store]]
- [[Foreign Key]]
- [[Primary Key]]
- [[Database Index]]
- [[Data Denormalization]]
- [[Database Sharding]]
- [[API Design for System Design Interviews]]
- [[Caching for System Design Interviews]]
- [[Sharding in System Design Interviews]]
- [[Hello Interview]]
