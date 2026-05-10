---
title: "Anycast"
type: concept
tags: [networking, anycast, dns, routing]
created: 2026-05-10
sources: ["algomaster-dns"]
---

# Anycast

**Anycast** is a network addressing and routing technique where the same IP address is advertised from multiple locations worldwide. Traffic automatically routes to the nearest available server.

## How It Works

- Multiple servers in different geographic locations announce the same IP address via BGP
- Routers forward packets to the closest server based on routing metrics
- If one server fails, traffic automatically shifts to the next closest

## DNS Use Case

Root servers and public recursive resolvers (Google 8.8.8.8, Cloudflare 1.1.1.1) use anycast:

- Queries go to the nearest server, reducing latency
- High availability: failure of one anycast node doesn't break service
- Load is naturally distributed across global nodes

## Benefits

| Benefit | Description |
|---------|-------------|
| Low Latency | Traffic routes to nearest server automatically |
| Fault Tolerance | Failover is instant and transparent |
| Load Distribution | Traffic spreads across nodes naturally |
| Simplicity | Single IP address, no client-side logic needed |

## Comparison

| Method | One IP → How Many Servers? | Selection |
|--------|---------------------------|-----------|
| Unicast | One | Fixed |
| Anycast | Many (same IP) | Nearest |
| Multicast | Many (group) | Subscription-based |

## Related Concepts

- [[DNS]] — Primary consumer of anycast in practice
- [[Recursive Resolver]] — Public resolvers use anycast
- [[CDN]] — Content delivery networks also use anycast
- [[GeoDNS]] — Geographic DNS routing (complementary to anycast)
