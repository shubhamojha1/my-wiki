---
title: "Failover"
type: concept
tags: [system-design, high-availability, fault-tolerance]
created: 2026-04-27
sources: ["druva.com/learning-center/glossary/what-is-a-failover-definition-and-related-faqs"]
---

# Failover

Automatic switch to backup system when primary fails.

## How It Works

1. Primary + standby connected via heartbeat
2. Heartbeat fails → standby detects
3. Standby takes over operations
4. Alerts sent for repair

## Configurations

### Active-Active
- Multiple servers active simultaneously
- Load balanced
- Zero downtime on failure

### Active-Passive
- One active, one standby
- Switchover on failure
- Brief delay possible

## Related

[[Redundancy]], [[High Availability]], [[Fault Tolerance]], [[Single Point of Failure (SPOF)]]