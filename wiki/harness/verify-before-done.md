---
type: concept
title: Verify Before Done
description: >
  Agents favour their first plausible answer and declare completion early, so
  the harness must force verification before "done": a pre-completion
  checklist, end-to-end tests run as a user would, or an agreed sprint
  contract.
evidence: moderate
sources:
  - title: "Improving Deep Agents with harness engineering"
    resource: "LangChain (Viv Trivedy), 17 Feb 2026 — https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
  - title: "Effective harnesses for long-running agents"
    resource: "Anthropic Engineering (Justin Young), 26 Nov 2025 — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - title: "Harness design for long-running application development"
    resource: "Anthropic Engineering (Prithvi Rajasekaran), 24 Mar 2026 — https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - title: "Best practices for Claude Code"
    resource: "Anthropic, undated, section 'Give Claude a way to verify its work' — https://www.anthropic.com/engineering/claude-code-best-practices"
  - title: "A harness for every task: dynamic workflows in Claude Code"
    resource: "claude.dev, 2 Jun 2026, 'agentic laziness' — https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/"
  - title: "Goal tracking"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/goal-tracking"
---

Left to themselves, agents stop too early. LangChain observed that models
favour their first plausible answer. Anthropic's long-running harness work
found agents marking features done without testing them end to end, and later
sessions declaring a whole project complete on the strength of partial
progress. A dynamic-workflows post on claude.dev names the same tendency
"agentic laziness". An agent's own "done" is therefore weak evidence that
anything works, and a self-chosen check is often a
[proxy that only resembles success](../evaluation/proxy-validation-failure-pattern.md).

The fix in every source is to make verification a step the harness enforces
rather than one the agent may choose. LangChain added a pre-completion
checklist middleware that runs a self-verification loop before the agent may
finish, as part of the harness-only changes that took its agent from 52.8% to
66.5% on Terminal-Bench 2.0. Anthropic's long-running harness found that
explicitly prompting agents to test through browser automation, as a user
would, markedly improved results. Its later application-development harness
goes further, with a separate evaluator that drives the live application,
grades against hard thresholds and agrees a "sprint contract" of testable
completion criteria with the generator before any code is written. Anthropic's
Claude Code guidance opens with giving the agent a way to verify its work.
Meta's Muse Code builds the check into the harness: a pinned goal names its
acceptance checks, and a completion audit refuses to close the goal until they
pass (see
[pinned goal with harness-audited acceptance checks](pinned-goal-acceptance-checks.md)).

The sources are consistent practitioner and lab reports, with LangChain's
benchmark gain covering a bundle of changes rather than verification alone.

Verification can be computational, through [back-pressure](back-pressure.md)
and [a runtime the agent can observe](agent-legibility-of-runtime.md), or done
by a [separate evaluator](../evaluation/separate-generator-from-evaluator.md).
For agents that change live systems, the strongest version is that the system
or its owner decides, not the agent: a repair is finished when an independent
check confirms the system is serving again, as argued in
[owner validation decides success](../evaluation/owner-validation-decides-success.md).
