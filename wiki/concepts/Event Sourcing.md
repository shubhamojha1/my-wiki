---
title: "Event Sourcing"
type: concept
tags: [architecture, patterns, events]
created: 2026-05-10
sources: ["algomaster-cdc"]
---

# Event Sourcing

**Event sourcing** is a pattern where every change to an application's state is recorded as an immutable, ordered sequence of events, rather than only storing the current state.

## How It Works

Instead of updating a record in place (e.g., changing an account balance), each operation (e.g., "deposit $50", "withdraw $20") is stored as an event. The current state is derived by replaying all events in order.

## Benefits

- **Complete audit trail**: Every state change is permanently recorded
- **Temporal query**: Reconstruct state at any point in history
- **Debugging and forensics**: Trace exactly what happened and when
- **Integration with CDC**: CDC can capture events from a database to build event-sourced systems

## Example

A financial application records every transaction as an event:

```
Deposit($50) → Withdraw($20) → Deposit($30) → Current balance: $60
```

Each event is immutable. To fix an error, a compensating event is appended rather than modifying history.

## Related Concepts

- [[Change Data Capture (CDC)]] — Often used to implement event sourcing
- [[Apache Kafka]] — Commonly used as the event store
- [[Distributed Commit Log]] — Append-only log structure underlying event sourcing
