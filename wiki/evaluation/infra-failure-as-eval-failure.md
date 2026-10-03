---
type: concept
title: Count Infrastructure Failures As Task Failures
description: >
  When computing an eval's pass rate, score a trial that dies on an
  infrastructure exception as a failure rather than discarding it, so the
  metric can't be inflated by silently dropping hard trials.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. A"
  - title: "Infrastructure noise"
    resource: "Anthropic Engineering, 5 Feb 2026 — https://www.anthropic.com/engineering/infrastructure-noise"
---

A rollout can fail two different ways: the agent genuinely fails the task, or
the surrounding infrastructure fails it first — a sandbox crash, an API
timeout, some fault that has nothing to do with the agent's competence. The
tempting convention is to discard the second kind and compute
[pass@1](pass-at-k-and-pass-hat-k.md) only over trials that ran to
completion. That convention is a hidden metric-inflation risk: harder tasks
are disproportionately likely to hit timeouts and resource exhaustion, so
discarding infra failures selectively removes the trials most likely to have
failed anyway, quietly raising the reported pass rate.

The harsher, more defensible convention: count every infrastructure exception
as a failed trial (reward 0) in the numerator and denominator of the pass
rate, exactly like a genuine task failure. This keeps the metric comparable
across runs and across leaderboards that use the same convention, and it
removes any incentive — deliberate or accidental — to make a configuration
*look* more reliable by making its failures crash instead of complete.
Token-cost figures are a legitimate exception to this rule: excluding
infra-aborted trials from a mean-tokens-per-trial figure (used in
[Succ/Mtok](successes-per-million-tokens.md)) is fine, since a truncated
trial's token count doesn't represent what a completed trial actually costs
— the harsher-counting rule applies to the success/failure tally, not to
every downstream statistic computed from completed trials.

Counting infra failures honestly does not remove them, and they are larger
than they look. Anthropic's engineering team measured the effect of container
resource limits on Terminal-Bench 2.0. The most- and least-resourced setups
differed by 6 percentage points (p < 0.01), and infrastructure error rates
fell from 5.8% under strict limits to 0.5% with no cap. Scores barely moved
between one and three times resource headroom (p = 0.40) but rose about 4
points from three times to uncapped. On SWE-bench, five times the RAM gave
+1.54 points. This is a lab research post with significance tests, not a
peer-reviewed study.

So CPU and memory limits are part of the harness. The post recommends
specifying guaranteed allocation and the hard kill threshold separately,
treating resources as a documented experimental variable (as a
[harness card](harness-card-disclosure.md) would), and viewing leaderboard
gaps under about 3 points with suspicion unless the setup is published. The
same noise bears on claims that the
[harness is a performance lever](../harness-as-performance-lever.md): small
harness differences can sit inside it. When diagnosing a single failed run
rather than scoring a suite, rule out resource kills and out-of-memory events
before attributing the failure to model behaviour.
