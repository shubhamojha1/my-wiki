---
title: "Cryptographic Hash"
type: concept
tags: [security, hash]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-checksums"]
---

# Cryptographic Hash

A **cryptographic hash function** maps arbitrary-length input to a fixed-length digest in a way that is designed to be computationally infeasible to reverse, find collisions in, or predict. It differs from a general-purpose hash (e.g., MurmurHash) by prioritizing security properties over throughput.

## Security Properties

| Property | Definition |
|----------|-----------|
| **Deterministic** | Same input always produces the same digest |
| **Pre-image resistance** | Given digest `h`, cannot efficiently find any `x` such that `H(x) = h` |
| **Second pre-image resistance** | Given `x`, cannot efficiently find `x' ≠ x` such that `H(x) = H(x')` |
| **Collision resistance** | Cannot efficiently find any pair `(x, x')` where `H(x) = H(x')` |
| **Avalanche effect** | Flipping one bit in input changes ~50% of the output bits |
| **Non-reversible** | Cannot recover `x` from `H(x)` without brute force |

## Algorithm Comparison

| Algorithm | Digest size | Status | Speed |
|-----------|------------|--------|-------|
| **MD5** | 128 bits | Broken (collisions found) | Fast |
| **SHA-1** | 160 bits | Deprecated (SHAttered collision 2017) | Fast |
| **SHA-256** | 256 bits | Secure | Moderate |
| **SHA-512** | 512 bits | Secure | Faster on 64-bit CPUs |
| **SHA-3 (Keccak)** | 224–512 bits | Secure, different design | Moderate |
| **BLAKE3** | 256+ bits | Secure, very fast | Fastest |

## Use Cases

| Use Case | Why Crypto Hash? | Notes |
|----------|-----------------|-------|
| **File integrity** | Detect tampering (SHA-256 checksums) | Compare hash before/after download |
| **Password storage** | One-way; can't reverse to plaintext | Use bcrypt/Argon2 (slow-by-design) for passwords, not raw SHA |
| **Digital signatures** | Sign the hash, not the full message | RSA/ECDSA signs `H(message)` |
| **HMAC** | Keyed authentication | `H(key ‖ message)` — verifies sender |
| **Merkle trees** | Verify subtrees efficiently | Git, blockchain, TLS certificate transparency |
| **Blockchain / PoW** | Find `nonce` such that `H(block ‖ nonce) < target` | Bitcoin uses SHA-256 twice |
| **Content addressing** | Derive storage key from content | IPFS, Git objects |

## Password Hashing vs General Crypto Hashing

SHA-256 is **fast** — that's a weakness for passwords (GPU can try 10⁹ guesses/sec). Password hashing algorithms are intentionally **slow** (cost factor) and include a **salt** to prevent rainbow table attacks:
- **bcrypt**: adaptive cost, 64-byte salt
- **scrypt**: memory-hard
- **Argon2** (Password Hashing Competition winner): memory+time adjustable

## Related Concepts

- [[SHA-256]] — current standard for general cryptographic hashing
- [[MD5]] — broken; avoid for security purposes
- [[HMAC]] — keyed variant for message authentication
- [[Merkle Tree]] — data structure built from crypto hashes
- [[Checksums]] — non-cryptographic checksums for error detection (CRC, Adler)
