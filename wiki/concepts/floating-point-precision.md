---
title: "Floating Point Precision"
type: concept
tags: [gpu, floating-point, numerical-computation, precision, accuracy]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# Floating Point Precision

The accuracy limitations of finite-precision arithmetic. Critical for numerical stability in scientific computing and deep learning.

## Overview

### The Fundamental Problem

Floating point numbers have **finite precision**:
- Cannot represent all real numbers
- Rounding errors accumulate
- Operations are not perfectly associative

### The Smallest Number Problem

There exists ε such that:
```
1 + ε = 1  (ε is too small to affect 1)
```

But:
```
(ε + 1) - 1 = 0  (different result!)
ε + (1 - 1) = ε  (correct result!)
```

**This demonstrates non-associativity.**

## IEEE 754 Floating Point

### Format Structure

```
Sign Bit (1) | Exponent (8) | Mantissa (23)
     S              E            M
```

### Single Precision (FP32)

| Field | Bits | Range |
|-------|------|-------|
| Sign | 1 | ± |
| Exponent | 8 | -126 to +127 |
| Mantissa | 23 | ~7 decimal digits |
| Total | 32 | ~3.4 × 10^38 |

### Double Precision (FP64)

| Field | Bits | Range |
|-------|------|-------|
| Sign | 1 | ± |
| Exponent | 11 | -1022 to +1023 |
| Mantissa | 52 | ~15 decimal digits |
| Total | 64 | ~1.8 × 10^308 |

### Half Precision (FP16)

| Field | Bits | Range |
|-------|------|-------|
| Sign | 1 | ± |
| Exponent | 5 | -14 to +14 |
| Mantissa | 10 | ~3 decimal digits |
| Total | 16 | ~65504 |

## Non-Associativity Demonstration

### The Problem

```cuda
// Mathematically equivalent, numerically different
float a = 1e-8, b = 1.0, c = -1.0;

// Order 1: (a + b) + c
((1e-8 + 1.0) + -1.0) = 1e-8 + 0 = 1e-8  ✓ Correct

// Order 2: a + (b + c)
(1e-8 + (1.0 + -1.0)) = 1e-8 + 0 = 1e-8  ✓ Correct

// But with rounding:
((1e-8 + 1.0) + -1.0) = 1.0 + -1.0 = 0.0  ✗ Wrong!
(1e-8 + (1.0 + -1.0)) = 1e-8 + 0.0 = 1e-8  ✓ Correct
```

### Why It Happens

1. `1e-8 + 1.0` rounds to `1.0` (ε too small)
2. `1.0 + -1.0` = `0.0` exactly
3. Result: `0.0` instead of `1e-8`

### Impact on Large Sums

```cuda
// Horrible: Adding in random order
float sum = 0;
for (int i = 0; i < n; i++) {
    sum += large_array[i];  // Order varies
}
// Result: Nearly random!

// Better: Add smallest to largest
// Sorts array, adds from smallest
// Preserves more significant bits
```

## Numerical Stability

### Stable vs Unstable Algorithms

**Unstable**: Errors grow exponentially
```cuda
// Unstable recurrence
x[n] = 2.0 * x[n-1] - x[n-2];
// Small errors grow rapidly
```

**Stable**: Errors stay bounded
```cuda
// Stable: Kahan summation
float c = 0.0;  // Error compensation
for (int i = 0; i < n; i++) {
    float y = large_array[i] - c;
    float t = sum + y;
    c = (t - sum) - y;  // Compensate error
    sum = t;
}
```

### FP16 Challenges

```cuda
// FP16 range: [-65504, 65504]
// Gradient clipping often needed!

// Without clipping: gradient explosion
if (abs(grad) > 65504) grad = sign(grad) * 65504;

// Or use loss scaling
loss = loss * 256;  // Scale up
backward();
optimizer.step();
optimizer.zero_grad();
```

## GPU Floating Point Types

### Supported Types

| Type | Bits | Range | Accuracy |
|------|------|-------|----------|
| FP64 (double) | 64 | Very large | Highest |
| FP32 (float) | 32 | Large | High |
| FP16 (half) | 16 | Limited | Medium |
| BF16 | 16 | Large | Medium |
| TF32 | 19 | Large | High |
| FP8 (E4M3/E5M2) | 8 | Limited | Low |

### Tensor Core Precision Support

| GPU | FP64 | FP32 | FP16 | BF16 | TF32 | FP8 |
|-----|------|------|------|------|------|-----|
| V100 | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| TITAN V | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| A100 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| RTX 30 | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| RTX 40 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| H100 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Numerical Accuracy in Practice

### Matrix Multiplication

```cuda
// FP32 accumulation vs FP16
// FP16 intermediate: faster but less accurate
// FP32 accumulation: more accurate

// CUBLAS does FP16 compute with FP32 accumulation
// This is "mixed precision"
```

### Summation

```cuda
// Naive: Error grows
float sum = 0;
for (int i = 0; i < n; i++) {
    sum += data[i];
}

// Better: Kahan summation
float sum = 0.0f;
float c = 0.0f;  // Compensation
for (int i = 0; i < n; i++) {
    float y = data[i] - c;
    float t = sum + y;
    c = (t - sum) - y;
    sum = t;
}

// Best (parallel): Pairwise summation
// Recursively pair and add
// O(log n) error growth instead of O(n)
```

### Numerical Gradient Issues

```cuda
// Numerical gradient calculation
float eps = 1e-4f;  // Too small for FP16!
float grad = (f(x + eps) - f(x - eps)) / (2 * eps);

// eps * x might be invisible in FP16 if x is large
// Solution: Use relative epsilon
float rel_eps = eps * max(1.0f, abs(x));
```

## Compiler Optimizations Gone Wrong

### Early C Compilers

Early compilers assumed floating point was associative for optimization:

```c
// Source
a = b + c + d + e;

// Compiler might transform to
a = (b + c) + (d + e);  // Different order!
a = (d + c) + (b + e);  // Even more different!

// With rounding, results differ!
// Early Fortran compilers destroyed scientific code
```

### Modern Compilers

Modern compilers are more conservative but still optimize:

```cuda
// -O3 might:
// 1. Reorder operations
// 2. Use FMA (fused multiply-add)
// 3. Vectorize with different precision

// Use -fp-model precise for strict IEEE
nvcc -fp-model precise ...
```

### FMA and Precision

```cuda
// FMA: Single rounding instead of two
// a * b + c

// Without FMA:
t = a * b;     // Round
result = t + c;  // Round again

// With FMA:
result = fma(a, b, c);  // One round

// FMA can be more OR less accurate depending on case
```

## Deep Learning Implications

### FP16 Training

```cuda
// Mixed precision training
// FP16 weights, activations, gradients
// FP32 master weights

model = model.cuda().half()  // FP16 model
optimizer = torch.optim.Adam(model.parameters())

with torch.cuda.amp.autocast():
    output = model(input)
    loss = loss_fn(output, target)

scaler.scale(loss).backward()
scaler.step(optimizer)
```

### Gradient Scaling

```cuda
// Problem: Small gradients vanish in FP16
// Solution: Scale loss, unscale gradients

scaler = GradScaler()

for data, target in dataloader:
    optimizer.zero_grad()
    
    # Scale up to prevent vanishing
    with autocast():
        output = model(data)
        loss = loss_fn(output, target) * scaler_scale
    
    scaler.scale(loss).backward()
    
    # Unscale and clip
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm)
    
    scaler.step(optimizer)
    scaler.update()
```

### BF16: No Scaling Needed

```cuda
// BF16 has same range as FP32
// No loss scaling needed!

with autocast(dtype=torch.bfloat16):
    output = model(input)
    loss = loss_fn(output, target)

loss.backward()  // No scaler needed!
```

## Best Practices

1. **Use FP32 for accumulation** — Sums, reductions
2. **Use double for critical scientific code** — FP64
3. **Add smallest to largest** — For stable summation
4. **Use Kahan summation** — For minimal error
5. **Test with known values** — Verify numerical stability
6. **Monitor for NaN/Inf** — Precision issues cause explosions
7. **Use loss scaling for FP16** — Prevents gradient underflow

## Related

- [[BF16]] — Range-extended FP16
- [[TF32]] — NVIDIA's fast FP32
- [[FP8]] — Low precision format
- [[Tensor Cores]] — Hardware with precision modes
