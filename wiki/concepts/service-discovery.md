---
title: "Service Discovery"
type: concept
tags: [distributed-systems, microservices, networking]
created: 2026-05-11
sources: [algomaster-service-discovery]
---

# Service Discovery

**Service discovery** is a mechanism that allows services in a distributed system to dynamically find and communicate with each other without hardcoded network locations.

## Service Registry

A central registry stores records for each service instance:

| Field | Description |
|-------|-------------|
| Service name | Logical identifier (e.g., `payment-service`) |
| IP:Port | Network address of the instance |
| Status | Health state (up/down/starting) |
| Metadata | Version, environment, region, tags |
| Health info | Last check timestamp, result |
| Load balancing | Weights, priorities |

## Registration Options

| Method | Description | Example |
|--------|-------------|---------|
| **Manual** | Operator adds service details by hand | Simple, not dynamic |
| **Self-registration** | Service registers itself on startup, sends periodic [[Heartbeat]] | Eureka client |
| **Sidecar (3rd-party)** | External agent detects and registers the service | Istio sidecar |
| **Orchestrator** | Platform auto-registers (Kubernetes detects deployment → updates DNS) | [[Kubernetes]] |
| **Config management** | Chef/Puppet/Ansible manage registration | Chef |

## Models

### Client-Side Discovery
The client queries the registry directly, selects an instance (via load balancing algorithm), and connects.

- **Pro**: No extra network hop, flexible load balancing
- **Con**: Client must implement discovery logic, registry protocol changes affect clients
- **Example**: Netflix Eureka

### Server-Side Discovery
The client sends requests to a load balancer or API gateway, which queries the registry and routes.

- **Pro**: Centralized logic, simpler clients
- **Con**: Extra network hop, load balancer can be SPOF
- **Example**: AWS ELB + service registry

## Best Practices

- Replicate the registry for HA
- Use health checks to deregister failing instances
- Cache registry lookups to reduce load
- Use clear naming conventions with versioning (`payment-service-v1`)
- Automate registration in dynamic environments

## Related

- [[Heartbeat]] — Signals used in self-registration for liveness
- [[API Gateway]] — Often used in server-side discovery
- [[Load Balancer]] — Routes to discovered instances
- [[Kubernetes]] — Built-in service discovery via DNS
