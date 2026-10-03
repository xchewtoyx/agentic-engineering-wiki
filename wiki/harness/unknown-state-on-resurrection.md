---
type: concept
title: Unknown State on Resurrection
description: >
  When a crash leaves a tool's outcome uncertain, tell the agent the state is
  unknown so it re-inspects the real resource before retrying, because agent
  checkpoints do not capture sandbox state and the newest commit may be lost.
evidence: weak
sources:
  - title: "Pi Durable (Hacker News discussion)"
    resource: "Hacker News item 49925969, Oct 2026, practitioner comments and Armin Ronacher on sandbox state — https://news.ycombinator.com/item?id=49925969"
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Tools and §Storage — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Audit and resume agent sessions"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026), crash-safe resume — https://dev.meta.ai/docs/cookbook/audit-agent-sessions"
---

A durable agent that comes back after a crash has two records that may
disagree: its own checkpoint, and the world. The checkpoint might say a restart
was intended but not that it finished, and the newest record might not even
have reached disk. An agent that trusts its checkpoint and carries on can
repeat an action that already happened or build on one that never did.

The practice, reported by practitioners in the Hacker News thread on Pi
Durable, is to record whether each tool call succeeded and, on resurrection,
tell the agent the state is "unknown" so it inspects the resource or retries.
Another commenter recommended declarative, idempotent interaction with the
environment in the style of Ansible. Two primary facts explain why this is
needed. First, agent checkpoints do not cover the execution environment: asked
how agent state stays in sync with sandbox state, Armin Ronacher said
full-sandbox agents probably need snapshots. Second, Pi Durable's SQLite
backend runs in WAL (write-ahead logging) mode with `synchronous = NORMAL`, so
commits survive a process crash but the newest may be lost on power or host
failure. Pi Durable does part of the signalling itself, returning an
`interrupted` result for any tool not marked
[replay-safe](replay-safe-tool-annotation.md). Meta's Muse Code now documents
the practice as product behaviour: on resume, an effect with an intent record
but no terminal record is flagged unknown, and the model must check the real
state before retrying.

The evidence is weak. The practice rests on forum comments, and no
peer-reviewed study of crash-mid-tool-call recovery for agents was found; only
the storage facts are primary.

The working rule is to treat an "intent committed" record as possibly lost or
possibly acted on, and to begin every resume by re-observing the resources
involved rather than trusting the journal. An explicit "unknown" is itself a
case of [actionable failure feedback](failures-returned-as-actionable-feedback.md).
The re-observation step is the same move as a
[start-of-session smoke test](../orchestration/start-of-session-smoke-test.md),
and it pairs naturally with a
[level-triggered reconcile loop](../orchestration/level-triggered-reconcile-loop.md)
that acts on observed state rather than on remembered events. The mechanics
that create the uncertainty are in
[the effect sandwich](../orchestration/effect-sandwich.md).
