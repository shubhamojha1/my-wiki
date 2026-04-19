---
title: "FLP Impossibility Result"
type: concept
tags: [distributed-systems, impossibility]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

FLP (Fischer, Lynch, Patterson) impossibility result shows consensus cannot be solved in asynchronous systems with even one faulty process.

## Statement
No deterministic algorithm can solve consensus in an asynchronous system subject to failures, even if:
- Messages are never lost
- At most one process fails
- Failure is only crash (stop executing)

## Proof Idea
- Can remain "bivalent" (undecided) indefinitely
- By delaying message delivery (allowed in async model)
- Algorithm cannot distinguish delay from crash

## Implications
Must give up either:
- **Safety** (never decide incorrectly)
- **Liveness** (eventually decide)

## Practical Meaning
Algorithms must choose between safety and liveness when message delivery bounds don't hold.