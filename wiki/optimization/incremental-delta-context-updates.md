---
type: concept
title: Incremental Delta Context Updates
description: >
  Evolve an agent's context by emitting small sets of candidate bullets to merge
  into the existing store instead of regenerating the whole context each step,
  keeping update output small and avoiding knowledge loss.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §3, §3.1, §4.7, App. A.3, A.5"
---

A delta context is a compact set of candidate bullets distilled from recent
experience. A Reflector distills the lessons and a Curator emits them as
additions. Deterministic system code, not an LLM, then merges them into the
existing [itemized bullet context](itemized-bullet-context.md). The system
never asks an LLM to rewrite the full context. The LLM roles only propose
additions, and the merge step applies them against stable bullet IDs.

What this buys over full rewrites:

- **Cost and latency** — each update *emits* only the delta, not the whole
  (possibly very long) context, and the merge is cheap deterministic code. So
  output tokens and merge work per step stay small as the context grows.
  Input cost does not stay constant. The Generator and Curator still read the
  full, growing playbook on every step, so input/prefill tokens per step grow
  with context size unless prefix caching or pruning absorbs them (see
  [context adaptation cost profile](context-adaptation-cost-profile.md)).
  Against full-rewrite and prompt-evolution baselines, the measured result
  was much lower total adaptation tokens and latency, not flat per-step
  cost.
- **Preservation** — past knowledge is never routed through a generation step
  that might summarize it away, which is the root cause of
  [context collapse](context-collapse.md).
- **Scalability** — contexts can keep accumulating detail for long-horizon or
  domain-heavy tasks without each update becoming a bigger, riskier rewrite.
- **Lower variance** — a localized merge has a bounded blast radius; a
  monolithic rewrite can change any part of the context at once.

Because merging is a deterministic, non-LLM operation, the expensive judgment
(what was learned) is separated from the bookkeeping (where it goes). Unbounded
appending is then held in check by
[grow-and-refine maintenance](grow-and-refine-context-maintenance.md).

Ablation evidence (App. A.5; AppWorld test-normal only, DeepSeek-V3.1): ReAct
base averaged 53.3. ACE *without* incremental updates reached 56.9, and
*with* them 70.3. On this benchmark most of the gain depended on not
rewriting the context. The authors read this as delta updates preserving
information otherwise lost to [context collapse](context-collapse.md). The
ablation has not been reported on other benchmarks.
