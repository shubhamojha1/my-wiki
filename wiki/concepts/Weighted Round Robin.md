---
title: "Weighted Round Robin"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Weighted Round Robin

**Weighted Round Robin** assigns weights to servers based on capacity.

## How It Works

1. Each server has a weight (processing power)
2. Higher weight = proportionally more requests
3. Algorithm iterates weights to maintain desired distribution ratio

## Implementation

```python
class WeightedRoundRobin:
    def __init__(self, servers, weights):
        self.servers = servers
        self.weights = weights
        self.current_weight = 0
        self.current_index = -1

    def get_next_server(self):
        while True:
            self.current_index = (self.current_index + 1) % len(self.servers)
            if self.current_index == 0:
                self.current_weight -= 1
                if self.current_weight <= 0:
                    self.current_weight = max(self.weights)
            if self.weights[self.current_index] >= self.current_weight:
                return self.servers[self.current_index]
    ```

## Example

- Server1 weight: 5
- Server2 weight: 1
- Server3 weight: 1

Server1 receives 5x the traffic of Server2 or Server3.

## Use Cases

- Heterogeneous server fleet with different capacities
- When you want capacity-aware distribution
- Migrating to newer, more powerful hardware alongside older servers

## Pros

- Balances load according to server capacity
- More efficient resource utilization

## Cons

- Does not consider current server load or response time
- Weights must be manually configured and tuned

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Round Robin]] — Basic version without weights