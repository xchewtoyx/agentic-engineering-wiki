---
type: concept
title: Seven Harness Subsystems
description: >
  A harness has to cover seven subsystems (loop, LLM integration, tools,
  memory and context, safety and permissions, orchestration, extensibility),
  which gives a shared vocabulary for saying which layer broke.
evidence: weak
sources:
  - title: "Harness Engineering"
    resource: "Barbaste, Darrigol, Vu, Wiltberger (Wavestone AI Lab), arXiv 2609.00006, July 2026 preprint, §2.3 and Table 1 — https://arxiv.org/html/2609.00006v1"
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Lin, Liu, Pan et al., arXiv 2604.25850, 28 Apr 2026 preprint, editable component types — https://arxiv.org/html/2604.25850v1"
  - title: "Stop Comparing LLM Agents Without Disclosing the Harness"
    resource: "Zhang, Wang, Ge, Xu, Hamm, Reddy, arXiv 2605.23950, 7 May 2026 position preprint, ETCSOVG taxonomy — https://arxiv.org/html/2605.23950v1"
---

"The agent is broken" is not an actionable diagnosis. Once a team accepts that
an agent is [a model plus a harness](../agent-equals-model-plus-harness.md), it
still needs names for the parts of the harness, so that an incident can be
pinned to a layer and the right owner or fix can be found.

The Wavestone source-code study of eleven harnesses proposes seven canonical
subsystems:

1. the agent loop;
2. LLM (large language model) integration;
3. tools and actions, the layer that descends from the
   [agent-computer interface](agent-computer-interface.md);
4. memory and context;
5. safety and permissions;
6. orchestration;
7. extensibility.

Two other 2026 taxonomies overlap heavily with it. The Agentic Harness
Engineering (AHE) paper lists seven editable component types: system prompt,
tool descriptions, tool implementations, middleware, skills, sub-agent
configurations and long-term memory. A position paper on harness disclosure
proposes a seven-layer ETCSOVG scheme (Execution, Tool, Context, Scheduling,
Observability, Verification, Governance), which it pairs with a
[harness card](../evaluation/harness-card-disclosure.md) for benchmark results.
The Wavestone list has the advantage of being grounded in reading the source
code of real harnesses, and its later sections on memory (§9), permissions
(§10) and orchestration (§11) work as reference descriptions of how those
layers are built in practice.

The evidence is weak in the sense that all three taxonomies are fresh 2026
preprints without peer review, and none has been validated as a diagnostic
tool. Their agreement with each other is the main reason to trust the shape.

A practical use, offered as an implication rather than a sourced finding, is to
tag every incident or failed run with one of the seven subsystems, so recurring
faults can be counted per layer. Several patterns sit squarely on one layer:
the [layered agent permission stack](../security/layered-agent-permission-stack.md)
is the safety layer, and the
[harness memory strategy spectrum](../knowledge/harness-memory-strategy-spectrum.md)
is the memory layer.
