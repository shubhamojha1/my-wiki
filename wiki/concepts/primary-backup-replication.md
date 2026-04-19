---
title: "Primary-Backup Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Primary-backup (also: master-slave, log shipping) replicates all updates through a single primary node.

## Variants

### Asynchronous
- Primary logs operations
- Ships logs to backups
- Common: MySQL replication

### Synchronous  
- Two messages (update + ACK)
- Better durability

## Characteristics
- Single, static master
- Slaves not involved in execution
- No bounds on replication lag

## Problems
- Only best-effort guarantees
- Susceptible to lost updates on inopportune failures
- Split-brain during network partitions
- Manual/ad-hoc failover only

## Usage
- MySQL
- MongoDB
- PostgreSQL (streaming replication)