---
title: "Foreign Key"
type: concept
tags: [database, relational, integrity]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Foreign Key

A constraint that establishes a relationship between two tables by referencing the primary key of another table.

## Purpose

- Enforces **referential integrity**: ensures referenced rows exist
- Creates relationships between tables (parent-child)
- Enables JOIN operations between related data

## Example

```sql
CREATE TABLE Artists (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Albums (
    id INT PRIMARY KEY,
    title VARCHAR(200),
    artist_id INT REFERENCES Artists(id)
);
```

## Behavior

- **CASCADE**: Delete/update parent affects child rows
- **SET NULL**: Child foreign key set to NULL
- **RESTRICT**: Prevent delete/update of parent
- **NO ACTION**: Check after other operations

## Related

- [[Primary Key]]
- [[Relational Model]]
- [[Relational Algebra]]