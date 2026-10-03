---
type: concept
title: Separate the Generator from the Evaluator
description: >
  A separately tuned, sceptical evaluator that does not share the generator's
  context is more tractable than self-critique, but it pays only when the task
  is beyond what the model does reliably on its own.
evidence: moderate
sources:
  - title: "Harness design for long-running application development"
    resource: "Anthropic Engineering (Prithvi Rajasekaran), 24 Mar 2026 — https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - title: "Cognition multi-agents update (multi-agents-working)"
    resource: "Cognition, 22 Apr 2026 — https://cognition.com/blog/multi-agents-working"
  - title: "A harness for every task: dynamic workflows in Claude Code"
    resource: "claude.dev, 2 Jun 2026 — https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/"
---

Agents praise their own work. The claude.dev dynamic-workflows post calls this
self-preferential bias, the tendency to favour one's own findings when judging
them, and lists it among the
[failures that grow the longer an agent stays in one context](../context/long-context-agent-failure-modes.md).
Asking the same agent to be harder on itself is an unreliable fix, for the
reasons behind [LLM self-assessment grading bias](llm-self-assessment-grading-bias.md).

Anthropic's application-development harness instead splits the roles. A
generator writes code, and a separate, sceptical evaluator, tuned on its own
with few-shot score breakdowns, drives the live application and grades it
against hard thresholds. The post reports that this split is more tractable
than making the generator self-critical. Cognition's 2026 update reaches a
similar conclusion from production: independent review agents catch about two
bugs per pull request, 58% of them severe, and work best without the coder's
context. Adversarial verification appears as one of six composable patterns
in the claude.dev post.

Both sides of the cost question come from the same Anthropic post. The
evaluator found real defects. It also added tokens and latency: the post's
sample run took about four hours and cost about $124. The authors conclude
that an evaluator is worth having only when the task lies beyond what the
model reliably does alone, and that harness pieces like this should be
stripped when a new model makes them unnecessary, because
[harness assumptions go stale](../harness-assumptions-go-stale.md).

The general rule: whatever proposes a change should not be the only judge of
whether it worked. The check should come from a different context, ideally a
different component. That is the evaluator side of
[verify before done](../harness/verify-before-done.md), the reason
[owner validation decides success](owner-validation-decides-success.md) for
operational agents, and the argument for an
[external supervisor over self-diagnosis](../orchestration/external-supervisor-over-self-diagnosis.md).
The same split applies inside optimisation loops as
[critique–optimizer separation](../optimization/critique-optimizer-separation.md).
