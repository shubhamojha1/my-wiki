---
title: "Eventual Consistency"
type: concept
tags: [distributed-systems, consistency]
created: 2026-04-19
sources: [mixu-distributed-systems-book, strong-vs-eventual-consistency]
---

# Eventual Consistency

A consistency model guaranteeing that if no new updates are made, all replicas will eventually converge to the same value. There is no guarantee about how soon convergence happens — during propagation, different replicas may serve different versions.

## How It Works

1. Client sends write to a node; node acknowledges immediately
2. Updated value asynchronously propagated to other replicas
3. Reads from replicas not yet updated return stale data
4. Once all replicas receive the update, the system is fully consistent

This allows high availability and responsiveness even during network partitions.

## Real-World Example

On social media, you update your profile picture:
- You see the new photo immediately
- A friend across the world may see the old photo for a few seconds
- After replication completes, everyone sees the new photo

This temporary inconsistency is acceptable because correctness doesn't depend on everyone seeing the same thing simultaneously.

## Strengths

- Low latency — writes don't wait for global coordination
- High availability — nodes accept reads/writes independently during partitions
- Great scalability — ideal for globally distributed, read-heavy workloads

## Weaknesses

- Temporary staleness — clients may read outdated data
- Application complexity — must handle read-after-write inconsistency
- Conflict potential — concurrent writes to different replicas require reconciliation

## Client-Centric Variants (Stronger Eventual)

- **Causal Consistency** — Causally related operations seen in order by all processes
- **[[Read-Your-Writes Consistency|Read-Your-Writes]]** — Client always sees its own writes
- **Monotonic Reads** — Client never sees an older version after a newer one
- **Monotonic Writes** — Client's writes always executed in order

## Conflict Resolution Strategies

- **Last Write Wins (LWW)** — Timestamp-based; simple but can lose data
- **[[CRDT]]** — Conflict-Free Replicated Data Types; guaranteed convergence via commutative operations
- **Custom merge logic** — Application-specific reconciliation

## Use Cases

- Social media metrics (likes, shares, view counts)
- Analytics and tracking (page visits, click events)
- Recommendation systems
- DNS caching (worldwide propagation delay is acceptable)
- CDNs (static assets eventually updated at edge locations)
- Shopping carts (conflict resolution merges items from different devices)

## Related

- [[Consistency Model]] — The broader contract
- [[CAP Theorem]] — Why eventual consistency trades C for A and P
- [[CRDT]] — Mathematical guarantee of convergence
- [[Consensus]] — What strong consistency requires
- [[Dynamo]] — Amazon's eventually consistent key-value store (R+W > N)
