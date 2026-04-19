---
title: "Redis Sentinel"
type: concept
tags: [redis, failover, monitoring]
created: 2026-04-20
sources: [redis-cluster-architecture]
---

Redis Sentinel provides monitoring, notification and automatic failover for Redis Master-Slave deployments.

## Responsibilities

- **Monitoring**: Continuously check master and slave availability
- **Notification**: Alert on failures via Pub/Sub
- **Automatic Failover**: Promote slave to master when master fails
- **Configuration Provider**: Provide current master address to clients

## How It Works

1. Sentinels monitor master health
2. When master fails, sentinel detects failure
3. Sentinels vote and elect new master
4. Remaining slaves redirected to new master
5. Clients notified of new master address

## Architecture Pattern

Typically:
- Multiple sentinel processes (odd number)
- Quorum-based decision making
- Works with Master-Slave replication

## Limitations

- Does not provide automatic sharding
- Single master still handles all writes
- Scaling limited by master capacity