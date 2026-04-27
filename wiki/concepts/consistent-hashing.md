---
title: "Consistent Hashing"
type: concept
tags: [distributed-systems, partitioning]
created: 2026-04-19
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/consistent-hashing"]
---

Consistent hashing maps keys to nodes in a way that minimizes remapping when nodes are added or removed.

## The Problem

`hash(key) mod N` causes massive reshuffling (2/3 keys) when nodes change.

## How It Works

1. Map servers and keys to points on circular hash ring
2. For key, walk clockwise to find first server
3. That server handles the key

## Key Property

When nodes change, only `k/n` keys reassigned (k=total keys, n=nodes).

## Virtual Nodes

Each physical server gets multiple positions on ring for even distribution.

## Used In

[[Dynamo]], distributed caches, load balancing