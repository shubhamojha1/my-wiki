---
title: "AlgoMaster: Latency vs Throughput vs Bandwidth"
type: source
tags: [system-design, performance]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/latency-vs-throughput"]
author: Ashish Pratap Singh
---

# Latency vs Throughput vs Bandwidth

**Source:** AlgoMaster.io System Design — Latency/Throughput/Bandwidth Chapter

## Highway Analogy

| Term | Analogy | What It Measures |
|------|--------|-----------------|
| **Bandwidth** | Number of lanes | Maximum capacity |
| **Throughput** | Cars per hour | Actual completed work |
| **Latency** | Travel time for one car | Delay per request |

---

## Latency

**Definition**: Time for a single request to travel from source to destination and back. Measures **delay**.

- Single request round-trip time
- Usually measured in milliseconds (ms)
- Lower is better

---

## Throughput

**Definition**: Amount of work completed per unit of time. Measures **volume**.

- Requests per second (RPS)
- Transactions per second (TPS)
- Higher is better

---

## Bandwidth vs Throughput

| Metric | Definition | Example |
|--------|------------|---------|
| Bandwidth | Maximum possible rate | 1 Gbps network link |
| Throughput | Actual achieved rate | 600 Mbps actual transfer |

**Key**: Throughput ≤ Bandwidth

Throughput is lower due to:
- Protocol overhead (headers, ACKs)
- Congestion and packet loss
- Processing limitations
- Inefficient resource utilization

---

## Bandwidth-Delay Product (BDP)

The amount of data that can be "in flight" at any moment.

```
BDP = Bandwidth × Latency
```

**Example**:
- Bandwidth: 1 Gbps = 125 MB/s
- Latency: 100ms (coast-to-coast US)
- BDP: 125 MB/s × 0.1s = 12.5 MB

If TCP window < BDP, you won't fully utilize bandwidth.

---

## The Bottleneck

> A system is only as fast as its slowest component.

Identify the bottleneck ( slowest part) and optimize there first.

---

## Key Takeaways

1. **Latency** = delay (one request)
2. **Throughput** = volume (requests/sec)
3. **Bandwidth** = max capacity
4. Throughput ≤ Bandwidth
5. Find and fix the bottleneck