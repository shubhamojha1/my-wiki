---
title: "Synchronous System Model"
type: concept
tags: [distributed-systems, timing, system-model]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Synchronous System Model

The **synchronous system model** assumes that processes execute in lockstep with known upper bounds on message transmission delay and accurate synchronized clocks. It is the most optimistic model and the easiest for algorithm design, but it is largely unrealistic for general-purpose distributed systems.

## Characteristics

- **Known message delay bound** — every message arrives within a fixed maximum time `d`
- **Known process step bound** — each process completes a step within `r` time units
- **Accurate clocks** — all nodes can agree on real time within a bounded error `ε`
- **Predictable behavior** — absence of a response within the time bound means failure

## Advantages

- **Failure detection is exact** — if no response arrives within `d`, the node has crashed
- **Algorithm design is simpler** — can use timeouts reliably
- **Can rule out ambiguity** — timing assumptions eliminate many pathological cases

## Disadvantages

- **Unrealistic for most settings** — real networks have unbounded delays (garbage collection pauses, TCP retransmits, routing changes)
- **Not practical at internet scale** — wide-area networks violate synchrony assumptions routinely

## When It Is Used

| Context | Why Synchrony Holds |
|---------|-------------------|
| Real-time embedded systems (automotive, avionics) | Hardware guarantees timing; deterministic OS |
| Tightly controlled local networks | Known network topology, bounded RTT |
| Academic analysis | Simplifies proofs; show what is possible |
| Simulations | Full control over timing |

## Partial Synchrony

Most real distributed systems assume **partial synchrony**: the system is asynchronous in general, but eventually the network stabilizes and bounded delays apply for long enough to make progress. This is the basis for practical algorithms like [[Raft]] and [[Paxos]].

## Related Concepts

- [[Asynchronous System Model]] — the opposite, pessimistic model
- [[System Model]] — the broader framing of distributed system assumptions
- [[FLP Impossibility Result]] — applies to the async model; solvable in synchronous
- [[Failure Detector]] — synchronous model enables perfect failure detectors
