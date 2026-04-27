---
title: "AlgoMaster: CAP Theorem"
type: source
tags: [system-design, distributed-systems, consistency]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/cap-theorem"]
author: Ashish Pratap Singh
---

# CAP Theorem

**Source:** AlgoMaster.io System Design — CAP Theorem Chapter

## Definition

A distributed data store **cannot** simultaneously provide all three guarantees:

| Property | Meaning |
|----------|---------|
| **Consistency (C)** | Every read receives most recent write or error |
| **Availability (A)** | Every request gets non-error response |
| **Partition Tolerance (P)** | System works despite network failures |

---

## The Trade-Off

> During a network partition, must choose between **Consistency** and **Availability**.

```
No partition: CA
With partition: Choose CP or AP
```

Real systems always face partitions → effectively choose 2 of 3.

---

## CP Systems (Consistency + Partition Tolerance)

- Sacrifice availability during partition
- Example: MongoDB, HBase, ZooKeeper
- Use when: Stale data causes problems (banking, inventory)

## AP Systems (Availability + Partition Tolerance)

- Always respond, may return stale data
- Example: Cassandra, DynamoDB
- Use when: Availability matters more (social feeds, analytics)

---

## Practical Considerations

1. **Partitions are inevitable** — Networks fail
2. **Choose based on use case** — Not all systems need strong consistency
3. **Tunable consistency** — Many systems allow tuning
4. **Not all-or-nothing** — Quorum, read/write replicas

## Related

- Eventual consistency
- Strong consistency
- Quorum reads/writes

---

## Key Takeaways

1. Cannot have all three during partition
2. CP → consistency over availability
3. AP → availability over consistency  
4. Choose based on application needs