---
type: concept
title: Splitting Skills
description: >
  Split one agent document into two only when the cut earns the load it
  spends: by sequence, when later steps tempt the agent to rush the current
  one, or by invocation, when a distinct leading word or another skill needs
  to reach part of it independently.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill and SKILL-MECHANICS.md"
    resource: "https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents (read 2 Oct 2026, v1.2.3)"
---

Every split spends one of the two loads in [context load versus cognitive load](context-load-versus-cognitive-load.md): a new model-invoked skill adds an always-loaded description, and a new user-invoked one adds something for the human to remember. Matt Pocock's `writing-for-agents` skill therefore names only two cuts that earn it.

Splitting by sequence applies when a run of steps lets the agent see work ahead of it and rush the step in front, which is [premature completion](premature-completion.md). Keeping the later steps out of view drives more legwork on the current one, but only if the split crosses a real context boundary.

Splitting by invocation applies when part of a skill has its own [leading word](leading-words-in-agent-instructions.md) that should trigger it independently, one you actually use in prompts, or when another skill must reach it. That is how `grilling` became its own model-invoked primitive behind several [thin orchestrators](thin-orchestrator-skills.md).

Neither cut is "the file is long". Length alone is [sprawl](information-hierarchy.md), cured by disclosing reference behind pointers rather than by creating more skills.

Boundary: merging is also a decision. Combining two sequences exposes the first to the second's steps; keep them apart when the first has a fuzzy [completion criterion](completion-criterion.md).
