---
title: "Least Response Time"
type: concept
tags: [load-balancing, algorithm]
created: 2026-05-10
sources: ["algomaster-load-balancing-algorithms"]
---

# Least Response Time

**Least Response Time** routes incoming requests to the server with the fastest response time, minimizing overall latency.

## How It Works

1. Monitor response time of each server
2. Assign new request to server with fastest response time
3. Update response time measurements after each request

## When to Use

- Servers with varying response times
- Environments where minimizing latency is critical
- Workloads where server performance fluctuates

## Pros

- Minimizes overall latency
- Adapts dynamically to changes in server performance
- Improves user experience with faster responses

## Cons

- Requires accurate measurement of response times (challenging in distributed systems)
- May not consider other factors like server load or connection count

## Implementation

```python
class LeastResponseTime:
    def __init__(self, servers):
        self.servers = servers
        self.response_times = {server: 0 for server in servers}

    def get_next_server(self):
        return min(self.response_times, key=self.response_times.get)

    def update_response_time(self, server, response_time):
        self.response_times[server] = response_time
```

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Least Connections]] — Connection-count-based alternative
- [[Round Robin]] — Simpler stateless alternative
