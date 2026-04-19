---
title: "Asynchronous System Model"
type: concept
tags: [distributed-systems, timing]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Asynchronous system model makes no timing assumptions - processes execute at independent rates, no bound on message delay, no useful clocks.

## Characteristics
- No upper bound on message delay
- Processes execute at independent rates
- Cannot rely on timing/timers

## Real-World Reality
Real systems are at best "partially synchronous":
- May occasionally work correctly
- Provides some bounds sometimes
- Messages delayed indefinitely
- Clocks out of sync

## Implications
- [[FLP Impossibility Result]] applies
- Cannot guarantee consensus termination
- Must choose between safety and liveness