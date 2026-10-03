---
type: concept
title: Context as a Compiled View
description: >
  Build each call's working context from richer durable state through named,
  ordered, observable processors, keeping storage separate from presentation,
  scoping by default and referencing artefacts by name rather than pasting them.
evidence: moderate
sources:
  - title: "Architecting efficient context-aware multi-agent framework for production"
    resource: "Google Developers Blog, 4 Dec 2025 — https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/"
  - title: "Agent Development Kit"
    resource: "Google, ADK docs — https://adk.dev/"
---

In many harnesses the context window is the agent's state: messages are
appended until something has to be cut, and whatever was cut is gone. That makes
compaction irreversible, makes it hard to swap models, and leaves no clean record
of what the model actually saw at each step.

Google's post on context engineering in its Agent Development Kit (ADK) inverts
this. Its thesis is that context is a compiled view over a richer stateful
system. Three principles follow. **Separate storage from presentation**, so the
durable record is not the same object as what the model is shown. **Make
transformations explicit**, as named, ordered processors whose effects can be
observed. **Scope by default**, so sub-agents get the minimum context and fetch
more through tools. State is held in tiers: the working context for one call, a
session that is a durable log of typed events, memory, and artefacts that are
referenced by name and version rather than pasted in. The post argues that typed
event logs enable model swaps, compaction, time-travel debugging and
observability. ADK itself filters events, summarises older turns, lazy-loads
artefacts and tracks tokens automatically.

This is one vendor's architecture, but it agrees with Anthropic's Managed Agents
design, where the session log sits outside the window and context transformation
happens in the harness (see
[session log outside the context window](../knowledge/session-log-outside-context-window.md)
and [brain–hands–session decoupling](../harness/brain-hands-session-decoupling.md)).
It is the agent-runtime version of the assembly step in
[prompt assembly algorithms](prompt-assembly-algorithms.md), with the difference
that the source is a durable event log rather than a fresh retrieval. It gives
the four moves in [write, select, compress, isolate](context-write-select-compress-isolate.md)
a concrete pipeline shape, and it sits towards the structured end of the
[harness memory strategy spectrum](../knowledge/harness-memory-strategy-spectrum.md).

Applied to an agent that investigates incidents, the pattern means keeping
evidence (logs, health outputs, actions taken) in a durable store and building
each model call's context from it through a few named steps, such as "last N
health results", "log excerpt for component X" and "actions taken so far".
Large artefacts are referenced by path rather than inlined. Reviewers can then
see exactly what the model was shown when it made each decision.
