---
title: "Disaster Recovery (DR)"
type: concept
tags: [disaster-recovery, business-continuity, backup]
created: 2026-05-11
sources: [gcp-disaster-recovery]
---

# Disaster Recovery (DR)

**Disaster recovery** is an organization's ability to restore access and functionality to IT infrastructure after a disaster event. It is a subset of **business continuity**, focused specifically on IT systems recovery.

## DR Planning Steps

1. **Risk assessment** — Identify threats and vulnerabilities
2. **Business impact analysis (BIA)** — Determine impact on critical functions
3. **DR planning** — Document procedures, roles, communication protocols
4. **Implementation** — Set up backup/replication, failover mechanisms
5. **Testing & maintenance** — Validate plan, update for changes

## 3-2-1 Backup Rule

- **3** copies of data
- **2** different storage media
- **1** copy offsite

## DR Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Backups** | Data copied to secondary location | Archiving, compliance |
| **BaaS** | Third-party manages backups | SMBs without DR resources |
| **DRaaS** | Third-party hosts + orchestrates DR | Full DR outsourcing |
| **Snapshots** | Point-in-time data replication | Quick recovery from corruption |
| **Virtual DR** | Failover to virtualized environment | Fast resumption of operations |
| **DR sites** | Physical secondary data center | Strict compliance requirements |

## Recovery Elements

- **Preventive**: Backups, monitoring, security (reduce disaster likelihood)
- **Detective**: Real-time monitoring, anomaly detection (trigger response)
- **Corrective**: Recovery procedures, failover mechanisms (restore operations)

## Related

- [[RPO and RTO]] — Key DR metrics
- [[Data Replication]] — DR relies on replication
- [[High Availability]] — Related but HA handles smaller-scale failures
- [[Backup]] — Data backup as a DR component
