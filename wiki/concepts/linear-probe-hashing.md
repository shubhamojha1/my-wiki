---
title: "Linear Probe Hashing"
type: concept
tags: [database, data-structure, hash]
created: 2026-04-23
---

# Linear Probe Hashing

**Linear probe hashing** is a static hash table scheme that resolves collisions by linearly searching for the next free slot.

## How It Works

1. Compute `h(key)` to get initial slot
2. If slot occupied, check next slot (wrapping around)
3. Continue until empty slot found

## Insert

- Hash to position, find first empty slot
- May cause primary clustering (long consecutive sequences)

## Lookup

- Hash to position
- Check each slot until: key found, empty slot (not present), or table full

## Delete

- **Tombstones**: Mark deleted, don't remove (would break probes)
- Periodic rehash to clean up

## Robin Hood Variant

- When inserting, if probe distance is shorter, swap items
- Reduces variance in probe distances

## Trade-offs

- **Pros**: Simple, good cache locality, no pointers
- **Cons**: Primary clustering, vulnerable to poor hash functions

## Related

- [[Hash Table]] — The data structure
- [[Hash Function]] — Computing initial position
- [[Collision]] — Problem being solved