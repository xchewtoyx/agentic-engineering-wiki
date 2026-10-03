---
type: concept
title: Single-Threaded Writes
description: >
  Multi-agent systems work when exactly one actor writes to a given piece of
  state and the others only add intelligence through review, consultation or
  research; parallel-writer swarms and second writers on a state store fail.
evidence: moderate
sources:
  - title: "Don't Build Multi-Agents"
    resource: "Walden Yan, Cognition, June 2025 — https://cognition.com/blog/dont-build-multi-agents"
  - title: "Multi-agents update (Cognition blog)"
    resource: "Cognition, 22 Apr 2026 — https://cognition.com/blog/multi-agents-working"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 Jun 2025 — https://www.anthropic.com/engineering/multi-agent-research-system"
  - title: "Ralph Wiggum as a 'software engineer'"
    resource: "Geoffrey Huntley, ghuntley.com — https://ghuntley.com/ralph/"
  - title: "What I learned building an opinionated and minimal coding agent"
    resource: "Mario Zechner, 30 Nov 2025 — https://mariozechner.at/posts/2025-11-30-pi-coding-agent/"
  - title: "Multi-agent orchestration"
    resource: "Meta Model API cookbook, Use Cases, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/multi-agent-orchestration"
  - title: "Subagent fanout"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/subagent-fanout"
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Storage — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Agent loop"
    resource: "OpenClaw documentation — https://docs.openclaw.ai/concepts/agent-loop"
  - title: "Compose operations"
    resource: "OpenClaw documentation — https://docs.openclaw.ai/install/docker/compose-operations"
  - title: "Docker"
    resource: "Hermes Agent documentation (Nous Research) — https://hermes-agent.nousresearch.com/docs/user-guide/docker"
---

Splitting work across several agents is tempting, because each gets a fresh
context and the work can run in parallel. The trouble starts when more than one
of them changes things. Cognition's 2025 post argued that agents should share
full context because every action carries implicit decisions, and two agents
acting on partial context make conflicting ones.

By 2026 the debate has largely converged. Cognition's April 2026 update reports
that review loops, a "smart friend" consultation pattern and manager
decomposition work, while parallel-writer swarms do not, nor do small models
escalating to larger ones. Independent review agents caught about two bugs per
pull request, 58% of them severe, and worked best without the coder's context.
Geoffrey Huntley runs many sub-agents for search but only one for build and
test. Anthropic's multi-agent research system, an Opus lead with Sonnet
sub-agents, beat single-agent Opus by 90.2% on an internal research evaluation,
but used about 15 times the tokens of chat; token usage alone explained 80% of
the variance on one benchmark (the cost side is
[multi-agent token inflation](multi-agent-token-inflation.md)). Anthropic says
the pattern suits breadth-first, parallel work and suits coding less, and has
sub-agents write outputs to a filesystem to avoid a "game of telephone".

**Dissent remains.** Mario Zechner rejects sub-agents altogether as an opaque
black box within a black box, and keeps plans in markdown files instead.
Huntley, at the other extreme, runs hundreds of sub-agents for read-heavy work.
The cost figure also argues against defaulting to multi-agent designs, which is
the position of [start simple and own the control
flow](start-simple-own-control-flow.md).

The principle is single-threaded writes: one actor changes state, and the
others add intelligence. It narrows the role split in [multi-agent
architecture](multi-agent-architecture.md): planners, critics and researchers
can multiply, but the executor that writes stays singular. It pairs naturally
with a [separate evaluator](../evaluation/separate-generator-from-evaluator.md),
which reads but does not write. Meta's cookbook takes a qualified position. Its
Hermes recipe keeps a coordinator that cannot run code but lets several
specialists write in parallel, sequenced through a [shared task
board](shared-task-board-coordination.md), and Muse Code gives each parallel
writer its own git worktree ([worktree-isolated sub-agent
fan-out](worktree-isolated-subagent-fanout.md)); both advise a single agent for
one-role tasks.

## At the storage layer

The same rule applies to the stores an agent runtime keeps: transcripts, task
state and memory in SQLite files or JSON Lines directories. These stores assume
a single owner, and a deployment can break that assumption without anyone
noticing, by scaling a service to two replicas, running a one-off command-line
container against the same volume, or starting a second gateway while
troubleshooting. Vendor documentation is explicit. Pi Durable allows one
process to own a store at a time and provides no cross-process locking, so
single-writer ownership has to be enforced outside the package, by a single
replica or a lease. OpenClaw serialises its per-session agent loop and fences
transcript writes with a durable `activeWriterRunId` claim, so a superseded run
cannot commit stale data, and a state-directory lock stops a second gateway
from owning the same state; a crashed owner's lock is reclaimed after about 90
seconds without a heartbeat, and filesystems without exclusive create can block
ownership altogether. Hermes's docs say never to run two gateway containers on
one data directory. The general mechanism is a fencing token: a claim that
increases with each new owner, which the store checks so that writes from a
superseded or zombie actor are rejected.

For an agent that operates other systems, the rule cuts both ways. Several
actors (platform restart policies, vendor supervisors, a repair agent, coding
agents) may be able to act on the same service, so exactly one should hold the
right to change it at a time while the others diagnose, review or advise. And
the operating agent must never become a second writer itself, for example by
opening a live database or starting a parallel instance to test a theory; that
is part of why it should act from outside, as an [external
supervisor](external-supervisor-over-self-diagnosis.md). At the task level the
same discipline appears as a [task ownership
tree](task-ownership-tree-abort-propagation.md).
