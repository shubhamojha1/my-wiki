---
title: "ACID Transactions"
type: concept
tags: [database, transactions, consistency, isolation]
created: 2026-05-08
sources: ["https://algomaster.io/learn/system-design/acid-transactions"]
---

# ACID Transactions

**Definition:** A set of four properties — Atomicity, Consistency, Isolation, Durability — that guarantee reliable processing of database transactions. A transaction is a sequence of operations treated as a single unit: either all succeed (commit) or all fail (rollback).

## 1. Atomicity

A transaction executes as an indivisible unit of work: it either fully commits or fully rolls back. If any operation within the transaction fails, the entire transaction is rolled back and the database restores to its pre-transaction state.

### How Databases Implement Atomicity

**Transaction Logs (Write-Ahead Log):** Before applying changes to data files, the database writes the change description to a durable log. If a crash occurs mid-transaction, the log is used on recovery to discard incomplete changes.

**Commit/Rollback Protocols:**
```sql
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- or ROLLBACK if anything fails
```

## 2. Consistency

A transaction brings the database from one valid state to another valid state, never leaving it in an invalid state. All data integrity constraints must be satisfied before and after the transaction:

- **Primary key constraints** — no duplicate IDs
- **Foreign key constraints** — related records must exist in parent tables
- **Check constraints** — business rules (e.g., age cannot be negative)
- **Unique constraints** — no duplicate values in specified columns

If a transaction violates any constraint, it is rolled back.

## 3. Isolation

Concurrently running transactions must not interfere with each other's intermediate states. Each transaction should appear to run sequentially, one at a time — even when multiple transactions execute simultaneously.

### Concurrency Anomalies

| Anomaly | Description |
|---------|-------------|
| **Dirty Read** | Reading uncommitted data from another transaction that may later be rolled back |
| **Non-Repeatable Read** | Same row read twice yields different values because another transaction modified and committed it in between |
| **Phantom Read** | Same query run twice returns different rows because another transaction inserted/deleted rows that match the filter |

### Isolation Levels

| Level | Dirty Reads | Non-Repeatable Reads | Phantom Reads | Performance |
|-------|-------------|---------------------|---------------|-------------|
| Read Uncommitted | Possible | Possible | Possible | Fastest |
| Read Committed | Prevented | Possible | Possible | Fast |
| Repeatable Read | Prevented | Prevented | Possible | Moderate |
| Serializable | Prevented | Prevented | Prevented | Slowest |

Higher isolation levels provide stronger data consistency but reduce concurrency and performance.

### How Databases Enforce Isolation

**Locking:** Transactions acquire locks on rows, pages, or tables to prevent conflicting access. Can use shared locks (readers) and exclusive locks (writers).

**MVCC (Multi-Version Concurrency Control):** Each transaction sees a snapshot of the database as of its start time. Readers do not block writers and vice versa. Old row versions are maintained in undo logs until no transaction needs them.

**Snapshot Isolation:** A specific form of MVCC where each transaction reads from a snapshot of committed data at the time the transaction started. Writes are validated for conflicts at commit time.

## 4. Durability

Once a transaction is committed, the changes it made persist permanently — surviving power failures, crashes, or other system failures.

### How Databases Ensure Durability

**Write-Ahead Logging (WAL):** Before changes are written to the main data files, they are first appended to a durable log file. On recovery, the WAL is replayed to restore any committed changes that hadn't yet been flushed to data files.

**Replication:**
- **Synchronous replication** — transaction is committed only when confirmed by primary and at least one replica
- **Asynchronous replication** — changes propagate to replicas after commit; small window for data loss on primary failure

**Backups:** Periodic full or incremental backups provide additional durability guarantees.

## Summary

| Property | What It Guarantees | Key Mechanism |
|----------|-------------------|---------------|
| Atomicity | All-or-nothing execution | WAL + commit/rollback |
| Consistency | Valid state transitions | Integrity constraints |
| Isolation | No interference between concurrent transactions | Locking, MVCC, snapshot isolation |
| Durability | Committed data survives failures | WAL, replication, backups |

## Related Pages

- [[Relational Database]], [[CAP Theorem]], [[Distributed Transactions]], [[Eventual Consistency]]
