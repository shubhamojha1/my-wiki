---
title: "Cryptographic Hash"
type: concept
tags: [security, hash]
created: 2026-04-28
sources: ["algomaster-checksums"]
---

# Cryptographic Hash

A **cryptographic hash** is a one-way function designed for security.

## Properties

- **Deterministic**: Same input → same output
- **One-way**: Cannot reverse to recover input
- **Collision-resistant**: Hard to find two inputs with same output
- **Avalanche effect**: Small input change → large output change

## Algorithms

- MD5 (128 bits, broken)
- SHA-1 (160 bits, deprecated)
- SHA-256 (256 bits, current)
- SHA-512 (512 bits)

## Use Cases

- File integrity
- Password storage (with salt)
- Digital signatures
- Blockchain

## Related Concepts

- [[Checksums]] — Parent concept
- [[SHA-256]] — Current standard