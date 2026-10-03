---
type: concept
title: Worktree-Isolated Sub-Agent Fan-Out
description: >
  When parallel sub-agents must write, give each its own git worktree checked
  out from a base commit, bound concurrency, and treat cancellation as
  cooperative, so parallel writers never collide mid-flight and the parent
  checkout stays untouched.
evidence: weak
sources:
  - title: "Subagent fanout"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/subagent-fanout"
  - title: "Harness engineering"
    resource: "OpenAI, per-worktree observability stack — https://openai.com/index/harness-engineering/"
---

Parallel sub-agents save wall-clock time, but parallel writers in one working
tree overwrite each other's files and leave the tree in states no single agent
intended. The usual answer is that only one agent should write ([single-threaded
writes](single-threaded-writes.md)). Some jobs, though, split naturally into
several write tasks that touch overlapping files.

Meta's Muse Code cookbook describes how its harness lets such tasks run in
parallel. With worktree isolation enabled, each write-capable child gets its
own git worktree under the harness's state directory, checked out detached from
the parent repository at a base commit. Children work only inside their
worktree and the parent's checkout is untouched until their results are
collected. Concurrency is bounded by the host, roughly the number of cores
minus two and clamped between four and eight, with further spawns queued. The
parent can check status, send a child a message, cancel it, wait and read its
result. Two caveats come with it: a queued steering message reaches a child
only on its next turn, so a hard redirect needs an interrupt, and cancellation
is cooperative, so a child already writing its result may finish anyway.
OpenAI's harness work uses worktrees for a related purpose, giving each one its
own observability stack.

The evidence is one undated vendor recipe, so the note is weak. It qualifies
rather than contradicts single-threaded writes: the writers never share a
tree, and merging their results remains a single, serial step. Cooperative
cancellation is a weaker guarantee than the abort propagation in a [task
ownership tree](task-ownership-tree-abort-propagation.md).

The pattern depends on the written state being forkable. Live services,
volumes and databases cannot be checked out like a worktree, so parallel
writers against a running system remain unsafe. For an agent that operates
such systems, worktree fan-out fits the offline side of the work instead, such
as trying several candidate configuration or runbook changes in parallel
before one is chosen and applied.
