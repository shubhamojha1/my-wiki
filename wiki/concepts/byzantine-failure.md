---
title: "Byzantine Failure"
type: concept
tags: [distributed-systems, fault-tolerance, byzantine]
created: 2026-05-11
updated: 2026-05-20
sources: [medium-consensus-distributed-system]
---

# Byzantine Failure

A **Byzantine failure** is when a node in a distributed system behaves arbitrarily — crashing, sending incorrect data, sending different messages to different peers, or actively colluding with other faulty nodes to subvert the system. The term comes from the [[Byzantine Generals Problem]] (Lamport, Shostak, Pease 1982).

## Why It's Harder Than a Crash

A crashed node is **silent** — other nodes notice the absence and can route around it. A Byzantine node is **deceptive** — it may look healthy to some nodes, send plausible-but-wrong data, or equivocate (say "yes" to A and "no" to B for the same proposal). Protocols cannot simply timeout and move on; they must be designed to reach agreement despite lies.

## Comparison with Crash (Fail-Stop) Failures

| Aspect | Crash (Fail-Stop) | Byzantine |
|--------|------------------|-----------|
| Behavior | Node stops responding | Arbitrary / conflicting messages |
| Detection | Timeout | May be undetectable |
| Tolerance threshold | f < n (any number can crash) | f < n/3 (at most 1/3 faulty) |
| Algorithm examples | Paxos, Raft, Zab | pBFT, HotStuff, Tendermint |
| Complexity | Relatively simple | High (cryptographic signatures, multi-round) |
| Typical context | Internal distributed DBs | Blockchain, open/permissionless networks |

## The n/3 Bound

To tolerate `f` Byzantine nodes, a system needs at least `n ≥ 3f + 1` total nodes. Intuition: the `f` faulty nodes can lie to split the `n - f` honest nodes into two groups of ≈ `(n-f)/2` each — if that split group is smaller than `f`, honest nodes can't achieve a majority against the liars. With `n = 3f+1`, honest nodes always outnumber faulty by enough to agree.

## Example Behaviors

- Equivocation: send `PREPARE(v=5)` to nodes A and B, and `PREPARE(v=7)` to nodes C and D.
- Selective dropping: ignore messages from specific nodes to stall their progress.
- Replay attacks: re-send old messages with valid signatures.
- Coalition: multiple faulty nodes coordinate votes.

## Where Byzantine Tolerance Matters

- **Blockchain** (Bitcoin, Ethereum): Nodes are anonymous and economically incentivized to cheat; no authority can identify honest nodes.
- **Safety-critical systems**: Aerospace, medical devices where hardware may flip bits or firmware may be buggy.
- **Federated systems**: Multi-organization consortia where participants cannot fully trust each other.

## Related Concepts

- [[Byzantine Generals Problem]] — the classic formulation
- [[Practical Byzantine Fault Tolerance]] — pBFT algorithm (Castro & Liskov, 1999)
- [[Consensus Problem]] — the goal BFT protocols achieve under Byzantine assumptions
- [[Crash Failure]] — simpler failure model (fail-stop)
