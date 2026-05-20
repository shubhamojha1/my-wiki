---
title: "Ledger Database"
type: concept
tags: [database, ledger, blockchain, immutable]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-15-db-types]
---

# Ledger Database

A **ledger database** is an append-only database where each record is cryptographically chained to the previous one — forming a tamper-evident history. Unlike blockchain, a ledger DB is managed by a **single trusted authority**; it provides auditability, not decentralization.

## How Cryptographic Chaining Works

```
Record 1: { txn_id: 1, amount: +500, hash: H(data_1) }
Record 2: { txn_id: 2, amount: -100, hash: H(data_2 ‖ prev_hash_1) }
Record 3: { txn_id: 3, amount: +200, hash: H(data_3 ‖ prev_hash_2) }
```

Changing record 2 changes its hash, which invalidates record 3's hash, and so on — any tampering cascades and is detectable. The chain is also periodically anchored to a journal (like a Merkle tree digest) stored separately.

## Characteristics

| Property | Description |
|----------|-------------|
| **Immutable** | Records are append-only; no UPDATE or DELETE |
| **Tamper-evident** | Altering any record breaks the hash chain |
| **Verifiable** | Any auditor can recompute hashes and detect inconsistency |
| **Centralized** | Single authority; no consensus protocol needed |
| **Queryable** | Unlike blockchain, typically supports SQL or key-value queries |

## Ledger DB vs Traditional DB vs Blockchain

| Feature | Traditional DB | Ledger DB | Blockchain |
|---------|---------------|-----------|-----------|
| Mutability | Full CRUD | Append-only | Append-only |
| Trust model | Operator | Operator + cryptographic proof | Decentralized consensus |
| Throughput | High | High | Low |
| Auditability | Manual audit logs | Built-in, cryptographic | Built-in, cryptographic |
| Decentralized | No | No | Yes |

## Use Cases

| Use Case | Why Ledger Fits |
|----------|----------------|
| Financial auditing | Regulators need immutable transaction history |
| Supply chain tracking | Provenance of goods; tampering immediately visible |
| Healthcare records | Consent forms, prescription changes cannot be altered retroactively |
| Legal documents | Contracts, ownership records with verifiable timestamp |
| Voting systems | Ballot chain verifiable by independent auditors |

## Examples

| System | Notes |
|--------|-------|
| **Amazon QLDB** | Managed ledger with SQL-like queries (PartiQL); SHA-256 hash chain; journal-based |
| **Hyperledger Fabric** | Permissioned blockchain framework; multi-party ledger |
| **Immudb** | Open-source immutable database with cryptographic verification |

## Related Concepts

- [[Event Sourcing]] — similar append-only pattern but for reconstructing state, not auditability
- [[Merkle Tree]] — data structure used to anchor ledger digests
- [[Cryptographic Hash]] — the building block of tamper detection
- [[Write-Ahead Logging]] — append-only log but not tamper-evident
