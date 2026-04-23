---
title: "Introduction to Architecting Systems for Scale"
type: source
tags: [infrastructure, architecture, scalability]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Introduction to Architecting Systems for Scale

**Author:** Will Larson  
**Published:** April 4, 2011  
**Source:** [lethain.com](https://lethain.com/introduction-to-architecting-systems-for-scale/)

## Summary

This foundational article by Will Larson (Digg, Yahoo!) documents core scalability architecture patterns learned through production experience. It covers four pillars essential for building systems that scale: load balancing, caching, offline processing, and platform layers.

## Key Takeaways

### Load Balancing

- Enables **horizontal scalability** — linear capacity increase with hardware
- Enables **redundancy** — graceful degradation when servers fail
- Three layers need balancing: user→web, web→platform, platform→database
- Three approaches: smart clients (complex, application-level), hardware (expensive, NetScaler), software (HAProxy, best starting point)

### Caching

- **Application caching**: explicit code integration with read-through pattern
- **Database caching**: transparent performance gains via configuration tuning
- **In-memory caches** (Memcached, Redis): RAM orders of magnitude faster than disk
- **CDNs**: static media distribution with geographic proximity
- **Cache invalidation**: write-through (update cache on write) or delete-and-repopulate (read-through)
- LRU (Least Recently Used) eviction keeps "hot" data in cache

### Offline Processing

- **Message queues** (RabbitMQ): decouple slow processing from user requests
- Two patterns: pure offline (inform user, poll) or optimistic inline (appear complete, finish async)
- Separate worker pools allow targeting resources to actual bottlenecks
- **Cron** for periodic tasks; trigger queue workers instead of direct execution
- **Map-reduce** (Hadoop/Hive/HBase) for large-scale data processing

### Platform Layer

- Separates web applications from backend services
- Enables independent scaling of components
- Allows specialization (SSD for DB servers, CPU for app servers)
- Enables infrastructure reuse across web, API, mobile products
- Organizes teams around platform/implementation split

## Color Convention

The article uses a diagram convention:
- **Green**: external client requests
- **Blue**: code running in containers (web apps, scripts)
- **Red**: infrastructure (databases, caches, queues)

## Related Concepts

[[Load Balancing]], [[Horizontal Scalability]], [[Redundancy]], [[Caching]], [[Application Caching]], [[Database Caching]], [[In-Memory Cache]], [[CDN]], [[Cache Invalidation]], [[Read-Through Cache]], [[Write-Through Cache]], [[Offline Processing]], [[Message Queue]], [[Scheduling Periodic Tasks]], [[Map-Reduce]], [[Platform Layer]]