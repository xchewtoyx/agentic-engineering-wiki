---
type: concept
title: Start Simple and Own the Control Flow
description: >
  Start with the simplest single-agent design, treated as mostly deterministic
  software with LLM steps at chosen points, and add agency or more agents only
  when the simpler design demonstrably falls short.
evidence: strong
sources:
  - title: "Building effective agents"
    resource: "Anthropic Engineering, 19 Dec 2024 — https://www.anthropic.com/engineering/building-effective-agents"
  - title: "A practical guide to building agents"
    resource: "OpenAI business guide (PDF, undated) — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"
  - title: "12-Factor Agents"
    resource: "Dex Horthy, HumanLayer, GitHub — https://github.com/humanlayer/12-factor-agents"
  - title: "OpenAI Agents SDK"
    resource: "OpenAI, Python SDK docs overview — https://openai.github.io/openai-agents-python/"
  - title: "Agent Development Kit"
    resource: "Google, ADK docs — https://adk.dev/"
  - title: "Agent Framework: Harness"
    resource: "Microsoft Learn — https://learn.microsoft.com/en-us/agent-framework/concepts/harness"
  - title: "Harness Engineering"
    resource: "Barbaste et al. (Wavestone AI Lab), arXiv 2609.00006, July 2026 preprint, §13.2 — https://arxiv.org/html/2609.00006v1"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 Jun 2025 — https://www.anthropic.com/engineering/multi-agent-research-system"
---

A new agent project faces strong pull towards frameworks, multi-agent
topologies and open-ended autonomy. Each adds behaviour that is harder to see
and debug, and a team can end up unable to explain why its agent did what it
did.

The major providers agree on the opposite default. Anthropic's "Building
effective agents" says to start with the simplest solution, which may mean no
agent at all, and to add complexity only when needed; it warns that frameworks
can hide prompts and responses, and recommends fewer abstraction layers in
production. Its three principles are simplicity, transparent planning, and
investment in the agent-computer interface. OpenAI's practical guide says to
maximise a single agent before adding more. Google's Agent Development Kit
(ADK) starts with prompts and tools and grows to multi-agent, and Microsoft
makes its Harness Agent the default. HumanLayer's 12-Factor Agents puts it most
sharply: good agents are mostly ordinary software with large language model
(LLM) steps at chosen points. Several of its factors (own your prompts, own
your context window, own your control flow, make the agent a stateless reducer)
express the same stance. OpenAI's Agents software development kit (SDK)
documentation likewise suggests calling the Responses API directly when you
want to own the loop yourself. A supporting observation comes from a 2026
preprint studying eleven harnesses: none of them imports LangChain, LangGraph
or AutoGen.

This is the same direction as [progressive agent
architecture](progressive-agent-architecture.md), which orders the components
to add, and as [non-LLM task implementation](non-llm-task-implementation.md)
at the level of a single task. The distinctive point here is ownership: keep
the loop, the prompts and the context assembly in your own code, so that the
[agent control flow](agent-control-flow.md) is something you wrote rather than
something a framework decided.

Not every voice is this conservative about agent count. Anthropic reports a
multi-agent research system beating a single agent by 90.2% at around 15 times
the tokens of chat, and the conditions under which extra agents help are
covered in [single-threaded writes](single-threaded-writes.md).

For an agent that takes operational actions, the practical shape is a
deterministic pipeline (collect evidence, decide, act within limits) with the
LLM placed at the judgement step, rather than a free-roaming agent. That fits
[the LLM proposes, code applies](../harness/llm-proposes-code-applies.md) and
the posture of [diagnose by default, act by
exception](../harness/diagnose-by-default-act-by-exception.md). Owning the
control flow also keeps the agent's own harness legible, which matters because
[an agent is a model plus a harness](../agent-equals-model-plus-harness.md) and
the harness is where most fixes land.
