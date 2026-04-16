---
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
type: source
tags: [attention, transformers, gpu, optimization, transformers]
created: 2026-04-17
sources: [flash-attention.pdf]
url: "https://arxiv.org/abs/2205.14135"
authors: [Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré]
institutions: [Stanford University, University at Buffalo SUNY]
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

## Paper Details

- **Authors**: Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré
- **Institution**: Stanford University, University at Buffalo, SUNY
- **Published**: June 2022 (arXiv:2205.14135)
- **Code**: https://github.com/HazyResearch/flash-attention

## Abstract

FlashAttention computes exact self-attention with O(N²) FLOPs but sub-quadratic memory. The key innovation is making attention **IO-aware** — accounting for reads/writes between GPU SRAM and HBM.

## Problem Statement

Standard attention has O(N²) time and memory complexity where N is sequence length. For long sequences (4K+), this becomes prohibitive.

**Approximate attention methods** (sparse, low-rank) reduce FLOPs but often don't achieve wall-clock speedup because they ignore memory access overhead.

## Key Contributions

### 1. IO-Awareness
- Account for reads/writes between GPU SRAM (fast, 19 TB/s, 192 KB/SM) and HBM (slow, 1.5-2 TB/s, 80 GB)
- Compute-bound FLOPs have improved faster than memory bandwidth
- Most Transformer operations are memory-bound

### 2. Tiling Algorithm
- Split Q, K, V into blocks that fit in SRAM
- Compute softmax incrementally with running statistics
- Never materialize full N×N attention matrix in HBM

### 3. Recomputation
- Store O (output) and softmax statistics (m, l) instead of S, P matrices
- Recompute attention matrix during backward pass
- Faster than reading from HBM despite extra FLOPs

### 4. Block-Sparse Extension
- Skip computation of zero blocks
- 2-4x faster than FlashAttention
- Scales to 64K sequence length

## Results Summary

### Training Speedup

| Model | Baseline | Speedup |
|-------|----------|---------|
| BERT-large (512) | MLPerf 1.1 Record | **1.15x** |
| GPT-2 small (1K) | HuggingFace | **3.0x** |
| GPT-2 small (1K) | Megatron-LM | **1.7x** |
| Long-Range Arena | Standard Attention | **2.4x** |

### Quality Improvements

| Achievement | Result |
|-------------|--------|
| GPT-2 perplexity improvement | 0.7 better (4K context) |
| MIMIC-III classification | 6.4 points lift |
| Path-X (16K seq) | 61.4% (first non-random) |
| Path-256 (64K seq) | 63.1% (first non-random) |

### Benchmark Performance

- Up to **3x faster** than standard attention for sequence lengths up to 2K
- Up to **20x more memory efficient**
- Block-sparse FlashAttention faster than all existing methods

## Technical Specifications

### A100 GPU Memory Hierarchy

| Memory | Bandwidth | Size |
|--------|-----------|------|
| SRAM (per SM) | 19 TB/s | 192 KB |
| HBM | 1.5-2 TB/s | 40-80 GB |

### IO Complexity Comparison

| Algorithm | HBM Accesses |
|-----------|--------------|
| Standard Attention | O(Nd + N²) |
| FlashAttention | O(N²d²/M) |
| Block-Sparse FlashAttention | O(N²d²s/M) |

Where:
- N = sequence length
- d = head dimension
- M = SRAM size
- s = sparsity ratio

## Related

- [[FlashAttention]] — The algorithm
- [[IO-Awareness]] — The core principle
- [[Tiling]] — Block-based computation
- [[Recomputation]] — Gradient checkpointing for attention
- [[Block-Sparse Attention]] — Approximate variant
- [[Attention]] — Standard attention mechanism
