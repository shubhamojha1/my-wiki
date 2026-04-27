---
title: "MD5"
type: concept
tags: [checksum, hash]
created: 2026-04-28
sources: ["algomaster-checksums"]
---

# MD5

**MD5** is a cryptographic hash function producing 128-bit output.

## Characteristics

- **Output**: 128 bits (32 hex characters)
- **Deterministic**: Same input → same output

## Status

- **Deprecated for security** (collision attacks known)
- Still used for non-security file verification
- Should not be used for passwords or security decisions

## Related Concepts

- [[Checksums]] — Parent concept
- [[SHA-256]] — Current standard
- [[Cryptographic Hash]] — Category