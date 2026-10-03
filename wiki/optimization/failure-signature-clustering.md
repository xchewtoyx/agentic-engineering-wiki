---
type: concept
title: Cluster Failures by Signature Before Fixing
description: >
  Grouping failed traces by a verifier-grounded failure signature before
  proposing minimal fixes per group targets recurring mechanisms rather than
  one-off errors.
evidence: weak
sources:
  - title: "Self-Harness"
    resource: "Zhang et al. (Shanghai AI Lab), arXiv 2606.09498, 8 Jun 2026 (preprint) — https://arxiv.org/html/2606.09498v1"
  - title: "Agentic Harness Engineering (AHE)"
    resource: "Lin, Liu, Pan et al., arXiv 2604.25850, 28 Apr 2026, Agent Debugger (preprint) — https://arxiv.org/html/2604.25850v1"
---

A system that fixes failures one at a time tends to patch symptoms. Twenty
failed runs might reflect three underlying mechanisms, and a fix written for
one run may not generalise, or may collide with a fix written for another.

Two 2026 preprints on automatic harness improvement both group failures before
fixing them. Self-Harness clusters failed traces by a failure signature
grounded in the verifier's verdict, a step it calls weakness mining, and
proposes minimal targeted fixes per cluster rather than per trace. Agentic
Harness Engineering reaches the same place through
[trajectory distillation](agent-debugger-trajectory-distillation.md), whose
benchmark-level overview aggregates per-task root causes before any edit is
written. The pattern resembles incident problem management, where symptoms
are deduplicated before a root cause is pursued; that comparison is an
inference, not the papers' claim.

The evidence is weak: both are preprints, and their reported gains come from
whole pipelines, so the separate contribution of clustering is not isolated.

A usable signature is stable across runs and grounded in a check rather than
in a model's description, for example the failing component, the exit code or
error class, and the check that caught it. Aim each fix at a cluster, which
turns repeated corrections into the durable change described in
[fix the environment, not the output](../instructions/fix-the-environment-not-the-output.md).
The categories come from [error analysis](../evaluation/error-analysis-first.md),
each cluster still needs its originating step found by
[root-cause step localisation](../evaluation/root-cause-step-localisation.md),
and any resulting harness change should pass
[in-loop regression control](in-loop-regression-control.md).
