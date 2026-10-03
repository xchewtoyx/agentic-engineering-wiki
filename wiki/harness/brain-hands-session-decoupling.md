---
type: concept
title: Decouple Brain, Hands and Session
description: >
  Separate the model loop (brain), the sandbox (hands) and the durable session
  log so each can fail and be replaced on its own; a dead container surfaces as
  a tool error and is re-provisioned, not nursed.
evidence: moderate
sources:
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
---

Anthropic's first managed-agent design put the loop, the tools and the session
together in one container, and that container became a "pet". A stuck session
looked the same whether the cause was a harness bug, a dropped event or a dead
container, and debugging meant opening a shell inside a container that held
user data.

The redesign splits the agent into three virtualised parts. The session is an
append-only event log. The harness is the loop that calls the model and routes
tool calls. The sandbox is the execution environment. Once separated, the
container becomes cattle: it is called like any tool through an
`execute(name, input)` interface, its death reaches the model as an ordinary
tool error (see
[failures returned as actionable feedback](failures-returned-as-actionable-feedback.md)),
and a replacement is provisioned on demand. The harness is cattle too, because
recovery wakes a session by ID and resumes from the last event it wrote.
Credentials are kept out of reach of the sandbox entirely, which the separation
makes possible (see
[credentials stay outside the sandbox](../security/credentials-outside-the-sandbox.md)).
Anthropic reports that the decoupling cut median time to first token by about
60% and 95th-percentile time by more than 90%.

This rests on one vendor's account of its own platform, and the latency figures
are its own.

The pattern transfers to any containerised agent deployment: treat agent
containers as disposable, keep the event log outside them in a
[session log outside the context window](../knowledge/session-log-outside-context-window.md)
and a durable store, and let the loop crash and resume like any other
replaceable part, in the spirit of
[journal-then-replay](../orchestration/journal-then-replay-durable-execution.md).
There is a limit for agents that operate infrastructure: a worker cannot
outlive the host or daemon failure it is meant to repair, which is one reason
to prefer an
[external supervisor over self-diagnosis](../orchestration/external-supervisor-over-self-diagnosis.md).
