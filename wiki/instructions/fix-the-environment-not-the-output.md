---
type: concept
title: Fix the Environment, Not the Output
description: >
  Every agent mistake should become a permanent change to the agent's
  environment (an AGENTS.md line, a tool, a check), asking which capability
  is missing rather than telling the agent to try harder.
evidence: moderate
sources:
  - title: "My AI Adoption Journey"
    resource: "Mitchell Hashimoto, Feb 2026, read via Bloss0m summary (primary not fetched) — https://www.bloss0m.com/en/blog/16-mitchell-hashimoto-harness-origin/"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026 — https://openai.com/index/harness-engineering/"
---

When an agent gets something wrong, the cheapest response is to correct the output by hand or re-prompt with firmer wording. Both fix one instance and leave the cause in place, so the same mistake comes back in the next session or the next agent.

The alternative, attributed to Mitchell Hashimoto, is to treat each mistake as a defect in the environment. In his account of adopting AI tools (read here only through a secondary summary, because the primary post was not fetched), engineering the harness is the fifth of six stages, and his rule is that whenever an agent errs you change its environment so it cannot make that error again. He reports that almost every line of Ghostty's AGENTS.md came from a past bad agent behaviour. OpenAI's harness-engineering post, which is primary, makes the same move at organisational scale: when the agent fails, ask what capability is missing and make it legible and enforceable, rather than asking the agent to try harder.

This is close to a blameless postmortem whose action item is always a new guide or a new sensor, in the sense used in [guides and sensors](../harness/guides-and-sensors.md). The fix might be a line in a [steering file that acts as a map](steering-files-as-navigation-pointers.md), a [skill that captures a repeated correction](skill-as-repeated-correction.md), a new tool, or a deterministic check that supplies [back-pressure](../harness/back-pressure.md). What matters is that the fix lives in the repository or environment, where the next agent will meet it. Prefer the deterministic check when the rule is mechanical, because a check cannot be skipped the way a written line can.

For an agent that takes operational actions, such as a repair or operations agent, this becomes a closing step on every fix: once the failure is resolved, the failure class should leave a durable trace, such as a runbook entry, a new health check or a guard on the action that caused it. Grouping repeated failures first, as in [failure signature clustering](../optimization/failure-signature-clustering.md), keeps that from becoming one rule per incident. Each added line also has a cost, so the same discipline needs the opposite move too: pruning lines that no longer change behaviour, as described in [sediment](sediment.md).
