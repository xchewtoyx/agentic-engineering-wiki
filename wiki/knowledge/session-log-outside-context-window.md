---
type: concept
title: Session Log Outside the Context Window
description: >
  An append-only, queryable session or event log held outside the context
  window keeps compaction decisions recoverable and lets a crashed harness
  resume from its last event.
evidence: strong
sources:
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
  - title: "Architecting efficient context-aware multi-agent framework for production"
    resource: "Google Developers Blog, 4 Dec 2025 — https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/"
  - title: "OpenClaw docs: Compaction"
    resource: "OpenClaw — https://docs.openclaw.ai/concepts/compaction"
  - title: "Hermes Agent docs: Architecture"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/developer-guide/architecture"
  - title: "Agent Framework: Harness"
    resource: "Microsoft Learn — https://learn.microsoft.com/en-us/agent-framework/concepts/harness"
  - title: "OpenAI Agents SDK"
    resource: "OpenAI, Python SDK docs — https://openai.github.io/openai-agents-python/"
  - title: "Hermes Agent docs: Memory"
    resource: "Nous Research, session_search — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory"
  - title: "Audit and resume agent sessions"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/audit-agent-sessions"
---

If the conversation in the context window is the only record of an agent's
session, two things go wrong. Every compaction destroys information that cannot
be recovered, and a crash of the harness process loses the session or leaves
someone to reconstruct it by hand.

Several providers have converged on keeping a durable log outside the window.
Anthropic's Managed Agents design virtualises the session as an append-only
event log, separate from both the harness loop and the sandbox. The harness
writes events with `emitEvent` and reads slices with `getEvents()`. Context
transformation stays in the harness, so compaction decisions remain recoverable.
A crashed harness is replaced and resumes from the last event using
`wake(sessionId)` and `getSession(id)`. Google's Agent Development Kit treats the
session as a durable log of typed events from which the working context is
compiled. Microsoft's Agent Framework persists history after each model call,
and OpenAI's Agents software development kit (SDK) has sessions as a persistence
layer. OpenClaw keeps the full history on disk when it auto-compacts, and Hermes
stores sessions in SQLite with full-text search, keeps lineage across
compressions and exposes a `session_search` tool to recall older sessions.
Meta's Muse Code writes each session as an append-only JSON Lines (JSONL) log of
every model call, tool run and approval, resumes by appending to the same log,
and exports it byte-deterministically so audits can be compared; its cookbook
also turns curated slices of these logs into CI regression fixtures, described
in [deterministic session replay in CI](../evaluation/deterministic-session-replay-ci.md).

The log is not memory in the [agent memory tiers](agent-memory-tiers.md) sense:
nothing in it is retrieved into context by default. It resembles a
[memory stream](memory-stream.md) in being append-only, but its job is fidelity
and recovery rather than recall, and it is to an agent session what a
[knowledge activity journal](knowledge-activity-journal.md) is to a knowledge
base. It is the storage half of
[context as a compiled view](../context/context-as-compiled-view.md), the
"session" leg of [brain–hands–session decoupling](../harness/brain-hands-session-decoupling.md),
and the agent-level counterpart of
[journal-then-replay durable execution](../orchestration/journal-then-replay-durable-execution.md).

Two practical consequences follow. An agent diagnosing another agent should read
that agent's durable logs and session store rather than any compacted transcript,
because the raw record is what supports diagnosis
([raw traces over summaries](../optimization/raw-traces-over-summaries.md)). And
any long-running agent should keep its own append-only log outside its container
and its context window, so a crash or restart resumes the task rather than
starting it again.
