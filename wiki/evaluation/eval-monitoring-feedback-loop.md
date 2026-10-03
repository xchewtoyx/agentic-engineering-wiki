---
type: concept
title: Eval/Monitoring Feedback Loop
description: >
  Couple an agent's offline eval suite and its production telemetry in both
  directions: eval scores should predict what production shows, and every
  production failure should come back as an eval case.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
  - title: Demystifying evals for AI agents
    resource: "Demystifying evals for AI agents (Anthropic), Evaluating research agents"
  - title: Observability Engineering
    resource: "Observability Engineering, 2nd ed. (Majors, Fong-Jones, Miranda), ch. 21"
---

Offline evaluation and production monitoring have the same job: catching
failures, regressions, and drift before they hurt users. The difference is
only where in the lifecycle each one runs. Treat them as one loop rather than
as separate pre-deploy and post-deploy stages:

- **Eval scores should predict production.** If the suite passes a change and
  monitoring then catches a regression the suite could never have caught, the
  blind spot is in the eval suite, not just in monitoring. This is the
  production-side test of whether your
  [offline evaluation proxies](offline-evaluation-proxies.md) actually track
  the target.
- **Production failures become eval cases.** Promote real traces into eval
  fixtures. A failure found in telemetry, or a rejected agent proposal,
  becomes tomorrow's [regression case](capability-vs-regression-evals.md), so
  the same class of failure is caught before the next deploy. Prune fixtures
  that no longer reflect real usage. This is the continuous form of
  [mining real usage for eval samples](eval-sample-sourcing.md).

**Expect a drop on first contact.** A suite built before launch usually
scores sharply lower once real traffic arrives. Generic public benchmarks
mislead in the same way: an agent can score well on them and still fail its
actual users. Track eval pass rate as a service-level indicator, and rerun
the suite against the history of past cases after every prompt, harness, or
model change. That rerun is the main defence against the
[silent model swaps and prompt edits](harness-drift-awareness.md) that change
behaviour without a code diff.

**Change failure rate (CFR) tells you whether the loop works.** CFR is the
share of deploys that need a fix or a rollback. Not knowing your CFR is itself
a sign the system lacks observability. A high CFR doesn't automatically mean
monitoring failed. It can equally mean the eval suite needs rework so that bad
changes are caught before deploy instead of after.

**The human criteria drift too.** Developers' sense of a good or bad output
shifts as they see more real production data (Shankar et al., 2024). Sampled
manual review of production traces therefore stays valuable after automated
graders exist. Automated judges report pass or fail but miss the *why*, and
human reading surfaces new failure modes, such as an agent confidently acting
on a meaning the user never gave. Those findings should flow back into the
eval rubric and into
[recalibrating model-based graders against human judgment](grounding-llm-assessment-in-human-evaluation.md).
Score these production signals at
[episode scale rather than per request](episode-scale-evaluation-vs-request-apm.md).
