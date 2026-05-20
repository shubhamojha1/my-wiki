---
title: "Tuple"
type: concept
tags: [database, storage, data]
created: 2026-04-23
updated: 2026-05-20
---

# Tuple

A **tuple** (or **row**) is the fundamental unit of storage in a relational database — a sequence of attribute values representing one record. Physically, a tuple is a byte string in a [[Database Page]].

## Physical Layout

```
┌──────────────────────────────────────────────────────────────┐
│  TUPLE HEADER        │  FIXED-LENGTH DATA  │  VAR-LENGTH DATA │
│  txn_id | null_bitmap│  int(4B) | float(8B)│  VARCHAR offset→ │
└──────────────────────────────────────────────────────────────┘
```

### Header Fields

| Field | Size | Purpose |
|-------|------|---------|
| **Transaction ID (xmin/xmax)** | 4–8 B | MVCC visibility — which transaction created/deleted this version |
| **Null bitmap** | ⌈n_cols/8⌉ B | One bit per column; 1 = NULL |
| **Record length** | 2–4 B | Total byte length of the tuple |
| **CTID / heap pointer** | 6 B | PostgreSQL physical location (page_id, slot) for index pointers |

### Data Layout

- **Fixed-length attributes** (INT, BIGINT, FLOAT, DATE): stored in-place, aligned to their natural boundary.
- **Variable-length attributes** (VARCHAR, TEXT, BYTEA): stored inline up to a threshold; beyond that, **TOASTed** out-of-line to a separate overflow table. The tuple stores a pointer and length.
- **NULL values**: no storage consumed for the value; the null bitmap bit is set instead.

## Tuple Identification

Each tuple is identified by a **TID (Tuple ID)** or **RID (Row ID)**: `(page_id, slot_number)`. Indexes store TIDs as row locators; they remain stable as long as the tuple isn't moved.

Heap updates in PostgreSQL create a **new tuple version** in place (or on overflow); the old version is kept for MVCC readers and reclaimed by VACUUM.

## MVCC and Tuple Versions

```
INSERT:  tuple created with xmin=current_txn, xmax=∞
UPDATE:  old tuple: xmax=current_txn; new tuple: xmin=current_txn, xmax=∞
DELETE:  tuple: xmax=current_txn (logically deleted; physically reclaimed by VACUUM)
```

A reader in transaction T sees a tuple iff: `xmin ≤ T.snapshot AND xmax > T.snapshot`.

## Storage Schemes

| Scheme | Description |
|--------|-------------|
| [[Slotted Page]] | Tuples packed into heap pages; slot array at page end |
| [[Index-Organized Table]] | Tuples stored in B+Tree leaf nodes (InnoDB, Oracle IOT) |
| [[Columnar Storage]] | Attributes stored column-by-column; no traditional tuple layout |
| [[Heap File]] | Unordered collection of slotted pages containing tuples |

## Related Concepts

- [[Database Page]] — the physical container holding tuples
- [[Slotted Page]] — the standard page organization for variable-length tuples
- [[Schema]] — defines the attribute types and order within a tuple
- [[MVCC]] — uses per-tuple transaction IDs for snapshot isolation
- [[VACUUM]] — reclaims space from dead (deleted/updated) tuple versions
