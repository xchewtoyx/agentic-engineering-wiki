---
type: concept
title: Curator Delta Operation Contract
description: >
  Prompt a Curator to emit only new, non-redundant playbook additions as typed
  JSON operations (type, section, content), never a regenerated playbook,
  leaving IDs and counters to deterministic system code.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §3, §3.2, App. F, Figs. 11, 14"
---

The Curator in the
[generator–reflector–curator loop](generator-reflector-curator-loop.md) turns
a [Reflector diagnosis](reflector-diagnostic-prompt-contract.md) into
[incremental delta updates](incremental-delta-context-updates.md). Its prompt
contract is what keeps the model from rewriting the whole context.

**Inputs.** The two published Curator prompts take different inputs:

- **AppWorld (Fig. 11):** the question context, the current playbook, the
  Generator's final generated code, and the current reflections (passed as
  `guidebook`).
- **FINER (Fig. 14):** the recent reflection, the current playbook, the
  question context, and a **training-context** block. That block gives the
  total token budget, training progress ("sample i of N"), and current
  playbook stats. The paper does not ablate it. Its presumable purpose is to
  let the Curator calibrate how much to add.

**Instructions that matter.**

- Identify ONLY new insights, strategies, or mistakes that are missing from
  the current playbook. Add something only if it is a "perfect complement",
  not a restatement.
- "Do NOT regenerate the entire playbook — only provide the additions needed."
- Quality over quantity: a focused, well-organized playbook beats an
  exhaustive one.
- Return an empty `operations` list when nothing is worth adding. A no-op must
  be a legal output.
- The reflection used ground truth that "will NOT be available when the
  playbook is being used". Additions must help *future* predictions without
  that signal.
- For coding tasks (AppWorld), carry API output-format and schema
  clarifications from the reflection into the playbook.
- Respond with pure JSON, because code parses the output. The FINER prompt
  adds a "CRITICAL" line: valid JSON only, no markdown formatting or code
  blocks.

**Output schema.** `reasoning` plus `operations`, where each operation has
`type`, `section`, and `content`, in both variants. In the published prompts
the only operation type is **ADD**. Sections are named, so each addition lands
in a stable region of the playbook. The AppWorld prompt shows
`strategies_and_hard_rules`, `apis_to_use_for_specific_information`, and
`verification_checklist`. The FINER prompt shows
`formulas_and_calculations`.

**Model writes content, system writes bookkeeping.** The model never assigns
bullet IDs or helpful/harmful counters. A deterministic merge step adds those.
This keeps metadata trustworthy. Because deltas are itemized, the authors
note that several can be merged in parallel. Their experiments use batch
size 1.
Redundancy is controlled in two layers. First, at the prompt level, the
Curator is told to admit only insights missing from the current playbook and
never restatements. Second, after the merge,
[grow-and-refine maintenance](grow-and-refine-context-maintenance.md) runs an
embedding-based de-dup pass that catches near-duplicates the Curator let
through.
