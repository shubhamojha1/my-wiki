---
title: "Ledger Database"
type: concept
tags: [database, ledger, blockchain, immutable]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Ledger Database

A **ledger database** provides an immutable, append-only record of transactions. Once recorded, a transaction cannot be altered or deleted, creating a verifiable and tamper-evident history.

## Characteristics

- **Immutable**: No updates or deletes, only appends
- **Cryptographic chaining**: Each record linked to previous via hash
- **Verifiable integrity**: Tampering detectable through hash chain
- **Append-only**: History is permanent and auditable
- **Centralized trust**: Unlike blockchain, managed by a single authority

## Use Cases

- **Supply chain**: Track goods movement with transparent history
- **Healthcare**: Immutable patient records and consent forms
- **Financial auditing**: Transaction trails for regulatory compliance
- **Voting systems**: Tamper-evident ballot recording

## Examples

- Amazon QLDB — Fully managed ledger database
- Hyperledger Fabric — Permissioned blockchain framework

## Related

- [[Event Sourcing]] — Similar append-only pattern
- [[CRDT]] — Also handles immutable convergent state
