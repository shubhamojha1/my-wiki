---
title: "Iterator Model"
type: concept
tags: [database, query, execution]
created: 2026-04-23
---

# Iterator Model

The **iterator model** (also **Volcano model**) is a pull-based query execution model where each operator implements `Next()` to return one tuple.

## How It Works

- Each operator has `Init()` and `Next()` methods
- Parent calls `Next()` on children to get tuples
- Data flows upward: leaves → root
- Returns tuple or "no more tuples" signal

## Characteristics

- **Pull-based**: Parent drives execution
- **Composable**: Easy to combine operators
- **Streaming**: Produces output as available
- **Overhead**: Function call per tuple

## Variants

- **Materialization**: Child returns all results at once
- **Vectorization**: Return batches, not single tuples

## Related

- [[Query Plan]] — Tree of iterators
- [[Sequential Scan]] — Leaf iterator
- [[Query Execution]] — Where iterators are used