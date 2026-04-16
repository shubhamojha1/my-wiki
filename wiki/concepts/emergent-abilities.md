---
title: "Emergent Abilities"
type: concept
tags: [machine-learning, nlp, scale]
created: 2026-04-05
sources: [Language Models are Few-Shot Learners.pdf]
---

# Emergent Abilities

Capabilities that appear in large language models at certain scale thresholds but are absent in smaller models, without being explicitly trained for those tasks.

## Definition

Phenomenon where model performance on certain tasks suddenly improves (or appears) as model size increases beyond a threshold, rather than gradually improving.

## Examples from GPT-3

- Arithmetic (addition, multiplication)
- Word unscrambling
- Bigram shift detection
- Novel reasoning tasks
- Cross-lingual translation

## Significance

Emergent abilities challenge traditional scaling assumptions — they suggest that scale doesn't just improve existing capabilities but unlocks qualitatively new ones.

## Controversy

Some argue emergent abilities are artifacts of evaluation:
- Metrics may not be smooth
- Benchmarks may not measure what we think
- Small model performance may be at random chance levels

## Implications

- Scale beyond certain thresholds can unlock unexpected capabilities
- Harder to predict model behavior from smaller models
- Safety properties may also emerge (or not) at scale

## Related

- [[Scaling Laws]] — The relationship between scale and performance
- [[GPT-3]] — First paper to highlight this phenomenon