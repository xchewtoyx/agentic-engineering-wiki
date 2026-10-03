---
type: concept
title: MAST Multi-Agent Failure Taxonomy
description: >
  Annotated traces sort multi-agent failures into system design, inter-agent
  misalignment and task verification, and targeted prompt or topology fixes
  give only modest gains.
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
an LLM annotator reaching κ = 0.77. The three categories partition the
taxonomy itself, so the shares show how failures distribute across those
categories. They do not compare system-caused failures against model-caused
ones. "Design matters more than the model" is the authors' interpretation,
not a measured comparison.

The authors also tried two targeted interventions on one framework (ChatDev)
with the underlying model fixed. Improved role specification in the prompts
gave +9.4 points, and a changed topology with stronger verification gave
+15.6 points. Both changed the prompts or the topology, so neither is a
controlled test of a single factor. The authors describe the gains as modest
and read them as a sign that deeper redesign is needed.

This is a peer-reviewed benchmark paper with good agreement figures, so the
category split is reasonably trustworthy for the frameworks it covered.

Read as a practitioner's checklist, the taxonomy points at the design and
verification layers, which you control. Where several agents act on the same systems, coordination is itself a source
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
