---
title: "Asynchronous System Model"
type: concept
tags: [distributed-systems, timing, system-model]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Asynchronous System Model

The **asynchronous system model** makes no timing assumptions: processes execute at arbitrary rates, message delivery has no upper time bound, and clocks are not reliable. It represents the most pessimistic, but often most realistic, view of distributed systems.

## Characteristics

- **No message delay bound** — a message may be delayed for an arbitrary (but finite) time
- **Independent process speeds** — processes execute at different, unpredictable rates
- **No useful clocks** — cannot rely on timeouts or real-time assumptions
- **Cannot distinguish slow from crashed** — a process that hasn't responded may just be slow

## Implications

Because no timing assumptions can be made:
- The [[FLP Impossibility Result]] applies: consensus cannot be solved deterministically with even one crash
- Timeout-based failure detection is fundamentally unreliable
- Algorithms must be designed for **safety** even when liveness cannot be guaranteed

## Real-World Reality

Real production systems are **partially synchronous** — a middle ground between fully synchronous and fully asynchronous:
- Networks are usually fast, but occasionally slow or partition
- Clocks drift but can be synchronized to within bounded error (NTP, GPS)
- Message delivery bounds hold most of the time but not always

Practical algorithms like [[Raft]] and [[Paxos]] assume partial synchrony: they guarantee safety always and liveness when the network is eventually well-behaved.

## System Model Spectrum

| Model | Timing Assumptions | Practical? | Algorithms Possible |
|-------|-------------------|-----------|---------------------|
| Synchronous | Known bounds on delay and clocks | No (except embedded) | Easiest |
| Partially Synchronous | Eventually bounded | Yes | Raft, Paxos |
| Asynchronous | No bounds | Closest to reality | Hardest; FLP applies |

## Related Concepts

- [[Synchronous System Model]] — the opposite extreme
- [[System Model]] — the broader framing of distributed system assumptions
- [[FLP Impossibility Result]] — key theorem about async systems
- [[Failure Detector]] — tool for approximating crash detection in async models
- [[Raft]] — practical algorithm designed for partial synchrony
