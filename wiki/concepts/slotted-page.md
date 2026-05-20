---
title: "Slotted Page"
type: concept
tags: [database, storage, page, tuple]
created: 2026-04-23
updated: 2026-05-20
---

# Slotted Page

A **slotted page** is the standard page organization scheme used in disk-based databases. Tuples grow inward from the start of the page while a **slot array** grows inward from the end, meeting in the middle at the free-space boundary.

## Layout

```
┌─────────────────────────────────────────────────────┐
│ Header │ Tuple 1 │ Tuple 2 │ ... │  free  │ ... │S2│S1│
│        │──────────────────→│        │←────────────│  │
│        │           (tuples grow →)  (← slots grow)│  │
└─────────────────────────────────────────────────────┘
```

| Region | Contents |
|--------|----------|
| **Header** | Page ID, checksum, number of slots, free-space pointer |
| **Tuple area** | Variable-length rows packed from the left |
| **Free space** | Gap between tuples and slot array |
| **Slot array** | Fixed-size entries at the right; each holds `(offset, length)` for its tuple |

A **slot entry** (typically 4–8 bytes) holds the byte offset of the tuple within the page and its length. The slot number is the stable external identifier — it never changes even if the tuple is moved.

## Key Properties

- **Variable-length tuples**: Slot lengths differ, so strings, NULLs, and BLOBs all fit naturally.
- **Stable tuple IDs**: External references (e.g., secondary indexes) store `(page_id, slot_number)`. Moving a tuple during defragmentation only updates the slot array entry, not every external pointer.
- **Defragmentation**: After deletes leave holes, tuples can be compacted toward the start. The slot array is updated in place; callers see no change.
- **Space check**: Before insert, check `free_space = free_space_pointer - (num_slots × slot_size)`.

## Deletion

Deleting a tuple marks its slot as invalid (offset = -1 or a sentinel). The space is recovered only during compaction; marking is O(1).

## Related Concepts

- [[Database Page]] — the fixed-size unit containing the slotted layout
- [[Tuple]] — the row data stored in each slot
- [[Heap File]] — unordered collection of slotted pages
- [[Buffer Pool]] — caches pages in memory before writes reach disk
- [[Frame (Buffer Pool)]] — the in-memory slot that holds one page
