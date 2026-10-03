---
type: concept
title: Agent = Model + Harness
description: >
  An agent's behaviour comes from the model weights plus all the non-weight
  runtime code around them (loop, tools, context, safety, orchestration,
  extensions), and that harness can be engineered independently of the model.
evidence: moderate
sources:
  - title: "Harness Engineering"
    resource: "Barbaste, Darrigol, Vu, Wiltberger (Wavestone AI Lab), arXiv 2609.00006, July 2026 preprint, §2.1 — https://arxiv.org/html/2609.00006v1"
  - title: "The Anatomy of an Agent Harness"
    resource: "Viv Trivedy, LangChain, 10 Mar 2026, read via secondary summary — https://businessdatasolutions.github.io/ai-wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026, harness definition — https://earendil.com/posts/pi-durable/"
  - title: "Agent Framework: Harness"
    resource: "Microsoft Learn, Agent Framework concepts — https://learn.microsoft.com/en-us/agent-framework/concepts/harness"
---

When an [LLM agent](llm-agent.md) misbehaves, the reflex is to blame the model
or reach for a bigger one. That framing hides most of what is actually running:
the loop that calls the model, the tools it can invoke, how its context is
assembled and trimmed, what it is allowed to do, and how work is split across
sub-agents. Harness engineering starts by naming all of that as a separate
artefact that can be designed, tested and changed on its own.

By 2026 the research and practitioner literature converges on the shorthand
Agent = Model + Harness. A Wavestone source-code study of eleven harnesses (a
July 2026 preprint) defines the harness as the runtime that couples a large
language model (LLM) to the world: its loop, tools, context and safety
controls. Viv Trivedy of LangChain draws the same line, treating the harness as
all code, configuration and execution logic that is not the model, although his
post was read only through a secondary summary. Earendil's Pi Durable post
defines a harness as storage plus the machinery that runs one or more LLM
conversations, together with their tools and execution environments.
Microsoft's Agent Framework documentation describes it as the scaffolding that
drives model and tool calls, manages state and context, applies approval
policies and keeps a multistep task progressing. The framing descends from
SWE-agent's [agent-computer interface](harness/agent-computer-interface.md).

The name itself was popularised in February 2026, almost simultaneously, by
Mitchell Hashimoto and by OpenAI's Ryan Lopopolo, and then formalised by
Birgitta Böckeler. That timeline comes from secondary write-ups, and the exact
ordering is unconfirmed.

The practical consequence is diagnostic: a fault in an agent system is at least
as likely to sit in the harness as in the model, and the harness is the part a
team can actually change. Inspect the loop, tools, context and permissions
before concluding the model is at fault. The decomposition is refined in
[seven harness subsystems](harness/seven-harness-subsystems.md) and
[inner and outer harness](inner-and-outer-harness.md). How much the harness
matters empirically is covered in
[harness as a performance lever](harness-as-performance-lever.md), and how much
of it to build is argued in [thin vs thick harness](thin-vs-thick-harness-debate.md).
