---
title: "Public IP Address"
type: concept
tags: [ip-address, networking, public]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-ip-address"]
---

# Public IP Address

A **public IP address** is a globally unique address routable across the internet. Any host on the internet can send a packet to a public IP and routers worldwide know how to forward it to the destination.

## Characteristics

| Property | Detail |
|----------|--------|
| **Uniqueness** | Globally unique — no two devices on the public internet share the same public IP |
| **Allocation** | Assigned by ISPs or cloud providers, who in turn receive blocks from Regional Internet Registries (RIRs) |
| **Routable** | Advertised via BGP; all backbone routers have routes toward it |
| **Cost** | IPv4 addresses are scarce and leased; IPv6 public addresses are abundant |
| **Visibility** | Your public IP is visible to every server you connect to |

## Well-Known Examples

| Address | Organization |
|---------|-------------|
| `8.8.8.8` | Google Public DNS |
| `1.1.1.1` | Cloudflare DNS |
| `9.9.9.9` | Quad9 DNS |
| `203.0.113.x` | TEST-NET-3 (documentation only, not routed) |

## IPv4 Scarcity

The 32-bit IPv4 address space (~4.3 billion addresses) is exhausted at the RIR level. Organizations hoard and trade blocks; large cloud providers received large early allocations. This scarcity is why:
- Most home users get **one** public IP shared via NAT across many devices.
- Cloud instances use **Elastic IPs** (reserved public IPs detached from specific VMs).
- IPv6 provides 128-bit addresses (3.4×10³⁸) — effectively unlimited.

## Static vs Dynamic Public IP

| Type | Description | Use case |
|------|-------------|---------|
| **Dynamic** | Changes on reconnect or lease renewal | Home broadband, cost-saving |
| **Static** | Permanently assigned | Servers, email (SPF/DKIM), VPN endpoints |
| **Elastic (cloud)** | Static, detachable from VM instances | AWS EIP, GCP External IP |

## Obtaining a Public IP

1. **From your ISP**: Automatic via DHCP when connecting; dynamic by default, static on request.
2. **From a cloud provider**: AWS, GCP, Azure allocate public IPs to instances and load balancers.
3. **From an RIR**: ARIN (Americas), RIPE NCC (Europe), APNIC (Asia-Pacific) — only for ISPs/large orgs.

## Related Concepts

- [[IP Address]] — general IP address concepts
- [[Private IP Address]] — non-routable ranges (10.x, 172.16.x, 192.168.x)
- [[NAT]] — maps multiple private IPs to one public IP
- [[IPv6]] — successor with abundant address space
- [[BGP]] — the routing protocol that makes public IPs globally reachable
