---
title: "Chained Hashing"
type: concept
tags: [database, data-structure, hash]
created: 2026-04-23
---

# Chained Hashing

**Chained hashing** is a hash table implementation where each slot contains a linked list (bucket) of entries that hash to that slot.

## How It Works

- Array slots point to first element in linked list
- Collision: add new entry to bucket's list
- Lookup: hash to bucket, traverse list

## Characteristics

- **Simple**: Easy to implement
- **Pointer overhead**: Each entry needs next pointer
- **Unbounded buckets**: Can grow indefinitely
- **No clustering**: Unlike linear probe

## Database Use

- Often used in buffer pool management
- Simple to make thread-safe with latches

## Trade-offs

- **Pros**: Simple, no rehashing needed, handles variable data
- **Cons**: Pointer chasing is cache-unfriendly, pointer overhead

## Related

- [[Hash Table]] — The data structure
- [[Linear Probe Hashing]] — Alternative static scheme
- [[Extendible Hashing]] — Dynamic version