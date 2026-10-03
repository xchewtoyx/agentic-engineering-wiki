---
type: concept
title: Brevity Bias
description: >
  Prompt and context optimizers tend to converge on short, generic instructions
  that drop domain heuristics, tool-use guidance, and known failure modes, which
  hurts detail-hungry agent and domain tasks.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §1, §2.2"
---

Brevity bias is a failure mode of iterative
[context adaptation](context-adaptation.md). Many prompt optimizers reward
concise, broadly applicable instructions over the accumulation of knowledge,
and some treat brevity as a design goal. The abstraction can still score well
on a validation metric while discarding exactly what multi-step agents and
knowledge-intensive tasks depend on:

- domain-specific heuristics and tactics
- tool-use guidelines (API quirks, schemas, pagination rules)
- catalogues of common failure modes

Evidence: in a study of prompt optimization for unit-test generation (Gao
et al., 2025, cited by ACE), iterative methods repeatedly produced
near-identical generic instructions ("Create unit tests to ensure methods
behave as expected"). Diversity and domain detail disappeared.

Consequences:

- **Narrowed search**: successive candidates collapse to one generic form.
- **Error propagation**: optimized prompts inherit their seed's faults,
  because the compressed form has no room for the corrective detail.
- **Domain penalty**: agents, program synthesis, and financial or legal
  analysis succeed by *accumulating* task-specific insight, not compressing it.

The counter-stance (ACE's "playbooks, not summaries") is the authors'
position, not a general result. Unlike humans, who often benefit from concise
generalization, they argue LLMs are more effective with long, detailed
contexts and can distill relevance themselves at inference time. So keep
tactics in the context and let the model select. ACE itself names exceptions
(see [prompt evolution vs playbook accumulation](prompt-evolution-vs-playbook-accumulation.md)).

The stance is in tension with [lost in the middle](../context/lost-in-the-middle.md)
and with token budgets. Make a detailed context selectable rather than
monolithic: an [itemized bullet context](itemized-bullet-context.md) with
named sections, plus an instruction to use only the relevant parts. That
gets the detail without forcing every token to matter.

Do not confuse brevity bias with [context collapse](context-collapse.md).
Brevity bias is where an optimizer's *objective* drifts. Collapse is a
*mechanical* loss caused by rewriting the whole context at each step.
