---
title: "Wiki Index"
type: index
tags: []
created: 2026-04-05
---

# LLM Wiki

A persistent knowledge base for LLM inference systems and distributed databases.

## Sources

- [[Event-Driven Architecture (EDA): A Complete Introduction]] — Confluent: comprehensive EDA guide covering patterns, tech stack, advantages (2026)
- [[Peer-To-Peer Networks: Features, Pros, and Cons]] — Spiceworks: P2P network architecture, features, trade-offs, and applications (2023)
- [[System Design: Top 15 Trade-Offs]] — AlgoMaster: catalog of 15 fundamental system design trade-offs with examples (2024)
- [[System Design: Vertical vs Horizontal Scaling]] — AlgoMaster: detailed guide on scaling up vs scaling out, pros/cons, decision framework (2024)
- [[Concurrency vs Parallelism]] — AlgoMaster: distinguishing managing multiple tasks from executing simultaneously, with examples and code (2024)
- [[Long Polling vs WebSockets]] — AlgoMaster: comparing real-time communication techniques with decision framework and alternatives (2025)
- [[Batch vs Stream Processing - What's the Difference?]] — AlgoMaster: batch and stream processing workflows, challenges, frameworks, and decision guidance (2024)
- [[Stateful vs. Stateless Architecture]] — AlgoMaster: comparing stateful and stateless designs with patterns, trade-offs, and hybrid approach (2025)
- [[Strong vs. Eventual Consistency]] — AlgoMaster: consistency models, replication lag mechanics, client-centric variants, and decision framework (2025)

- [[OSI Model]] — AlgoMaster: 7-layer network framework, encapsulation (2026)
- [[IP Address]] — AlgoMaster: IPv4, IPv6, CIDR, subnetting, NAT (2026)
- [[DNS]] — AlgoMaster: domain name resolution, DNS records, caching (2026)
- [[Proxy vs Reverse Proxy]] — AlgoMaster: forward proxy, reverse proxy, load balancing (2026)
- [[HTTP and HTTPS]] — AlgoMaster: HTTP methods, TLS handshake, HTTP/2, HTTP/3 (2025)
- [[TCP vs UDP]] — AlgoMaster: TCP reliable vs UDP fast (2025)
- [[Load Balancing Algorithms]] — AlgoMaster: round robin, least connections, health checks (2024)
- [[Checksums]] — AlgoMaster: CRC, MD5, SHA, error detection (2025)
- [[Publish-Subscribe (Pub/Sub)]] — AlgoMaster: async messaging, broker, topics (2026)
- [[Message Queues]] — AlgoMaster: broker, P2P/Pub/Sub/DLQ, async processing (2025)
- [[Change Data Capture (CDC)]] — AlgoMaster: timestamp/trigger/log-based CDC, Debezium, Kafka (2025)
- [[API]] — AlgoMaster: APIs, REST, GraphQL, gRPC (2025)
- [[API Gateway]] — AlgoMaster: central entry point, rate limiting (2024)
- [[REST vs GraphQL]] — AlgoMaster: REST vs GraphQL comparison (2025)
- [[Kafka: A Distributed Messaging System for Log Processing]] — Summary of the original Kafka paper from LinkedIn (2011)
- [[Language Models are Few-Shot Learners (GPT-3)]] — The GPT-3 paper demonstrating scaling improves few-shot learning (2020)
- [[Distributed Systems: for fun and profit]] — Mixu's comprehensive intro to distributed systems fundamentals
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Caltech course intro covering GPU architecture, CUDA, and parallel computing fundamentals
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — GPU internals: SIMD vs SIMT, thread hierarchy, warp divergence, streaming multiprocessors
- [[CS179 Recitation 1 - GPU Overview and Prefix Sum]] — Recitation covering RTX 5090, prefix sum algorithm, VS Code remote setup
- [[Best GPUs for Deep Learning in 2023]] — Tim Dettmers' comprehensive guide on GPU specs, Tensor Cores, precision formats, and recommendations
- [[CS 179: GPU Memory Systems - Lecture 4]] — GPU memory hierarchy, coalescing, bank conflicts, register spilling, computational intensity
- [[CS 179: Synchronization and ILP - Lecture 5]] — CUDA synchronization, atomic operations, ILP, warp scheduler, occupancy, floating point precision
- [[CS 179: Matrix Transpose Optimization - Lecture 6]] — GPU matrix transpose using tiling, shared memory, and coalesced access
- [[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness]] — Stanford paper: IO-aware exact attention with tiling and recomputation, 3-7x speedup
- [[FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]] — Tri Dao 2023: 2x faster than FlashAttention, 73% theoretical max, Split-Q warp partitioning
- [[FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision]] — Tri Dao 2024: 740 TFLOPs/s (75% util), FP8 ~1.2 PFLOPs/s, warp specialization, GEMM-softmax overlap
- [[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]] — Google: 9.1% byte miss reduction, 1.8% CPU overhead, impact distribution analysis
- [[Dynamo: Amazon's Highly Available Key-Value Store]] — SOSP 2007: eventual consistency, vector clocks, sloppy quorum, hinted handoff
- [[CMU 15-445: Relational Model & Algebra - Lecture 1]] — CMU database systems intro: relational model, relational algebra, SQL fundamentals
- [[CMU 15-445: Modern SQL - Lecture 2]] — Modern SQL: aggregates, GROUP BY, window functions, CTEs, recursive CTEs
- [[CMU 15-445: Database Storage I - Lecture 3]] — Disk-oriented DBMS architecture, database pages, heap files, storage manager, buffer pool
- [[CMU 15-445: Memory Management & Buffer Pools - Lecture 4]] — Buffer pool organization, page table, replacement policies, memory-mapped I/O
- [[CMU 15-445: Database Storage II - Lecture 5]] — Slotted pages, index-organized tables, log-structured storage, B+Tree
- [[CMU 15-445: Storage Models & Compression - Lecture 6]] — Row stores vs column stores, OLTP vs OLAP, compression techniques
- [[CMU 15-445: Hash Tables - Lecture 7]] — Static and dynamic hash tables: linear probe, chained, extendible, linear hashing
- [[CMU 15-445: B+Tree Indexes - Lecture 8]] — B+Tree properties, node structure, insert/delete, composite indexes
- [[CMU 15-445: Indexes & Filters II - Lecture 9]] — Advanced index topics: inverted index, vector index, partial/covering indexes
- [[CMU 15-445: Index Concurrency Control - Lecture 10]] — Latches vs locks, reader-writer latch, latch crabbing protocol
- [[CMU 15-445: Query Processing - Lecture 11]] — Query plans, execution models, sequential scan, index scan
- [[CMU 15-445: Join Algorithms - Lecture 12]] — Nested loop, sort-merge, hash join algorithms
- [[A Survey of Deep Learning: From Activations to Transformers]] — Survey: activations, normalization, transformers, self-supervised learning
- [[Introduction to Architecting Systems for Scale]] — Will Larson (Digg/Yahoo!): load balancing, caching, offline processing, platform layer
- [[REST API Design Best Practices]] — Abdul Rafee Wahab: 13 best practices for REST API design (2021)
- [[AlgoMaster: Rate Limiting Algorithms]] — AlgoMaster: 5 algorithms with code (Token Bucket, Leaky Bucket, Fixed/Sliding Window) (2024)
- [[AlgoMaster: Idempotency]] — AlgoMaster: idempotent operations, keys, deduplication stores (2024)
- [[AlgoMaster: Webhooks]] — AlgoMaster: event-driven push notifications, receiver setup, scalable pipeline (2025)
- [[Classes and Objects]] — AlgoMaster: classes as blueprints, objects as instances, practical order management example
- [[12 OOP Concepts Every Developer Should Know]] — AlgoMaster: 12 OOP concepts covering building blocks, four pillars, and object relationships
- [[Enums]] — AlgoMaster: enumerations with properties/methods, state machine pattern for order processing
- [[Interfaces]] — AlgoMaster: contracts, payment gateway and notification service examples, SOLID principles
- [[Encapsulation]] — AlgoMaster: access modifiers, getters/setters, BankAccount and PaymentProcessor examples
- [[Abstraction]] — AlgoMaster: abstract classes, interfaces, public APIs, media player example
- [[Inheritance]] — AlgoMaster: extends, notification system example, method overriding
- [[Polymorphism]] — AlgoMaster: overloading vs overriding, runtime vs compile-time
- [[AlgoMaster: Association]] — AlgoMaster: "knows-about" relationships, UML, multiplicity types, hospital example
- [[AlgoMaster: Aggregation]] — AlgoMaster: "has-a" with independent parts, UML hollow diamond
- [[AlgoMaster: Dependency]] — AlgoMaster: temporary "uses-a", UML dashed arrow
- [[AlgoMaster: Composition]] — AlgoMaster: strong "owns-a" with dependent lifecycle, UML filled diamond
- [[AlgoMaster: DRY Principle]] — AlgoMaster: "don't repeat yourself", single source of truth
- [[AlgoMaster: YAGNI Principle]] — AlgoMaster: "you aren't gonna need it", build for now not later
- [[AlgoMaster: KISS Principle]] — AlgoMaster: "keep it simple", avoid over-engineering
- [[AlgoMaster: SOLID Principles]] — AlgoMaster: SRP, OCP, LSP, ISP, DIP with code examples
- [[AlgoMaster: Scalability]] — AlgoMaster: vertical vs horizontal scaling, stateless services, load balancing
- [[AlgoMaster: Availability]] — AlgoMaster: redundancy, active-active, circuit breakers
- [[AlgoMaster: Reliability]] — AlgoMaster: fault tolerance, graceful degradation
- [[AlgoMaster: Single Point of Failure (SPOF)]] — AlgoMaster: eliminating SPOFs, redundancy strategies
- [[AlgoMaster: Latency vs Throughput vs Bandwidth]] — AlgoMaster: delay vs volume vs capacity
- [[AlgoMaster: Consistent Hashing]] — AlgoMaster: hash ring, virtual nodes, minimal remapping
- [[AlgoMaster: CAP Theorem]] — AlgoMaster: C/A/P tradeoff, CP vs AP systems
- [[Druva: Failover]] — Druva: heartbeat, active-active vs active-passive, clusters
- [[CockroachDB: Fault Tolerance]] — CockroachDB: quorum, replication factor, automatic recovery
- [[algomaster-Introduction to Concurrency]] — AlgoMaster: concurrency fundamentals, benefits, challenges (2026)
- [[algomaster-Concurrency vs Parallelism]] — AlgoMaster: restaurant analogy, levels of parallelism (2026)
- [[algomaster-Processes vs Threads]] — AlgoMaster: context switching, fault isolation (2026)
- [[algomaster-Thread Lifecycle and States]] — AlgoMaster: NEW, RUNNABLE, BLOCKED, WAITING, TERMINATED (2026)
- [[OSI Model]] — AlgoMaster: 7-layer framework, encapsulation, OSI vs TCP/IP (2026)
- [[algomaster-Race Conditions and Critical Sections]] — AlgoMaster: read-modify-write, check-then-act (2026)
- [[AlgoMaster: WebSockets]] — AlgoMaster: full-duplex real-time protocol, handshake, use cases (2024)
- [[AlgoMaster: Client-Server Architecture]] — AlgoMaster: computing model, tiers (1T to NT), scaling techniques (2025)
- [[Hashmap: The What, Why, and How of a Microservices Architecture]] — Hashmap: microservices definition, benefits, 8-key implementation framework (2018)
- [[AlgoMaster: Serverless Architecture]] — AlgoMaster: serverless/FaaS model, benefits, challenges, use cases, best practices (2026 draft)
- [[AWS Caching Overview]] — AWS: 5-layer caching stack, ElastiCache, CloudFront, Route 53 (2026)
- [[System Design Primer: Cache]] — Donne Martin: 5 cache locations, 2 caching levels, 4 update strategies (2026)
- [[HTTP Caching In-Depth Part 1]] — Léo Jacquemin: 3 HTTP caching actors, latency bottleneck, request anatomy (2018)
- [[HTTP Caching: Cache-Control & Vary]] — Léo Jacquemin: cache-control directives, Vary header, 4-outcome decision tree (2019)
- [[Two Hard Things]] — Martin Fowler: Phil Karlton's "cache invalidation and naming things" quote (2009)
- [[Cache Invalidation Strategies]] — CoVaib DeepLearn: purge/ban, 6 strategies, 3 advanced patterns, stampede (2025)
- [[Broadcasting Live Video to Millions]] — Facebook Engineering: multi-layer edge cache, request coalescing, thundering herd, RTMP (2015)
- [[RFC 2308: DNS NCACHE]] — Standards Track: negative caching of DNS queries, NXDOMAIN/NODATA, SOA MINIMUM field (1998)
- [[AlgoMaster: ACID Transactions]] — Ashish Pratap Singh: atomicity, consistency, isolation, durability, WAL, MVCC (2025)
- [[AlgoMaster: SQL vs NoSQL]] — Ashish Pratap Singh: 7 differences across data model, schema, scalability, query, transactions, performance, use cases (2025)
- [[AlgoMaster: Indexing]] — Ashish Pratap Singh: database indexes overview, types, B-Tree/Hash/Bitmap data structures, best practices (2025)
- [[AlgoMaster: How to Scale a Database]] — Ashish Pratap Singh: 8 strategies (vertical scaling, indexing, sharding, vertical partitioning, caching, replication, materialized views, denormalization) (2024)
- [[AlgoMaster: 15 Types of Databases]] — Ashish Pratap Singh: relational, key-value, document, graph, wide-column, in-memory, time-series, OODB, search, spatial, blob, ledger, hierarchical, vector, embedded (2024)
- [[AlgoMaster: Bloom Filters]] — Ashish Pratap Singh: probabilistic data structure, bit array, k hash functions, false positives, applications (2025)
- [[MongoDB Atlas Architecture Center]] — MongoDB's Well-Architected Framework: 5 pillars, replica sets, auto-scaling, high availability, DR (2026)
- [[AlgoMaster: Heartbeats in Distributed Systems]] — Ashish Pratap Singh: push/pull heartbeats, failure detection, frequency/timeout trade-offs, split-brain (2024)
- [[AlgoMaster: Service Discovery in Distributed Systems]] — Ashish Pratap Singh: service registry, self/sidecar/orchestrator registration, client-side vs server-side discovery (2024)
- [[Consensus in Distributed System]] — Bhattacharjee & Mahapatra: consensus properties, crash vs Byzantine failures, pBFT, PoW/PoS (2023)
- [[How to Do Distributed Locking]] — Martin Kleppmann: Redlock critique, fencing tokens, process pause problem, efficiency vs correctness locks (2016)
- [[Gossip Protocol Explained]] — NK: anti-entropy/rumor-mongering/aggregation models, push/pull strategies, fanout, real-world uses (Cassandra, Consul, Dynamo, S3) (2023)
- [[Circuit Breaker Pattern (Design Patterns for Microservices)]] — Hasitha Subhashana: 3 states (closed/open/half-open), cascading failure prevention, threshold-based tripping (2021)
- [[Google Cloud: What Is Disaster Recovery?]] — GC: DR planning, 3-2-1 rule, BaaS/DRaaS/snapshots/virtual DR, RTO/RPO, 5-step DR process
- [[Dynatrace: What Is Distributed Tracing?]] — Trace IDs, spans, observability pillars, head-based vs tail-based sampling, MTTD/MTTR (2026)
- [[Design a Distributed Rate Limiter]] — Hello Interview: API-gateway rate limiter with token bucket, Redis/Lua atomicity, sharding, fail-closed policy, latency, hot keys, and dynamic config (2026)
- [[Lecture 01. Strong Models Don't Mean Reliable Execution]] — Learn Harness Engineering: model capability vs. execution reliability, five failure modes, Anthropic/OpenAI case studies (2026)
- [[Lecture 02. What a Harness Actually Is]] — Learn Harness Engineering: five-subsystem harness model (instruction/tool/environment/state/feedback), tool survey, staged 20%->100% case study (2026)
- [[Lecture 03. Making the Repository the Single Source of Truth]] — Learn Harness Engineering: repo as system of record, knowledge visibility gap, fresh session test, ACID-based agent state management, 30-microservice case study (2026)
- [[Lecture 04. Split Instructions Across Files]] — Learn Harness Engineering: instruction bloat, lost-in-the-middle effect, entry file + topic docs split, SaaS 45%->72% case study (2026)
- [[Lecture 05. Keeping Context Alive Across Sessions]] — Learn Harness Engineering: rebuild cost, drift, compaction vs reset, decision logs, harness initialization flow, 78% rebuild-time reduction case study (2026)
- [[Lecture 06. Make the Agent Initialize Before Every Work Session]] — Learn Harness Engineering: dedicated initialization phase vs. implementation, unverified accumulation, startup readiness checklist, Anthropic 31% case study (2026)

## Entities

- [[MongoDB Atlas]] — Fully managed multi-cloud MongoDB service
- [[Apache Kafka]] — The open-source distributed messaging system that evolved from the paper; core event broker for EDA
- [[Apache Flink]] — Open-source stream processing framework for event-time and stateful computations
- [[Confluent]] — Managed data streaming platform built on Kafka and Flink
- [[Redis]] — In-memory data structure store, used as cache/database
- [[Redis Cluster]] — Redis distributed implementation with sharding and failover
- [[Dynamo]] — Amazon's highly available key-value store (eventual consistency)
- [[Paxos]] — Classic consensus algorithm (Lamport)
- [[Raft]] — Understandable consensus algorithm (Ongaro & Ousterhout 2013)
- [[ZAB]] — Zookeeper Atomic Broadcast protocol
- [[Two-Phase Commit]] — Distributed atomic commit protocol
- [[GPT-3]] — 175B parameter language model from OpenAI that pioneered few-shot learning
- [[OpenAI]] — AI research company that built GPT-3
- [[Andy Pavlo]] — CMU professor teaching 15-445 Database Systems
- [[SQLite]] — Single-file embedded database using heap file organization
- [[CUDA]] — NVIDIA's parallel computing platform for GPU programming
- [[H100]] — Hopper architecture data center GPU, fastest for deep learning
- [[A100]] — Ampere data center GPU, workhorse for enterprise deep learning
- [[RTX 4090]] — Ada Lovelace consumer flagship, best single-GPU for individuals
- [[RTX 3090]] — Ampere consumer flagship, popular for 24GB VRAM
- [[LRB]] — Learning Relaxed Belady: learned cache eviction using regression
- [[ARC]] — Adaptive Replacement Cache: balances recency and frequency
- [[Adaptive-TinyLFU]] — Frequency-based cache algorithm
- [[B-LRU]] — LRU with Bloom filter admission control
- [[BERT]] — Bidirectional encoder transformer from Google
- [[Will Larson]] — Engineer, author of "An Elegant Puzzle" and "Staff Engineer"
- [[HAProxy]] — Open-source software load balancer
- [[Memcached]] — In-memory key-value cache
- [[RabbitMQ]] — Message broker implementing AMQP
- [[Hadoop]] — Distributed data processing framework with MapReduce
- [[Ashish Pratap Singh]] — Educator running AlgoMaster.io for LLD interview preparation
- [[Abdul Rafee Wahab]] — Software architect, REST API design best practices author
- [[Amazon ElastiCache]] — Managed Redis/Memcached caching service on AWS
- [[Amazon CloudFront]] — Global CDN service on AWS
- [[Amazon Route 53]] — Cloud DNS web service on AWS
- [[Martin Fowler]] — Software engineer, author of Refactoring, popularized the "two hard things" quote
- [[Hello Interview]] — Interview-preparation publisher of system design problem breakdowns
- [[ZooKeeper]] — Distributed coordination service for configuration, watches, leader election, and coordination
- [[Learn Harness Engineering]] — Lecture series on making coding agents reliable via harness design
- [[Walking Labs]] — Publisher/host of the Learn Harness Engineering lecture series
- [[Anthropic]] — AI company; source of the planner/generator/evaluator harness case study
- [[Claude Sonnet]] — Model family used in the lecture's API-endpoint harness example
- [[Codex]] — OpenAI's coding agent; reference point for harness engineering, git worktrees, observability
- [[SWE-bench]] — Benchmark for coding agents on real GitHub-issue tasks
- [[Cursor]] — AI-assisted code editor; `.cursorrules` instructions, weak state management across IDE sessions
- [[AutoGPT]] — Cautionary example of missing state management causing context accumulation and loops

## Entities

- [[Debezium]] — Open-source CDC platform for streaming database changes to Kafka

## Concepts

- [[Graph Neural Network]] — Deep learning on graph-structured data
- [[Message Passing]] — Core GNN aggregation mechanism
- [[Graph Convolution]] — Convolution on graphs (spectral/spatial)
- [[Graph Attention]] — Attention mechanism on graphs

## ## ## ## Observability

- [[Distributed Tracing]] — End-to-end request tracking across microservices via trace IDs and spans

## Disaster Recovery

- [[Disaster Recovery]] — Restoring IT infrastructure after disaster events, 5-step planning, 3-2-1 rule

## Microservices Patterns

- [[Circuit Breaker Pattern]] — Fail-fast pattern preventing cascading failures via 3-state proxy

## Distributed Systems Mechanisms

- [[Service Discovery]] — Dynamic service-to-service communication without hardcoded addresses
- [[Consensus]] — Agreement on common values across non-faulty nodes
- [[Byzantine Failure]] — Arbitrary/malicious node behavior in distributed systems
- [[Practical Byzantine Fault Tolerance]] — Consensus algorithm tolerating Byzantine faults
- [[Distributed Lock]] — Exclusive access guarantees across nodes
- [[Fencing Token]] — Monotonically increasing numbers for safe lock usage
- [[Redlock]] — Redis-based distributed lock algorithm (controversial)

- [[Heartbeat]] — Periodic health signals between nodes for failure detection

## Probabilistic Data Structures

- [[Bloom Filter]] — Space-efficient probabilistic set membership with false positives
- [[Counting Bloom Filter]] — Bloom filter variant with counter-based deletion support

## Database Type Concepts

- [[Key-Value Store]] — Simple key-value pairs for high-throughput lookups
- [[Graph Database]] — Nodes, edges, and traversals for connected data
- [[Wide-Column Store]] — Dynamic column schema for large-scale distributed storage
- [[In-Memory Database]] — RAM-resident database for microsecond latency
- [[Time-Series Database]] — Append-heavy storage for timestamped data points
- [[Object-Oriented Database]] — Objects with attributes and methods, OOP-native
- [[Blob Datastore]] — Large unstructured binary data (images, videos, backups)
- [[Ledger Database]] — Immutable append-only records with cryptographic chaining
- [[Hierarchical Database]] — Tree-structured parent-child records
- [[Embedded Database]] — In-process database with zero configuration

## Database Scaling Concepts

- [[Vertical Partitioning]] — Splitting tables by column access frequency
- [[Materialized View]] — Pre-computed, disk-stored query results
- [[Data Denormalization]] — Intentional redundancy to avoid joins

## Replication Concepts

- [[Data Replication]] — Keeping copies of data synced across locations
- [[Transactional Replication]] — Real-time ordered change streaming
- [[Snapshot Replication]] — Point-in-time data copy
- [[Merge Replication]] — Independent concurrent writes reconciled
- [[Key-Based Replication]] — Timestamp/ID incremental replication
- [[Full Replication]] — Complete dataset to all replicas
- [[Partial Replication]] — Subset of data per region/workload
- [[Active-Active Geo Distribution]] — Multi-master with CRDTs
- [[Replication Lag]] — Staleness window in async replication
- [[RPO and RTO]] — Disaster recovery metrics

## Sharding Concepts

- [[Database Sharding]] — Horizontal scaling via independent shards across servers
- [[Shard Key]] — Attribute determining shard placement
- [[Hash-Based Sharding]] — Hash function distributes data evenly
- [[Range-Based Sharding]] — Contiguous value ranges per shard
- [[Geo-Based Sharding]] — Geographic region placement
- [[Directory-Based Sharding]] — Lookup table mapping keys to shards
- [[Cross-Shard Query]] — Query spanning multiple shards
- [[Data Rebalancing]] — Redistributing data across shards

## Index Concepts

- [[Database Index]] — Core concept: lookup structure for fast data retrieval
- [[Primary Index]] — Auto-created index on primary key
- [[Dense Index]] — Entry for every search key value
- [[Sparse Index]] — Entry for some search key values
- [[Bitmap Index]] — Binary array index for low-cardinality columns
- [[Hash Index]] — Hash-function-based index for exact-match lookups
- [[Filtered Index]] — Index on a subset of rows
- [[Function-Based Index]] — Index on expression/function result
- [[Full-Text Index]] — Index for efficient text search
- [[Spatial Index]] — Index for geographical/geometric data

## Event-Driven Architecture

- [[Event-Driven Architecture]] — Software design pattern for real-time event detection, processing, and reaction
- [[Event Sourcing]] — Recording state changes as immutable event sequences
- [[CQRS]] — Command Query Responsibility Segregation: separating read and write operations
- [[Event-Driven Microservices]] — Microservices communicating asynchronously through events

## Concepts (Distributed Systems)

- [[Distributed Commit Log]] — The append-only, ordered data structure underlying Kafka's architecture
- [[Pub/Sub Messaging]] — The publish-subscribe pattern that Kafka implements
- [[Log Aggregation]] — The original use case that motivated Kafka at LinkedIn
- [[Change Data Capture (CDC)]] — Track and stream database changes in real time
- [[Redis Sentinel]] — Redis monitoring and automatic failover system
- [[Hash Slot]] — Redis Cluster's 16,384-slot partitioning mechanism
- [[Few-Shot Learning]] — Paradigm where models learn from examples in the prompt without fine-tuning
- [[In-Context Learning]] — Mechanism enabling few-shot learning via attention to examples
- [[Emergent Abilities]] — Capabilities that appear at scale without explicit training

## Distributed Systems Concepts

### Properties & Goals

- [[Scalability]] — Ability to handle growing work without degradation
- [[Availability]] — Proportion of time system is functioning
- [[Latency]] — Time between action and visible impact
- [[Fault Tolerance]] — Well-defined behavior when faults occur
- [[Partitioning]] — Dividing dataset across nodes
- [[Replication (Distributed)]] — Copying data across multiple machines

### Models & Tradeoffs

- [[System Model]] — Assumptions about environment/facilities
- [[Synchronous System Model]] — Known timing bounds
- [[Asynchronous System Model]] — No timing guarantees
- [[CAP Theorem]] — Consistency/Availability/Partition tradeoff
- [[FLP Impossibility Result]] — Consensus impossible in async with failures
- [[Consistency Model]] — Contract between programmer and system

### Time & Ordering

- [[Total Order]] — Exact order for every element
- [[Partial Order]] — Natural distributed systems state
- [[Lamport Clocks]] — Logical ordering without physical clocks
- [[Vector Clocks]] — Accurate causal ordering
- [[Failure Detector]] — Timeout-based crash detection
- [[Epoch]] — Logical time period for consensus

### Replication & Consensus

- [[Synchronous Replication]] — Wait for all replicas
- [[Asynchronous Replication]] — Replicate later
- [[Primary-Backup Replication]] — Single master replication
- [[Quorum (Distributed)]] — Agreement from subset of nodes
- [[Network Partition]] — Network link failure
- [[Consensus Problem]] — Getting all nodes to agree

### Eventual & Weak Consistency

- [[Eventual Consistency]] — Replicas eventually agree
- [[CRDT]] — Convergent Replicated Data Types (guaranteed convergence)
- [[CALM Theorem]] — Monotonic programs are eventually consistent
- [[Bloom Language]] — Language for disorderly programming
- [[Gossip Protocol]] — Probabilistic replica sync
- [[Merkle Tree]] — Hierarchical hashes for efficient comparison
- [[Consistent Hashing]] — Key-to-node mapping that minimizes remapping

- [[What is In-Context Learning?]] — How LLMs learn from prompt examples without training
- [[GPU Computing]] — Using GPUs for general-purpose parallel computation
- [[Kernel (GPU)]] — Parallel functions that execute across many GPU threads
- [[SIMD]] — Single Instruction, Multiple Data vector processing
- [[SIMT]] — Single Instruction, Multiple Threads (CUDA model)
- [[Streaming Multiprocessor]] — GPU processing unit that executes warps
- [[Warp Divergence]] — Performance issue when threads in a warp branch differently
- [[Prefix Sum]] — Parallel algorithm for computing running sums (scan operation)
- [[Tensor Cores]] — Specialized GPU hardware for efficient matrix multiplication
- [[Memory Bandwidth]] — Critical metric for feeding data to Tensor Cores
- [[L2 Cache]] — On-chip GPU cache that speeds up memory access
- [[BF16]] — BrainFloat16, stable 16-bit format for deep learning
- [[TF32]] — TensorFloat32, NVIDIA's fast 19-bit format
- [[FP8]] — 8-bit float, emerging format for maximum speed
- [[Sparse Network Training]] — 2x speedup via structured sparsity on Ampere+
- [[Memory Hierarchy (GPU)]] — Complete GPU memory types from registers to global memory
- [[Memory Coalescing]] — Optimizing global memory access patterns
- [[Bank Conflicts]] — Avoiding shared memory serialization
- [[Register Spilling]] — When registers overflow to slow local memory
- [[Computational Intensity]] — Ratio of compute to memory I/O
- [[Latency vs Throughput]] — CPU latency-optimized vs GPU throughput-optimized design
- [[CUDA Synchronization]] — Block-level barriers (__syncthreads) and deadlock prevention
- [[Atomic Operations]] — CUDA atomic intrinsics (atomicAdd, atomicCAS) for fine-grained sync
- [[Instruction Dependencies]] — Sequential constraints that limit parallelism
- [[ILP]] — Instruction-level parallelism to hide latency
- [[Warp Scheduler]] — Hardware latency hiding via rapid warp switching
- [[Warp (CUDA)]] — Group of 32 threads executing in lockstep
- [[Shared Memory (GPU)]] — Fast on-chip block-level memory with bank structure
- [[Occupancy]] — Active warps ratio for latency hiding
- [[Floating Point Precision]] — Numerical accuracy, associativity, and FP16/BF16 stability
- [[FlashAttention]] — IO-aware exact attention via tiling and recomputation
- [[IO-Awareness]] — Algorithm design accounting for memory hierarchy
- [[Matrix Transpose (GPU)]] — Optimizing matrix transpose to match memory copy bandwidth
- [[Tiling]] — Block-based computation for fast memory
- [[Recomputation]] — Trading compute for memory via gradient checkpointing
- [[Block-Sparse Attention]] — Approximate attention via structured sparsity
- [[FlashAttention-2]] — Improved algorithm: Split-Q, sequence parallelization, reduced non-matmul FLOPs
- [[Split-Q]] — Warp partitioning scheme that eliminates synchronization overhead
- [[Warp Specialization]] — Producer-consumer asynchrony exploiting TMA and WGMMA
- [[GEMM-Softmax Overlap]] — Pingpong scheduling to hide softmax latency under matmul
- [[FP8 Attention]] — Low-precision attention with block quantization and incoherent processing
- [[Cache Eviction Policy]] — Algorithms for removing data from cache (LRU, LFU, ARC, learned policies)
- [[Pairwise Learning to Rank]] — Learning ranking via pairwise comparisons
- [[Impact Distribution Analysis]] — Measuring algorithm impact in noisy production environments
- [[Sloppy Quorum]] — Quorum variant that skips unavailable nodes
- [[Hinted Handoff]] — Failure handling: temporarily store replica on another node
- [[Relational Model]] — Table-based data model with tuples, attributes, and constraints
- [[Relational Algebra]] — Fundamental query operations: select, project, union, join
- [[Primary Key]] — Unique identifier for each row in a table
- [[Foreign Key]] — Reference to primary key in another table
- [[SQL]] — Declarative query language for relational databases
- [[Document Database]] — NoSQL stores JSON/BSON documents (MongoDB)
- [[Vector Database]] — Stores embeddings for nearest-neighbor search
- [[GROUP BY]] — Partition rows into groups for aggregation
- [[HAVING]] — Filter groups after aggregation
- [[Window Function]] — Sliding calculations across related rows
- [[CTE]] — Common Table Expression: named temporary result set
- [[Recursive CTE]] — Self-referencing CTE enabling recursion
- [[Lateral Join]] — Subquery referencing left table columns
- [[Database Page]] — Fixed-size block containing tuples or index data
- [[Heap File]] — Unordered collection of pages
- [[Storage Manager]] — DBMS component managing disk I/O
- [[Buffer Pool]] — Memory area caching disk pages
- [[Disk-Oriented DBMS]] — Architecture assuming disk is primary storage
- [[Frame (Buffer Pool)]] — Fixed-size slot in buffer pool
- [[Page Table]] — Hash table tracking in-memory pages
- [[Dirty Page]] — Modified page not yet written to disk
- [[LRU]] — Least Recently Used cache eviction policy
- [[Clock Replacement]] — Efficient LRU approximation
- [[Slotted Page]] — Page with slot array for variable-length tuples
- [[Index-Organized Table]] — B+Tree with data in leaf nodes
- [[B+Tree]] — Self-balancing tree index structure
- [[Log-Structured Storage]] — Append-only storage with compaction
- [[Tuple]] — Row data stored in pages
- [[Row Store]] — N-ary storage (row-oriented)
- [[Column Store]] — Decomposition storage (column-oriented)
- [[OLTP]] — Online transaction processing (row store workload)
- [[OLAP]] — Online analytical processing (column store workload)
- [[Data Compression]] — Reducing storage size
- [[Run-Length Encoding]] — Compression for repeated values
- [[Hash Table]] — Associative array using hash function
- [[Hash Function]] — Maps keys to array indices
- [[Linear Probe Hashing]] — Static hash with collision probing
- [[Chained Hashing]] — Bucket-linked list hash table
- [[Extendible Hashing]] — Dynamic hash with directory
- [[Linear Hashing]] — Dynamic hash with split pointer
- [[Clustered Index]] — Table physically ordered by index key
- [[Secondary Index]] — Non-clustered index
- [[Index Scan]] — Access method using index
- [[Inverted Index]] — For full-text search
- [[Vector Index]] — For embeddings and nearest-neighbor search
- [[Partial Index]] — Subset of table
- [[Covering Index]] — Query satisfied from index only
- [[Latch]] — Short-duration lock for data structures
- [[Reader-Writer Latch]] — Concurrent read/write lock
- [[Latch Crabbing]] — B+Tree concurrency protocol
- [[Query Plan]] — Tree of operators for query execution
- [[Iterator Model]] — Pull-based query execution (Volcano)
- [[Sequential Scan]] — Full table access
- [[Nested Loop Join]] — Simple nested iteration join
- [[Sort-Merge Join]] — Sort and merge approach
- [[Hash Join]] — Hash-based matching
- [[Transformer]] — Attention-based deep learning architecture
- [[Self-Attention]] — Core transformer mechanism
- [[Vision Transformer]] — Transformers for images
- [[Self-Supervised Learning]] — Pretraining paradigm
- [[Activation Function]] — ReLU, GELU, SwiGLU
- [[Normalization]] — BatchNorm, LayerNorm, RMSNorm
- [[Skip Connection]] — Residual connections
- [[Multi-Head Attention]] — Parallel attention heads
- [[Positional Encoding]] — Position information in transformers
- [[BERT]] — Bidirectional encoder transformer

## Concepts (Scalability Architecture)

- [[Load Balancing]] — Distributing requests across multiple resources
- [[Horizontal Scalability]] — Linear capacity increase with added machines
- [[Redundancy]] — Graceful degradation when components fail
- [[Software Load Balancer]] — Software-based load distribution (HAProxy)
- [[Hardware Load Balancer]] — Dedicated appliance for load balancing
- [[Smart Client]] — Client-side load balancing logic
- [[Caching]] — Storing copies for faster access
- [[Application Caching]] — Explicit caching in application code
- [[Database Caching]] — Transparent database-level caching
- [[In-Memory Cache]] — RAM-based caching (Memcached, Redis)
- [[CDN]] — Content distribution network for static assets
- [[Cache Invalidation]] — Maintaining consistency between cache and source
- [[Read-Through Cache]] — Cache that self-populates on miss
- [[Write-Through Cache]] — Synchronous cache and database updates
- [[Offline Processing]] — Computation decoupled from user requests
- [[Batch Processing]] — Scheduled bulk data processing with collection, execution, and completion stages
- [[Stream Processing]] — Real-time event-driven data processing on continuous unbounded streams
- [[Message Queue]] — Asynchronous communication channel
- [[Scheduling Periodic Tasks]] — Cron-based recurring computation
- [[Map-Reduce]] — Batch processing model for large datasets
- [[Platform Layer]] — Intermediate API layer between apps and backend

## Concepts (Networking)

- [[IP Address]] — 32-bit (IPv4) / 128-bit (IPv6) network identifiers
- [[IPv4]] — Classic 32-bit addressing
- [[IPv6]] — Modern 128-bit successor
- [[CIDR Notation]] — /prefix subnet notation
- [[Subnet Mask]] — Binary mask separating network/host portions
- [[Broadcast Address]] — Send to all devices on a local subnet (all host bits = 1)
- [[Multicast Address]] — One-to-many group communication (Class D / ff00::/8)
- [[Static vs Dynamic IP]] — Manual configuration vs DHCP-assigned addresses
- [[SLAAC]] — IPv6 stateless address autoconfiguration without DHCP
- [[Private IP Address]] — RFC 1918 non-routable addresses
- [[Public IP Address]] — Globally routable addresses
- [[NAT]] — Network Address Translation
- [[OSI Model]] — 7-layer network communication framework
- [[OSI Layer 1: Physical]] — Raw bit transmission over physical medium
- [[OSI Layer 2: Data Link]] — Frame organization, MAC addresses, switches
- [[OSI Layer 3: Network]] — Packet routing, IP addresses, routers
- [[OSI Layer 4: Transport]] — Application delivery, ports, TCP/UDP
- [[OSI Layer 5: Session]] — Connection lifecycle management
- [[OSI Layer 6: Presentation]] — Translation, encryption, compression
- [[OSI Layer 7: Application]] — User-facing protocols (HTTP, DNS, FTP)
- [[Encapsulation and Decapsulation]] — How data flows through the stack
- [[OSI vs TCP/IP Model]] — Theoretical vs deployed standards
- [[DNS]] — Domain name to IP resolution
- [[DNS Record]] — A, AAAA, CNAME, MX, TXT records
- [[Recursive Resolver]] — DNS query resolver
- [[Authoritative Name Server]] — Domain's official DNS server
- [[DNS Caching]] — DNS response caching
- [[Anycast]] — Global routing to nearest server (same IP, multiple locations)
- [[GeoDNS]] — Geographic DNS resolution for latency and compliance
- [[Proxy]] — Acts on behalf of clients
- [[Reverse Proxy]] — Acts on behalf of servers
- [[SSL Termination]] — SSL offloading at reverse proxy
- [[WAF]] — Web Application Firewall
- [[HTTP]] — HyperText Transfer Protocol
- [[HTTPS]] — HTTP over TLS
- [[TLS]] — Transport Layer Security
- [[HTTP/2]] — HTTP version 2 (multiplexing)
- [[HTTP/3]] — HTTP version 3 (QUIC/UDP)
- [[TCP]] — Connection-oriented, reliable
- [[UDP]] — Connectionless, fast
- [[Round Robin]] — Sequential distribution
- [[Weighted Round Robin]] — Capacity-based distribution
- [[Least Connections]] — Fewest active connections
- [[Least Response Time]] — Fastest response time routing
- [[IP Hash]] — Client IP hash for sticky sessions
- [[Health Check]] — Server health monitoring
- [[Checksums]] — Error detection fingerprints
- [[CRC]] — Cyclic Redundancy Check
- [[Parity Bit]] — Single-bit odd/even error detection
- [[MD5]] — 128-bit hash (deprecated)
- [[SHA-256]] — 256-bit current standard
- [[Cryptographic Hash]] — One-way security function
- [[API]] — Application Programming Interface
- [[REST API]] — Representational State Transfer
- [[GraphQL]] — Query language for APIs
- [[gRPC]] — High-performance RPC
- [[API Gateway]] — Central API management
- [[Rate Limiting]] — Request throttling per client
- [[Distributed Rate Limiter]] — Global rate-limit enforcement across gateways using shared state
- [[Rate Limit Rule]] — Policy object defining client scope, endpoint scope, quota, and priority
- [[Token Bucket]] — Token-based rate limiting that allows bursts
- [[Leaky Bucket]] — Queue-based rate limiting that smooths traffic
- [[Fixed Window Counter]] — Time-windowed counter with boundary problem
- [[Sliding Window Log]] — Timestamp log; accurate but memory-intensive
- [[Sliding Window Counter]] — Hybrid: weighted sum of current + previous window
- [[Rate Limiter Failure Mode]] — Fail-open vs fail-closed behavior when limiter state is unavailable
- [[Rate Limiter Hot Key]] — One client identifier overloading a rate-limit shard
- [[Dynamic Rate Limit Configuration]] — Runtime updates to rate-limit rules via polling or push
- [[DDoS Protection]] — Edge filtering and mitigation for malicious distributed traffic
- [[REST API Design Best Practices]] — Resource-oriented URIs, proper HTTP usage, predictable errors
- [[HTTP 202 Accepted]] — Request accepted for async processing (not yet complete)
- [[Error Response Format]] — Standardized JSON error structure with field-level details
- [[URI Naming Conventions]] — Plural nouns, no verbs, no nesting, trailing slash handling
- [[Query String Filtering]] — Filter resource collections via URL query parameters
- [[Page Pagination]] — Numbered pages with page + page_size parameters
- [[Over-fetching]] — Returns more data than needed (REST issue)
- [[Under-fetching]] — Multiple requests for related data (REST issue)
- [[WebSockets]] — Full-duplex bidirectional communication over persistent TCP connection
- [[HTTP 101]] — Switching Protocols status code for WebSocket handshake
- [[Polling]] — Client repeatedly requests server at fixed intervals
- [[Long-Polling]] — Server holds response until data available
- [[Frame (WebSocket)]] — Minimal-overhead data unit in WebSocket protocol
- [[Webhooks]] — Event-driven push notifications via HTTP POST
- [[Event Idempotency]] — Exactly-once processing via event ID deduplication
- [[Web Caching]] — Server-side and client-side caching of web artifacts
- [[Session Management]] — Centralized HTTP session store for elastic architectures
- [[Cache-Aside]] — Lazy loading pattern: app checks cache, loads from DB on miss (Memcached pattern)
- [[Write-Behind Cache]] — Async write-back pattern: app writes to cache, async flush to DB
- [[Refresh-Ahead Cache]] — Proactive refresh of hot entries before TTL expiry
- [[HTTP Caching]] — Protocol-level caching across browsers, proxies, and CDNs (RFC 7234)
- [[Browser Caching]] — Client-side filesystem HTTP cache, heuristics, multi-layer complexity
- [[Proxy Cache]] — Private HTTP reverse proxy caches (Varnish, Squid, Nginx, Traffic Server)
- [[Cache-Control]] — HTTP caching directives: max-age, no-store, no-cache, must-revalidate, public, private, s-maxage
- [[Vary Header]] — Content negotiation cache key extension, normalization, combinatorial explosion
- [[Conditional Request]] — ETag/If-Modified-Since validation, 304 Not Modified flow
- [[ETag]] — Entity Tags for resource version validation (strong vs weak)
- [[Write-Around Cache]] — Bypass cache on writes, cache only reads
- [[Tag-Based Invalidation]] — Bulk cache invalidation by grouping entries under tags
- [[Version-Based Invalidation]] — Version counters for cache freshness without explicit purge
- [[Cache Warming]] — Pre-populating cache before expected load
- [[Cache Stampede]] — Thundering herd problem when multiple requests miss cache simultaneously
- [[Edge Cache]] — Geographically distributed cache layer for low-latency content delivery
- [[DNS Negative Caching]] — Caching DNS nonexistence (NXDOMAIN/NODATA), RFC 2308
- [[ACID Transactions]] — Atomicity, Consistency, Isolation, Durability: database transaction guarantees
- [[NoSQL]] — Non-relational databases: key-value, document, column-family, graph; horizontal scaling, BASE
- [[Dead Letter Queue]] — Holding queue for permanently failing events
- [[Exponential Backoff]] — Retry strategy with increasing delays and jitter
- [[Idempotency]] — Same operation multiple times = same result; critical for distributed systems
- [[Idempotency Key]] — Unique client-generated ID to prevent duplicate processing
- [[Deduplication Store]] — Storage for tracking processed operation identifiers
- [[Upsert]] — Update-or-insert database operation for idempotent writes

## Concepts (OOP/LLD)

### Building Blocks

- [[Class]] — Blueprint/template defining object structure and behavior
- [[Object]] — Concrete instance of a class with actual values
- [[Interface]] — Contract defining required methods without implementation

### Four Pillars

- [[Encapsulation]] — Bundling data with methods, restricting direct access
- [[Abstraction]] — Hiding complexity, exposing essential features
- [[Inheritance]] — Deriving child classes from parent classes
- [[Polymorphism]] — Objects of different types through common interface

### Object Relationships

- [[Association]] — "Knows-about" relationship, both independent
- [[Aggregation]] — "Has-a" with independent parts
- [[Composition]] — "Has-a" with owned parts that die with whole
- [[Dependency]] — Temporary "uses-a" relationship
- [[Realization]] — Interface to implementing class relationship
- [[Enum]] — Fixed set of named constants with type safety
- [[Type Safety]] — Compiler prevents operations on inappropriate types
- [[State Machine]] — System in finite states with transitions
- [[Interface Segregation Principle]] — Clients not forced to depend on unused methods
- [[Dependency Inversion Principle]] — High-level and low-level depend on abstractions
- [[Dependency Injection]] — Dependencies passed in from external sources
- [[SOLID Principles]] — Five OOP design principles (SRP, OCP, LSP, ISP, DIP)
- [[Access Modifiers]] — private, protected, public visibility control
- [[Getter and Setter Pattern]] — Controlled access via getX()/setX()
- [[Data Validation]] — Checking constraints before accepting data
- [[Abstract Class]] — Blueprint with abstract + concrete methods

### Design Principles

- [[DRY Principle]] — Don't repeat yourself, single source of truth
- [[YAGNI Principle]] — Don't build for requirements that don't exist yet
- [[KISS Principle]] — Keep it simple, avoid over-engineering
- [[Public API]] — External interface hiding internal complexity
- [[Method Overriding]] — Subclass provides specific implementation of parent method
- [[Method Overloading]] — Multiple methods with same name, different parameters

## Architecture Patterns

- [[Client-Server Architecture]] — Foundational computing model with clients, servers, and networks
- [[Peer-to-Peer Network]] — Decentralized architecture where peers act as both clients and servers
- [[Stateful Architecture]] — Server retains client data across requests (sessions, carts, auth)
- [[Stateless Architecture]] — Each request independent; server discards all temporary data after responding

## Design Principles & Trade-Offs

- [[System Design Trade-Offs]] — The meta-framework of 15 fundamental system design trade-offs
- [[One-Tier Architecture]] — Monolithic single-application model (UI + logic + data together)
- [[Two-Tier Architecture]] — Client (UI) + server (logic + data) split
- [[Three-Tier Architecture]] — Presentation + application + data layers
- [[N-Tier Architecture]] — 3-tier plus specialized layers (caching, auth, LB, etc.)
- [[Microservices]] — Loosely coupled, independently deployable services per bounded context
- [[Serverless Architecture]] — Cloud-managed event-driven functions, pay-per-use, auto-scaling
- [[FaaS]] — Functions as a Service, the execution model behind serverless

## Harness Engineering (AI Agents)

- [[Harness Engineering]] — Everything outside model weights: instruction/tool/environment/state/feedback subsystems
- [[Capability Gap]] — Benchmark pass rate vs. real-world task success
- [[Harness-Induced Failure]] — Capable model fails because the surrounding system prevents reliable execution
- [[Verification Gap]] — Distance between agent confidence and actual correctness
- [[Diagnostic Loop]] — Execute, observe, attribute to a layer, fix, rerun
- [[Definition of Done]] — Explicit, command-checkable completion criteria
- [[Context Anxiety]] — Rushed, verification-skipping behavior under low remaining context
- [[Agent State Management]] — Preserving progress and decisions across sessions
- [[Controlled Variable Exclusion Test]] — Ablate one harness subsystem at a time to measure its marginal contribution
- [[Knowledge Visibility Gap]] — Project knowledge that lives only in people's heads, invisible to the agent
- [[System of Record]] — The repo as authoritative source, not just code storage
- [[Fresh Session Test]] — Diagnostic: can a brand-new agent session answer baseline questions from repo contents alone?
- [[Agent State ACID Principles]] — Atomicity/consistency/isolation/durability applied to agent progress tracking
- [[Instruction Bloat]] — Instruction file occupying 10-15% of the context window, crowding out task reasoning
- [[Lost in the Middle]] — LLMs use mid-document information worse than start/end (Liu et al. 2023)
- [[Instruction Signal-to-Noise Ratio]] — Proportion of a file's instructions actually relevant to the current task
- [[Entry File]] — Short router document (50-200 lines) pointing to topic docs, not containing all detail itself
- [[Rebuild Cost]] — Time for a new agent session to reach executable, oriented state
- [[Drift]] — Growing gap between agent's believed repo state and actual repo state
- [[Compaction vs. Reset]] — Within-session summarization vs. fresh session from persisted artifacts
- [[Decision Log]] — DECISIONS.md capturing why a choice was made, not just what was built
- [[Harness Initialization Flow]] — Explicit clock-in/clock-out routines bookending an agent session
- [[Initialization Phase]] — Dedicated one-time project setup phase separated from implementation work
- [[Startup Readiness Checklist]] — Document verifying, not just claiming, that setup steps completed successfully

## Queries

- [[How does YouTube HALP work?]] — HALP: hybrid ML + heuristic cache eviction for YouTube CDN
