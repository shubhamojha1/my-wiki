---
title: "Relational Algebra"
type: concept
tags: [database, algebra, query]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Relational Algebra

Fundamental operations for querying and manipulating data in the relational model. Each operator takes one or more relations as input and outputs a new relation.

## Basic Operators

### Select (σ)
Filters tuples by a predicate.
```
σpredicate(R)
```
Example: `σage > 21(Students)` returns students over 21.

### Projection (π)
Selects specific columns, removing others.
```
πA1,A2,...,An(R)
```
Example: `πname, email(Users)` returns only name and email columns.

### Union (∪)
Combines tuples from two relations.
```
R ∪ S
```
Both relations must have identical schemas.

### Intersection (∩)
Returns tuples in both relations.
```
R ∩ S
```

### Difference (−)
Returns tuples in first relation but not second.
```
R − S
```

### Product (×)
Cartesian product: all possible combinations.
```
R × S
```

### Join (▷◱)
Combines tuples from two relations based on shared attributes.
```
R ▷◱ S
```
Equivalent to product + select + projection.

## Extended Operators

Many DBMSs also support:
- **Rename (ρ)**
- **Division**
- **GroupBy/Aggregation**
- **Natural Join**

## Query Optimization

The critical insight: declarative queries let the DBMS optimize execution order. The query `σb_id=102(R ▷◱ S)` has multiple valid evaluation orders, and the DBMS picks the most efficient based on statistics.

This is why SQL (declarative) outperforms procedural data access.

## Related Concepts

- [[Relational Model]]
- [[SQL]]
- [[Query Optimization]]