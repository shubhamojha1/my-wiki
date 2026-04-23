---
title: "Map-Reduce"
type: concept
tags: [distributed, batch-processing, analytics]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Map-Reduce

**Definition:** Programming model for processing large datasets in parallel across distributed clusters, consisting of Map and Reduce phases.

## Origins

Google research paper (2004) popularized the pattern. Apache Hadoop provides the open-source implementation.

## Two-Phase Pattern

### Map Phase
```python
# Input: Large dataset
# Output: Key-value pairs
def map(document):
    for word in document:
        yield (word, 1)  # (word, count)
```

### Reduce Phase
```python
# Input: (word, [1, 1, 1, ...])
# Output: Aggregated results
def reduce(word, counts):
    yield (word, sum(counts))
```

## Flow

```
[Input Data]
    ↓
[Map: Extract and tag] → (key1, val1), (key2, val2), ...
    ↓ (shuffle: group by key)
[Shuffled Data]
    ↓
[Reduce: Aggregate] → Final results
    ↓
[Output]
```

## Use Cases

- **Social graph calculations** — "Suggested users" based on connections
- **Analytics reports** — Page views, revenue, engagement
- **Log processing** — Clickstreams, server logs
- **Text processing** — Word counts, inverted indices

## Why Use Map-Reduce?

Ad-hoc SQL queries work for small systems but fail when:
- Data volume requires database sharding
- Write load too high for analytical queries
- Separate query infrastructure needed
- Complex calculations beyond SQL expressiveness

## Hadoop Ecosystem

| Component | Purpose |
|-----------|---------|
| HDFS | Distributed file storage |
| MapReduce | Processing framework |
| Hive | SQL-like queries on Hadoop |
| HBase | NoSQL on Hadoop |
| Spark | In-memory MapReduce alternative |

## Tradeoffs

| Pros | Cons |
|------|------|
| Scales to petabytes | High latency (batch) |
| Fault tolerant | Complex development |
| Flexible | Not for real-time needs |

## Related Concepts

[[Offline Processing]], [[Hadoop]], [[Scalability]], [[Horizontal Scalability]]