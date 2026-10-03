---
type: concept
title: Meta-Training Simple-Cue Bias
description: >
  Meta-training for in-context learning can make a model rely on easy prompt
  cues such as pair structure and token distributions instead of exact mappings.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

Models meta-trained across supervised tasks with an explicit in-context
learning objective can lean more heavily on simple surface cues than on the
demonstrated input-to-output relation. In controlled experiments, pair format
became more influential while correct mappings became less influential; which
distribution mattered depended on whether inference generated outputs or
conditioned on candidate outputs.

Do not assume that a model advertised or tuned for few-shot use interprets
examples semantically. Use [component-level harness ablation](../evaluation/component-level-harness-ablation.md)
to vary mappings, [paired demonstration format](paired-demonstration-format.md),
inputs, and outputs separately before attributing gains to task learning.
