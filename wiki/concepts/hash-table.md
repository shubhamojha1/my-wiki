---
title: "Hash Table"
type: concept
tags: [database, data-structure, index]
created: 2026-04-23
---

# Hash Table

A **hash table** is a data structure that implements an associative array, mapping keys to values using a hash function.

## Basics

- **Hash function**: `h(key) → index` in array
- **Collision handling**: What to do when `h(k1) = h(k2)`
- **O(1) average-case lookup/insert/delete**

## In Databases

Used extensively for:
- **Buffer pool page table**: page_id → frame
- **Table catalog**: table name → metadata
- **Hash indexes**: key → tuple pointer
- **Hash joins**: join predicate matching

## Related Concepts

- [[Hash Function]] — Computing index from key
- [[Linear Probe Hashing]] — Collision resolution via probing
- [[Chained Hashing]] — Collision resolution via linked lists
- [[Extendible Hashing]] — Dynamic resizing
- [[Collision]] — When keys hash to same index