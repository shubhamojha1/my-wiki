---
title: "Epoch"
type: concept
tags: [distributed-systems, consensus, leader-election]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Epoch

An **epoch** (also called a **term** or **ballot**) is a logical time period during which a single leader is recognized as authoritative in a consensus-based distributed system. Each epoch is identified by a monotonically increasing number.

## Purpose

Epochs solve the **split-brain** problem: when a network partition causes a new leader election while the old leader is still running, epoch numbers let nodes reject messages from outdated leaders.

## Properties

- **Unique epoch number per period** — each election attempt increments the counter
- **Single leader per epoch** — at most one node can win any given epoch
- **Monotonically increasing** — epochs never decrease
- **Elections can fail** — if no quorum is reached, no leader wins that epoch; a new election begins with a higher number

## How It Works

1. Nodes suspect the current leader has failed (timeout or missed heartbeats)
2. A candidate increments the epoch counter and requests votes
3. The winning candidate becomes leader for that epoch
4. All messages include the epoch number; nodes reject messages from lower epochs
5. A stale leader that reconnects sees a higher epoch and steps down to follower

## Terminology by System

| System | Term Used |
|--------|-----------|
| [[Raft]] | "term" |
| [[Paxos]] | "ballot number" / "proposal number" |
| [[Zab]] | "epoch" |
| Viewstamped Replication | "view number" |

## Related Concepts

- [[Consensus]] — the problem epochs help solve
- [[Raft]] — uses terms as epochs
- [[Paxos]] — uses ballot numbers similarly
- [[Lamport Clocks]] — another mechanism for logical time ordering
- [[Leader Election]] — the process by which epochs change
