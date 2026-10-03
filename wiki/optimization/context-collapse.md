---
type: concept
title: Context Collapse
description: >
  When an LLM monolithically rewrites an accumulated context at each adaptation
  step, it can abruptly compress thousands of tokens of learned detail into a
  short summary, which in an observed case dropped accuracy below the
  no-adaptation baseline.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §1, §2.2, Fig. 2, §3, App. C.2"
  - title: "Hermes Agent docs: Curator"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/user-guide/features/curator"
---

Context collapse is the failure where an evolving context (a learned system
prompt, a test-time memory, an agent's lessons file) is regenerated in full by
an LLM at every update, and one rewrite suddenly compresses it into a much
shorter, less informative summary. Accumulated knowledge is erased rather than
preserved.

Worked case (Dynamic Cheatsheet on AppWorld):

| Point in adaptation | Context size | Accuracy |
|---|---|---|
| Step 60 | 18,282 tokens | 66.7 |
| Next step | 122 tokens | 57.1 |
| No adaptation | none | 63.7 |

One rewrite discarded more than 99% of the context. Accuracy fell *below* the
no-adaptation baseline, so the adaptive system did worse than doing nothing.

Dynamic Cheatsheet has two update modes, and both rewrite end to end.
Cumulative mode (DC-CU) regenerates the full cheatsheet each step.
Retrieval-synthesis mode (DC-RS) writes a new summary from retrieved past
examples. Under either mode, detail can erode gradually or vanish in one step.

The authors argue collapse is not specific to that method but "a
fundamental risk of end-to-end context rewriting with LLMs". The evidence
shown is the Dynamic Cheatsheet case. The working hypothesis is that a
"rewrite this, incorporating the new lesson" step always carries
summarization pressure, so a larger accumulated context has more to lose in
any single rewrite. Collapse can be abrupt, as in the case above, so a
smoothed average-quality trend may not warn before it happens.

Design countermeasures:

- Never route the whole accumulated context through a generation step. Use
  [incremental delta updates](incremental-delta-context-updates.md) merged by
  deterministic code.
- Give the context addressable units
  ([itemized bullet context](itemized-bullet-context.md)) so an edit cannot
  touch unrelated knowledge.
- Do redundancy control with non-generative operations such as embedding
  de-dup ([grow-and-refine](grow-and-refine-context-maintenance.md)), not
  "summarize and replace".
- In offline regression checks of a self-updating harness, track context size
  per step. A sudden large drop is a collapse signature worth gating on.

The lesson generalises to any summary that replaces its source. It is why
[safeguarded compaction](../context/safeguarded-compaction.md) keeps the full
history and audits its summaries, why debuggers do better with
[raw traces than summaries](raw-traces-over-summaries.md), and it bears on
where a harness sits on the
[memory strategy spectrum](../knowledge/harness-memory-strategy-spectrum.md).
It applies directly to agents that write and consolidate their own memory or
skills. Hermes Agent's Curator, for example, can optionally run a model-based
consolidation pass over agent-made skills, which is exactly the operation
that can collapse, and a plausible source of
[self-authored skill drift](../instructions/self-authored-skill-drift.md). For
an agent's own runbooks or lessons, append itemised entries and merge them by
rule rather than letting a model rewrite the whole document.

Related but distinct: [brevity bias](brevity-bias.md) (an optimizer drifting
toward short prompts) and summarization-on-eviction in
[memory pressure eviction](../knowledge/memory-pressure-eviction.md). There, compression is
a deliberate response to a hard window limit rather than a side effect of
every update.
