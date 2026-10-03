---
type: concept
title: Tacit Knowledge Erosion Under AI-Assisted Work
description: >
  Coding and operations agents accelerate the loss of institutional knowledge that engineers used to
  accumulate as a side effect of personally authoring, debugging, and reviewing their systems.
sources:
  - title: "Observability Engineering"
    resource: "Observability Engineering, 2nd ed. (Majors, Fong-Jones, Miranda), ch. 10"
---

Senior engineers historically accumulated institutional knowledge — service topology, naming aliases, which dependencies are flaky, recent incident history, which endpoints matter to the business — "for free," as a side effect of writing, debugging, and reviewing code for years. That knowledge then seeded the informal context new teammates absorbed by osmosis.

Agent-assisted development breaks this loop. As agents write more code with less line-by-line review and pipelines automate further, fewer humans live through the debugging cycles and postmortems that generated the context as a byproduct (the human-side mirror of [cognitive debt](cognitive-debt-in-agent-synthesized-code.md)). Meanwhile the agent itself starts every task with zero tacit context: it cannot pick up unwritten knowledge by sitting near experienced colleagues, only what is in its prompt, tools, and retrievable stores. The informal layer erodes faster than most teams build an explicit replacement — and the question "can someone not involved operate this system safely?" gets sharper as more of that someone is an agent.

The response is to treat the context layer — topology, naming conventions, deploy state, known issues, recent incidents, business criticality — as a first-class engineering artifact kept explicit and current, rather than hoping it accumulates. Feed it to agents through deliberate [context engineering](../context-engineering.md) and durable [structured agent memory](../knowledge/structured-agent-memory.md), and record why generated code exists via [synthesis provenance tracking](synthesis-provenance-tracking.md) and why requests were declined via [out-of-scope records](out-of-scope-records.md). In the repository itself, short [steering files](../instructions/steering-files-as-navigation-pointers.md) point the agent at this material, on the rule that anything not written down there does not exist for it. Teams that do this get materially more from agents than teams that expect an agent to "figure it out" the way a curious new hire eventually would; agents simply remove the slack that let organizations skip it.
