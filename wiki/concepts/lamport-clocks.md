---
title: "Lamport Clocks"
type: concept
tags: [distributed-systems, time, causality]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Lamport clocks are a logical clock mechanism by Leslie Lamport for ordering events in distributed systems without physical clocks.

## Algorithm
Each process maintains a counter:
1. On doing work: increment counter
2. On sending message: include counter
3. On receiving: counter = max(local, received) + 1

## Properties
- Provides partial order
- If `timestamp(a) < timestamp(b)`: either a happened before b, or they're incomparable (from independent systems)

## Caveat
Only comparable within same causal history. Comparing across systems that never communicate may incorrectly order concurrent events.

## Limitation
Cannot distinguish between "happened before" and "concurrent but unrelated."

## Use Case
Foundation for more powerful [[Vector Clocks]].