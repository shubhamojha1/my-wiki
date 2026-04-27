---
title: "OSI vs TCP/IP Model"
type: concept
tags: [osi-model, networking, tcp-ip]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI vs TCP/IP Model

The **OSI model** is a theoretical 7-layer framework. The **TCP/IP model** is the pragmatic 4-layer implementation actually used by the modern internet.

## Layer Mapping

| OSI Layers | TCP/IP Layer | Example Protocols |
|------------|--------------|-------------------|
| Application + Presentation + Session | Application | HTTP, FTP, DNS, SSH, TLS |
| Transport | Transport | TCP, UDP |
| Network | Internet | IP, ICMP, ARP |
| Data Link + Physical | Network Access | Ethernet, WiFi, PPP |

## Key Differences

| Aspect | OSI Model | TCP/IP Model |
|--------|-----------|--------------|
| Layers | 7 distinct layers | 4 consolidated layers |
| Purpose | Theoretical reference framework | Practical, deployed internet standard |
| Troubleshooting Value | High: Granular separation allows precise issue pinpointing | Low: "Application" layer lumps too many functions |

## Why Learn OSI if TCP/IP Is Used?

The OSI model remains the better mental model for reasoning about network issues. Its 7-layer granularity lets teams quickly identify where a problem lives:

- "Layer 4 issue" → transport/ports/TCP/UDP
- "Layer 3 issue" → routing/IP/ICMP
- "Layer 2 issue" → switches/MAC addresses

The TCP/IP model's broader layers are less useful for precise debugging.

## Related Concepts

- [[OSI Model]] — The theoretical 7-layer framework
- [[TCP]] — Transport protocol in TCP/IP
- [[UDP]] — Connectionless transport protocol
- [[IP Address]] — Layer 3 protocol in TCP/IP