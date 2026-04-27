---
title: "Checksums"
type: source
tags: [system-design, networking, checksums]
created: 2026-04-28
sources: ["algomaster-checksums"]
---

# Checksums

A **checksum** is a small block of data derived from digital data to detect errors. Acts as a "fingerprint" - if data changes, checksum changes.

## How It Works

1. Take variable-length input
2. Process through algorithm
3. Produce fixed-length output
4. Verify by comparing sender and receiver values

## Common Algorithms

| Algorithm | Type | Output | Use Case |
|-----------|------|-------|---------|
| CRC32 | Non-crypto | 32 bits | Network packets, storage |
| Adler-32 | Non-crypto | 32 bits | Fast compression |
| MD5 | Crypto | 128 bits | Legacy file verification |
| SHA-256 | Crypto | 256 bits | File integrity (current) |
| SHA-512 | Crypto | 512 bits | High-security |

## Non-crypto vs Crypto

- **CRC**: Catches accidental errors (channel noise, physical damage)
- **MD5/SHA**: Defends against intentional tampering

## Use Cases

- File downloads verification
- Network packet integrity
- Disk I/O error detection
- Database replication
- Firmware updates

## Related Concepts

- [[CRC]] — Cyclic Redundancy Check
- [[MD5]] — Legacy hash (deprecated for security)
- [[SHA-256]] — Current standard
- [[Cryptographic Hash]] — One-way function

## Source

- AlgoMaster.io: [Checksums](https://algomaster.io/learn/system-design/checksums) (October 2025)