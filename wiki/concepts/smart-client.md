---
title: "Smart Client"
type: concept
tags: [infrastructure, load-balancing]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Smart Client

**Definition:** A client library that implements load balancing logic directly, managing a pool of service hosts and distributing requests across them.

## Why Developers Choose It

Developers naturally gravitate toward smart clients because:
- They are **developers**, so they write software to solve problems
- Smart clients **are software**, making it a familiar approach
- It seems like an elegant solution

## What a Smart Client Does

```python
class SmartDBClient:
    def __init__(self, host_pool):
        self.hosts = host_pool
        self.failed_hosts = set()
    
    def query(self, sql):
        # Find a healthy host
        host = self.select_host()
        
        # Try to execute
        try:
            return host.execute(sql)
        except ConnectionError:
            # Mark host as failed
            self.failed_hosts.add(host)
            # Retry with another host
            return self.query(sql)
    
    def select_host(self):
        # Round-robin or weighted selection
        # Avoid hosts in failed_hosts
        # Detect and track recovered hosts
```

## Responsibilities

A smart client must handle:
- **Host selection** — Round-robin, weighted, random
- **Health detection** — Detect downed hosts
- **Failure avoidance** — Don't route to failed hosts
- **Recovery detection** — Re-add recovered hosts
- **Pool management** — Add/remove hosts dynamically

## Tradeoffs

| Pros | Cons |
|------|------|
| No extra infrastructure | Complex to implement correctly |
| Works with any service | Must be implemented per-client |
| High performance | Hard to get edge cases right |
| No single point of failure | Testing is difficult |

## When to Use

- Multiple clients need the same load balancing
- You have the resources to implement and maintain it properly
- Infrastructure costs must be minimized

## When Not to Use

- Simplicity is paramount
- Few clients/connections
- Team lacks capacity for maintenance

## Related Concepts

[[Load Balancing]], [[Software Load Balancer]], [[Hardware Load Balancer]]