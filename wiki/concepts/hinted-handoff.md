---
title: "Hinted Handoff"
type: concept
tags: [distributed-systems, failure-handling, replication]
created: 2026-04-21
sources: []
---

A failure handling technique used in Dynamo where replicas meant for an unavailable node are sent to another node with a "hint" metadata indicating the intended recipient.

## How It Works

1. Write intended for node A fails because A is down
2. Replica sent to node D with metadata hint: "A was intended"
3. D stores replica with hint, monitors A for recovery
4. When A recovers, D delivers replica and deletes local copy

## Tradeoffs

- Maintains availability during transient failures
- Risk of data loss if D fails before handoff
- Used for temporary failures; Merkle trees handle permanent failures

See also: [[Dynamo]], [[Sloppy Quorum]], [[Merkle Tree]]