---
title: "Wiki Index"
type: index
tags: []
created: 2026-04-05
---

# LLM Wiki

A persistent knowledge base for LLM inference systems and distributed databases.

## Sources

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

## Entities

- [[Apache Kafka]] — The open-source distributed messaging system that evolved from the paper
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

## Concepts

- [[Distributed Commit Log]] — The append-only, ordered data structure underlying Kafka's architecture
- [[Pub/Sub Messaging]] — The publish-subscribe pattern that Kafka implements
- [[Log Aggregation]] — The original use case that motivated Kafka at LinkedIn
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

## Queries

- [[How does YouTube HALP work?]] — HALP: hybrid ML + heuristic cache eviction for YouTube CDN