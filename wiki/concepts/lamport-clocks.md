---
title: "Lamport Clocks"
type: concept
tags: [distributed-systems, time, causality, logical-clocks]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Lamport Clocks

**Lamport clocks** are a logical clock mechanism introduced by Leslie Lamport (1978) for ordering events in distributed systems without relying on synchronized physical clocks. They capture the **happened-before** relationship between events.

## Happened-Before Relation (→)

Lamport defined `a → b` ("a happened before b") if:
- `a` and `b` are events in the same process and `a` comes first, or
- `a` is a send event and `b` is the corresponding receive event, or
- There exists `c` such that `a → c` and `c → b` (transitivity)

Events with no happened-before relationship between them are **concurrent**.

## Algorithm

Each process maintains an integer counter `C`:

1. **Local event**: `C = C + 1` before the event
2. **Send message**: attach current `C` to the message
3. **Receive message** with timestamp `T`: `C = max(C, T) + 1`

## Properties

- **Consistent with causality**: if `a → b` then `C(a) < C(b)`
- **Partial order only**: `C(a) < C(b)` does not imply `a → b`; they may simply be concurrent events from unrelated processes
- Cannot distinguish "a caused b" from "a and b happened independently but a had a lower counter"

## Limitation

Lamport clocks cannot detect concurrency. If `C(a) < C(b)`, you cannot tell whether:
- `a` happened before `b` (causally related), or
- `a` and `b` are concurrent (happened independently)

This is the key weakness that [[Vector Clocks]] address.

## Example

```
Process 1:  C=1(send)  →  C=3(recv)
                              ↑
Process 2:       C=2(send)
```

P2 sends at C=2. P1 receives and sets C=max(1,2)+1=3. Now we know the send happened before the receive.

## Use Case

Lamport clocks are the foundation for:
- [[Vector Clocks]] — per-process counters that detect concurrency
- Distributed debugging and logging (ordering events across nodes)
- Some database systems for ordering transactions

## Related Concepts

- [[Vector Clocks]] — extension that distinguishes causality from concurrency
- [[Partial Order]] — the ordering Lamport clocks provide
- [[Total Order]] — what Lamport clocks cannot fully provide across all processes
- [[Causal Consistency]] — consistency model built on happened-before
