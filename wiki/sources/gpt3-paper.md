---
title: "Language Models are Few-Shot Learners (GPT-3)"
type: source
tags: [machine-learning, nlp, gpt, language-model]
created: 2026-04-05
sources: [Language Models are Few-Shot Learners.pdf]
---

# Language Models are Few-Shot Learners (GPT-3)

## Paper Details

- **Authors**: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, et al. (OpenAI)
- **Published**: 2020 (NeurIPS)
- **Paper**: arXiv:2005.14165

## Summary

This paper introduces GPT-3, a 175-billion-parameter language model, and demonstrates that scaling language models dramatically improves task-agnostic few-shot performance. Rather than fine-tuning for each task, GPT-3 can perform new tasks by receiving examples in its prompt.

## Key Contributions

1. **Scale Demonstration**: 175B parameters — the largest language model at its time, trained on 570GB of text
2. **Few-Shot Learning**: Introduced zero-shot, one-shot, and few-shot prompting as a new paradigm
3. **Emergent Capabilities**: At scale, models exhibit abilities not present in smaller models
4. **Broad Evaluation**: Tested on numerous NLP benchmarks without task-specific training

## Training Data

- Common Crawl (filtered)
- WebText2
- Books1, Books2
- Wikipedia

## Evaluation Approach

- **Zero-shot**: Task description only
- **One-shot**: Task description + 1 example
- **Few-shot**: Task description + few examples
- Compared against fine-tuned models

## Results

GPT-3 achieved competitive or state-of-the-art results on many benchmarks in the few-shot setting, demonstrating that scale can unlock capabilities not seen in smaller models.

## Limitations Noted

- Factual inaccuracies and "hallucinations"
- Lack of grounding in real-world understanding
- Bias in generated content
- Potential for misuse
- Limited practical usefulness for many tasks

## Related

- [[GPT-3]] — The model this paper describes
- [[Few-Shot Learning]] — The paradigm introduced
- [[In-Context Learning]] — How the model learns from prompts
- [[Scaling Laws]] — The relationship between model size and performance