---
title: "Parity Bit"
type: concept
tags: [error-detection, checksum]
created: 2026-05-10
sources: ["algomaster-checksums"]
---

# Parity Bit

A **parity bit** is the simplest form of checksum — a single bit added to a group of bits to make the total number of 1s either even (even parity) or odd (odd parity).

## How It Works

- **Even parity**: Parity bit set so total 1s (including parity) is even
- **Odd parity**: Parity bit set so total 1s is odd

If any single bit flips during transmission, the parity check fails.

## Limitation

Only detects an **odd number** of bit flips. If two bits flip, parity remains unchanged and the error goes undetected.

## Use Cases

- RAM error detection (ECC memory uses more sophisticated variants)
- Low-level serial communication
- Simple embedded systems

## Related Concepts

- [[Checksums]] — Parent concept
- [[CRC]] — More robust error detection
