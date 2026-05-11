---
title: "MongoDB Atlas Architecture Center"
type: source
tags: [mongodb, atlas, well-architected, reliability, performance]
created: 2026-05-11
sources: [mongodb-atlas-architecture]
---

# MongoDB Atlas Architecture Center

**URL:** https://www.mongodb.com/docs/atlas/architecture/current/
**Published:** 2026 (current version v20260330)

## Summary

MongoDB's Well-Architected Framework for Atlas deployments — official guidance across 5 pillars (Operational Efficiency, Security, Reliability, Performance, Cost Optimization) with deployment templates, automation examples, and best practices from large-scale enterprise production deployments.

## Key Concepts Covered

- **5-pillar framework**: Operational Efficiency, Security, Reliability, Performance, Cost Optimization
- **Shared Responsibility Model**: MongoDB manages platform security/operations; customers manage deployment configuration and data policies
- **Reliability foundations**: deployment HA architecture + DR plan with RTO/RPO targets
- **Replica sets**: default 3-node across AZs, automatic failover in seconds, retryable writes
- **RPO/RTO definitions**: RPO = max data loss (time-based), RTO = max acceptable downtime
- **Availability**: "five nines" = ~5.25 min downtime/year
- **Scalability**: auto-scaling (compute + storage), sharding (ranged/hashed/zoned), vertical tier upgrades with zero downtime
- **Performance Advisor**: automated index recommendations
- **Data tiering**: archive to low-cost storage with queryable access, TTL indexes for auto-expiry
- **Write concern**: `majority` as default, ensures cross-node replication before acknowledgment
- **Failover testing**: simulate primary failover and regional outages
- **Deployment paradigms**: single-region, multi-region, multi-cloud topologies
- **IaC support**: Atlas CLI, Terraform, Kubernetes Operator
