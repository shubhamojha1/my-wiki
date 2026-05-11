---
title: "Hierarchical Database"
type: concept
tags: [database, legacy, tree]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Hierarchical Database

A **hierarchical database** organizes data into a tree-like structure where each record has a single parent and can have multiple children, forming a one-to-many relationship.

## Characteristics

- **Tree structure**: Parent-child hierarchy
- **Single parent rule**: Each child has exactly one parent
- **Navigational access**: Follow parent/child pointers to find data
- **Rigid schema**: Changing relationships requires restructuring
- **Performance**: Fast access via known paths

## Use Cases

- **Organizational charts**: Employee → department → company
- **File systems**: Directory → subdirectory → file
- **Mainframe applications**: Legacy enterprise systems

## Examples

- IBM IMS — Mainframe hierarchical database
- Windows Registry — Hierarchical key-value store

## Limitations

- Cannot model many-to-many relationships without duplication
- Adding new relationship types may require restructuring entire hierarchy
- Mostly superseded by [[Relational Model]] and [[Graph Database|graph databases]]

## Related

- [[Graph Database]] — More flexible for complex relationships
- [[Relational Model]] — Industry standard replacement
