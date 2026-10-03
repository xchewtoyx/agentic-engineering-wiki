---
type: concept
title: Exactly-Once Only After Journaling
description: >
  Durable-execution "exactly-once" holds only for results already journaled
  and for submissions keyed by an idempotency key, because a crash between an
  effect and its journal write re-executes the effect.
evidence: weak
sources:
  - title: "restatedev/docs-restate issue #410"
    resource: "restatedev/docs-restate GitHub issue, opened 24 Sep 2026 — https://github.com/restatedev/docs-restate/issues/410"
  - title: "Durable execution: the key to harnessing AI agents"
    resource: "Inngest blog (Charly Poly), 19 Feb 2026 — https://www.inngest.com/blog/durable-execution-key-to-harnessing-ai-agents"
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Persist and Resume — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Pi Durable (Hacker News discussion)"
    resource: "Hacker News item 49925969, Oct 2026 — https://news.ycombinator.com/item?id=49925969"
  - title: "Rules of Workflows"
    resource: "Cloudflare Workflows documentation — https://developers.cloudflare.com/workflows/build/rules-of-workflows/"
---

Durable-execution vendors often promise that work happens "exactly once". For
an agent whose tools send messages, move money, deploy code or restart
services, the promise matters: a duplicated action is itself an incident.
Whether the promise holds depends on where the crash falls.

The two sides are as follows. Inngest's blog says each memoised step executes
exactly once. Against that, Restate documentation issue #410 reports that if a
worker dies after a `ctx.run` action but before its result is journaled, the
action re-executes; in 30 of 30 trials the external side effects were
duplicated, and no maintainer had replied at the time of writing. The same
window applies, by inference, to any design that journals after the effect,
which would include Inngest's. Pi Durable's own exactly-once claim is narrower.
When a client retries a submission with the same `requestId`, the existing
submission is returned rather than a new one created, so the key works as an
idempotency key. On Hacker News a commenter disputed the exactly-once wording,
and Pi's author Mario Zechner replied that `requestId` is an idempotency key.
The fair reading is narrower still. After a crash, Pi Durable reruns only
tools declared `replay: "safe"`. Any other interrupted tool is not rerun: the
model receives an `interrupted` result, and the effect may have happened zero
times or once. Exactly-once holds only for the harness's own durable commits
and for `requestId`-keyed submissions. Interrupted effects have an unknown
outcome, and the agent has to re-inspect real state before deciding what to
do.

The evidence is weak: one unanswered issue, a vendor blog claim, and a forum
dispute. It is enough to distrust the strong reading of "exactly once", not to
quantify how often duplicates occur.

The safe design assumption for any agent is that an external action
interrupted by a crash may have run zero times, once or (where the engine
re-executes) more than once. A reasonable design, not a sourced result, is to
give each side-effecting action an idempotency key recorded before acting.
The key must identify one logical invocation and stay stable across retries
of that invocation, for example a durable operation or sequence ID. A hash of
only task, action and target is not enough, because a task that legitimately
repeats an action (a second restart after a second failure) would have its
later action suppressed as a duplicate. Then follow Cloudflare's rule of
checking whether an operation already completed before repeating it. The surrounding
mechanics are in [the effect sandwich](effect-sandwich.md),
[journal-then-replay](journal-then-replay-durable-execution.md) and [unknown
state on resurrection](../harness/unknown-state-on-resurrection.md); approvals
need the same treatment, as [durable approval
state](../harness/durable-approval-state.md) describes.
