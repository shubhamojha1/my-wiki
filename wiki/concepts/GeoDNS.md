---
title: "GeoDNS"
type: concept
tags: [networking, dns, geo-routing]
created: 2026-05-10
sources: ["algomaster-dns"]
---

# GeoDNS

**GeoDNS** (Geographic DNS) returns different IP addresses for the same domain name depending on where the client's request originates geographically.

## How It Works

1. Recursive resolver queries the authoritative name server
2. Server identifies the resolver's approximate location (by IP range or subnet)
3. Server returns the IP of the nearest or most appropriate data center
4. Client connects to the geographically closest server

## Use Cases

- **Performance optimization**: Route users to the nearest server for lower latency
- **Compliance**: Direct users to country-specific data centers to meet data residency laws
- **Load management**: Spread traffic across regional deployments
- **Content restrictions**: Serve different content based on geographic region

## Example

A global service like `google.com` may resolve to:
- `216.58.xx.xx` for users in North America
- `142.250.xx.xx` for users in Europe
- `64.233.xx.xx` for users in Asia

## GeoDNS vs Anycast

| Aspect | GeoDNS | Anycast |
|--------|--------|---------|
| Mechanism | DNS returns different IPs per region | Same IP advertised from multiple locations |
| Granularity | Country/city level | Network topology level |
| Complexity | Requires geo-IP database | Configuration on routers |
| Use case | Data residency, content rules | Latency, fault tolerance |

Both are often used together for maximum performance.

## Related Concepts

- [[DNS]] — Parent concept
- [[Authoritative Name Server]] — Where GeoDNS logic is configured
- [[Anycast]] — Complementary routing technique
- [[CDN]] — CDNs often use GeoDNS for edge server selection
