---
title: "Slotted Page"
type: concept
tags: [database, storage, page, tuple]
created: 2026-04-23
---

# Slotted Page

A **slotted page** is a page organization scheme where tuples are stored from the beginning of the page, and a **slot array** at the end tracks their locations.

## Structure

- **Header**: Page metadata, number of slots, free space pointer
- **Slot Array**: Array at end of page mapping slot number → tuple offset
- **Tuples**: Stored sequentially from the beginning (growing inward)

## Benefits

- **Variable-length tuples**: Can store strings, blobs of different sizes
- **Tuple movement**: Can defragment by moving tuples without updating external pointers
- **Efficient space usage**: Free space in middle can be reused

## Related

- [[Database Page]] — The container
- [[Tuple]] — Row data stored in slots
- [[Heap File]] — Uses slotted pages