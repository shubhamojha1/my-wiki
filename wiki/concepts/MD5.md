---
title: "MD5"
type: concept
tags: [checksum, hash, cryptography, security]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-checksums"]
---

# MD5

**MD5** (Message-Digest Algorithm 5) is a widely used hash function that produces a 128-bit (16-byte) hash value, typically expressed as a 32-character hex string. Designed by Ron Rivest in 1991.

## Characteristics

- **Output**: 128 bits (32 hex characters), e.g., `d41d8cd98f00b204e9800998ecf8427e`
- **Speed**: Very fast — designed for performance, not security
- **Deterministic**: Same input always produces the same output

## Security Status: Broken

MD5 is **cryptographically broken** and should not be used for any security purpose:

- **Collision attacks** — two different inputs that produce the same MD5 hash can be found in seconds on modern hardware
- **Preimage attacks** — weaknesses exist that ease finding inputs matching a given hash
- **Password hashing** — completely unsuitable; use bcrypt, Argon2, or scrypt instead

## Acceptable Use Cases

MD5 remains useful for **non-security** purposes where collision resistance is not needed:

- **Checksums for accidental corruption** — verifying a downloaded file arrived intact (not tampered, just corrupted)
- **Cache keys** — generating unique keys for caching layers
- **Deduplication** — identifying duplicate files where adversarial collision is not a concern
- **Legacy systems** — interoperability with older protocols

## Algorithm Comparison

| Algorithm | Output | Secure? | Speed |
|-----------|--------|---------|-------|
| MD5 | 128 bits | No (broken) | Fastest |
| SHA-1 | 160 bits | No (deprecated) | Fast |
| [[SHA-256]] | 256 bits | Yes | Moderate |
| SHA-3 | Variable | Yes | Moderate |

## Related Concepts

- [[Checksums]] — parent concept
- [[SHA-256]] — current security standard
- [[Cryptographic Hash]] — the category MD5 belongs to (but fails at)
