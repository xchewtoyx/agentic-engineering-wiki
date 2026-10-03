---
type: concept
title: Itemized Bullet Context
description: >
  Represent an evolving agent context as a set of small, individually
  addressable bullets with IDs and helpful/harmful counters, not one monolithic
  prompt, so updates and retrieval can be localized.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §3.1, §5, App. F"
---

An itemized bullet context stores accumulated knowledge — reusable strategies,
domain concepts, common failure modes — as a collection of structured bullets
rather than a single prose system prompt. It is the core representational
choice of [ACE's generator–reflector–curator loop](generator-reflector-curator-loop.md).

Each bullet has two parts:

- **Metadata** — a unique identifier plus counters recording how often the
  bullet was marked *helpful* or *harmful* when the agent used it.
- **Content** — one small unit of knowledge (a tactic, a schema fact, a
  pitfall).

This is close to a memory entry in agent-memory systems (compare
[Zettelkasten agent memory notes](../knowledge/zettelkasten-agent-memory-notes.md)), but the
usage counters turn the store into something the agent's own task outcomes can
grade: while solving a task the Generator flags which bullets helped or misled,
and that signal steers the next corrective update.

In ACE's published prompts a bullet renders as
`[ctx-00263] helpful=1 harmful=0 :: <content>`, and bullets are grouped under
named sections such as `strategies_and_hard_rules`,
`apis_to_use_for_specific_information`, `verification_checklist`, and
`formulas_and_calculations` (the first three appear in the AppWorld prompts,
the last in the FINER prompts). IDs and counters are managed by system code
and kept out of model-authored content (see the
[curator delta operation contract](curator-delta-operation-contract.md)).
How usage is attributed differs by prompt variant. In the FINER prompts the
Generator outputs the IDs it used (`bullet_ids`), and the
[Reflector](reflector-diagnostic-prompt-contract.md) returns a `bullet_tags`
list (helpful, harmful, or neutral per ID). In the AppWorld prompts the
Reflector is told to tag the bullets, but neither listed output schema has a
bullet field.

Why itemize instead of keeping one monolithic prompt:

- **Localization** — an update touches only the relevant bullets; unrelated
  knowledge is not re-emitted and so cannot be silently dropped (the mechanism
  behind [context collapse](context-collapse.md)).
- **Fine-grained retrieval** — the agent can attend to the most pertinent
  bullets rather than an undifferentiated block.
- **Incremental adaptation** — merging, pruning, and de-duplication become
  per-item operations (append, update by ID, embedding comparison) instead of
  regeneration, which is what makes
  [incremental delta updates](incremental-delta-context-updates.md) and
  [grow-and-refine maintenance](grow-and-refine-context-maintenance.md)
  possible.

Design implication: if a harness lets a model edit its own instructions or
memory, give the editable surface addressable units (IDs) and per-unit
provenance/usage signals; whole-document rewrites forfeit all three properties.

Itemization also enables **selective unlearning**. A learned context is
human-readable, and each lesson is a separate bullet, so a specific item can
be deleted when it turns out outdated, wrong, or subject to an erasure
obligation (for example GDPR right to erasure). Weight updates offer no such
surgical removal.
