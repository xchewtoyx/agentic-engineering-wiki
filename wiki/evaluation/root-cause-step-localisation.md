---
type: concept
title: Localise the Root-Cause Step
description: >
  Errors in tool-using agents cascade from an early root cause, so diagnosis
  should find the step where the cascade began and feed back a correction
  from that point.
evidence: moderate
sources:
  - title: "Where LLM Agents Fail and How They Can Learn From Failures"
    resource: "Zhu, Liu, Li et al., arXiv 2509.25370, 29 Sep 2025 (AgentDebug) — https://arxiv.org/abs/2509.25370"
---

When a tool-using agent fails, the visible error is often far from its cause.
An early wrong assumption about a file, a misread tool result or a bad plan
produces a chain of reasonable-looking later steps that all fail. Fixing the
last step treats a symptom. The useful question is where the chain began.

The AgentDebug paper builds tooling around that question. It contributes:

- an error taxonomy organised by agent module (memory, reflection, planning,
  action and system);
- a benchmark of annotated failure trajectories drawn from ALFWorld, GAIA and
  WebShop;
- AgentDebug itself, which isolates the root-cause step in a failed
  trajectory and gives corrective feedback from that point.

The authors report 24% higher all-correct accuracy, 17% higher step accuracy,
and up to 26% relative gain in task success.

The paper is a 2025 arXiv preprint with released code. Its benchmarks are
agent tasks, not infrastructure incidents, so the size of the gain should not
be assumed to transfer.

In practice, diagnose a failed run by walking back through the raw trace to
the earliest step that went wrong, such as the first failed tool call, the
first configuration change or the first resource warning, rather than
reacting to the final error. That needs
[raw traces rather than summaries](../optimization/raw-traces-over-summaries.md).
Feedback to the agent should point at that step, which is how
[failures are returned as actionable feedback](../harness/failures-returned-as-actionable-feedback.md).
When many failures are being fixed at once, localise within each
[failure-signature cluster](../optimization/failure-signature-clustering.md)
rather than per run. The categories in the
[MAST taxonomy](mast-multi-agent-failure-taxonomy.md) and the
[agent runtime fault taxonomy](agent-runtime-fault-taxonomy.md) help name what
was found.
