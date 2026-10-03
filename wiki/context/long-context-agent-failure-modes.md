---
type: concept
title: Agent Failure Modes That Grow with One Long Context
description: >
  Agentic laziness, self-preferential bias and goal drift grow the longer an
  agent stays in one context window, as do one-shotting the whole job and
  declaring premature completion.
evidence: moderate
sources:
  - title: "A harness for every task: dynamic workflows in Claude Code"
    resource: "claude.dev, 2 Jun 2026 — https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/"
  - title: "Effective harnesses for long-running agents"
    resource: "Justin Young, Anthropic Engineering, 26 Nov 2025 — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

Some agent failures are not about what is in the context but about how the agent
behaves the longer it works in one window. They look like judgement problems
(stopping early, grading its own work too kindly, forgetting a constraint), and
adding more instructions does not fix them. They are distinct from the
content-level [four ways long contexts fail](four-context-failure-modes.md).

Anthropic's claude.dev post on dynamic workflows names three such failure modes
of a long single context. **Agentic laziness** is stopping early and declaring
the work done. **Self-preferential bias** is favouring its own findings when
asked to judge them. **Goal drift** is losing constraints to lossy compaction.
Anthropic's earlier long-running-agents post adds two from its own experiments.
The agent tries to **one-shot** the whole job and runs out of context halfway,
and a later session sees partial progress and **declares completion
prematurely** (the instruction-side view is in
[premature completion](../instructions/premature-completion.md)). Compaction
alone fixed neither. The same post lists leaving the environment broken and weak
verification among the observed failures.

The remedies Anthropic reports are structural rather than prompt-based. The
long-running harness limits each session to
[one unit of work](../orchestration/one-unit-of-work-per-session.md), with
progress held in files and git rather than in the window
([externalised progress artefacts](../knowledge/externalised-progress-artifacts.md)).
The dynamic-workflows post splits work across sub-agents in patterns such as
adversarial verification and loop-until-done, which counter self-preferential
bias by moving judgement to a
[separate evaluator](../evaluation/separate-generator-from-evaluator.md).
Explicit completion checks, as in [verify before done](../harness/verify-before-done.md),
target laziness and premature completion. Goal drift connects to the choice in
[compaction vs context reset](compaction-vs-context-reset.md), since a reset with
a clean handoff restates the goal while repeated compaction can wear it away.

The general lesson is not to run a long task as one ever-growing conversation.
Breaking it into bounded steps (for example diagnose, propose, act, verify), each
starting from written state rather than a long transcript, and having
verification done by a different agent or a deterministic check, addresses all
five modes. The same behaviours are worth watching for in any long-lived agent
session that claims success for work that never completed.
