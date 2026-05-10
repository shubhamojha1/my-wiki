---
title: "Subnet Mask"
type: concept
tags: [networking, ip-address, subnetting]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# Subnet Mask

A **subnet mask** is a 32-bit binary mask used to separate an IP address into its network and host portions.

## How It Works

The mask has 1s in the network portion and 0s in the host portion. A bitwise AND between the IP address and the subnet mask reveals the network address.

Example: IP `192.168.1.10` with mask `255.255.255.0`:
- Binary mask: `11111111.11111111.11111111.00000000`
- Network portion: first 24 bits
- Host portion: last 8 bits
- Network address: `192.168.1.0`

## Common Subnet Masks

| CIDR | Subnet Mask | Hosts |
|------|-------------|-------|
| /24  | 255.255.255.0   | 254 |
| /25  | 255.255.255.128 | 126 |
| /26  | 255.255.255.192 | 62  |
| /27  | 255.255.255.224 | 30  |
| /28  | 255.255.255.240 | 14  |
| /29  | 255.255.255.248 | 6   |
| /30  | 255.255.255.252 | 2   |

## Usage

- Devices use the subnet mask to determine if a destination is on the same local network (send directly) or a remote network (forward to default gateway)
- Subnetting borrows bits from the host portion to create more network IDs, enabling efficient network segmentation

## Related Concepts

- [[IP Address]] — What the mask operates on
- [[CIDR Notation]] — `/prefix` shorthand for subnet masks
- [[IPv4]] — Where subnet masks are commonly used
