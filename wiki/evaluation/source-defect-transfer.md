---
type: concept
title: Source Defect Transfer
description: >
  A grounded generator can faithfully reproduce promotional tone, dominant
  viewpoints, staleness, and other defects present in retrieved sources.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Retrieval constrains generation to evidence but does not make that evidence
neutral, current, or representative. A well-cited output can inherit emotional
language, promotional framing, stale facts, and dominant-viewpoint bias from
its source set. Diverse questioning cannot recover perspectives absent from
the search environment.

Treat source-set balance and post-retrieval content sifting as independent
harness responsibilities. Audit them alongside entailment under
[grounding quality dimensions](grounding-quality-dimensions.md); citation
presence alone cannot distinguish faithful grounding from faithful propagation
of flawed source material.
