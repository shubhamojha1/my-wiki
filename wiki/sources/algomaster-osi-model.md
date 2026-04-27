---
title: "OSI Model"
type: source
tags: [system-design, networking, osi-model]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Model

The **OSI (Open Systems Interconnection) Model** is a 7-layer conceptual framework published by the International Organization for Standardization (ISO) in 1984. It standardizes network communication by defining distinct responsibilities for each layer, acting as a contract (specifying *what* each layer does, not *how* to implement it) to enable vendor interoperability.

## The 7 Layers

| Layer | Name | Data Unit | Key Components |
|-------|------|-----------|----------------|
| 7 | Application | Data | HTTP, DNS, SMTP, FTP |
| 6 | Presentation | Data | TLS, SSL, encoding |
| 5 | Session | Data | NetBIOS, RPC |
| 4 | Transport | Segment/Datagram | TCP, UDP, ports |
| 3 | Network | Packet | IP, routers |
| 2 | Data Link | Frame | MAC, switches |
| 1 | Physical | Bits | Cables, NICs |

Mnemonic (bottom to top): **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

## Key Concepts

- [[Encapsulation and Decapsulation]] — How data flows through the stack
- [[OSI vs TCP/IP Model]] — Comparison of theoretical vs deployed models
- [[MAC Address]] — Layer 2 hardware address for local delivery
- [[IP Address]] — Layer 3 logical address for cross-network routing
- [[Port (Network)]] — Layer 4 identifier for specific applications

## Why OSI Matters

The OSI model remains valuable for troubleshooting. Its 7-layer granularity lets teams quickly identify where a problem lives (e.g., "Layer 4 issue" clearly refers to transport/ports/TCP/UDP), while the broader TCP/IP layers are less useful for precise debugging.

## Source

- AlgoMaster.io: [OSI Model](https://algomaster.io/learn/system-design/osi) (March 15, 2026)