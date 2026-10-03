---
type: concept
title: Grow-and-Refine Context Maintenance
description: >
  Keep an incrementally growing bullet context compact by appending new bullets,
  updating existing ones in place, and periodically de-duplicating via semantic
  embeddings, either proactively or lazily.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §3.2, App. A.4, A.6"
---

[Incremental delta updates](incremental-delta-context-updates.md) only add;
grow-and-refine is the complementary housekeeping step that keeps an
[itemized bullet context](itemized-bullet-context.md) relevant as it grows.

Mechanics:

1. Bullets carrying **new identifiers are appended**.
2. **Existing bullets are updated in place** — e.g. their helpful/harmful
   counters incremented.
3. A **de-duplication** pass compares bullets by **semantic embedding**
   similarity and prunes redundant ones.

Refinement timing is a latency/accuracy knob:

- **Proactive** — refine after every delta; the context is always compact, at
  the cost of extra work per step.
- **Lazy** — refine only when the context would exceed the window; cheaper on
  average, but the context carries redundancy until the trigger fires.

The combination aims for contexts that expand adaptively, stay interpretable
(each bullet is human-readable and traceable to its usage counts), and avoid
the variance of monolithic rewriting. Embedding-based de-dup is a
non-LLM step, so it cannot introduce the summarization loss that
[context collapse](context-collapse.md) describes — though a too-loose
similarity threshold can still merge bullets that differ in a detail that
matters. Compare the eviction-driven alternative, where pressure on the window
triggers summarization ([memory pressure eviction](../knowledge/memory-pressure-eviction.md)),
which trades this preservation for a hard size bound.

Knobs and sensitivity (App. A.6; FiNER only, base 70.7):

- **De-dup similarity threshold** (how aggressively a new bullet merges into
  an existing one): 50% → 77.0, 70% → 73.9, 90% → 78.6. Every setting beat
  base, and the authors call the effect mild. But 70% was about 4.7 points
  below 90%, so sweep this knob on your own task rather than assume any
  value works.
- **Pruning trigger** (maximum context length before older or low-utility
  bullets are merged or pruned): 10K → 78.6, 50K → 78.4, 100K → 78.3. Stable
  on this task. The authors' interpretation (not separately measured) is that
  pruning mostly removes stale or harmful fragments and keeps the core
  reusable strategies.

The refine step *can* also filter entries whose metadata flags them as
potentially harmful. The authors call it a "first line of defense" in
[context adaptation noise robustness](context-adaptation-noise-robustness.md).
