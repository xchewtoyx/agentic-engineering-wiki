---
type: concept
title: Context Adaptation
description: >
  Improve an LLM system by iteratively revising its inputs — system prompt,
  memory, strategies, evidence — from natural-language feedback on execution,
  instead of updating model weights.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §1–2.1, §5"
---

Context adaptation is the self-improving branch of
[context engineering](../context-engineering.md). The context is not assembled
once. It is a learned artifact that the system revises from its own
experience. The standard loop is:

1. An LM inspects the current context together with signals such as
   execution traces, reasoning steps, test or validation results.
2. It writes natural-language feedback on how the context should change.
3. The feedback is folded back into the context, and the cycle repeats.

Representative methods differ mainly in *what* the adapted context is.
[Reflexion](../orchestration/reflexion.md) adapts per-task reflections for agent planning.
[TextGrad](textual-gradients.md) applies gradient-like textual feedback to
prompts. GEPA iteratively rewrites a prompt from execution traces.
Dynamic Cheatsheet accumulates a test-time memory of strategies. ACE's
[generator–reflector–curator loop](generator-reflector-curator-loop.md)
evolves an itemized playbook.

There are two operating settings:

- **Offline**: optimize a system prompt on a training split, then ship it.
- **Online**: adapt test-time memory continuously while the agent runs.

Why adapt context rather than weights:

- **Interpretable**: developers can read, diff, and audit the learned
  artifact.
- **Fast to integrate**: new knowledge takes effect at runtime, with no
  training run.
- **Portable**: a context can be shared across models or modules of a
  compound AI system.
- Long-context models and context-efficient inference (e.g. KV-cache reuse)
  make large adapted contexts increasingly practical to deploy.

Two characteristic failure modes come from how the context is revised:
[brevity bias](brevity-bias.md) (the optimizer converges on short, generic
instructions) and [context collapse](context-collapse.md) (monolithic
rewrites erase accumulated detail). Both argue for
[incremental delta updates](incremental-delta-context-updates.md) over
regenerating the context.

The authors frame context adaptation as a continual-learning mechanism for
distribution shift and scarce training data. They present it as a flexible,
generally cheaper alternative to fine-tuning; that is a framing, not a
measured comparison in the paper.
Because the learned artifact is readable, it also supports selective
unlearning of specific items (see
[itemized bullet context](itemized-bullet-context.md)).
