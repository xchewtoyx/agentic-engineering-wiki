---
type: concept
title: Section-Scoped Evidence Retrieval
description: >
  Retrieve evidence separately for each outline section so long-form synthesis
  stays grounded without fitting the entire reference set into one context.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Use each section and its descendant headings from a
[research outline](../orchestration/research-outline-control-artifact.md) as a query against the
collected reference set. Generate sections from their most relevant evidence
in parallel, then reconcile repetition and produce the lead summary after
concatenation. This turns an outline into a retrieval partition and avoids
placing every source into every generation context.

Section-local grounding trades global context for tractability. The final
coherence pass must remove duplicated claims and reconcile terminology without
discarding [citation-backed support](../harness/citation-backed-agent-answers.md).
