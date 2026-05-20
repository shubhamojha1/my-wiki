---
title: "Iterator Model"
type: concept
tags: [database, query, execution]
created: 2026-04-23
updated: 2026-05-20
---

# Iterator Model (Volcano / Pipeline Model)

The **iterator model** (also called the **Volcano model**, after Goetz Graefe's 1994 paper) is the classic pull-based query execution strategy. Every operator in the query plan exposes the same two-method interface:

```
Init()  — set up internal state, call Init() on children
Next()  → tuple | EOF
```

The root operator drives execution: the result consumer repeatedly calls `Next()` on the root, which recursively calls `Next()` on its children, pulling one tuple at a time up through the pipeline.

## Example Query Plan

```sql
SELECT name FROM employees WHERE dept = 'Engineering' ORDER BY name;
```

```
Sort.Next()
  └─ Filter(dept='Engineering').Next()
       └─ SeqScan(employees).Next()
```

Execution:
1. `Sort.Next()` → needs all input first (blocking); calls `Filter.Next()` repeatedly.
2. `Filter.Next()` → calls `SeqScan.Next()`, discards tuples where dept ≠ 'Engineering'.
3. `SeqScan.Next()` → reads next page if needed, returns next tuple.

## Characteristics

| Characteristic | Detail |
|----------------|--------|
| **Pull-based** | Parent drives execution; children are passive |
| **Streaming** | Non-blocking operators (Filter, Project) produce output immediately |
| **Composable** | Uniform interface lets operators compose arbitrarily |
| **Low memory** | Only one tuple in flight per non-blocking operator |
| **Overhead** | One virtual function call per tuple — costly at millions of tuples/sec |

## Operator Types

- **Pipeline-breakers** (blocking): Must consume all input before producing any output. Examples: Sort, Hash Join build phase, Hash Aggregation.
- **Non-blocking**: Produce output incrementally. Examples: Filter, Projection, Nested Loop Join.

## Variants

| Model | How it works | Advantage |
|-------|-------------|-----------|
| **Iterator (Volcano)** | Pull one tuple per `Next()` call | Simple, streaming |
| **Materialization** | Operator returns all tuples at once | Simpler operator implementation |
| **Vectorization (SIMD)** | `Next()` returns a batch of N tuples | Amortizes call overhead; CPU-cache friendly; used in DuckDB, Snowflake |
| **Push / Morsel-driven** | Producer pushes tuples to consumer | Better parallelism; used in HyPer, Umbra |

Modern analytical databases (DuckDB, Velox) use vectorized execution with batches of 1024–8192 tuples — retaining the pull interface but eliminating per-tuple overhead.

## Related Concepts

- [[Query Plan]] — the tree of iterator operators
- [[Vectorized Execution]] — the modern batch-oriented evolution
- [[Hash Join]] — common pipeline-breaking operator
- [[Sequential Scan]] — the leaf iterator reading pages from disk
