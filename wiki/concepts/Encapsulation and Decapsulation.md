---
title: "Encapsulation and Decapsulation"
type: concept
tags: [osi-model, networking, encapsulation]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# Encapsulation and Decapsulation

Data moves through the OSI stack via two core processes when being sent between devices.

## Encapsulation (Sending Data Down the Stack)

Each layer wraps incoming data with its own header (and sometimes trailer) as it moves down to the physical layer:

1. **Layer 7 (Application)**: Generates raw data (e.g., HTTP request) → called **Data**
2. **Layer 4 (Transport)**: Adds TCP/UDP header (source port, destination port, sequence numbers) → creates **Segment** (TCP) or **Datagram** (UDP)
3. **Layer 3 (Network)**: Adds IP header (source IP, destination IP) → creates **Packet**
4. **Layer 2 (Data Link)**: Adds Ethernet header (source MAC, destination MAC) and trailer (checksum/FCS) → creates **Frame**
5. **Layer 1 (Physical)**: Converts frame into raw binary bits and transmits

### Analogy

Mailing a letter: letter (app data) → envelope with address (IP header) → mail bag with barcode (Ethernet frame) → truck transports the bag (physical bits)

## Data Unit Names by Layer

| Layer | Data Unit Name |
|-------|----------------|
| Application (L7) | Data |
| Transport (L4) | Segment (TCP) / Datagram (UDP) |
| Network (L3) | Packet |
| Data Link (L2) | Frame |
| Physical (L1) | Bits |

## Decapsulation (Receiving Data Up the Stack)

The reverse of encapsulation: each layer strips its own header, reads required metadata, and passes the remaining payload up to the next layer. By the time data reaches Layer 7, all networking headers are removed, and the application receives clean data.

## Related Concepts

- [[OSI Model]] — The framework this process operates in
- [[OSI Layer 1: Physical]]
- [[OSI Layer 2: Data Link]]
- [[OSI Layer 3: Network]]
- [[OSI Layer 4: Transport]]