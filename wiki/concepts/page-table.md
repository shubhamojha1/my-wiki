---
title: "Page Table"
type: concept
tags: [database, storage, buffer-pool, metadata]
created: 2026-04-23
updated: 2026-05-20
---

# Page Table (Buffer Pool)

The **page table** is the in-memory hash map that tracks which disk pages are currently loaded in the [[Buffer Pool]] and in which frame. It is the index into the buffer pool.

> **Note**: Do not confuse with the OS virtual memory page table (maps virtual → physical memory addresses). The DBMS page table maps *disk page IDs* → *buffer pool frame indices*.

## Data Structure

```
page_id  →  frame entry
──────────────────────────────────────
page_id  │ frame_idx │ pin_count │ dirty │ ref_bit
─────────┼───────────┼───────────┼───────┼────────
   42    │     7     │     2     │  true │   1
   99    │     3     │     0     │ false │   0
  201    │    15     │     1     │  true │   1
```

Typically implemented as an open-addressing or chained hash table keyed by `page_id`.

## Fields per Entry

| Field | Type | Purpose |
|-------|------|---------|
| `frame_idx` | int | Index into the buffer pool array where the page lives |
| `pin_count` | int | Number of threads currently holding a reference; 0 = evictable |
| `dirty` | bool | Modified since last flush — must be written to disk before eviction |
| `ref_bit` | bool | Set on access; used by the Clock/LRU-K replacement policy |

## Operations

**Lookup** (page fetch path):
```
1. Hash page_id → bucket
2. If found: increment pin_count, return frame pointer
3. If not found: cache miss → evict a frame, load page, insert entry
```

**Unpin** (caller done with page):
```
1. Hash page_id → entry
2. Decrement pin_count
3. If caller modified data: set dirty = true
```

**Eviction** (replacement policy picks victim):
```
1. Find frame with pin_count = 0 (not in use)
2. If dirty: flush frame's page to disk (WAL first)
3. Remove old page_id entry from page table
4. Load new page into the freed frame
5. Insert new page_id entry
```

## Thread Safety

The page table is shared across all threads. It is protected by a **latch** (lightweight mutex, typically per-bucket for fine-grained concurrency) rather than a single global lock, to allow parallel lookups.

## Related Concepts

- [[Buffer Pool]] — the array of frames the page table indexes
- [[Frame (Buffer Pool)]] — the in-memory slot for one page
- [[Database Page]] — the unit mapped by the page table
- [[Latch]] — the synchronization primitive protecting the page table
- [[LRU]] — replacement policy that uses the page table's ref/pin fields
- [[Dirty Page]] — a page table entry with dirty=true
