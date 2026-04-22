---
title: "Page Table"
type: concept
tags: [database, storage, buffer-pool, metadata]
created: 2026-04-23
---

# Page Table

The **page table** is a hash table data structure that tracks which database pages are currently in the [[Buffer Pool]].

## Information Tracked

- **Page ID to frame mapping**: Which frame holds which page
- **Pin count**: Number of threads currently using the page
- **Dirty flag**: Whether the page has been modified
- **Reference bit**: Used by CLOCK replacement policy

## Thread Safety

- Protected with **latches** (lightweight locks) for concurrent access
- Must support multiple readers/writers without blocking too long

## Operations

- **Lookup**: Find if a page is in memory
- **Pin/Unpin**: Increment/decrement usage count
- **Mark dirty**: Flag modified pages for later write-back

## Related

- [[Buffer Pool]] — Memory area the page table tracks
- [[Frame (Buffer Pool)]] — Individual slot in buffer pool
- [[Database Page]] — Unit of data being tracked
- [[Latch]] — Lock for thread-safe metadata access