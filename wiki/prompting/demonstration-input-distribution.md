---
type: concept
title: Demonstration Input Distribution
description: >
  Few-shot demonstrations teach the model which input distribution the current
  task belongs to, independently of whether their labels are correct.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

An [in-context learning](in-context-learning.md) example conveys more than an
input-to-output rule: its input tells the model what kind of text the task will
operate on. Controlled ablations found substantial losses when task inputs in
demonstrations were replaced with length-matched out-of-distribution text even
though the label set and paired format remained intact. Thus example selection
should preserve the production input distribution, not merely reuse the right
labels or schema.

This signal is not equivalent to repeating the current input. Repetition can
turn a constant input into a structural separator and distort the sequence
pattern. Sample varied, representative inputs and test the selection through
[offline prompt evaluation](../evaluation/offline-prompt-evaluation.md).
