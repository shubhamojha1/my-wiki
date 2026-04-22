---
title: "Frame (Buffer Pool)"
type: concept
tags: [database, storage, buffer-pool]
created: 2026-04-23
---

# Frame (Buffer Pool)

A **frame** is a fixed-size slot in the [[Buffer Pool]] memory region. Each frame can hold one database page.

## Characteristics

- **Fixed size**: Same size as a [[Database Page]] (typically 4KB-16KB)
- **Array organization**: Buffer pool is an array of frames
- **Reusable**: The same frame can hold different pages over time

## Usage

When the DBMS needs to fetch a page from disk:
1. Find a free frame (or evict one using replacement policy)
2. Read the disk page into the frame
3. Return pointer to requesting component

## Related

- [[Buffer Pool]] — Array of frames
- [[Database Page]] — Data stored in frames
- [[Page Table]] — Maps pages to frames