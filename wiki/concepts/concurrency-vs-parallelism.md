---
title: "Concurrency vs Parallelism"
type: concept
tags: [concurrency, parallelism]
created: 2026-04-24
sources: [introduction-to-concurrency]
---

# Concurrency vs Parallelism

These terms are often used interchangeably but represent distinct concepts.

## Core Distinction

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| **Definition** | Structuring a program to handle multiple tasks | Actually executing multiple tasks |
| **Goal** | Make progress on multiple tasks | Speed up by executing simultaneously |
| **Execution** | Interleaved on single core | Simultaneous on multiple cores |
| **Focus** | Dealing with multiple things at once | Doing multiple things at once |

## Analogy

- **Concurrency** = One barista handling multiple drink orders by starting each drink then switching while waiting for espresso
- **Parallelism** = Multiple baristas each making a drink simultaneously

## In Practice

A concurrent program may run on a single CPU core with time-slicing (context switching), achieving interleaved execution. A parallel program explicitly uses multiple CPU cores.

```python
# Concurrent (interleaved on single core)
async def fetch_all(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)

# Parallel (simultaneous on multiple cores)  
def fetch_all(urls):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(fetch, urls))
```

## When Each Applies

- **Concurrency**: I/O-bound tasks (network, disk) — waiting dominates, use async/await
- **Parallelism**: CPU-bound tasks (computation) — use multiple cores

## Related

- [[Processes vs Threads]] — Units enabling concurrency/parallelism
- [[Introduction to Concurrency]]