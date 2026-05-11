---
title: "AlgoMaster: Indexing"
type: source
tags: [database, index, btree, hashtable, bitmap]
created: 2026-05-11
sources: [algomaster-indexing]
---

# AlgoMaster: Indexing

**Author:** Ashish Pratap Singh
**URL:** https://algomaster.io/learn/system-design/indexing
**Accessed via:** Wayback Machine (Jan 2026 archive)
**Published:** October 3, 2025

## Summary

A comprehensive overview of database indexes covering what they are, how they work, types, underlying data structures, and best practices. Uses a book index analogy to explain the concept.

## Key Concepts Covered

- **Book analogy**: Like a book's index, database indexes provide sorted lookup entries with pointers to data location
- **CREATE INDEX** syntax with MySQL examples (single-column and composite)
- **5-step working**: creation → building → query check → index search → data retrieval
- **Benefits**: faster queries, reduced CPU, rapid retrieval, efficient sorting, data organization
- **Types by structure**: primary, clustered (physical order), non-clustered (virtual pointers)
- **Types by coverage**: dense (every key) vs sparse (some keys)
- **Specialized types**: bitmap (low cardinality), hash (exact match), filtered, covering, function-based, full-text, spatial
- **Data structures**: B-Tree/B+Tree (logarithmic, disk-friendly, ordered), Hash Tables (O(1) exact match), Bitmaps (bitwise ops for analytics)
- **Best practices**: index selective/high-cardinality columns, composite indexes, avoid over-indexing, monitor performance
