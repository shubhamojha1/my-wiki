---
title: "Practical Byzantine Fault Tolerance (pBFT)"
type: concept
tags: [distributed-systems, consensus, byzantine, fault-tolerance]
created: 2026-05-11
sources: [medium-consensus-distributed-system]
---

# Practical Byzantine Fault Tolerance (pBFT)

**pBFT** is a consensus algorithm that tolerates Byzantine failures by using a 3-phase protocol (pre-prepare, prepare, commit) with a rotating primary node.

## Assumptions

- **≤ f faulty nodes** out of `n = 3f + 1` total nodes (up to 1/3 can be Byzantine)
- **Partially synchronous** network (bounded delay after some unknown global stabilization time)

## Protocol Phases

1. **Pre-prepare**: Primary (leader) proposes a value to all backup (secondary) nodes
2. **Prepare**: Backups broadcast their acceptance; each node collects prepare messages
3. **Commit**: Nodes broadcast commit messages after collecting 2f+1 prepare messages

A value is committed when the client receives matching replies from **2f+1** distinct nodes.

## View Change

If the primary is suspected faulty (doesn't propose within a timeout), a **view change** elects a new primary. This ensures liveness even when the leader fails.

## Related

- [[Byzantine Failure]] — The failure model pBFT handles
- [[Consensus]] — General consensus concept
- [[HotStuff]] — Modern improvement on pBFT for blockchain
