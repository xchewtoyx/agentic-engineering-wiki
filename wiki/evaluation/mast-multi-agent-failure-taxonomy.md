---
type: concept
title: MAST Multi-Agent Failure Taxonomy
description: >
  Annotated traces show multi-agent failures come mostly from system design
  and inter-agent misalignment rather than the model, and targeted role or
  verification fixes give only modest gains.
evidence: strong
sources:
  - title: "Why Do Multi-Agent LLM Systems Fail?"
    resource: "Cemri, Pan, Yang et al., arXiv 2503.13657, NeurIPS 2025 Datasets and Benchmarks (MAST) — https://arxiv.org/abs/2503.13657"
---

When a system of cooperating agents fails, it is easy to blame the model. The
MAST (Multi-Agent System failure Taxonomy) study asked instead where such
failures actually come from, by annotating real traces.

The Berkeley-led team annotated 1,642 traces across seven multi-agent
frameworks and arrived at fourteen failure modes in three categories:

| Category | Share of failures |
|---|---|
| System design issues | 44.2% |
| Inter-agent misalignment | 32.3% |
| Task verification | 23.5% |

Annotation was reliable, with human inter-annotator agreement of κ = 0.88 and
an LLM annotator reaching κ = 0.77. The authors then tried targeted
interventions on one framework with model and prompt held constant: clearer
role specification gave +9.4% and stronger high-level verification gave
+15.6%. They describe these gains as modest and read them as a sign that
deeper redesign is needed.

This is a peer-reviewed benchmark paper with good agreement figures, so the
category split is reasonably trustworthy for the frameworks it covered.

Most failures sit in the design and verification layers, not in the model.
Where several agents act on the same systems, coordination is itself a source
of failure. That argues for
[single-threaded writes](../orchestration/single-threaded-writes.md), for
recording every cross-role decision on a
[shared task board](../orchestration/shared-task-board-coordination.md), and
for explicit [verification before done](../harness/verify-before-done.md).
MAST's categories give a vocabulary for incidents involving more than one
agent and a seed for your own [error analysis](error-analysis-first.md). The
step-level view is in
[root-cause step localisation](root-cause-step-localisation.md), and runtime
fault classes are in the
[agent runtime fault taxonomy](agent-runtime-fault-taxonomy.md).
