---
title: "OSI Layer 6: Presentation"
type: concept
tags: [osi-model, networking, layer-6]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Layer 6: Presentation

**Layer 6** of the OSI model translates data between application formats and network-required formats.

## Responsibility

- Translate data between application and network formats
- Data format conversion
- Encoding and decoding

## Three Core Functions

1. **Encryption**: TLS/SSL for HTTPS connections
2. **Compression**: gzip, Brotli to reduce bandwidth usage
3. **Encoding**: character sets (ASCII/UTF-8), data formats (JPEG/JSON)

## Key Details

- HTTPS connections perform Layer 6 encryption as part of the Layer 7 HTTPS protocol
- Modern protocols often consolidate Presentation functions into Application layer

## Related Concepts

- [[OSI Model]] — The 7-layer framework this layer belongs to
- [[TLS]] — Transport Layer Security
- [[OSI Layer 5: Session]] — The layer below
- [[OSI Layer 7: Application]] — The layer above