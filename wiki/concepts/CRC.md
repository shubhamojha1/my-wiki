---
title: "CRC"
type: concept
tags: [checksum, networking]
created: 2026-04-28
sources: ["algomaster-checksums"]
---

# CRC

**CRC** (Cyclic Redundancy Check) is a non-cryptographic checksum using polynomial division.

## Characteristics

- **Output**: 32 bits (CRC32)
- **Fast**: Efficient to compute
- **Burst error detection**: Excellent at detecting consecutive bit errors

## Use Cases

- Network packets (Ethernet, ZIP)
- Storage media
- Data integrity (non-security)

## Limitation

- Not secure against intentional tampering
- Only catches accidental corruption

## Related Concepts

- [[Checksums]] — Parent concept
- [[Cryptographic Hash]] — Secure alternative