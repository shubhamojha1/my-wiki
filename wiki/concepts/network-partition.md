---
title: "Network Partition"
type: concept
tags: [distributed-systems, failures]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

A network partition is failure of network links to one or more nodes, while nodes themselves remain operational.

## Characteristics
- Nodes stay active
- May receive client requests
- Cannot distinguish from node failure

## Challenge
Cannot tell if remote node is down or network is down.

## Implications for Consistency
During partition:
- Must choose [[Availability]] vs [[CAP Theorem|Consistency]]
- Single-copy systems: only one partition can be active

## [[Paxos]]/[[Raft]] Behavior
- Minority partition stops accepting writes
- Majority continues operating
- Prevents divergence