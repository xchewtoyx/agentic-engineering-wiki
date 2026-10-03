---
type: concept
title: Write, Select, Compress, Isolate
description: >
  Context management reduces to four moves: write state out, select what to
  load, compress what is loaded, and isolate work across sub-agents,
  sandboxes or partitioned state.
evidence: moderate
sources:
  - title: "Context Engineering for Agents"
    resource: "Lance Martin, LangChain, 23 Jun 2025 — https://rlancemartin.github.io/2025/06/23/context_engineering/"
  - title: "Context engineering (post on X)"
    resource: "Andrej Karpathy, June 2025 — https://x.com/karpathy/status/1937902205765607626"
---

In June 2025 Andrej Karpathy publicly backed "context engineering" over "prompt
engineering", describing it as the art and science of filling the window with
the right information for the next step. The phrase names the problem
([context engineering](../context-engineering.md)) but not the toolkit. Once
[context rot](context-rot.md) is accepted, a team needs a short list of moves it
can make.

Lance Martin's "Context Engineering for Agents" supplies four:

- **Write** state out of the window, into scratchpads and long-term memory.
- **Select** what to bring in: retrieve memories, tools and knowledge, including
  retrieval over tool descriptions.
- **Compress** what is loaded, by summarising or trimming; Claude Code, for
  example, auto-compacts at about 95% of the window.
- **Isolate** work across sub-agents, sandboxes or partitioned state, so each
  context holds only what its task needs.

Martin draws on Breunig's [four context failure modes](four-context-failure-modes.md),
on Cognition's multi-agent arguments and on Anthropic's multi-agent work. The
list is a practitioner synthesis rather than a measured result, but it organises
most agent context practice. Writing out is what a
[session log outside the context window](../knowledge/session-log-outside-context-window.md)
and [externalised progress artefacts](../knowledge/externalised-progress-artifacts.md)
do, and the long-term side of it is
[memory management](../knowledge/memory-management.md). Selecting is
[progressive disclosure](../instructions/progressive-disclosure.md) and retrieval.
Compressing is compaction, with its trade-offs in
[compaction vs context reset](compaction-vs-context-reset.md). Isolating is what
sub-agents are best at, provided
[writes stay single-threaded](../orchestration/single-threaded-writes.md).
Google's alternative framing, building each call's context from durable state,
is in [context as a compiled view](context-as-compiled-view.md).

The four moves also work as a design checklist for any long-running agent:
write task state to a file or log rather than keep it in conversation; select
log excerpts and reference sections on demand; compress only the working
context, never the raw evidence; and isolate read-heavy investigation (for
example one sub-agent per subsystem) from the single actor allowed to change
anything.
