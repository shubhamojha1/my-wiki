---
title: "Document Database"
type: concept
tags: [database, nosql, document]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Document Database

A NoSQL database that stores data as documents, typically in JSON or BSON format. Documents contain hierarchical field-value pairs.

## Characteristics

- **Schema-less**: Documents in same collection can have different fields
- **Hierarchical**: Supports nested objects and arrays
- **Flexible**: Easy to evolve over time
- **Denormalized**: Embed related data in single document

## Examples

```json
{
  "name": "Wu-Tang Clan",
  "year": 1992,
  "albums": [
    {"title": "Enter the Wu-Tang", "year": 1993},
    {"title": "Wu-Tang Forever", "year": 1997}
  ]
}
```

## Use Cases

- Content management systems
- User profiles and session data
- Catalogs with varying attributes
- Rapid prototyping

## Popular Systems

- **MongoDB**: Most popular document DB
- **CouchDB**: Apache project
- **Firebase**: Google real-time database

## Tradeoffs

- **Pros**: Flexible schema, natural mapping to objects
- **Cons**: Limited joins, potential data duplication, eventual consistency

## Related Concepts

- [[Relational Model]]
- [[NoSQL]]