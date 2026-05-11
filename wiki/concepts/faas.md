---
title: "FaaS"
type: concept
tags: [serverless, cloud, architecture, compute]
created: 2026-05-11
sources: ["algomaster-serverless-architecture"]
aliases: ["Functions as a Service"]
---

# FaaS (Functions as a Service)

A cloud computing paradigm that enables developers to deploy individual **functions** — discrete, single-purpose units of code — that are executed in response to events, with the cloud provider managing all underlying infrastructure.

## Core Concept

FaaS is the execution model at the heart of [[Serverless Architecture]]. Developers write functions that are triggered by events (HTTP requests, file uploads, database changes, scheduled tasks) and the cloud provider automatically provisions compute resources, executes the function, scales it based on demand, and releases resources when done.

## Key Characteristics

- **Event-Driven** — functions respond to specific triggers
- **Stateless** — no persistent state between invocations
- **Ephemeral** — short-lived execution; terminate after completion
- **Auto-Scaling** — provider runs multiple parallel instances on demand
- **Pay-per-Invocation** — billed per execution, duration, and memory allocated

## Examples

| Provider | Service |
|----------|---------|
| AWS | Lambda |
| Azure | Azure Functions |
| Google Cloud | Cloud Functions |
| Open Source | Knative, OpenFaaS |

## Limitations

- Execution time limits (e.g., 15 minutes for AWS Lambda)
- Cold start latency on first invocation
- Memory and CPU constraints per function
- No persistent local state

## See Also

- [[Serverless Architecture]]
- [[Microservices]]
- [[Event-Driven Architecture]]
