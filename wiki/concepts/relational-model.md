---
title: "Relational Model"
type: concept
tags: [database, relational, theory]
created: 2026-04-22
sources: [cmu_15-445_lec01]
---

# Relational Model

Data model proposed by Ted Codd at IBM in 1969. The foundation of modern relational database management systems (RDBMS).

## Three Components

### Structure
- **Relation**: A set of tuples (table)
- **Attribute**: Column in a relation
- **Tuple**: Row in a relation
- **Domain**: Set of allowed values for an attribute

### Integrity
- **Primary Key**: Uniquely identifies each tuple
- **Foreign Key**: References a tuple in another relation
- **Constraints**: User-defined conditions (NOT NULL, UNIQUE, etc.)

### Manipulation
- **Declarative**: Specify what you want, not how to get it
- [[Relational Algebra]] operations for data retrieval

## Key Properties

- **Unordered**: Relations are sets of tuples; order doesn't matter
- **Atomic Values**: Each cell contains a single value (historically; modern DBs support nested)
- **NULL**: Special value representing undefined/missing data

## Data Independence

The relational model provides isolation between application logic and physical storage. DBMS can change storage layout without breaking applications.

## Related Concepts

- [[Primary Key]]
- [[Foreign Key]]
- [[SQL]]
- [[Relational Algebra]]
- [[Relational Database]]
