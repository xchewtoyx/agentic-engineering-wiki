---
type: concept
title: Demonstrations as Task Location
description: >
  Few-shot examples may activate a task correspondence learned during
  pretraining rather than teach the demonstrated mapping at inference time.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

When performance survives randomized example labels, demonstrations are likely
locating a pretrained capability rather than supervising a new input-output
rule. They still help by exposing the relevant input distribution, output
space, and task format, but the semantic correspondence comes from associations
already encoded in the model.

Treat this as a failure boundary for [in-context learning](in-context-learning.md).
If the task semantics were absent from pretraining—as in novel synthetic
mappings or unfamiliar outputs—prompt examples may not be enough. Use a
[demonstration mapping ablation](demonstration-mapping-ablation.md) to test the
assumption, then consider labelled supervision and the
[fine-tuning decision](../fine-tuning-decision.md) when the intended mapping does
not emerge.
