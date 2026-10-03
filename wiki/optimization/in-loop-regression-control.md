---
type: concept
title: Regression Control Inside the Loop
description: >
  Harness optimisers compound only when edits that lose previously solved
  tasks are rejected inside the search loop; without that gate, gains
  transfer negatively or stall on re-optimisation.
evidence: weak
sources:
  - title: "Do Agent Optimizers Compound?"
    resource: "arXiv 2607.14004, Jul 2026 (preprint; authors not captured) — https://arxiv.org/html/2607.14004v1"
  - title: "Self-Harness"
    resource: "Zhang et al. (Shanghai AI Lab), arXiv 2606.09498, 8 Jun 2026 (preprint) — https://arxiv.org/html/2606.09498v1"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 Jun 2025, rainbow deployments — https://www.anthropic.com/engineering/multi-agent-research-system"
---

An optimiser that repeatedly edits an agent's harness will usually find
improvements on the tasks it is currently looking at. The danger is that each
round quietly breaks tasks earlier rounds had solved, so the gains do not
accumulate and may reverse when the harness meets new work. The optimiser
cannot be trusted to see this coming: an evolve loop's own regression
predictions barely beat chance
([regression blindness](harness-self-attribution-regression-blindness.md)).

A July 2026 preprint tested this with a two-phase continual protocol on hard
Terminal-Bench 2.0 tasks:

| Optimiser | Phase 1 | Transfer to phase 2 | Re-optimised |
|---|---|---|---|
| GEPA | 70.8% | 54.5% | — |
| Meta-Harness | — | 68.2% | 59.1% |
| RELAI-VCL | 79.2% | 72.7% | 77.3% |

GEPA transferred negatively, Meta-Harness transferred well but stalled when
re-optimised, and RELAI-VCL led throughout. The authors attribute its lead to
regression control enforced inside the search loop: edits that lose
previously solved tasks are rejected before they are accepted, not caught
afterwards. Self-Harness takes a similar stance, requiring each edit to pass
regression gates on both held-in and held-out splits.

The evidence is weak. Both are preprints, and the authors of the first note
that their protocol assumes reliable verifiers and repeatable execution,
conditions that are hard to meet on live infrastructure.

The rule: treat any change to an agent's playbooks or harness configuration
like a deploy. Re-run a fixed regression set of previously solved tasks,
several times each, and reject the change if any of them stops passing, with a
[reliable (lower-percentile) lift](../evaluation/reliable-lift-not-mean-lift.md)
checked alongside the mean.
That set is a [regression eval](../evaluation/capability-vs-regression-evals.md)
run inside the optimiser rather than after it. A cheap deterministic layer
for the same gate is
[deterministic session replay in CI](../evaluation/deterministic-session-replay-ci.md),
which checks that recorded sessions still produce the same model context. The
gate is one of the controls that keep a
[self-modifying harness controllable](self-modifying-harness-controllability.md),
and it is what fixes from
[failure-signature clustering](failure-signature-clustering.md) should pass.

Shipping the accepted change is a separate concern. Anthropic reports using
rainbow deployments so that harness changes do not break agents already
mid-run, which matters whenever a harness is reconfigured with sessions in
flight.
