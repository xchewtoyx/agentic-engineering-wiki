---
type: concept
title: Intermediate Artifact Evaluation
description: >
  Evaluating planning artifacts separately reveals whether a workflow fails in
  research and organization before final generation obscures the cause.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

When an agentic workflow creates an explicit plan or outline, score that
artifact before scoring the final output. Coverage measures over headings,
entities, or task-specific required elements can distinguish weak discovery
and organization from failures introduced during drafting.

Pair artifact-level metrics with end-output groundedness and expert review.
Automatic similarity against a mature human artifact is only a proxy: the
reference may embody many rounds of work that a one-pass system was never
expected to reproduce. A [research outline](../orchestration/research-outline-control-artifact.md)
is valuable partly because it supplies this observable checkpoint.
