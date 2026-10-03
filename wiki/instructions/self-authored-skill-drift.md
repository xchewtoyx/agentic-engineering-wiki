---
type: concept
title: Self-Authored Skill Drift
description: >
  When an agent writes its own skills and memory, yesterday's agent can author
  an instruction today's agent obeys, creating a drift failure class with no
  code or config change that operators gate with staged write approval and a
  stale-and-archive lifecycle.
evidence: moderate
sources:
  - title: "Hermes Agent docs: Skills"
    resource: "Nous Research official docs as of v0.21.5 (v2026.9.24), retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"
  - title: "Hermes Agent docs: Memory"
    resource: "Nous Research official docs, retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory"
  - title: "Hermes Agent docs: Curator"
    resource: "Nous Research official docs, retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/features/curator"
---

When an agent rewrites its own standing instructions, a fault can appear with no code change, no config change and no upgrade: yesterday's agent wrote a skill or a memory entry that today's agent obeys. Agent-built [skill libraries](../orchestration/skill-library.md) make self-improvement a feature, but they also make it an operational failure class, because the instruction set is now changing under the operator rather than through review.

Hermes Agent (official docs, v0.21.5, October 2026) is the clearest worked example because it makes self-authoring first-class. A `skill_manage` tool lets the agent create, update and delete its own skills as procedural memory, and the system prompt nudges it to record multi-step workflows, recoveries from dead ends and user corrections; an advisory linter runs on writes. After a turn, a background review can also save memory or update skills, at tunable nudge intervals.

The controls Hermes exposes generalise to any self-authoring agent:

- **Staged writes.** A write-approval setting queues the agent's skill and memory writes for a human to approve, turning self-authoring back into reviewed change.
- **A usage lifecycle.** An idle-time curator marks unused skills stale (14 days by default) and archives them (30 days), exempting pinned skills and those used by scheduled jobs, which is a mechanical defence against [sediment](sediment.md).
- **Dry runs.** The curator can preview a pass before applying it.
- **Containment.** In Docker, self-authored state is confined to a writable data directory while the install tree is read-only, so the agent can rewrite its instructions but not its harness.

Two cautions apply. Wider research shows self-modifying agents can make large gains, while secondary reports describe Goodhart-style erosion of properties nobody measures (see [self-modifying harness controllability](../optimization/self-modifying-harness-controllability.md)). And there is a mechanism risk in letting a model consolidate its accumulated skills or memory wholesale: by analogy with the [context collapse](../optimization/context-collapse.md) seen when models rewrite accumulated context in one pass, an LLM consolidation step deserves the most caution of all. The alternative design line keeps agent memory as plain, operator-legible Markdown and routes change through operator-owned contracts; it treats legibility, rather than agent authorship, as the safeguard, and the trade-off between the two is contested rather than settled.

Operationally, "the agent got worse" should prompt an inspection of recent skill and memory writes before anyone looks at infrastructure. Hermes's own troubleshooting checklist adds that small models (under about 30B parameters) often claim memory saves they never made, so the files themselves, not the agent's report, are the evidence. Periodic drift review is the self-authored counterpart of the scheduled clean-up agents in [entropy garbage collection](../development/entropy-garbage-collection-agents.md).
