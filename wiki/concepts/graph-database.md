---
title: "Graph Database"
type: concept
tags: [database, nosql, graph]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-15-db-types]
---

# Graph Database

A **graph database** stores and queries data as a network of **nodes** (entities) connected by **edges** (relationships), with optional properties on both. The core optimization is **index-free adjacency**: each node directly references its neighboring nodes, so traversing a relationship is O(1) regardless of total graph size — unlike relational JOIN, which is O(n log n).

## Data Model

```
(Alice: User {age: 30})
      │
  [FOLLOWS]
      │
 (Bob: User {age: 25})
      │
  [PURCHASED]
      │
(Laptop: Product {price: 999})
```

| Element | Description |
|---------|-------------|
| **Node** | An entity (person, product, location). Has a label and properties. |
| **Edge** | A directed relationship between two nodes. Has a type and optional properties. |
| **Property** | Key-value attributes on nodes or edges (name, since, weight) |
| **Label/Type** | Categorizes nodes (`:User`, `:Product`) and edges (`[:FOLLOWS]`) |

## Query Language

**Cypher** (Neo4j, openCypher standard):
```cypher
-- Find friends of friends of Alice
MATCH (alice:User {name: 'Alice'})-[:FOLLOWS*2]->(fof)
RETURN fof.name

-- Fraud: accounts sharing device AND IP
MATCH (a:Account)-[:USED]->(d:Device)<-[:USED]-(b:Account),
      (a)-[:FROM]->(ip:IP)<-[:FROM]-(b)
WHERE a <> b
RETURN a, b
```

## Why Graph DBs Beat Relational for Traversals

Modeling a social network in SQL requires self-joins:
```sql
-- 3-hop friends in SQL: expensive recursive JOIN
SELECT u3.name FROM users u1
JOIN follows f1 ON u1.id = f1.follower_id
JOIN follows f2 ON f1.followee_id = f2.follower_id
JOIN users u3 ON f2.followee_id = u3.id
WHERE u1.name = 'Alice';
```

With 1M users, each JOIN scans the entire `follows` table. In a graph DB, the same traversal follows pointers in microseconds.

## Use Cases

| Use Case | Why Graph Fits |
|----------|---------------|
| Social networks | Friendship/follow relationships; recommendations |
| Fraud detection | Suspicious shared attributes (device, IP, address) across accounts |
| Knowledge graphs | Entity resolution, semantic search (Google Knowledge Graph) |
| Recommendation engines | "Customers who bought X also liked Y" collaborative filtering |
| Network topology | IT infrastructure dependency mapping |
| Supply chain | Multi-hop traceability |

## Popular Graph Databases

| Database | Notes |
|----------|-------|
| **Neo4j** | Native graph; Cypher; property graph model; most mature |
| **Amazon Neptune** | Managed; supports Gremlin (property graph) + SPARQL (RDF) |
| **TigerGraph** | GSQL; scales to billions of nodes; analytics focus |
| **Memgraph** | In-memory; compatible with Cypher/Neo4j clients |

## Graph DB vs Relational vs Document

| Aspect | Graph DB | Relational | Document |
|--------|----------|-----------|---------|
| Relationship traversal | O(1) per hop | O(n log n) JOIN | Hard (no joins) |
| Schema | Flexible | Rigid | Flexible |
| Query for connected data | Natural | Complex multi-joins | Manual denorm |
| Aggregations | Limited | Excellent | Moderate |

## Interview Caution

Graph databases are the most common over-selection mistake in system design interviews — they sound sophisticated but add operational complexity that's rarely justified by the scoped problem. Even Facebook models its social graph in MySQL, and LinkedIn/Twitter use SQL for their core relationship data, despite both looking like the canonical "social network → graph DB" case. If a relational model handles the world's largest social graph, it likely handles the interview's version too. See [[Data Modeling]] for the broader database-selection framework this fits into.

## Related Concepts

- [[Relational Model]] — alternative; joins become expensive for multi-hop traversals
- [[Document Database]] — better for hierarchical/self-contained data
- [[Graph Neural Network]] — ML on graph-structured data
- [[Data Modeling]] — interview framework for when (and when not) to reach for a specialized database type
