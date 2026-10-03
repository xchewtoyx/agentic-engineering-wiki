---
type: concept
title: The Effect Sandwich
description: >
  Commit the intent, perform the external effect, then commit the outcome, so
  that a process reopening in the intent phase knows the effect may already
  have happened and must retry safely, poll an external handle, or record an
  interruption.
evidence: moderate
sources:
  - title: "pi-durable specification (spec.md)"
    resource: "Earendil, earendil-works/pi repository, §1 and §5.2 — https://github.com/earendil-works/pi/blob/main/packages/durable/docs/spec.md"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026 — https://earendil.com/posts/pi-durable/"
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Audit and resume agent sessions"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/audit-agent-sessions"
---

A durable agent runtime can make its own records atomic, but it cannot make a
call to the outside world atomic with them. A deploy, a payment, a restart or
an API call either happened before the crash or did not, and the runtime may
not know which. The question is how to structure the code so that this
uncertainty is visible rather than silently resolved.

Pi Durable, Earendil's experimental TypeScript runtime launched on 1 October
2026, answers with what its specification calls the effect sandwich. A task
first commits an intent phase, then performs the external effect, then commits
the outcome or its next phase. Its invariants keep external effects out of the
mutation transaction and require every visible change to be durable first. If
the process reopens while a task is still in the intent phase, the effect may
already have happened, so the handler must do one of three things: retry in a
way that is safe to repeat, poll an external handle to learn the real result,
or record an interruption. Deferred providers are modelled the same way, as a
durable phase holding a handle and a next-poll time. Meta's Muse Code documents
the same discipline in its audit contract: an action is proposed, reviewed,
decided and recorded as an intent, and the effect runs only once that intent
record is durable, followed by a terminal result record.

The Pi Durable README warns that it is experimental and that its interface
changes without notice, and version 1.0.1 shipped two days after launch. The
pattern is documented by its authors but untested in the field, and no
peer-reviewed study yet covers crash-mid-tool-call semantics for agents.

In practice, every tool call with a side effect should be bracketed by an
intent record and an outcome record, and an intent with no outcome should
trigger a re-inspection of the target before any retry. Which tools need the
bracket is the job of [replay-safe tool
annotation](../harness/replay-safe-tool-annotation.md), and reporting the gap
honestly is [unknown state on
resurrection](../harness/unknown-state-on-resurrection.md); a [level-triggered
reconcile loop](level-triggered-reconcile-loop.md) sidesteps much of the
problem by observing the world again instead of trusting the journal. The
sandwich also explains why [exactly-once holds only after
journaling](exactly-once-only-after-journaling.md), and how it differs from
Temporal-style [journal-then-replay](journal-then-replay-durable-execution.md).
