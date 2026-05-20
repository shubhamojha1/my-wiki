---
title: "Geo-Based Sharding"
type: concept
tags: [database, sharding, geo, latency]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Geo-Based Sharding

**Geo-based sharding** partitions data by geographic region so each shard is deployed in the data center closest to that region's users, reducing network latency and satisfying data residency laws.

## Example Layout

```
┌─────────────────────────────────────┐
│            Global Router            │
│  (GeoDNS / anycast / lat/lng lookup) │
└───────────┬──────────┬──────────────┘
            │          │          │
      [US Shard]  [EU Shard]  [APAC Shard]
       AWS us-east  AWS eu-west  AWS ap-southeast
       US user data  EU user data  Asia user data
```

The shard key is typically a country code, region identifier, or derived from the user's registered locale — not the request's IP (which can change).

## Pros and Cons

| Pro | Con |
|-----|-----|
| Low read/write latency (data near users) | Uneven data distribution (EU << APAC population) |
| Data residency compliance (GDPR, CCPA, PIPL) | Cross-region queries require scatter-gather or federation |
| Fault isolation — regional outage does not affect other shards | User mobility (expats, travelers) must pin to home shard |
| Simpler compliance audit surface | Adding a new region requires shard migration tooling |

## Compliance: Data Residency

Data sovereignty laws require that certain data (health records, financial data, PII) never leave the jurisdiction. Geo-sharding is often the only architecture that satisfies these requirements at scale.

- **GDPR** (EU): EU resident data must stay within the EU or an adequate country.
- **CCPA** (California): Operational controls on California resident data.
- **PIPL** (China): Personal data of Chinese residents must be stored in China.

## User Mobility Problem

A French user traveling to the US still has their data on the EU shard. Solutions:

1. **Always read from home shard**: Route every request back to EU (adds latency).
2. **Cache in local region**: Read locally, write back to home shard asynchronously.
3. **Pin on account creation**: Shard is set once and never changes.

## Comparison with Other Sharding Strategies

| Strategy | Basis | Best for |
|----------|-------|---------|
| Geo-based | Region / country | Latency, compliance |
| Hash-based | Hash of key | Even distribution |
| Range-based | Key range | Range queries |
| Directory-based | Lookup table | Arbitrary mapping |

## Related Concepts

- [[Database Sharding]] — general sharding concepts
- [[Range-Based Sharding]] — often combined with geo (region + range within region)
- [[Hash-Based Sharding]] — alternative that prioritizes even distribution
- [[Cross-Shard Query]] — challenge that arises with any sharding approach
