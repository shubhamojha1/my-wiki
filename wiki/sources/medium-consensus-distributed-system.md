---
title: "Consensus in Distributed System"
type: source
tags: [distributed-systems, consensus, byzantine, pBFT]
created: 2026-05-11
sources: [medium-consensus-distributed-system]
---

# Consensus in Distributed System

**Author:** Sourajit Bhattacharjee and Sahil Mahapatra (MTech CSE, IIT Kharagpur)
**URL:** https://medium.com/@sourabhatta1819/consensus-in-distributed-system-ac79f8ba2b8c
**Published:** January 31, 2023

## Summary

An educational article on distributed consensus — the problem, required properties, failure models (crash vs Byzantine), voting-based algorithms (pBFT in detail), proof-based algorithms (PoW/PoS), and real-world applications.

## Key Concepts Covered

- **Definition**: Multiple nodes agreeing on a common value through message passing
- **3 properties**: Agreement (same value), Validity (decided value proposed by non-faulty node), Termination (all non-faulty nodes decide)
- **Crash failure**: Node stops responding (common, easy to handle — ignore the node)
- **Byzantine failure**: Node behaves arbitrarily, sends different messages to different peers (hard to handle)
- **pBFT (Practical Byzantine Fault Tolerance)**: Pre-prepare → Prepare → Commit phases, requires ≤ 1/3 faulty nodes, primary node rotates via view change
- **Byzantine Generals Problem**: Lamport's classic framing — loyal generals must agree despite traitors
- **Proof-based**: PoW (mining), PoS (stake-based)
- **Applications**: blockchain, Google PageRank, load balancing
