## [2026-05-01] ingest | REST API Design Best Practices

Ingested source: Abdul Rafee Wahab - REST API Design Best Practices (Oct 2021).
Created 1 source summary, 6 concept pages (REST API Design Best Practices, HTTP 202, Error Response Format, URI Naming Conventions, Query String Filtering, Page Pagination), 1 entity page.
Key concepts: resource-oriented URIs (plural nouns, no verbs, no nesting), Content-Type importance, meaningful HTTP status codes (never 200 with error body), 401 vs 403 distinction, query string filtering + pagination, REST-specific frameworks, trailing slash handling.

## [2026-05-01] ingest | Rate Limiting Algorithms

Ingested source: AlgoMaster.io Rate Limiting Algorithms (Jul 2024).
Created 1 source summary, 5 concept pages (Token Bucket, Leaky Bucket, Fixed Window Counter, Sliding Window Log, Sliding Window Counter). Updated existing Rate Limiting page with cross-references.
Key concepts: Token Bucket (burst-friendly, simple), Leaky Bucket (smooths traffic, drops excess), Fixed Window Counter (boundary problem allows 2x rate), Sliding Window Log (accurate but memory-heavy), Sliding Window Counter (hybrid: weighted approximation with O(1) memory).

## [2026-05-01] ingest | Idempotency

Ingested source: AlgoMaster.io Idempotency (Nov 2024).
Created 1 source summary, 4 concept pages (Idempotency, Idempotency Key, Deduplication Store, Upsert).
Key concepts: idempotent operations (GET/PUT/DELETE vs POST), idempotency keys for deduplication, database upsert patterns, deduplication store design, two-phase reservation pattern, handling race conditions in distributed systems.

## [2026-05-01] ingest | Webhooks

Ingested source: AlgoMaster.io Webhooks (Apr 2025).
Created 1 source summary, 4 concept pages (Webhooks, Event Idempotency, Dead Letter Queue, Exponential Backoff).
Key concepts: event-driven push notifications, webhook anatomy (POST, JSON, HMAC signature), receiver setup (idempotency, signature verification), scalable pipeline (queue → store → async workers → retry with backoff → DLQ → observability).

## [2026-04-28] ingest | REST vs GraphQL

Ingested source: AlgoMaster.io REST vs GraphQL (March 2025).
Created 1 source summary, 2 concept pages (Over-fetching, Under-fetching).
Key differences: over-fetching, under-fetching, single vs multiple endpoints, caching.

## [2026-04-28] ingest | API Gateway

Ingested source: AlgoMaster.io API Gateway (December 2024).
Created 1 source summary, 1 concept page (Rate Limiting).
Key features: request validation, auth, rate limiting, routing.

## [2026-04-28] ingest | API

Ingested source: AlgoMaster.io API (October 2025).
Created 1 source summary, 4 concept pages (REST API, GraphQL, gRPC, API Gateway).
Key concepts: request-response model, REST, GraphQL, gRPC, API Gateway.

## [2026-04-28] ingest | Checksums

Ingested source: AlgoMaster.io Checksums (October 2025).
Created 1 source summary, 4 concept pages (CRC, MD5, SHA-256, Cryptographic Hash).
Key concepts: CRC for errors, cryptographic hashes, SHA-256 standard.

## [2026-04-28] ingest | Load Balancing Algorithms

Ingested source: AlgoMaster.io Load Balancing Algorithms (June 2024).
Created 1 source summary, 4 concept pages (Round Robin, Weighted Round Robin, Least Connections, Health Check).
Key concepts: algorithms (round robin, weighted, least connections), L4 vs L7, health checks.

## [2026-04-28] ingest | TCP vs UDP

Ingested source: AlgoMaster.io TCP vs UDP (November 2025).
Created 1 source summary, 2 concept pages (TCP, UDP).
Key concepts: three-way handshake, reliable vs fastest, use cases.

## [2026-04-28] ingest | HTTP and HTTPS

Ingested source: AlgoMaster.io HTTP and HTTPS (October 2025).
Created 1 source summary, 5 concept pages (HTTP, HTTPS, TLS, HTTP/2, HTTP/3).
Key concepts: HTTP methods, TLS handshake, HTTP/2 multiplexing, HTTP/3 QUIC.

## [2026-04-28] ingest | Proxy vs Reverse Proxy

Ingested source: AlgoMaster.io Proxy vs Reverse Proxy (October 2024).
Created 1 source summary, 4 concept pages (Proxy, Reverse Proxy, SSL Termination, WAF).
Key concepts: forward proxy vs reverse proxy, load balancing, SSL termination.

## [2026-04-28] ingest | DNS

Ingested source: AlgoMaster.io DNS (September 2025).
Created 1 source summary, 4 concept pages (DNS Record, Recursive Resolver, Authoritative Name Server, DNS Caching).
Key concepts: resolution process, DNS hierarchy, record types, caching levels.

## [2026-04-28] ingest | IP Address

Ingested source: AlgoMaster.io IP Address (March 2026).
Created 1 source summary, 6 concept pages (IPv4, IPv6, CIDR, NAT, Private/Public IP).
Key concepts: 32-bit IPv4, 128-bit IPv6, CIDR notation, subnetting, NAT, RFC 1918.

## [2026-04-28] ingest | OSI Model

Ingested source: AlgoMaster.io OSI Model (March 2026).
Created 1 source summary, 9 concept pages (7 layers + encapsulation + OSI vs TCP/IP), updated index.
Key concepts: 7-layer framework, MAC/IP/ports, encapsulation, decapsulation, troubleshooting value.

## [2026-04-27] ingest | CockroachDB: Fault Tolerance

Ingested source: CockroachDB Fault Tolerance (2023).
Created 1 source summary, updated 1 concept page.
Key concepts: quorum, replication factor, automatic recovery.

## [2026-04-27] ingest | Druva: Failover

Ingested source: Druva Failover Definition (2026).
Created 1 source summary, 1 concept page.
Key concepts: heartbeat, active-active vs active-passive, cluster.

## [2026-04-27] ingest | AlgoMaster: CAP Theorem

Ingested source: AlgoMaster.io CAP Theorem (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: C/A/P tradeoff, CP vs AP systems.

## [2026-04-27] ingest | AlgoMaster: Consistent Hashing

Ingested source: AlgoMaster.io Consistent Hashing (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: hash ring, virtual nodes, minimal remapping on scaling.

## [2026-04-27] ingest | AlgoMaster: Latency vs Throughput vs Bandwidth

Ingested source: AlgoMaster.io Latency vs Throughput vs Bandwidth (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: delay vs volume vs capacity, BDP, bottleneck.

## [2026-04-27] ingest | AlgoMaster: Single Point of Failure (SPOF)

Ingested source: AlgoMaster.io SPOF (2026).
Created 1 source summary, 1 concept page.
Key concepts: single points of failure, redundancy, load balancing, strategies to eliminate.

## [2026-04-27] ingest | AlgoMaster: Scalability, Availability, Reliability

Ingested sources: AlgoMaster.io Scalability, Availability, Reliability (2026).
Created 3 source summaries, updated 2 concept pages.
Key concepts: vertical/horizontal scaling, stateless services, redundancy, nines, circuit breakers.

## [2026-04-27] ingest | AlgoMaster: SOLID Principles

Ingested source: AlgoMaster.io SOLID Principles (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: SRP, OCP, LSP, ISP, DIP with code examples.

## [2026-04-27] ingest | AlgoMaster: KISS Principle

Ingested source: AlgoMaster.io KISS Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: "keep it simple", over-engineering, clear over clever.

## [2026-04-27] ingest | AlgoMaster: YAGNI Principle

Ingested source: AlgoMaster.io YAGNI Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: "you aren't gonna need it", build for now not later.

## [2026-04-27] ingest | AlgoMaster: DRY Principle

Ingested source: AlgoMaster.io DRY Principle (2026).
Created 1 source summary, 1 concept page.
Key concepts: don't repeat yourself, single source of truth, Rule of Three.

## [2026-04-27] ingest | AlgoMaster: Composition

Ingested source: AlgoMaster.io Composition (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: strong "owns-a", filled diamond UML, parts die with whole, tight coupling.

## [2026-04-27] ingest | AlgoMaster: Dependency

Ingested source: AlgoMaster.io Dependency (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: temporary "uses-a", UML dashed arrow, method parameters, loose coupling.

## [2026-04-27] ingest | AlgoMaster: Aggregation

Ingested source: AlgoMaster.io Aggregation (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: "has-a" with independent parts, hollow diamond UML symbol, reassignment allowed.

## [2026-04-27] ingest | AlgoMaster: Association

Ingested source: AlgoMaster.io Association (2026).
Created 1 source summary, updated 1 concept page.
Key concepts: "knows-about" relationship, UML representation, multiplicity (1-to-1, 1-to-many, many-to-many), unidirectional vs bidirectional, intermediary pattern for many-to-many.

## [2026-04-24] ingest | Race Conditions and Critical Sections

Ingested source: AlgoMaster.io race conditions (2026).
Created 1 source summary, updated 2 concept pages.

## [2026-04-24] ingest | Thread Lifecycle and States

Ingested source: AlgoMaster.io thread lifecycle (2026).
Created 1 source summary, 1 concept page.

## [2026-04-24] ingest | Processes vs Threads

Ingested source: AlgoMaster.io processes vs threads (2026).
Enhanced concept page with context switching details.
Created 1 source summary, updated 1 concept page.

## [2026-04-24] update | Concurrency vs Parallelism

Enhanced concept page with AlgoMaster's restaurant analogy, four scenarios, and levels of parallelism.

## [2026-04-24] ingest | Introduction to Concurrency

Ingested source: AlgoMaster.io intro to concurrency (2026).
Created 1 source summary, 6 concept pages.
Key concepts: concurrency vs parallelism, processes vs threads, race conditions, critical sections, thread safety.

## [2026-04-05] init | Wiki initialized

Empty wiki created, ready for first ingest.

## [2026-04-05] ingest | Kafka: A Distributed Messaging System for Log Processing

Ingested source: Kafka paper (2011) from LinkedIn.
Created 1 source summary, 1 entity page, 3 concept pages.
Key concepts: distributed commit log, pub/sub messaging, log aggregation.

## [2026-04-05] ingest | Language Models are Few-Shot Learners (GPT-3)

Ingested source: GPT-3 paper (2020) from OpenAI.
Created 1 source summary, 2 entity pages, 3 concept pages.
Key concepts: few-shot learning, in-context learning, emergent abilities.

## [2026-04-16] ingest | CS 179: Introduction to GPU Programming - Lecture 1

Ingested source: Caltech CS 179 Lecture 1 (2026) covering GPU architecture and CUDA.
Created 1 source summary, 1 entity page, 2 concept pages.

## [2026-04-19] ingest | Distributed Systems: for fun and profit

Ingested source: Mixu's distributed systems book (2013).
Created 1 source summary, 5 entity pages, 25+ concept pages.
Key concepts: scalability, availability, CAP, FLP, partitions, replication, consensus, eventual consistency, CRDTs, CALM.
Key concepts: GPU computing, kernel functions, CPU vs GPU architecture, thread indexing.

## [2026-04-16] ingest | CS 179: Intro to SIMD and GPU Internals - Lecture 2

Ingested source: Caltech CS 179 Lecture 2 (2026) covering GPU hardware internals.
Created 1 source summary, 4 concept pages.
Key concepts: SIMD vs SIMT, thread hierarchy, warp divergence, streaming multiprocessors.

## [2026-04-16] ingest | CS179 Recitation 1 - GPU Overview and Prefix Sum

Ingested source: CS 179 Recitation 1 (2025) covering GPU hardware and prefix sum.
Created 1 source summary, 1 concept page.
Key concepts: prefix sum (scan), RTX 5090 Blackwell architecture.

## [2026-04-16] query | What is In-Context Learning?

Saved answer explaining ICL mechanism, few-shot relation, and scaling behavior.

## [2026-04-16] ingest | Best GPUs for Deep Learning in 2023

Ingested source: Tim Dettmers' GPU guide (2023).
Created 1 source summary, 4 entity pages, 8 concept pages.
Key concepts: Tensor Cores, memory bandwidth, precision formats (BF16/TF32/FP8), sparse training, L2 cache.

## [2026-04-16] ingest | CS 179: GPU Memory Systems - Lecture 4

Ingested source: CS 179 Lecture 4 (2026) covering GPU memory systems.
Created 1 source summary, 6 concept pages.
Key concepts: Memory hierarchy, coalescing, bank conflicts, register spilling, computational intensity, latency vs throughput.

## [2026-04-17] ingest | CS 179: Synchronization and ILP - Lecture 5

Ingested source: CS 179 Lecture 5 (2026) covering synchronization and ILP.
Created 1 source summary, 8 concept pages.
Key concepts: CUDA synchronization, atomic operations, instruction dependencies, ILP, warp scheduler, occupancy, floating point precision.

## [2026-04-17] ingest | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Ingested source: FlashAttention paper by Dao et al. (Stanford, 2022).
Created 1 source summary, 5 concept pages.
Key concepts: FlashAttention, IO-awareness, tiling, recomputation, block-sparse attention.

## [2026-04-17] ingest | FlashAttention-2: Faster Attention with Better Parallelism

Ingested source: FlashAttention-2 paper by Tri Dao (2023).
Created 1 source summary, 2 concept pages.
Key concepts: FlashAttention-2, Split-Q warp partitioning, sequence-length parallelization.

## [2026-04-17] ingest | FlashAttention-3: Fast and Accurate Attention with Asynchrony

Ingested source: FlashAttention-3 paper by Shah et al. (2024).
Created 1 source summary, 4 concept pages.
Key concepts: FlashAttention-3, warp specialization, GEMM-softmax overlap, FP8 attention with block quantization.

## [2026-04-19] ingest | HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN

Ingested source: Google paper (USENIX NSDI 2024).
Created 1 source summary, 3 concept pages, 2 entity pages.
Key concepts: learned cache eviction, pairwise learning to rank, impact distribution analysis.
Key entities: HALP, LRB, ARC.

## [2026-04-20] ingest | Redis Cluster: Architecture, Replication, Sharding and Failover

Ingested source: Redis Cluster article by Sajal Jain (2019).
Created 1 source summary, 2 entity pages, 2 concept pages.
Key concepts: Redis Cluster, hash slots (16384), failover, Redis Sentinel, master-slave.

## [2026-04-21] query | How does YouTube HALP work?

Saved answer to wiki/queries/HALP.md describing HALP's hybrid ML+heuristic cache eviction.

## [2026-04-21] ingest | Dynamo: Amazon's Highly Available Key-Value Store

Ingested source: SOSP 2007 paper (DeCandia et al.).
Created 1 source summary, 3 new concept pages (Sloppy Quorum, Hinted Handoff).
Key techniques: consistent hashing, vector clocks, sloppy quorum, hinted handoff, Merkle trees.
Key concepts: eventual consistency, application-assisted conflict resolution.

## [2026-04-22] ingest | CS 179: Matrix Transpose Optimization - Lecture 6

Ingested source: CS 179 Recitation 2 (2025) covering matrix transpose optimization.
Created 1 source summary, 3 concept pages.
Key concepts: matrix transpose, warp, shared memory, bank conflict resolution via padding.

## [2026-04-22] ingest | CMU 15-445: Relational Model & Algebra

Ingested source: CMU 15-445 Lecture 1 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 1 entity page, 7 concept pages.
Key concepts: relational model, relational algebra (select/project/union/join), primary key, foreign key, SQL, document/vector databases.

## [2026-04-22] ingest | CMU 15-445: Modern SQL

Ingested source: CMU 15-445 Lecture 2 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: aggregates, GROUP BY, HAVING, window functions, CTEs, recursive CTEs, lateral joins.

## [2026-04-23] ingest | CMU 15-445: Database Storage I

Ingested source: CMU 15-445 Lecture 3 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 1 entity page, 5 concept pages.
Key concepts: disk-oriented DBMS, database pages, heap files, storage manager, buffer pool.

## [2026-04-23] ingest | CMU 15-445: Memory Management & Buffer Pools

Ingested source: CMU 15-445 Lecture 4 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: buffer pool organization, page table, frame, dirty page, LRU, clock replacement, memory-mapped I/O.

## [2026-04-23] ingest | CMU 15-445: Database Storage II

Ingested source: CMU 15-445 Lecture 5 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: slotted pages, index-organized tables, B+Tree, log-structured storage, tuple storage.

## [2026-04-23] ingest | CMU 15-445: Storage Models & Compression

Ingested source: CMU 15-445 Lecture 6 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 7 concept pages.
Key concepts: row store, column store, OLTP, OLAP, data compression, run-length encoding.

## [2026-04-23] ingest | CMU 15-445: Hash Tables

Ingested source: CMU 15-445 Lecture 7 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 6 concept pages.
Key concepts: hash tables, linear probe, chained hashing, extendible hashing, linear hashing.

## [2026-04-23] ingest | CMU 15-445: B+Tree Indexes

Ingested source: CMU 15-445 Lecture 8 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: B+Tree, clustered index, secondary index, index scan.

## [2026-04-23] ingest | CMU 15-445: Indexes & Filters II

Ingested source: CMU 15-445 Lecture 9 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 4 concept pages.
Key concepts: inverted index, vector index, partial index, covering index.

## [2026-04-23] ingest | CMU 15-445: Index Concurrency Control

Ingested source: CMU 15-445 Lecture 10 (Spring 2026) by Jignesh Patel.
Created 1 source summary, 3 concept pages.
Key concepts: latch vs lock, reader-writer latch, latch crabbing.

## [2026-04-23] ingest | CMU 15-445: Query Processing

Ingested source: CMU 15-445 Lecture 11 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: query plan, iterator model, sequential scan.

## [2026-04-23] ingest | CMU 15-445: Join Algorithms

Ingested source: CMU 15-445 Lecture 12 (Spring 2026) by Andy Pavlo.
Created 1 source summary, 3 concept pages.
Key concepts: nested loop join, sort-merge join, hash join.

## [2026-04-23] ingest | A Survey of Deep Learning: From Activations to Transformers

Ingested source: arXiv paper by Schneider & Vlachos (2023/2024).
Created 1 source summary, 9 concept pages, 1 entity page.
Key concepts: transformer, self-attention, vision transformer, self-supervised learning.
Additional: activation functions, normalization, skip connections, multi-head attention, positional encoding.

## [2026-04-23] ingest | Inheritance + Polymorphism

Ingested sources: AlgoMaster articles on Inheritance and Polymorphism (2026).
Created 2 source summaries, 3 concept pages.
Key concepts: extends, inheritance types, method overriding, method overloading, compile-time vs runtime polymorphism.
Key examples: Notification system (Email/SMS/Push), Calculator.

Ingested source: AlgoMaster article on Abstraction (2026).
Created 1 source summary, 3 concept pages.
Key concepts: abstract classes (shared behavior + abstract methods), public APIs, abstraction vs encapsulation.
Key example: MediaPlayer with PlayerController (player-agnostic).

Ingested source: AlgoMaster article on Encapsulation (2026).
Created 1 source summary, 4 concept pages.
Key concepts: access modifiers (private/protected/public), getter/setter pattern, data validation.
Key examples: BankAccount (balance protection), PaymentProcessor (sensitive data masking).

Ingested sources: AlgoMaster articles on interfaces and SOLID principles (2026).
Created 1 source summary, 5 concept pages.
Key concepts: interface contracts, interface segregation (ISP), dependency inversion (DIP), dependency injection pattern, SOLID principles.
Key examples: payment gateway, notification service.

Ingested source: AlgoMaster article on Enums (2026).
Created 1 source summary, 3 concept pages.
Key concepts: enum with properties/methods, type safety, state machine pattern.
Key example: order processing system with OrderStatus and PaymentMethod enums.

Ingested sources: AlgoMaster.io articles on OOP fundamentals (2026).
Created 2 source summaries, 1 entity page, 12 concept pages.
Key concepts: class, object, interface, four pillars (encapsulation, abstraction, inheritance, polymorphism), five object relationships (association, aggregation, composition, dependency, realization).
Key entity: Ashish Pratap Singh (AlgoMaster.io creator).

Ingested source: Will Larson's foundational article on scalable system architecture (2011).
Created 1 source summary, 6 entity pages, 18 concept pages.
Key concepts: load balancing (smart clients, hardware, software), caching (application, database, in-memory, CDN), cache invalidation, offline processing (message queues, cron, map-reduce), platform layer.
## [2026-05-08] ingest | Broadcasting Live Video to Millions

Ingested source: Facebook Engineering blog (Dec 2015).
Created 1 source summary, 1 concept page (Edge Cache). Updated Cache Stampede page with request coalescing strategy and Facebook Live case study.
Key concepts: multi-layer edge cache architecture (98%+ hit rate), request coalescing for thundering herd prevention, HLS 3-second segments vs RTMP push model (4KB chunks, 5x latency reduction), nginx-rtmp modification for Facebook Live.

## [2026-05-08] ingest | Cache Invalidation Strategies

Ingested source: Medium article by CoVaib DeepLearn (Sep 2025).
Created 1 source summary, 5 concept pages (Write-Around Cache, Tag-Based Invalidation, Version-Based Invalidation, Cache Warming, Cache Stampede). Updated Cache Invalidation page with purge/ban methods, event-driven strategy, dependency-based invalidation.
Key concepts: purge vs ban, TTL/event-driven/write-through/write-around/write-behind/lazy-loading strategies, tag-based/dependency-based/version-based advanced patterns, cache warming (scheduled/event-driven/JIT), cache stampede (thundering herd) with 5 mitigations.

## [2026-05-08] ingest | Two Hard Things

Ingested source: Martin Fowler's bliki (2009, updated 2021).
Created 1 source summary, 1 entity page (Martin Fowler). Updated Cache Invalidation page with the Phil Karlton quote.
Key content: famous Phil Karlton quote "there are only two hard things: cache invalidation and naming things", 4 notable variations.

## [2026-05-08] ingest | HTTP Caching: Cache-Control & Vary

Ingested source: freeCodeCamp article by Léo Jacquemin (Oct 2019), Part 2 of series.
Created 1 source summary, 5 concept pages (Cache-Control, Vary Header, Conditional Request, ETag). Updated HTTP Caching, Web Caching, Browser Caching, and Caching pages.
Key concepts: 4-outcome caching decision tree, Cache-Control directives (max-age, no-store, no-cache, must-revalidate, public/private, s-maxage, stale-while-revalidate, stale-if-error), Vary header for content negotiation, normalization (44 Accept-Encoding values, 8000+ User-Agent values), strong vs weak ETags, freshness vs validation distinction, conditional request flow (304 vs 200).

## [2026-05-08] ingest | HTTP Caching In-Depth Part 1

Ingested source: freeCodeCamp article by Léo Jacquemin (Dec 2018).
Created 1 source summary, 3 concept pages (HTTP Caching, Browser Caching, Proxy Cache). Updated Caching, Web Caching, and CDN pages.
Key concepts: 3 HTTP caching actors (browser, CDN, private proxy), latency vs bandwidth as bottleneck, web request anatomy (DNS + TCP + TLS + slow-start = ~8 RT per request), TCP slow-start and congestion window evolution, cache abstraction (all proxies speak HTTP), browser cache multi-layer complexity, private proxy caches as first solution (Varnish, Squid, Nginx), CDN programmatic purging.

## [2026-05-08] ingest | System Design Primer: Cache

Ingested source: Donne Martin's system-design-primer cache section (GitHub).
Created 1 source summary, 3 concept pages (Cache-Aside, Write-Behind Cache, Refresh-Ahead Cache). Updated Caching and Application Caching pages.
Key concepts: 4 cache update strategies (cache-aside/lazy loading, write-through, write-behind/write-back, refresh-ahead), 2 caching levels (database query hashing vs object-level), 5 cache locations (client, CDN, web server, database, application).

## [2026-05-08] ingest | AWS Caching Overview

Ingested source: AWS Caching Overview page (2026).
Created 1 source summary, 3 entity pages (Amazon ElastiCache, Amazon CloudFront, Amazon Route 53), 2 concept pages (Web Caching, Session Management). Updated Caching and CDN concept pages.
Key concepts: 5-layer caching stack (client, DNS, web, app, database), distributed caching with independent lifecycle, 5 benefits (performance, cost, predictability, hotspots, IOPS), use cases across 9 domains and 10 industries, AWS caching services (ElastiCache for Redis/Memcached, CloudFront CDN, Route 53 DNS).

## [2026-05-01] ingest | WebSockets

Ingested source: AlgoMaster.io WebSockets (Aug 2024).
Created 1 source summary, 5 concept pages (WebSockets, HTTP 101, Polling, Long-Polling, Frame).
Key concepts: full-duplex bidirectional communication, HTTP handshake with 101 switch, persistent connections vs HTTP/polling/long-polling, use cases (chat, gaming, notifications, financial feeds, collaboration, IoT), challenges (scalability, security, network reliability, proxy compatibility).

Key entities: Will Larson, HAProxy, Memcached, RabbitMQ, Hadoop.