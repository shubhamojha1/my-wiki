---
title: "IP Hash"
type: concept
tags: [load-balancing, algorithm, session-persistence]
created: 2026-05-10
sources: ["algomaster-load-balancing-algorithms"]
---

# IP Hash

**IP Hash** uses a hash of the client's IP address to determine which server handles the request, ensuring the same client always routes to the same server (session persistence / sticky sessions).

## How It Works

1. Calculate hash of client IP address
2. Use modulo of hash against server list size to select server
3. Same IP → same hash → same server every time

## When to Use

- Applications requiring sticky sessions (session state stored in-memory on server)
- Stateful applications that don't use a shared session store

## Pros

- Simple to implement
- Guarantees session persistence without cookies
- No shared session store needed

## Cons

- Uneven load distribution if some IPs generate more traffic
- Server failures break hash mapping — requires reconfiguration
- Not suitable for stateless or horizontally-scaled systems

## Implementation

```python
import hashlib

class IPHash:
    def __init__(self, servers):
        self.servers = servers

    def get_next_server(self, client_ip):
        hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        return self.servers[hash_value % len(self.servers)]
```

## Related Concepts

- [[Load Balancing Algorithms]] — Parent concept
- [[Sticky Session]] — Session persistence pattern
- [[Round Robin]] — Stateless alternative
