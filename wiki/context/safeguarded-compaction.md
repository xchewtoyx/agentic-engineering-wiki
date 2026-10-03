---
type: concept
title: Safeguarded Compaction
description: >
  Compaction should keep full history on disk, never split tool-call and
  result pairs, audit summary quality before replacing history, and flush
  notes to memory first, with the compaction prompt tuned for recall before
  precision.
evidence: strong
sources:
  - title: "OpenClaw docs: Compaction"
    resource: "OpenClaw — https://docs.openclaw.ai/concepts/compaction"
  - title: "Effective context engineering for AI agents"
    resource: "Anthropic Engineering, 29 Sep 2025 — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - title: "Hermes Agent docs: Agent loop"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop"
  - title: "Hermes Agent docs: Context compression & caching"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026, background thresholds and compact-once-and-retry — https://earendil.com/posts/pi-durable/"
  - title: "Multi-turn context management"
    resource: "Meta Model API cookbook, Agent Patterns, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/multi-turn-context-management"
---

Compaction replaces part of a conversation with a summary of it. Done
carelessly, it is irreversible, it can corrupt the structure the model relies
on, and a poor summary can quietly delete the one detail that mattered. Since
most harnesses compact automatically, these risks run on every long session.

Vendor documentation describes a consistent set of safeguards:

- **Keep full history on disk.** OpenClaw's auto-compaction summarises older
  turns as the session nears its limit, or compacts and retries on a
  context-overflow error, while keeping the full history on disk.
- **Never split a tool call from its result**, so the compacted transcript stays
  structurally valid.
- **Audit the summary before accepting it.** OpenClaw's default "safeguard" mode
  audits summary quality, and a failed audit keeps the original history.
- **Flush notes to memory first.** OpenClaw reminds the agent to flush important
  notes before compacting; Hermes runs a preflight compression check above 50%
  of context and flushes memory before context is lost.
- **Make lossiness explicit.** Hermes routes compression through a pluggable
  context engine whose default is a lossy summariser, while lossless engines
  must be selected explicitly.
- **Compact early and in the background.** Pi Durable starts background
  summarisation at a token threshold, makes a request wait for the summary only
  when close to the window limit, and compacts once and retries if the provider
  rejects a request as too long.
- **Protect the edges.** Meta's multi-turn recipe replaces the middle of the
  session with a summary carrying the goal, files and plan while keeping the
  system prompt and recent turns intact, which also respects
  [lost in the middle](lost-in-the-middle.md).
- **Tune the compaction prompt for recall first.** Anthropic advises maximising
  recall on real traces, then improving precision.
- **Log every compaction**, so its start, completion and audit outcome are
  visible afterwards.

These safeguards target a known failure: wholesale rewrites drift towards
generic brevity and can collapse, as described in
[context collapse](../optimization/context-collapse.md). They harden the running
summary of [memory summarization](../knowledge/memory-summarization.md) for
agents that compact automatically. Keeping full history on disk is the same
principle as a
[session log outside the context window](../knowledge/session-log-outside-context-window.md).
The broader choice of whether to compact at all is in
[compaction vs context reset](compaction-vs-context-reset.md), and where
different harnesses sit on memory design is in the
[harness memory strategy spectrum](../knowledge/harness-memory-strategy-spectrum.md).

When an agent appears to have forgotten something, the compaction log lines and
the audit outcome show whether a compaction happened and whether it was
accepted, and the selected context engine tells you whether compression was
lossy. An agent that investigates incidents should compact only its working
context, while raw logs and traces stay untouched outside the window for later
analysis.
