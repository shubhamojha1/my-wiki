---
title: "Broadcast Address"
type: concept
tags: [networking, ip-address, broadcast]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# Broadcast Address

A **broadcast address** is a special IP address used to send a message to all devices on a local subnet simultaneously.

## IPv4 Broadcast

In IPv4, the broadcast address has all host bits set to 1. For network `192.168.1.0/24`:
- Broadcast address: `192.168.1.255`
- Host 1: `192.168.1.1`
- Host 254: `192.168.1.254`

The network address (all host bits = 0) and broadcast address (all host bits = 1) are reserved and cannot be assigned to devices.

## IPv6

IPv6 has **no broadcast**. It uses multicast instead, which is more efficient since only interested devices process the message.

## Uses

- ARP requests (find MAC address for a given IP)
- DHCP Discover messages (find DHCP servers)
- Routing protocol announcements

## Related Concepts

- [[IP Address]] — Parent concept
- [[Subnet Mask]] — Used to determine the broadcast address
- [[Multicast Address]] — IPv6 replacement for broadcast
- [[IPv4]] — Where broadcast is used
- [[IPv6]] — Uses multicast instead of broadcast
