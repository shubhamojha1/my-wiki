---
title: "Static vs Dynamic IP"
type: concept
tags: [networking, ip-address, dhcp]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# Static vs Dynamic IP

IP addresses can be assigned statically (manual) or dynamically (automatic via DHCP).

## Static IP

- Manually configured on a device, never changes
- Essential for servers, printers, and devices that must be consistently reachable
- Reliable but often costs more and requires manual management

## Dynamic IP (DHCP)

- Assigned automatically by a **DHCP (Dynamic Host Configuration Protocol)** server
- The address is leased for a period and can change on reconnection
- Used by most consumer devices (laptops, phones)
- Highly efficient for managing large numbers of devices

## How DHCP Works

1. Device broadcasts a DHCP Discover message
2. DHCP server responds with an Offer (available IP, lease time)
3. Device sends a Request for the offered IP
4. DHCP server acknowledges with an ACK

## Comparison

| Aspect | Static | Dynamic (DHCP) |
|--------|--------|----------------|
| Configuration | Manual | Automatic |
| Address change | Never | Can change |
| Management overhead | High | Low |
| Use case | Servers, infrastructure | End-user devices |

## Related Concepts

- [[IP Address]] — The address being assigned
- [[Private IP Address]] — Often assigned via DHCP on local networks
- [[Public IP Address]] — Typically static for servers, dynamic for home users
