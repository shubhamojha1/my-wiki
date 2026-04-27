---
title: "OSI Layer 2: Data Link"
type: concept
tags: [osi-model, networking, layer-2]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Layer 2: Data Link

**Layer 2** of the OSI model organizes raw bits into structured **frames** and introduces hardware addressing.

## Responsibility

- Organize raw bits into structured frames
- Introduce hardware addressing (MAC addresses)
- Flow control and error checking
- Medium access management

## Key Details

- Uses 48-bit **MAC addresses** (e.g., `00:1A:2B:3C:4D:5E`) burned into network interfaces
- Split into two sublayers:
  - **LLC** (Logical Link Control): Flow control, error checking
  - **MAC** (Media Access Control): Hardware addressing, medium access
- Only operates within a single local network

## Key Device

- **Switch**: Reads destination MAC address and forwards frames only to the correct port (contrasts with Layer 1 hubs that broadcast to all ports)

## Related Concepts

- [[OSI Model]] — The 7-layer framework this layer belongs to
- [[MAC Address]] — Layer 2 hardware address
- [[OSI Layer 1: Physical]] — The layer below
- [[OSI Layer 3: Network]] — The layer above