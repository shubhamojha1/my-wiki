---
title: "OSI Layer 1: Physical"
type: concept
tags: [osi-model, networking, layer-1]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Layer 1: Physical

**Layer 1** of the OSI model is responsible for transmitting raw binary bits (0s and 1s) over a physical medium.

## Responsibility

- Transmit raw bits over physical medium (copper wire, fiber optic, radio waves)
- Define connector types, cable specifications, and bit-level sender-receiver synchronization
- Convert data into electrical signals, light pulses, or radio waves

## Key Details

- No understanding of bit meaning—only movement between points
- Physical layer failures cannot be fixed by software configuration (e.g., a broken cable breaks all higher-layer functionality)

## Examples

- Ethernet cables (copper)
- Fiber optic cables
- Network interface cards (NICs)
- Hubs, repeaters

## Related Concepts

- [[OSI Model]] — The 7-layer framework this layer belongs to
- [[OSI Layer 2: Data Link]] — The layer above