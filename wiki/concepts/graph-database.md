---
title: "Graph Database"
type: concept
tags: [database, nosql, graph]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Graph Database

A **graph database** specializes in storing, managing, and querying complex networks of interconnected data using nodes, edges, and properties.

## Data Model

- **Nodes**: Entities (users, products, places)
- **Edges**: Relationships between entities (follows, purchased, located_in)
- **Properties**: Attributes on nodes and edges (name, since, weight)
- **Traversals**: Navigate relationships efficiently via index-free adjacency

## Use Cases

- **Social networks**: Friend graphs, recommendations, influence analysis
- **Recommendation engines**: "Customers who bought X also bought Y"
- **Knowledge graphs**: Semantic search, entity resolution
- **Fraud detection**: Suspicious connection patterns

## Examples

- Neo4j — Leading native graph database
- Amazon Neptune — Managed graph service (property graph + RDF)

## Related

- [[Document Database]] — Alternative for less connected data
- [[Relational Model]] — Graphs can be modeled with join tables (less efficient)
