---
type: concept
title: Context Adaptation Cost Profile
description: >
  Token cost of self-adapting contexts splits between an adaptation stage,
  where prompt evolution is dominated by candidate validation while delta
  playbooks stay cheap, and a serving stage, where longer playbooks cost more
  per request unless prefix caching absorbs them.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §4 (cost analysis, KV cache reuse), §4.7, Table 4, App. A.3"
---

[Context adaptation](context-adaptation.md) has two separate cost stages, and
each design choice moves cost between them.

**Adaptation stage (building the context).** In an offline AppWorld
comparison (App. A.3: ACE with 1 epoch and 1 Reflector round), a GEPA-style prompt evolver ([DSPy](dspy-compiler-three-stages.md),
heavy setting) spent 204M input tokens and 1.87M output tokens. ACE's
[generator–reflector–curator loop](generator-reflector-curator-loop.md) spent
39M and 0.31M: about 81% and 84% less, despite running about 43% more rollouts.
Two things drive the gap:

- **The validation loop dominates prompt evolution.** Each candidate prompt is
  re-scored on a held-out set; that accounted for 139M of the evolver's 204M
  input tokens. Selecting among whole candidates is expensive. Accumulating
  edits needs no candidate selection.
- **Delta updates keep output small.** The Curator emits only additions
  ([incremental delta updates](incremental-delta-context-updates.md)), not a
  regenerated prompt, so output tokens stay low. Input is a different matter:
  the Generator and Curator read the whole current playbook on every step,
  so input/prefill per step grows as the playbook grows. In this run, per
  rollout, ACE used about 19K input tokens versus about 140K for the evolver.
  Within ACE, the Generator dominated input (31M); the Reflector (4.7M) and
  Curator (3.6M) were small.

**Serving stage (using the context).** The trade reverses. A rich playbook
makes every request longer: about 25K input tokens per rollout versus about
11K for the evolved short prompt, roughly 2.2× more. Output length barely
changes.

**Mitigation: prefix caching.** A frozen playbook is a stable prefix shared
across requests, so provider prompt/KV caching can serve most of it. In the
paper's evaluation-stage study (OpenAI API, GPT-5.1, default prompt caching),
about 92% of ACE's input tokens were cache hits, cutting billed input cost by
about 83%. That figure is for evaluation, not for online adaptation. With
per-sample online updates the prefix changes each step, so expect a lower hit
rate (an inference; not measured). Design implication: put the adapted
context where it stays byte-identical across requests (the
[static part of the prompt](../context/static-vs-dynamic-prompt-content.md)), and batch
its updates so the cache is not invalidated on every step.

The general rule: choose between a short evolved prompt and a long
accumulated playbook on serving volume × cache hit rate, not only on
adaptation cost or accuracy.

Headline §4.7 comparison (offline AppWorld vs GEPA, Table 4(a)): 82.3% lower
adaptation latency (9,517 s vs 53,898 s) and 75.1% fewer rollouts (357 vs
1,434). The appendix's one-epoch token breakdown above used more rollouts but
still far fewer tokens. The authors attribute both results to delta updates
plus non-LLM merging and de-duplication.

**Online:** compared with a full-rewrite memory (Dynamic Cheatsheet,
cumulative) on financial tagging, delta-based adaptation cut adaptation
latency from 65,104 s to 5,503 s (−91.5%) and token cost from $17.7 to $2.9
(−83.6%). This is consistent with full rewrites being expensive per
update, though the paper reports totals rather than a per-update
breakdown.

**Longer context need not mean proportionally higher serving cost.**
Serving stacks increasingly reuse, compress, or offload KV caches for
frequently reused segments, so prefill need not be paid again on every
request. The authors project that this will keep lowering amortized
long-context cost. Budget a context-rich design on expected cached cost, not
raw token count, and check the cache hit rate actually achieved.
