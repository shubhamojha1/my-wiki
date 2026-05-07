---
title: "ACID Transactions"
type: source
tags: [database, transactions, acid, system-design]
created: 2026-05-08
sources: ["https://algomaster.io/learn/system-design/acid-transactions"]
---

# ACID Transactions

**Source:** AlgoMaster.io by Ashish Pratap Singh (Updated Oct 2025)

Covers the four ACID properties — Atomicity, Consistency, Isolation, Durability — including how databases implement them and the tradeoffs between isolation levels.

## Content Summary

- **Transaction definition:** A sequence of operations treated as a single unit; fully succeeds or fully fails.
- **Atomicity:** All-or-nothing execution via transaction logs (WAL) and commit/rollback protocols.
- **Consistency:** Valid state → valid state; integrity constraints (primary keys, foreign keys, check constraints) enforced before/after transaction.
- **Isolation:** Concurrent transactions must not interfere; enforced via locking, MVCC, snapshot isolation.
- **Isolation Levels:** Read Uncommitted → Read Committed → Repeatable Read → Serializable; trade correctness for performance.
- **Concurrency Anomalies:** Dirty reads, non-repeatable reads, phantom reads.
- **Durability:** Committed data survives crashes via WAL, replication (sync/async), and backups.

## Related Pages

- [[ACID Transactions]], [[Relational Database]]
