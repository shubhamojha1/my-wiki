---
title: "Availability"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Availability is the proportion of time a system is in a functioning condition.

## Definition
`Availability = uptime / (uptime + downtime)`

## Availability Tiers

| Availability | Downtime per Year |
|-------------|------------------|
| 90% ("one nine") | > 1 month |
| 99% ("two nines") | < 4 days |
| 99.9% ("three nines") | < 9 hours |
| 99.99% ("four nines") | < 1 hour |
| 99.999% ("five nines") | ~ 5 minutes |
| 99.9999% ("six nines") | ~ 31 seconds |

## Fault Tolerance
Availability from a technical perspective is about fault tolerance. Distributed systems can take unreliable components and build a reliable system on top of them through redundancy.

## Distinction
Availability differs from reliability. A service can be unavailable due to network outage or company failure, not just technical faults.