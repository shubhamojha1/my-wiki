---
title: "Vector Clocks"
type: concept
tags: [distributed-systems, time, causality]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Vector clocks extend [[Lamport Clocks]] with an array of counters - one per node - enabling accurate causal ordering.

## Structure
`[t1, t2, ..., tN]` - one logical clock per node

## Algorithm
1. On work: increment own entry in vector
2. On send: include full vector
3. On receive: merge (max of each), then increment own entry

## Causal Ordering
With vector clocks `{A:2, B:4, C:1}`:
- Can identify what (potentially) influenced an event
- Two events are concurrent if neither vector dominates the other

## Advantages
- Accurate causality tracking
- [[Dynamo]] uses them for conflict detection

## Limitations
- One entry per node → large for big systems
- Requires garbage collection
- Periodic size reduction techniques needed

## Usage
- Riak
- Voldemort
- Dynamo (original)