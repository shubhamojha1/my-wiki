---
title: "ZAB (Zookeeper Atomic Broadcast)"
type: entity
tags: [distributed-systems, consensus, atomic-broadcast]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

ZAB is the atomic broadcast protocol used in Apache Zookeeper. Provides total ordered broadcast similar to Paxos, optimized for primary-backup systems.

## Purpose
Zookeeper provides coordination primitives (locks, leader election) for distributed systems. ZAB ensures atomic ordering of operations across the cluster.

## Properties
- **Total order**: Total broadcast of operations
- **Reliable**: Delivers messages despite failures
- **FIFO**: Per-client ordering preserved
- **Crash recovery**: Recovers from failed leaders

## Comparison to Paxos
- Atomic broadcast differs from pure consensus but achieves similar goals
- Optimized for primary-backup pattern
- Used in ZooKeeper, supports HBase, Storm, Kafka

## Usage
- Apache Zookeeper coordination
- Hadoop ecosystem coordination
- Kafka broker coordination