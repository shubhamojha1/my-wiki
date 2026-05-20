---
title: "Frame (Buffer Pool)"
type: concept
tags: [database, storage, buffer-pool]
created: 2026-04-23
updated: 2026-05-20
---

# Frame (Buffer Pool)

A **frame** is a fixed-size memory slot inside the [[Buffer Pool]]. The buffer pool is simply an array of frames; each frame can hold exactly one [[Database Page]] at a time.

## Frame Metadata

Each frame carries a small control block alongside the page data:

| Field | Purpose |
|-------|---------|
| `page_id` | Which disk page is currently loaded (-1 = empty) |
| `pin_count` | How many threads are actively using this frame |
| `dirty` | Whether the frame has been modified since it was loaded |
| `ref_bit` | Used by Clock/LRU-approx replacement policies |

## Page Fetch Lifecycle

```
DBMS needs page P
  ├─ Page table lookup: P already in frame F?  → return pointer to F
  └─ Cache miss:
       ├─ Find free frame (pin_count=0, any replacement policy)
       ├─ If dirty: flush frame's current page to disk
       ├─ Read page P from disk into the frame
       ├─ Update page table: P → frame F
       └─ Return pointer to F
```

## Pin / Unpin

- **Pin** (increment `pin_count`): called before a thread uses a frame; prevents eviction.
- **Unpin** (decrement `pin_count`): called when done; when count reaches 0 the frame is eligible for replacement.

A frame with `pin_count > 0` is **never** a candidate for eviction — the page is being actively read or written.

## Dirty Frames

When a transaction modifies data in a frame it sets the dirty bit. Before the frame can be reused, the page must be **flushed** (written) to disk to ensure durability. The WAL protocol requires the log record to reach disk before the dirty page does (**write-ahead logging**).

## Related Concepts

- [[Buffer Pool]] — manages the array of frames and the replacement policy
- [[Database Page]] — the unit of data stored in a frame
- [[Page Table]] — the hash map from page_id → frame index
- [[LRU]] — common frame replacement policy
- [[Dirty Page]] — a frame whose page has been modified but not yet written to disk
