---
title: "Round Robin"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Round Robin

A **Round Robin** load balancing algorithm that sequentially distributes requests across servers.

## How It Works

1. Request goes to first server
2. Next request goes to second server
3. Loops back to first after last server

## Implementation

```python
class RoundRobin:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = -1

    def get_next_server(self):
        self.current_index = (self.current_index + 1) % len(self.servers)
        return self.servers[self.current_index]
```

## Use Cases

- All servers have similar capacity — homogeneous fleet
- Simple, stateless workloads
- When simplicity and even distribution matter more than optimization

## Pros

- Simple to implement and understand
- Even distribution under uniform load

## Cons

- Does not consider server load or response time
- Inefficient for different server capacities

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Weighted Round Robin]] — Capacity-aware version