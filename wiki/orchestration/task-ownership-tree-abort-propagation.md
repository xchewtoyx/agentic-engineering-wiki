---
type: concept
title: Task Ownership Trees
description: >
  Tasks and sub-agent conversations should form an explicit ownership tree in
  which parents wait on children under allSettled or failFast, aborts propagate
  down, and a replay-safe spawn finds its existing child instead of creating a
  duplicate.
evidence: moderate
sources:
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Child Tasks and §Abort and Subagents — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
---

An agent that spawns sub-agents or parallel probes has to answer some awkward
questions after a crash. Which children were already running? Should the
parent wait for all of them or stop at the first failure? And when the parent
is cancelled, what happens to work it started? Without explicit ownership, a
restarted parent can spawn duplicate children or leave orphans running.

Pi Durable answers these with an explicit ownership tree. A task can create
child tasks and commit a waiting state with one of two policies: `allSettled`
resumes the parent once every child has finished, while `failFast` also aborts
the remaining children when the first one fails. A waiting task runs no code,
and a task that finishes while work it owns is still running enters a
`completing` state until that work drains. Sub-agents are child conversations
owned by a tool-call task. Inside its commit, the sub-agent tool scans for an
existing child with its owner task ID, so a rerun finds the same child rather
than creating a second, and it submits work with a request ID derived from the
task ID, which makes the tool itself replay-safe. Aborting or failing the
parent aborts the child, the parent is idle only once the child is idle, and
tasks marked as background form a boundary that survives the parent's abort.
The README's examples include a checkout task owning four payments under
`failFast`.

This is author documentation of an experimental package, without independent
evaluation.

The structure suggests natural mappings, offered as design rather than sourced
result: a diagnosis as a parent task with child probe tasks under
`allSettled`, and a multi-step action with compensating rollbacks on the
checkout-and-payment pattern under `failFast`. A clear tree also limits who
may write, which fits [single-threaded writes](single-threaded-writes.md).
Meta's Muse Code offers a weaker contrast in [worktree-isolated sub-agent
fan-out](worktree-isolated-subagent-fanout.md), where cancellation is only
cooperative. The tree mirrors the parent-child restart structure of
[supervision-tree escalation](supervision-tree-escalation.md), and it depends
on [journal-then-replay](journal-then-replay-durable-execution.md) style
persistence and [durable approval state](../harness/durable-approval-state.md)
for children that wait on humans.
