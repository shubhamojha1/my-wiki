---
title: "Sloppy Quorum"
type: concept
tags: [distributed-systems, replication, quorum]
created: 2026-04-21
sources: []
---

A quorum variant used in Dynamo where read/write operations are performed on the first N *healthy* nodes from the preference list, skipping failed or unreachable nodes.

## vs Strict Quorum

Strict quorum requires R/W responses from the same N nodes. Sloppy quorum allows skipping unavailable nodes, improving availability at the cost of potentially reading stale data temporarily.

## Parameters

- **N**: Total replicas
- **R**: Min nodes for read
- **W**: Min nodes for write
- **R + W > N**: Provides consistency guarantee

## Usage in Dynamo

Dynamo uses sloppy quorum because:
1. Temporary failures are common at scale
2. Writes must never be rejected ("always writeable")
3. Hinted handoff handles recovery

See also: [[Quorum (Distributed)]], [[Dynamo]], [[Consistent Hashing]]