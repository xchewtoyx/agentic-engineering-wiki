---
type: concept
title: Shared Task Board Coordination
description: >
  Multi-agent work can be coordinated through a durable, dependency-aware task
  board in which every cross-role decision is a card comment, a dispatcher
  promotes cards when their dependencies finish, and the coordinator has no
  tools to do the work itself.
evidence: weak
sources:
  - title: "Multi-agent orchestration"
    resource: "Meta Model API cookbook, Use Cases (Hermes Agent with Muse Spark), undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/multi-agent-orchestration"
  - title: "Why Do Multi-Agent LLM Systems Fail?"
    resource: "Cemri, Pan, Yang et al., arXiv 2503.13657, NeurIPS 2025 Datasets and Benchmarks (MAST) — https://arxiv.org/abs/2503.13657"
---

When several agents share a task, the coordination itself becomes a failure
point. Decisions made in one agent's context never reach another, work starts
before what it depends on is finished, and afterwards nobody can reconstruct
why the result looks as it does. The [MAST
taxonomy](../evaluation/mast-multi-agent-failure-taxonomy.md) puts inter-agent
misalignment at about a third of observed multi-agent failures.

Meta's multi-agent recipe answers this with a shared Kanban board, running on
Hermes Agent. Four agent profiles (product manager, backend, frontend and
go-to-market) work from one board stored in SQLite and dispatched from inside
the Hermes gateway. Cards move between ready, running, blocked and done; parent
and child links hold a card in ready until its dependencies are done, so
sequencing comes from dependencies rather than polling, much like a task in a
[DAG workflow](workflow-topology.md) waiting on its upstream tasks. The
product-manager profile is the only arbiter and deliberately has no terminal or
code-execution tools. A specialist that needs input blocks its card, the
manager answers in a card comment and unblocks it, and rework goes back as a
new card with file-level acceptance criteria. The recipe's rule is that every
cross-role decision is a comment on a card, "never a back-channel chat", so the
run can be audited and replayed later. It recommends a single coding agent
instead for one-role tasks such as a bug fix.

Compared with free-form agent chat, the board is a structured message channel
of the kind [inter-agent coordination
protocols](inter-agent-coordination-protocols.md) argue for, and it plays the
role of a [session log outside the context
window](../knowledge/session-log-outside-context-window.md) for the team. It
keeps the coordinator asymmetry of [single-threaded
writes](single-threaded-writes.md) while allowing parallel specialists. A
board with decisions as comments is also a natural home for a [full-trace
audit](../harness/full-trace-remediation-audit.md) of what a team of agents
did and why.

The recipe also documents its own failure modes, which generalise to any
dispatcher-driven board: cards sit in ready forever if the dispatcher is down,
misspelt agent names fail silently, rate limits or context overruns crash a
specialist until someone unblocks the card by hand, and a clarifying question
that times out (after 600 seconds in Hermes) blocks the run. A stalled
dispatcher or a card stuck in ready is therefore a failure signature worth
monitoring for. The evidence is one worked vendor example without results, so
the note is weak.
