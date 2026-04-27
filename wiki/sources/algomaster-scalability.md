---
title: "AlgoMaster: Scalability"
type: source
tags: [system-design, scalability]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/scalability", "algomaster.io/learn/system-design/vertical-vs-horizontal-scaling"]
author: Ashish Pratap Singh
---

# Scalability

**Source:** AlgoMaster.io System Design — Scalability Chapter

## Definition

**Scalability** is the property of a system to handle a growing amount of load by adding resources to the system.

A system that can continuously evolve to support a growing amount of work is scalable.

---

## Types of Scaling

### Vertical Scaling (Scale Up)

Adding more power to existing machines — upgrading CPU, RAM, storage.

- **Simple** — No code changes needed
- **Limitations** — Physical hardware limits, single point of failure
- **Use case** — Quick fix for immediate needs

### Horizontal Scaling (Scale Out)

Adding more machines to distribute load across multiple servers.

- **More capacity** — Can scale infinitely
- **Better fault tolerance** — No single point of failure
- **Requires** — Load balancer, stateless services
- **Use case** — Large-scale systems

---

## Key Scaling Strategies

### 1. Make Services Stateless

**Stateful problem**: Session stored on Server 1 → all requests must go to same server → hotspots

**Stateless solution**: Session in shared store (Redis) → any server can handle any request

```java
// Bad (stateful)
class UserService {
    private Map<String, Session> sessions;  // Stored locally
}

// Good (stateless)
class UserService {
    private RedisTemplate<String, Session> sessionStore;  // Shared
}
```

### 2. Load Balancing

Distribute traffic across multiple servers using a load balancer.

- Adds/removes servers without redesign
- Automatically routes around failures
- Enables horizontal scaling

### 3. Auto-Scaling

Automatically adjust server count based on:
- CPU usage
- Memory usage
- Request count

### 4. Database Scaling

Databases are hardest to scale because of state.

**Patterns:**
- **Read replicas** — Separate read/write, replicate to replicas
- **Connection pooling** — Reuse connections (e.g., PgBouncer)
- **Sharding** — Partition data across multiple databases

### 5. Caching

Reduce database load with caches:
- Application caching
- CDN for static assets
- Redis/Memcached

### 6. Asynchronous Communication

Use message queues to decouple services:
- Handle traffic spikes
- Enable independent scaling

---

## Scaling Approaches by Stage

| Stage | Users | Approach |
|-------|-------|---------|
| 1 | 0-100 | Single server (monolith) |
| 2 | 100-1K | Separate database |
| 3 | 1K-10K | Load balancer + horizontal scaling |
| 4 | 10K-100K | Caching + read replicas |
| 5 | 100K-1M | Database sharding |
| 6 | 1M+ | Multi-region |

---

## Key Takeaways

1. **Start simple** — Don't over-engineer from start
2. **Identify bottlenecks** — Scale incrementally
3. **Stateless first** — Enable horizontal scaling
4. **Database is hard** — Plan for scaling early
5. **Combine strategies** — Vertical + horizontal