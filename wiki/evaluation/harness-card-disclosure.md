---
type: concept
title: Harness Cards
description: >
  Agent results should ship with a structured disclosure of the harness they
  ran in, plus measures of harness and model variance, so that score
  differences can be attributed to the right cause.
evidence: weak
sources:
  - title: "Stop Comparing LLM Agents Without Disclosing the Harness"
    resource: "Zhang, Wang, Ge, Xu, Hamm, Reddy, arXiv 2605.23950, 7 May 2026, §5 and Appendix A Table 3 (position preprint) — https://arxiv.org/html/2605.23950v1"
---

A benchmark score for "model X" is really a score for model X inside some
harness, on some infrastructure. When the harness is not reported, two results
cannot be compared, and an apparent model advantage may be a harness
advantage, as the evidence that the
[harness is a performance lever](../harness-as-performance-lever.md) shows.

A May 2026 position preprint proposes a fix modelled on model cards. Every
agent benchmark result would ship with a "Harness Card" describing the harness
against a seven-layer taxonomy it calls ETCSOVG: Execution, Tool, Context,
Scheduling, Observability, Verification and Governance. The layers overlap
with the [seven harness subsystems](../harness/seven-harness-subsystems.md).
The paper also asks for four quantities:

- per-model harness variance;
- per-harness model variance;
- the ratio of the two;
- any ranking reversals.

Its motivation is the size of harness effects it compiles from other work,
including a controlled three-by-three factorial in which harness-induced
variance was about 7.8 times model-induced variance.

The evidence is weak. This is a position paper, not an evaluation of whether
cards improve attribution, and several of its compiled swings were not traced
back to their primary sources.

The idea is useful even without adoption by benchmark publishers. When an
agent, or a change to its configuration, is evaluated internally, recording
which harness layers changed and on what container resources lets a later
reader tell harness effects from model or
[infrastructure effects](infra-failure-as-eval-failure.md). It generalises
the rule to
[compare (model, program, strategy) triples, not models alone](lm-pipeline-comparison-unit.md),
and it gives [reliable-lift](reliable-lift-not-mean-lift.md) comparisons the
context they need to be read.
