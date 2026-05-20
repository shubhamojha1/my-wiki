---
title: "Clock Replacement"
type: concept
tags: [database, storage, cache, eviction]
created: 2026-04-23
updated: 2026-05-20
---

# Clock Replacement (CLOCK)

**CLOCK** is a buffer pool page replacement algorithm that approximates [[LRU]] using a single reference bit and a circular scan, achieving O(1) per operation without maintaining timestamps or sorted lists.

## Data Structure

A circular array of frames, each with:
- `page_id` — which disk page is loaded
- `pin_count` — threads currently using the frame
- `ref_bit` — set to 1 on any access; cleared by the clock hand

```
Frames:   [ F0 ]  [ F1 ]  [ F2 ]  [ F3 ]  [ F4 ]
ref_bit:     1       0       1       1       0
                           ↑
                       clock hand
```

## Algorithm

**On page access**: set `ref_bit = 1` for the frame.

**On eviction needed** (find a victim):
```
while true:
    frame = frames[clock_hand]
    if frame.pin_count > 0:
        clock_hand++          # skip pinned frames
    elif frame.ref_bit == 1:
        frame.ref_bit = 0     # give a second chance
        clock_hand++
    else:
        evict frame           # ref_bit == 0 → victim found
        return frame
```

The clock hand advances around the circle, giving each frame a "second chance" before eviction. Pages that were recently used (ref_bit=1) survive the first pass.

## Worked Example

```
Frame:  F0(ref=1)  F1(ref=0)  F2(ref=1)  F3(ref=0)
Hand starts at F0:
  F0: ref=1 → clear ref, advance
  F1: ref=0 → EVICT F1
```

## CLOCK vs LRU

| Aspect | CLOCK | LRU |
|--------|-------|-----|
| Complexity | O(1) amortized | O(1) with doubly-linked list + hashmap |
| Accuracy | Approximate (second-chance) | Exact |
| Timestamp maintenance | None needed | Update on every access |
| Memory overhead | One bit per frame | Pointers + order info |
| Sequential scan | Vulnerable | Also vulnerable (LRU-K needed) |

## CLOCK-Pro / LRU-K

For sequential scan workloads (full table scans pollute the buffer pool), CLOCK is extended to **CLOCK-Pro** or **LRU-K** which tracks K accesses per page, evicting pages with low access frequency rather than just recency.

PostgreSQL uses a **clock sweep** algorithm (clock + a usage count per frame). InnoDB uses LRU-based with a young/old sub-list to resist sequential scan pollution.

## Related Concepts

- [[LRU]] — the policy CLOCK approximates
- [[Buffer Pool]] — the structure CLOCK manages
- [[Frame (Buffer Pool)]] — the circular array CLOCK scans
- [[Dirty Page]] — frames with dirty=true must be flushed before eviction
