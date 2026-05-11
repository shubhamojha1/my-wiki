---
title: "Geo-Based Sharding"
type: concept
tags: [database, sharding, geo, latency]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Geo-Based Sharding

**Geo-based sharding** distributes data based on geographic location, placing shards closer to users in each region.

## How It Works

**Example**: Shard 1 serves North America, Shard 2 serves Europe, Shard 3 serves Asia.

## Pros and Cons

| Pro | Con |
|-----|-----|
| Low latency (data near users) | Uneven population distribution across regions |
| Compliance (data sovereignty laws) | Cross-region queries are expensive |
| Natural fault isolation | Handling user mobility is complex |

## Compliance Considerations

Geo-sharding helps satisfy data residency requirements (GDPR, CCPA) by storing user data within specific jurisdictions.

## Related

- [[Database Sharding]] — General concept
- [[GeoDNS]] — Geographic DNS routing for regional affinity
