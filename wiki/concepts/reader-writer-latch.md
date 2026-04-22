---
title: "Reader-Writer Latch"
type: concept
tags: [database, concurrency, latch]
created: 2026-04-23
---

# Reader-Writer Latch

A **reader-writer latch** allows multiple concurrent readers or a single exclusive writer.

## Modes

- **Read mode**: Multiple threads can hold simultaneously
- **Write mode**: Exclusive access, no other readers/writers

## Implementation Considerations

- **Writer starvation**: Readers may starve writers
- **Reader starvation**: Writers may starve readers
- **Fairness**: Queue-based ensures fairness

## Use Cases

- Protecting B+Tree nodes
- Hash table access
- Any read-heavy data structure

## Related

- [[Latch]] — General concept
- [[Lock]] — Transaction-level lock