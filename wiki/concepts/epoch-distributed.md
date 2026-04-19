---
title: "Epoch"
type: concept
tags: [distributed-systems, consensus]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Epoch (term in [[Raft]]) is a logical time period during which a single leader coordinates operations.

## Properties
- Unique epoch number per period
- Single leader per epoch
- Acts as logical clock

## Purpose
- Identify outdated proposals
- Ignore messages from old leaders
- Elections can fail, changing epochs

## Usage in Consensus
- [[Paxos]]: "term"
- [[Raft]]: "term"
- Similar to Japanese era names