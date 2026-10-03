---
type: concept
title: Replay-Safe Tool Annotation
description: >
  After a crash, only tools declared replay-safe rerun; every other interrupted
  tool returns an "interrupted" result to the model, so read-only diagnostics
  repeat freely while deploys or restarts cannot.
evidence: moderate
sources:
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Tools — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026, search_issues vs deploy example — https://earendil.com/posts/pi-durable/"
---

When an agent process dies in the middle of a tool call, a runtime that blindly
reruns the call on restart risks doing something twice, and one that never
reruns it leaves the model stalled. Whether repetition is safe depends on the
tool, so the decision cannot be made generically.

Pi Durable makes it a property of the tool definition. Each tool call is its
own durable task, and its intent is committed before `execute()` runs. If the
process dies mid-call, the call reruns on reopen only if the tool was declared
`replay: "safe"`. Every other tool returns an `interrupted` error result to the
model, including whatever output had been committed so far, and the model
decides what to do next. The launch post's example marks a read-only
`search_issues` tool as safe and leaves a destructive `deploy` tool
unannotated. This is the per-tool application of
[the effect sandwich](../orchestration/effect-sandwich.md). Model requests are
treated more simply: an aborted request is resent, with its partial answer kept
in the transcript and marked as aborted.

The mechanism is documented by its authors in an experimental package, and no
published reference implementation of an operations agent built on it was
found.

As a design suggestion rather than sourced fact, the annotation follows the
read/write split in [agent tool categories](agent-tool-categories.md). For an
agent that operates infrastructure, read-only diagnostics (status listings, log
reads, health checks, config reads) would be marked replay-safe, while
remediations (restart, recreate, prune, config writes) stay non-replayable, and
on an `interrupted` result the agent re-probes the system before deciding, as
described in [unknown state on resurrection](unknown-state-on-resurrection.md).
This split lines up with
[diagnosing by default and acting by exception](diagnose-by-default-act-by-exception.md),
and is easiest to hold to when writes go through a
[narrow action verb set](narrow-action-verb-set.md) rather than a raw shell,
since a shell call's replay safety depends on what string it was given.
