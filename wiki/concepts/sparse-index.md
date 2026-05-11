---
title: "Sparse Index"
type: concept
tags: [database, index, structure]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Sparse Index

A **sparse index** has entries only for some of the search key values in the table. It stores pointers to blocks or pages rather than individual rows.

## Characteristics

- **Partial entries**: Only some keys are indexed
- **Block pointers**: Points to the page/block, not the exact row
- **Smaller size**: Fewer entries than dense index
- **Best for**: Tables with many distinct key values where sequential storage is used

## How It Works

1. Search the sparse index for the largest key ≤ the search key
2. Follow the pointer to the data block
3. Scan within the block to find the exact record

## Related

- [[Dense Index]] — Indexes every key
- [[Database Index]] — General concept
