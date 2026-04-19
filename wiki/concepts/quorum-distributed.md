---
title: "Quorum (Distributed)"
type: concept
tags: [distributed-systems, replication]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Quorum systems require agreement from a subset of nodes before proceeding.

## Strict Quorum
- Any two quorums overlap
- Majority quorum: N/2+1
- Guarantees single history

## Partial Quorum (Dynamo-style)
- No overlap requirement
- Different subsets can have different versions
- User chooses R, W parameters

## Parameters
- **R**: nodes contacted for read
- **W**: nodes required for write
- **N**: total replicas

## Guidelines
- R + W > N → read-write quorum overlap
- Typical: N=3, R=2, W=2

## Comparison
- Strict quorum: stronger consistency
- Partial quorum: higher availability, more divergence