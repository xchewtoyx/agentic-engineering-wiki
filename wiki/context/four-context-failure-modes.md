---
type: concept
title: Four Ways Long Contexts Fail
description: >
  Long contexts fail through poisoning (a hallucination keeps being reused),
  distraction (repeating history instead of planning), confusion (too many
  tools) and clash (contradictory information split across turns).
evidence: moderate
sources:
  - title: "How Long Contexts Fail"
    resource: "Drew Breunig, 22 Jun 2025 — https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html"
  - title: "Context Engineering for Agents"
    resource: "Lance Martin, LangChain, 23 Jun 2025 — https://rlancemartin.github.io/2025/06/23/context_engineering/"
---

Knowing that [long contexts degrade performance](context-rot.md) does not tell
an engineer what to fix. A model that is "confused" by a long session could be
suffering from several different problems, each with a different remedy.

Drew Breunig's taxonomy separates four failure modes, each with an example from
his post:

- **Poisoning.** A [hallucination](../hallucination.md) enters the context and
  keeps being reused as if it were fact. His example is Gemini playing Pokémon.
- **Distraction.** Past about 100,000 tokens, the agent starts repeating actions
  from its history instead of planning new ones.
- **Confusion.** Too many tools degrade tool use. One quantised Llama 3.1 8B
  model failed with 46 tools and succeeded with 19.
- **Clash.** Information split across turns contradicts itself. Splitting a task
  this way cut performance by 39%, and o3 fell from 98.1 to 64.1.

The taxonomy is from one practitioner's post rather than a controlled study, but
Lance Martin's context-engineering guide builds on it, and each mode lines up
with a remedy. Confusion is the main argument for a
[minimal, general tool surface](../harness/minimal-general-tool-surface.md) and a
lean [tool inventory](../harness/tool-inventory.md). Distraction is what loop
detection catches when it shows up as repeated actions (see
[doom-loop detection](../harness/doom-loop-detection.md)). Poisoning is a risk for
any summary that carries a wrong conclusion forward, which is one reason
[context collapse](../optimization/context-collapse.md) matters. Clash argues for
keeping one consistent source of truth rather than accumulating contradicting
turns. Behavioural failures such as premature completion and goal drift, which
also grow with session length, are covered separately in
[agent failure modes that grow with one long context](long-context-agent-failure-modes.md).

The modes double as a diagnostic vocabulary when any agent behaves strangely
after a long session. A session that keeps acting on a wrong belief may be
poisoned; one that repeats the same tool call may be distracted; one with a large
plugin or Model Context Protocol (MCP) tool set may be confused. Recording which
mode is suspected makes it easier to choose the fix: a compaction, a fresh
session or a smaller tool set.
