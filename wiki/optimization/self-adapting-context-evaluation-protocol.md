---
type: concept
title: Self-Adapting Context Evaluation Protocol
description: >
  Evaluate a system that rewrites its own context by predicting before
  updating on each online sample, using the same model for every role, and
  reporting with and without labels against a no-adaptation baseline.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §4.1–4.4, §4.6–4.7, App. A.4–A.6"
---

Evaluating [context adaptation](context-adaptation.md) needs controls that a
fixed-prompt eval doesn't, because the system under test changes during the
test.

**Two settings, two protocols.**

- **Offline:** adapt on the train split (possibly over several epochs), freeze
  the context, and score the test split once (pass@1).
- **Online:** walk the test split in sequence. For each sample, *predict with
  the current context first, then update the context from that sample*.
  Updating before predicting leaks the sample's own feedback into its answer.
  Use the **same shuffled order** for every method, so all methods see the
  same sequence (online adaptation can be order-sensitive).

**Isolate the context effect.**

- Run Generator, Reflector, and Curator on the **same model**. The authors
  do this to prevent knowledge transfer from a stronger Reflector or Curator
  to a weaker Generator, which would confound the gain from context
  construction itself.
- Build every method on the same base agent (e.g. the official ReAct harness)
  with identical setups. Treat externally engineered agents, such as
  leaderboard entries, as context only, not as baselines.
- Report a **no-adaptation baseline**. Adaptation can regress below it (see
  [feedback dependence](context-adaptation-feedback-dependence.md)).
- Report **with and without ground-truth labels** available to the
  reflection step, since deployments usually lack labels.

**Ablate the loop's parts.** On AppWorld (DeepSeek-V3.1), each of the
following added measurable gain. The first three are four-split averages from
§4.6. The incremental-update row comes from a separate App. A.5 ablation on
test-normal only, so it isn't directly comparable:

| Added component | Average-score gain |
|---|---|
| Dedicated Reflector with iterative refinement | about +1.7 |
| Multi-epoch offline adaptation | about +2.6 |
| Offline warmup before online adaptation | about +3.4 |
| Incremental delta updates (separate ablation) | +13.4 |

**Probe robustness.** Measure sensitivity to Reflector quality and inject
harmful reflections at a controlled rate
([noise robustness](context-adaptation-noise-robustness.md)). Sweep the
refinement-round, de-dup, and pruning knobs to confirm that gains don't hinge
on fine tuning.

**Report cost.** Count adaptation latency, rollouts, and tokens per stage
alongside accuracy ([cost profile](context-adaptation-cost-profile.md)).
These are offline regression criteria for iterating the adaptation harness
itself. They are not runtime monitoring.
