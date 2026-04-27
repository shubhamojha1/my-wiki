---
title: "OSI Layer 4: Transport"
type: concept
tags: [osi-model, networking, layer-4]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Layer 4: Transport

**Layer 4** of the OSI model delivers data to the correct application on a destination device.

## Responsibility

- Deliver data to the correct application
- Identify specific applications using ports
- Segmentation of large data chunks
- Flow control (prevents fast senders from overwhelming slow receivers)

## Key Details

- Adds **ports** (e.g., 443 for HTTPS, 22 for SSH)
- IP + port = socket
- Two protocol options:
  - **TCP**: Reliable, connection-oriented
  - **UDP**: Fast, connectionless

## Related Concepts

- [[OSI Model]] — The 7-layer framework this layer belongs to
- [[Port (Network)]] — Layer 4 application identifier
- [[TCP]] — Reliable transport protocol
- [[UDP]] — Fast, connectionless transport protocol
- [[OSI Layer 3: Network]] — The layer below
- [[OSI Layer 5: Session]] — The layer above