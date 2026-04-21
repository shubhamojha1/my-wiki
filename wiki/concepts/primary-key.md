---
title: "Primary Key"
type: concept
tags: [database, relational, integrity]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Primary Key

A constraint that uniquely identifies each tuple (row) in a relation (table).

## Properties

- **Unique**: No two rows can have the same primary key value
- **Not Null**: Must have a value (enforced by most DBMS)
- **Immutable**: Should not change after creation
- **Single or Composite**: Can be one column or multiple

## Examples

```sql
-- Single column
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Composite key
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)
);
```

## Auto-generation

Most DBMSs support auto-generated primary keys:
- **MySQL**: `AUTO_INCREMENT`
- **PostgreSQL**: `SERIAL` or identity columns
- **SQL Server**: `IDENTITY`

## Related

- [[Foreign Key]] — References primary key in another table
- [[Relational Model]]
- [[Relational Algebra]]