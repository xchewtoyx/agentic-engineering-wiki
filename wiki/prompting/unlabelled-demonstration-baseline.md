---
type: concept
title: Unlabelled Demonstration Baseline
description: >
  Pairing representative unlabelled inputs with random valid labels provides a
  strong baseline for measuring what ground-truth demonstrations add.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

A test-input-only zero-shot condition understates how much performance can be
obtained without labelled supervision. Construct a stronger baseline from
unlabelled in-distribution inputs, the true label set, and a recognizable
input-output pair format, but randomize the pairings. This preserves the major
structural and distributional signals while withholding the ground-truth
mapping.

Compare this condition with gold demonstrations in
[offline prompt evaluation](../evaluation/offline-prompt-evaluation.md). A small gap suggests
[task location](demonstrations-as-task-location.md); a large gap indicates that
correct pairings matter for this model-task combination. Call the condition
zero-shot only when access to unlabelled task data is allowed by the evaluation
contract.
