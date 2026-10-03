---
type: concept
title: Skill Library
description: >
  Persist newly composed skills that proved useful so later tasks can reuse
  them as first-class tools instead of rediscovering the composition.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), App. B.1, §3.1"
---

When an agent frequently chains the same tools, those transitions are
candidates for composition into a larger composite tool. Voyager-style systems
go further with a **skill manager**: newly created skills (often programs) that
helped complete a task are added to a skill library — conceptually an evolving
extension of the [tool inventory](../harness/tool-inventory.md) — for reuse on future
tasks.

This is external memory for capabilities, not just facts: the harness grows the
action repertoire from successful trajectories. Pair with
[tool selection ablation](../evaluation/tool-selection-ablation.md) so the library stays
useful rather than accumulating unused or unreliable skills.

Close relatives store other reusable units distilled from trajectories:
induced workflows (Agent Workflow Memory), cached plan templates (agentic plan
caching), or itemized strategy bullets (ACE). See
[prompt evolution vs playbook accumulation](../optimization/prompt-evolution-vs-playbook-accumulation.md)
for where these sit among context-adaptation designs.
