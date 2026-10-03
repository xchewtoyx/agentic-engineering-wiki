---
type: concept
title: Paired Demonstration Format
description: >
  Repeated input-output pairs act as a structural trigger that makes the task
  signals in few-shot demonstrations usable by the model.
sources:
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

The paired sequence structure of [in-context learning](in-context-learning.md)
examples can preserve most few-shot gains even when only one side of each pair
contains task-relevant information. Removing one side and concatenating only
inputs or only outputs performs near or below a zero-demonstration baseline.
The pair pattern appears to trigger continuation of the demonstrated task
structure, allowing [demonstration input distribution](demonstration-input-distribution.md)
or [demonstration output space](demonstration-output-space.md) to guide the
completion.

Format includes diversity and repetition, not just delimiters. Constant labels
or repeated identical inputs may behave like separators and change the pattern
the model perceives. Preserve varied pairs when testing a compact or partially
synthetic demonstration suite.
