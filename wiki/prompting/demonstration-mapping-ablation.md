---
type: concept
title: Demonstration Mapping Ablation
description: >
  Randomizing demonstration labels tests whether few-shot gains come from the
  intended input-output rule or from other prompt signals.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

To test whether an [in-context learning](in-context-learning.md) prompt teaches
the intended rule, replace each demonstrated output with a random member of the
true output set while preserving the inputs, output distribution, and pair
format. If performance remains close to the gold-demonstration condition, the
gain cannot primarily come from learning the demonstrated mapping.

Across natural-language classification and multiple-choice tasks, this
ablation often preserved most few-shot improvement, while model and dataset
exceptions remained. The result is a diagnostic, not a license to use wrong
examples: synthetic mappings, open-set generation, and tasks whose labels lack
strong pretrained associations may behave differently. Run the ablation on the
actual model and task, alongside separate tests of
[demonstration input distribution](demonstration-input-distribution.md),
[demonstration output space](demonstration-output-space.md), and
[paired demonstration format](paired-demonstration-format.md).
