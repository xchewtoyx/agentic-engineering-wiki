---
type: concept
title: Context Engineering
description: >
  Deliberate structuring of instructions, examples, retrieved material, and
  working memory inside the context window for reliable model behaviour.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §1"
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §2.1"
---

Context engineering packs the right information — system instructions, few-shot
examples, tool documentation, retrieved knowledge, and intermediate agent state —
into the finite context window at useful density. In Huyen's usage, the
**prompt** is the whole model input; **context** is the enabling information
inside it ([in-context learning](prompting/in-context-learning.md)). Operationally this is
the [feedforward pass](context/llm-application-feedforward-pass.md): retrieve, snippetize, score, and
assemble under [prompt element importance](context/prompt-element-importance.md).

Place critical material with [lost in the middle](context/lost-in-the-middle.md) in
mind: edges beat the middle. Prefer [context grounding](context/context-grounding.md)
over hoping parametric memory is enough. Placement affects more than passive
recall, too: a warning appended to the tail of a tool observation can go
unacted-on for the same reason — see
[next-turn salience promotion](context/next-turn-salience-promotion.md) for surfacing
it at the point where the model actually decides what to do next instead. For [LLM agents](llm-agent.md), tool
descriptions, [ReAct](orchestration/react-loop.md) traces, and reflection compete with task
content — over-large [tool inventories](harness/tool-inventory.md) starve the budget.
Treat every token of format scaffolding as a cost that must earn its keep.
When the context itself should improve from the system's own execution
feedback rather than being hand-tuned, see
[context adaptation](optimization/context-adaptation.md).

For conversational task agents, assemble
[conversational agent context](context/conversational-agent-context.md) deliberately:
phase-relevant tools only, elastic [conversation artifacts](context/conversation-artifacts.md),
and prior-history extent that matches topic continuity rather than unbounded
retention. Long tool trajectories also benefit from
[collapsed observations](harness/collapsed-observations.md) and an
[agent episode prompt stack](harness/agent-episode-prompt-stack.md) so system, demo,
instance, and next-step layers compete predictably for tokens. When the task
outlives any fixed window, prefer
[OS-inspired agent memory](knowledge/os-inspired-agent-memory.md) (virtual context /
paging) over hoping a larger maximum length will use mid-prompt material well.
