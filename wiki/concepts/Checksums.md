---
title: "Checksums"
type: concept
tags: [networking, data-integrity, error-detection]
created: 2026-05-10
sources: ["algomaster-checksums"]
---

# Checksums

A **checksum** is a small block of data derived from a larger dataset to detect errors. Acts as a "fingerprint" — if the data changes, the checksum changes.

## Analogy: Postal Letter Photo

Before sealing an envelope, take a photo of the letter. When the recipient receives it, they take a photo and send it back. If the two photos match, the letter wasn't tampered with. Checksums work the same way for digital data.

## How It Works

1. **Calculate**: Process original data through an algorithm to produce a checksum
2. **Transmit/Store**: Append checksum to data
3. **Verify**: Recipient recalculates checksum on received data, compares to original
4. **Detect**: Match = intact; mismatch = corruption or tampering

## Types

- [[Parity Bit]] — Single bit, detects odd number of bit flips
- [[CRC]] — Polynomial division, catches burst errors from channel noise
- [[Cryptographic Hash]] — One-way functions (MD5, SHA-256) for security

## Use Cases

- File download verification
- Network packet integrity (TCP, Ethernet)
- Data backups — ensure backed-up data is accurate
- Disk I/O error detection
- Database replication consistency
- Firmware update verification

## Related Concepts

- [[CRC]] — Non-cryptographic checksum
- [[MD5]] — Deprecated cryptographic hash
- [[SHA-256]] — Current integrity standard
- [[Cryptographic Hash]] — One-way security functions
