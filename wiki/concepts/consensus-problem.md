---
title: "Consensus Problem"
type: concept
tags: [distributed-systems, problems]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Consensus is the problem of getting all nodes to agree on a single value.

## Properties

1. **Agreement**: Every correct process agrees on same value
2. **Integrity**: Each decides at most one value
3. **Termination**: All eventually decide
4. **Validity**: If all propose V, all decide V

## Importance
Core of many distributed systems:
- Leader election
- Atomic commit
- Atomic broadcast

## Challenges
- [[FLP Impossibility Result]]: Cannot solve in async systems with failures
- Requires [[CAP Theorem]] tradeoffs

## Solutions
- [[Paxos]], [[Raft]], [[Two-Phase Commit]]
- Need failure detectors or synchronous assumptions