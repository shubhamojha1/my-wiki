---
title: "FLP Impossibility Result"
type: concept
tags: [distributed-systems, impossibility, consensus]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# FLP Impossibility Result

The **FLP impossibility result** (Fischer, Lynch, Paterson, 1985) proves that no deterministic algorithm can solve consensus in a fully asynchronous distributed system if even one process may fail by crashing.

## Formal Statement

In an asynchronous message-passing system where:
- Messages are never lost (reliable delivery)
- At most one process may fail (crash-stop)
- Failure means only that the process stops executing (no Byzantine behavior)

...there is no deterministic algorithm that satisfies all three consensus properties simultaneously:
1. **Agreement** — all processes decide the same value
2. **Validity** — the decided value was proposed by some process
3. **Termination** — all non-faulty processes eventually decide

## Proof Intuition

The key insight is **indistinguishability**:

- In an asynchronous system, there is no upper bound on message delivery time
- A slow process looks identical to a crashed process
- The algorithm cannot decide: "Is this process just delayed, or has it failed?"

An adversary can always delay one message to prevent the algorithm from reaching a "bivalent" → "univalent" decision, keeping it undecided indefinitely.

## Practical Implications

Real consensus algorithms escape FLP by weakening one assumption:

| Escape Route | Mechanism | Example |
|-------------|-----------|---------|
| Partial synchrony | Assume eventual time bounds | [[Raft]], [[Paxos]] |
| Randomization | Probabilistic termination | Ben-Or's algorithm |
| Failure detectors | Oracle that suspects failures | Chandra-Toueg |

[[Raft]] and [[Paxos]] do not violate FLP — they sacrifice **liveness** (may not terminate) in fully asynchronous scenarios, but guarantee **safety** (never decide wrong). In practice, network timing is eventually good enough that they terminate.

## Relationship to CAP

FLP and [[CAP Theorem]] are complementary:
- CAP says: cannot have C + A + P simultaneously
- FLP says: cannot have consensus in fully async systems with any failure

Both point to the same fundamental limit: distributed systems must make trade-offs under uncertainty.

## Related Concepts

- [[Consensus Problem]] — what FLP proves is impossible
- [[Asynchronous System Model]] — the model in which FLP applies
- [[CAP Theorem]] — related impossibility for distributed storage
- [[Raft]] — practical consensus algorithm that lives with FLP via partial synchrony
- [[Paxos]] — another practical consensus algorithm
