---
title: "Critical Sections"
type: concept
tags: [concurrency, synchronization, critical-section]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency]
---

# Critical Sections

A **critical section** is a code segment that accesses shared resources (memory, files, devices) and must not be executed by more than one thread concurrently.

## Definition

From the source: Critical sections are "code sections accessing shared resources" — sections where race conditions can occur.

## Requirements

A correct critical section implementation must satisfy:

1. **Mutual exclusion** — Only one thread executes at a time
2. **Progress** — If no thread is in critical section, one should enter
3. **Bounded waiting** — Thread can't wait indefinitely to enter
4. **No deadlock** — Threads don't permanently block each other

## Implementation Approaches

```python
# Mutex (mutual exclusion lock)
lock = Lock()

def critical_section():
    with lock:  # Only one thread passes here
        access_shared_resource()
```

### Hardware Primitives
- **Test-and-set** — Atomic read-modify-write
- **Compare-and-swap** — Atomic conditional write
- **Load-linked/store-conditional** — LL/SC pattern

### OS Primitives
- **Mutex** — Lock with ownership verification
- **Semaphore** — Counting permit-based access
- **Monitor** — Encapsulated lock + condition variables

## Common Patterns

- **Producer-consumer** — Bounded buffer
- **Readers-writers** — Read-heavy access
- **Dining philosophers** — Resource allocation

## Related

- [[Race Conditions]] — Incorrect behavior in critical sections
- [[Thread Safety]] — Correct access to critical sections
- [[Mutex]] — Common critical section primitive
- [[Semaphores]] — Counting synchronization
- [[Introduction to Concurrency]]