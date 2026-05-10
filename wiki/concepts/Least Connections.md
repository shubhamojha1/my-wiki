---
title: "Least Connections"
type: concept
tags: [load-balancing, algorithm]
created: 2026-04-28
sources: ["algomaster-load-balancing-algorithms"]
---

# Least Connections

**Least Connections** routes to the server with fewest active connections.

## How It Works

1. Track active connections per server
2. New request goes to server with fewest active connections
3. Release connection when request completes (decrement count)

## Implementation

```python
class LeastConnections:
    def __init__(self, servers):
        self.connections = {server: 0 for server in servers}

    def get_next_server(self):
        server = min(self.connections, key=self.connections.get)
        self.connections[server] += 1
        return server

    def release_connection(self, server):
        if self.connections[server] > 0:
            self.connections[server] -= 1
```

## Use Cases

- Varying request durations (some fast, some slow)
- Similar server capabilities
- Workloads where connection count approximates actual load

## Pros

- Dynamic load distribution adapting to current load
- Prevents any single server from becoming overloaded

## Cons

- May not be optimal if servers have different processing capabilities
- Requires tracking active connections per server
- Assumes connection count correlates with actual load

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Least Response Time]] — Response time-based version