---
title: "Druva: Failover Definition and FAQs"
type: source
tags: [system-design, failover, high-availability]
created: 2026-04-27
sources: ["druva.com/learning-center/glossary/what-is-a-failover-definition-and-related-faqs"]
---

# Failover

**Source:** Druva Learning Center — Failover Definition

## Definition

**Failover** is the ability to switch automatically and seamlessly to a backup system when a primary component fails. The standby system takes over to minimize or eliminate impact on users.

---

## How Failover Works

### Heartbeat Mechanism

Primary and standby servers connected via heartbeat. As long as heartbeat continues:
- Primary handles all traffic
- Standby remains idle, monitoring

When heartbeat fails:
- Standby detects failure
- Standby takes over operations
- Alerts technician to repair primary

---

## Types of Failover Configurations

### Active-Active

- Multiple servers run same service simultaneously
- All nodes active, share workload
- Load balancing across nodes

**Benefits:**
- No single node overload
- Better throughput
- Zero downtime if node fails

**Trade-off:** If node fails, remaining must handle full load

### Active-Passive (Active-Standby)

- One server active, one on standby
- Passive node ready but idle
- Takes over only when active fails

**Benefits:**
- Lower resource use
- Simpler configuration
- Standby always ready

**Trade-off:** Short delay during switchover

---

## Failover Cluster

A set of servers providing fault tolerance (FT), high availability (HA), or continuous availability (CA).

- If one server fails → workload transfers to another
- Prevents downtime
- HA: minimal downtime, no data loss
- CA: zero downtime

---

## Failover vs Failback

| Term | Definition |
|------|------------|
| Failover | Switch to backup during failure |
| Failback | Return to primary after recovery |

---

## Key Takeaways

1. **Automatic switch** — No manual intervention needed
2. **Heartbeat** — Monitors primary health
3. **Active-Active** — Better performance, shared load
4. **Active-Passive** — Simpler, standby ready
5. **Cluster** — Multiple servers for HA/FT