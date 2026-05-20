---
title: "CRC"
type: concept
tags: [checksum, networking, error-detection]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-checksums"]
---

# CRC

**CRC** (Cyclic Redundancy Check) is a non-cryptographic error-detection code based on polynomial division over a binary field. It is optimized for detecting accidental data corruption — particularly burst errors — not security.

## How It Works

Both sender and receiver agree on a **generator polynomial** (e.g., CRC-32 uses `0x04C11DB7`):

1. Sender appends a CRC value to the data (computed by polynomial division)
2. Receiver recalculates CRC on received data
3. If the computed CRC matches the appended CRC → data is intact
4. If they differ → data was corrupted in transit

## Variants

| Variant | Output | Common Use |
|---------|--------|-----------|
| CRC-8 | 8 bits | Simple embedded systems |
| CRC-16 | 16 bits | USB, Modbus |
| CRC-32 | 32 bits | Ethernet, ZIP, PNG, gzip |
| CRC-64 | 64 bits | Storage (ECMA-182) |

## Strengths

- **Burst error detection** — excellent at detecting consecutive bit errors (common in hardware noise)
- **Fast** — hardware CRC support built into CPUs, NICs, and storage controllers
- **Deterministic** — same input always yields same checksum

## Limitations

- **Not cryptographic** — an attacker can craft data with any desired CRC
- **Cannot correct errors** — only detects them (contrast with ECC memory)
- **Undetected errors possible** — some error patterns pass undetected (probability ~1/2^n for CRC-n)

## Use Cases

- **Ethernet frames** — CRC-32 in the FCS (Frame Check Sequence)
- **ZIP, gzip, PNG** — file integrity during storage and transfer
- **Serial protocols** — UART, SPI, I2C communications
- **Disk I/O** — storage controllers check sector CRCs

## Related Concepts

- [[Checksums]] — parent concept
- [[Parity Bit]] — simpler but weaker error detection
- [[Cryptographic Hash]] — use instead when security matters
