---
title: "Merkle Tree"
type: concept
tags: [distributed-systems, synchronization, data-structures, hashing]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Merkle Tree

A **Merkle tree** (hash tree) is a tree in which every leaf node contains the hash of a data block, and every non-leaf node contains the cryptographic hash of its children. This structure enables fast, bandwidth-efficient comparison of large datasets across replicas.

## Structure

```
        Root Hash
       /          \
  Hash(L)        Hash(R)
  /     \        /     \
H(A)   H(B)   H(C)   H(D)
 |      |      |      |
Data   Data   Data   Data
 A      B      C      D
```

Each internal node's hash is computed from its children. If any leaf changes, all ancestor hashes change, propagating up to the root.

## Comparison Algorithm

1. Exchange root hashes between two replicas
2. If roots match → data is identical (done in O(1) messages)
3. If roots differ → recurse into child subtrees that differ
4. Continue until mismatched leaf nodes are identified
5. Transfer only the differing data blocks

Divergences are found in **O(log n)** comparisons, not O(n) full scans.

## Advantages

- **Bandwidth-efficient** — only diverging subtrees are inspected; no need to transfer the entire dataset
- **Tamper-detectable** — any change to data changes the root hash
- **Incremental verification** — verify a single leaf without downloading the full tree

## Use Cases

- **[[Dynamo]]** — anti-entropy replica synchronization using Merkle trees to identify diverged key ranges
- **[[Gossip Protocol]]** — anti-entropy passes Merkle tree root hashes to detect out-of-sync nodes
- **Git** — commit objects form a Merkle DAG; comparing SHA hashes identifies changed blobs
- **Blockchain** — transactions are arranged in a Merkle tree; the root (Merkle root) is stored in block headers
- **Certificate Transparency** — append-only log of TLS certificates uses Merkle trees for tamper evidence

## Related Concepts

- [[Gossip Protocol]] — uses Merkle trees for anti-entropy
- [[Dynamo]] — uses Merkle trees for replica repair
- [[Cryptographic Hash]] — the building block of every node
- [[Data Replication]] — Merkle trees make replication efficient
