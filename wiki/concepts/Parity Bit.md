---
title: "Parity Bit"
type: concept
tags: [error-detection, checksum]
created: 2026-05-10
updated: 2026-05-20
sources: ["algomaster-checksums"]
---

# Parity Bit

A **parity bit** is a single extra bit appended to a group of data bits so that the total count of 1s in the group is either always even (even parity) or always odd (odd parity). It is the simplest possible error-detection scheme.

## How It Works

**Example (even parity)**:
```
Data bits:   1 0 1 1 0 1 0   → five 1s (odd)
Parity bit:  1               → add a 1 to make six 1s (even)
Transmitted: 1 0 1 1 0 1 0 1

Receiver recomputes: 1+0+1+1+0+1+0+1 = six 1s (even) ✓ no error detected

If bit 3 flips in transit:
Received:    1 0 0 1 0 1 0 1 → five 1s (odd) ✗ error detected!
```

## Parity vs Error Detection Ability

| Bit-flip count | Detected? | Reason |
|----------------|-----------|--------|
| 1 bit (any) | Yes | Total 1-count parity changes |
| 2 bits | No | Two flips cancel each other |
| 3 bits | Yes | Net change is odd |
| Even number of flips | No | Parity unchanged |

## 2D Parity (Longitudinal + Transverse)

Adding a parity bit per row and per column allows **single-bit error correction** (locate the row and column of the error):

```
Data   parity
1 0 1  | 0
0 1 1  | 0
1 1 0  | 0
-------+--
0 0 0    0  ← column parities
```

## Variants

| Scheme | Bits overhead | Detects | Corrects |
|--------|--------------|---------|---------|
| Simple parity | 1 bit | Odd # of flips | Nothing |
| 2D parity | n+m bits | All 1-bit errors, most burst errors | 1-bit errors |
| Hamming code | O(log n) bits | All 1-bit errors | 1-bit errors |
| CRC-32 | 32 bits | Burst errors ≤ 32 bits | Nothing (detect only) |

## Where Used

- **Serial communication** (RS-232, UART): One parity bit per byte; cheap and fast.
- **DRAM error detection**: Simple parity chips detect but cannot correct.
- **ECC memory**: Uses Hamming code (an extension of parity) — detect 2-bit, correct 1-bit errors.
- **RAID-5**: Uses XOR parity across drives to reconstruct a failed disk.

## Related Concepts

- [[CRC]] — polynomial-based, much stronger error detection
- [[Checksums]] — general family of error-detection techniques
- [[Hamming Code]] — extends parity to also locate and correct errors
