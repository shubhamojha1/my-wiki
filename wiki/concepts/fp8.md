---
title: "FP8"
type: concept
tags: [gpu, deep-learning, precision, floating-point, nvidia, llm]
created: 2026-04-16
sources: [gpu-deep-learning-guide.md]
---

# FP8 (8-bit Float)

8-bit floating point format supported on NVIDIA RTX 40 series and H100 GPUs. Provides 2x faster data loading than FP16 with sufficient accuracy for many deep learning tasks.

## Format Specification

FP8 has two variants:

| Variant | Sign | Exponent | Mantissa | Range | Use Case |
|---------|------|----------|----------|-------|----------|
| E4M3 | 1 | 4 | 3 | ~±448 | Activations, weights |
| E5M2 | 1 | 5 | 2 | ~±57344 | Gradients |

### E4M3 (8 values per exponent)
- 4 exponent bits, 3 mantissa bits
- Better precision, narrower range
- For data that stays in moderate range

### E5M2 (16 values per exponent)
- 5 exponent bits, 2 mantissa bits
- Wider range, less precision
- For data with large dynamic range (gradients)

## Why FP8 Matters

### The Promise

| Metric | Improvement |
|--------|-------------|
| Data loading speed | 2x faster than FP16 |
| Cache capacity | 2x more data fits |
| Compute throughput | ~2x FP16 (RTX 4090: 0.66 PFLOPS) |
| Memory bandwidth | 2x effective |

**Context**: RTX 4090 FP8 compute exceeds the world's fastest supercomputer in 2007.

### The Challenge

Very low precision (especially E4M3) causes instability in transformers:
- Loss spikes
- NaN/Inf values
- Model collapse during training
- Nonsense output during inference

Research shows:
- Pure INT8 fails for LLMs
- Need mixed precision strategies

## Solutions for Stability

### LLM.int8() (From Microsoft's BitsAndBytes)

Key insight: Keep specific dimensions (outlier features) in FP16, quantize rest to INT8.

```python
# Pseudo-code concept
for weight_matrix in model.weights:
    # Find outlier columns (> threshold)
    # Keep outlier columns in FP16
    # Quantize remaining to INT8
```

Results:
- Same accuracy as FP16
- 2x memory savings
- 35% inference speedup

### FP8-Specific: Mixed Precision

Keep in FP16/FP32:
- Layer normalization
- Softmax
- Non-linear functions (GELU, SiLU)
- Embedding tables
- Output layers

Use FP8 for:
- Linear layer weight matrices
- Matrix multiplications
- Large tensor operations

## GPU Support

| GPU | FP8 Support |
|-----|-------------|
| V100 (Volta) | ✗ |
| RTX 20/30, A100 | ✗ |
| RTX 40 (Ada) | ✓ (E4M3 + E5M2) |
| H100 (Hopper) | ✓ (full E4M3 + E5M2) |

FP8 support began with Ada and Hopper (2022-2023).

## Why FP8 Over INT8?

### INT8 Problems
- Integer arithmetic (no decimal points)
- Difficult for layer norm, softmax, non-linearities
- Requires careful quantization (outlier handling)
- Not stable for training

### FP8 Advantages
- Floating point arithmetic
- Easier to use with existing code
- Natural for non-linearities
- Better for training (though still tricky)

### Evidence: Float vs Integer

From research on 4-bit inference scaling:

| Format | LLM Zero-Shot Accuracy |
|--------|------------------------|
| FP4 | Higher (bit-by-bit) |
| INT4 | Lower |

Float preserves more information per bit.

## Usage in Practice

### PyTorch (with TransformerEngine)

```python
import transformer_engine.pytorch as te

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.ModuleList([
            te.Linear(hidden_size, hidden_size, fuse_qkv=True)
            for _ in range(num_layers)
        ])
    
    def forward(self, x):
        with te.fp8_autocast(enabled=True):
            for layer in self.layers:
                x = layer(x)
        return x
```

### TensorRT-LLM

```python
from tensorrt_llm import BuildConfig

config = BuildConfig()
config.precision = 'fp8'
# Builds optimized FP8 engine
```

## Performance Targets

Expected speedup (FP8 vs FP16/BF16):

| Task | Speedup |
|------|---------|
| LLM inference | 1.5-2x |
| LLM training | 2-4x (if caches are fast) |
| Transformer (short seq) | 1.3-1.5x |

**Note**: 8-bit training performance depends on L1/L2 cache latency, which is proprietary.

## Current Status (2023)

FP8 training is **emerging but not yet mainstream**:
- Inference: Widely used (GPTQ, AWQ, LLM.int8)
- Training: Experimental, requires careful implementation
- Ecosystem: Improving (TransformerEngine, TensorRT-LLM)

**Recommendation**: Use FP8 for inference now, watch for training adoption.

## Related

- [[BF16]] — More stable alternative
- [[Tensor Cores]] — FP8 hardware support
- [[H100]] — Best FP8 performance
- [[RTX 4090]] — Consumer FP8 option
- [[GPU Deep Learning Guide]] — Source analysis
