---
type: concept
title: Tool Inventory
description: >
  The declared set of tools an agent may call; inventory size is a capability
  versus reliability and context-budget tradeoff.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

A tool inventory is the full set of tools an [LLM agent](../llm-agent.md) can use.
Each entry typically declares a name, parameters, and documentation so the
planner can select and call tools via [function calling](function-calling.md).

Sizing the inventory is a real design decision. More tools increase capability,
but make correct selection harder and consume context with tool descriptions —
which itself caps how many tools can practically be declared. Published agents
span tiny inventories (a handful of tools) to thousands of APIs; the right size
is found by [tool selection ablation](../evaluation/tool-selection-ablation.md), not by
maximal coverage. Within a conversation, drop tools known to be irrelevant to
the current phase so they do not distract the planner under
[conversational agent context](../context/conversational-agent-context.md).

Without external tools, an agent is limited to what the base model can do alone
(for example, generate text). With tools, actions split into perception
(read-only) and environment change (write) under
[agent tool categories](agent-tool-categories.md). Two practitioner positions
pull the sizing decision in opposite directions: coding-agent builders argue
for a [minimal, general tool surface](minimal-general-tool-surface.md) (a few
tools plus a shell), while security guidance for agents that change live
systems argues for a [narrow action verb set](narrow-action-verb-set.md) with no
raw shell; a common resolution is general tools for reading and narrow verbs
for writing. Prefer clear, simple tool
APIs: ambiguous or overly complex functions increase
[planning failure modes](../orchestration/agent-planning-failure-modes.md) such as invalid
parameters or wrong values.
