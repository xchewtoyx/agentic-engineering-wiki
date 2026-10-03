---
type: concept
title: Inferential-Link Grounding Failure
description: >
  A synthesis can connect individually supported facts in a relationship that
  no cited source actually establishes.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Retrieval grounding does not prevent the model from inventing the relation
between retrieved facts. It may transfer a general statement to a specific
place, infer causation from topical proximity, or attach an irrelevant detail
to the subject. Every component fact can appear in context while the combined
claim remains unsupported.

Sentence-level citation entailment catches only part of this failure. Require
the evidence to support the scope and relationship asserted, not merely its
entities, and include this check among
[grounding quality dimensions](grounding-quality-dimensions.md). High-level
sensemaking still needs expert review when the relationship is consequential.
