---
type: concept
title: Journal Then Replay
description: >
  Durable-execution engines persist step results in a journal or event history
  and recover a crashed agent run by replaying it, with deterministic step
  identifiers acting as memoisation keys so work resumes from the failure
  point.
evidence: strong
sources:
  - title: "Durable execution meets AI: why Temporal is the perfect foundation for AI"
    resource: "Temporal blog (Cornelia Davis), 10 Jul 2025 — https://temporal.io/blog/durable-execution-meets-ai-why-temporal-is-the-perfect-foundation-for-ai"
  - title: "Durable agents"
    resource: "Restate documentation — https://docs.restate.dev/ai/patterns/durable-agents"
  - title: "Durable execution for crashproof AI agents"
    resource: "DBOS blog (Qian Li), 24 Feb 2025 — https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents"
  - title: "Durable execution: the key to harnessing AI agents"
    resource: "Inngest blog (Charly Poly), 19 Feb 2026 — https://www.inngest.com/blog/durable-execution-key-to-harnessing-ai-agents"
  - title: "Rules of Workflows"
    resource: "Cloudflare Workflows documentation — https://developers.cloudflare.com/workflows/build/rules-of-workflows/"
  - title: "Durable execution (persistence)"
    resource: "LangGraph documentation — https://docs.langchain.com/oss/python/langgraph/durable-execution"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 Jun 2025 — https://www.anthropic.com/engineering/multi-agent-research-system"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026 — https://earendil.com/posts/pi-durable/"
---

Agents are stateful and their errors [compound](compound-mistake-amplification.md),
so restarting a long run from scratch after a crash wastes work and can repeat
side effects. Anthropic's multi-agent research system resumes from the failure
point rather than restarting, and the wider durable-execution industry has
converged on one way of doing that.

The shared model has three parts: orchestration code that is deterministic,
side effects wrapped in journaled "steps", "activities" or "tasks" whose
results are memoised, and recovery by replaying the journal. Temporal runs the
agent loop as a workflow, with model and tool calls as retried activities and a
full event history to replay. Restate records each `ctx.run()` step in a
journal. DBOS checkpoints workflows and steps to Postgres without an external
orchestrator. Inngest memoises `step.run` results so a restart replays from the
last successful step. LangGraph checkpointers save per-thread state snapshots,
though its in-memory saver does not survive restarts and checkpoints can grow
without bound. Cloudflare's rules spell out the discipline this demands: step
names are the cache key and must be deterministic, only step return values
persist, and logic outside steps may run more than once, so calls must be
idempotent.

Pi Durable is the notable variant. It does not deterministically replay user
code; it persists explicit task phases and checkpoints, closer to a persisted
state machine, so code need not be deterministic between checkpoints. Its phase
discipline is described in [the effect sandwich](effect-sandwich.md), and its
parent-child structure in [task ownership
trees](task-ownership-tree-abort-propagation.md).

What replay does not give is exactly-once execution of the effect itself, a
contested point covered in [exactly-once only after
journaling](exactly-once-only-after-journaling.md). A journaled engine is a
reasonable substrate for a multi-step agent run, provided that every step's key
is stable, every external action is idempotent or checked before it is
repeated, and human waits are modelled as [durable approval
state](../harness/durable-approval-state.md). File-based [externalised progress
artefacts](../knowledge/externalised-progress-artifacts.md) offer a lighter
alternative where full replay is not needed.
