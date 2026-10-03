---
type: concept
title: Pinned Goal with Harness-Audited Acceptance Checks
description: >
  Pin the objective once, with named acceptance checks such as a test file or
  command, and let the harness refuse to close the goal until those checks
  pass; a progress probe nudges the agent when it stalls.
evidence: moderate
sources:
  - title: "Goal tracking"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/goal-tracking"
  - title: "Finding the Right Fit: Model–Harness Interactions"
    resource: "Li et al., arXiv 2610.00917, October 2026 (preprint), §5.2 — https://arxiv.org/html/2610.00917"
  - title: "Harness design for long-running application development"
    resource: "Anthropic Engineering (Prithvi Rajasekaran), 24 Mar 2026, sprint contracts — https://www.anthropic.com/engineering/harness-design-long-running-apps"
---

Over a long task an agent's sense of what it is meant to achieve drifts, and
its sense of when it has finished is unreliable. A 2026 model–harness preprint
found that every failed run ending with a final report (35 of them) claimed the
requirements had been verified, because no harness exposed the true acceptance
criteria and agents checked against tests they had written themselves, the
hazard described in
[self-generated test evaluators](../evaluation/self-generated-test-evaluator.md)
and [proxy validation failure](../evaluation/proxy-validation-failure-pattern.md).
A finish line that lives only in the conversation is easy to lose and easy to
redefine.

Meta's Muse Code moves both the objective and the finish line into the harness.
A `/goal` command stores the objective for the session before work starts, and
the recipe asks for concrete oracles in it, such as a named test file or
command, phrased as "done only when these checks pass". The harness then tracks
status, queues a nudge to continue after roughly ten model calls with no
reported progress, and runs a completion audit that blocks the agent from
marking the goal complete until every acceptance check passes. The page
metadata describes this audit as a judge that refuses to close the turn. The
recipe limits the pattern to multi-turn tasks where drift is likely.
Anthropic's sprint contracts, in which generator and evaluator agree testable
criteria before work begins, are the same idea negotiated rather than declared.

The note is moderate because the mechanism comes from one undated vendor
recipe, while the failure it answers is documented independently. It is a
harness-enforced form of [verify before done](verify-before-done.md), it relies
on the checker being separate from the worker as in
[separate the generator from the evaluator](../evaluation/separate-generator-from-evaluator.md),
and its stall probe is a gentler relative of
[doom-loop detection](doom-loop-detection.md).

For an agent that repairs or operates a live system, the acceptance checks
should be the system owner's checks (a readiness probe, a clean diagnostic
run, an end-to-end round trip), and the agent should be unable to record the
incident as resolved until the harness has run them. That makes
[owner validation](../evaluation/owner-validation-decides-success.md) a property
of the harness rather than a promise in the prompt.
