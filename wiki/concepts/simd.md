---
title: "SIMD"
type: concept
tags: [gpu, cpu, vector-processing, parallelism]
created: 2026-04-16
sources: [cs179_2026_lec02.pdf]
---

# SIMD

Single Instruction, Multiple Data. A class of parallel computers (Flynn's taxonomy) where a single instruction operates on multiple data elements simultaneously using vector registers.

## Overview

SIMD describes instructions that perform the same operation on multiple registers at once. For example, adding a scalar to multiple values in parallel.

**Example use case**: Brightness adjustment across an image — one instruction increases all pixel values simultaneously.

## SIMD in CPUs

CPUs include SIMD instruction sets:
- **x86**: SSE, AVX, AVX-512
- **ARM**: NEON

Video codecs (x264/x265) heavily rely on SIMD for encoding/decoding speed.

## SIMD in GPUs

GPUs use SIMD but abstract it behind [[SIMT]]. The hardware executes SIMD instructions, but the programming model exposes threads.

## Vectorization

Converting an algorithm to use SIMD is called "vectorizing". Not all algorithms benefit or can be vectorized (e.g., parsing with branching).

**Trade-offs**:
- Performance gain comes at cost of additional power and heat
- Code complexity increases
- May not be worth it for small gains

Modern compilers (GCC, LLVM/Polly) increasingly auto-vectorize code, but manual vectorization remains important.

## Related

- [[SIMT]] — Looser extension of SIMD used by GPUs
- [[GPU Computing]] — Broader context
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — Source lecture
