---
type: concept
title: Judge Reliable Lift, Not Mean Lift
description: >
  Judge harness changes by a lower-percentile held-out "reliable lift" and by
  repeatability rather than by mean gain, because search procedures can select
  brittle edits with large average improvements.
evidence: weak
sources:
  - title: "Beyond Prompts"
    resource: "Zhao, Ruan, Chen, Tu, Abbasi, Hesch (Airbnb), arXiv 2609.05736, 4 Sep 2026, §3 and Table 2 (preprint) — https://arxiv.org/html/2609.05736v1"
  - title: "τ-bench"
    resource: "Yao, Shinn, Razavi, Narasimhan (Sierra), arXiv 2406.12045, 17 Jun 2024 — https://huggingface.co/papers/2406.12045"
---

A harness change that raises the average score can still be a bad change. If
the gain comes from a few lucky runs, or collapses on tasks outside the tuning
set, the mean hides it. Automated search over harness edits makes this worse,
because it will find whatever edit scores highest, brittle or not.

Two lines of work address this. τ-bench, a 2024 benchmark from Sierra,
introduced [pass^k](pass-at-k-and-pass-hat-k.md), the rate of succeeding on
the same task in all k independent trials, and showed how far it falls below
single-run success: GPT-4o succeeded on under half of tasks, and pass^8 in the
retail domain was below 25%.

A 2026 preprint from Airbnb, "Beyond Prompts", adds metrics for
effectiveness, stability, repeatability and efficiency, and a reliable-lift
estimator called RelLift95 that reports a lower-percentile held-out gain
rather than the mean. Its middleware optimiser shows the gap:

| Benchmark | Mean held-out lift | Reliable lift |
|---|---|---|
| Multi-round | 14.2 points | 12.0 points |
| Retail | 14.9 points | 10.1 points |

The abstract warns that some search procedures find large gains yet still
select brittle updates.

τ-bench is established. RelLift95 is a single preprint, so the specific
estimator is weakly supported even though the principle is well grounded.

The practical rule: judge any change to an agent's prompts, tools or
playbooks, or to its harness settings, on repeated runs over held-out tasks,
reporting the worst-case or lower-percentile result rather than the average.
This is the acceptance criterion inside
[in-loop regression control](../optimization/in-loop-regression-control.md)
and in [guarded self-modification](../optimization/self-modifying-harness-controllability.md).
Disclose what changed through [harness cards](harness-card-disclosure.md), and
read the [transcripts](agent-eval-outcome-vs-transcript.md) of the runs that
fail to see why a change is brittle.
