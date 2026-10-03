---
type: concept
title: Demonstration Output Space
description: >
  Few-shot outputs establish the label or answer distribution a model should
  generate, even when their pairings with inputs are incorrect.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

In direct inference, demonstrations expose the model to the set and
distribution of outputs expected at test time. Controlled replacements of
task labels with arbitrary English words caused substantial losses even when
the inputs and pair structure were retained. The useful signal can therefore
be the output vocabulary and distribution rather than the exact
input-to-output mapping.

The effect depends on the inference contract. It is strong when the model must
generate a label, but small when a channel-style system conditions on candidate
labels that are already supplied. Choose examples according to what the model
must produce, and treat output-space coverage as distinct from
[demonstration input distribution](demonstration-input-distribution.md).
