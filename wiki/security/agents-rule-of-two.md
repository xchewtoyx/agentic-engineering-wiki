---
type: concept
title: The Agents Rule of Two
description: >
  An autonomous agent should hold at most two of untrusted input, sensitive
  access, and state change or external communication; holding all three needs a
  human in the loop, because that combination enables exfiltration.
evidence: moderate
sources:
  - title: "New prompt injection papers: Agents Rule of Two and The Attacker Moves Second"
    resource: "Simon Willison, 2 Nov 2025 — https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/"
  - title: "The lethal trifecta for AI agents"
    resource: "Simon Willison, 16 Jun 2025 — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/"
---

Prompt injection cannot currently be prevented at the model layer (see
[injection defences are bypassable](prompt-injection-defences-are-bypassable.md)),
so the practical question is which agents are dangerous when injection
succeeds. Willison's "lethal trifecta" (June 2025) answered it for data theft:
an agent that combines access to private data, exposure to untrusted content
and a channel for external communication can be steered into exfiltrating that
data, because the attacker's text can tell it what to read and where to send
it. That is the [confused deputy](confused-deputy.md) problem with a concrete
recipe for damage.

Meta's "Agents Rule of Two", which Willison endorsed in November 2025,
generalises the trifecta into a design rule. An autonomous agent should have at
most two of three properties: (A) it processes untrusted input, (B) it has
access to sensitive systems or private data, and (C) it can change state or
communicate externally. An agent that needs all three should not run
unattended; a human must approve its actions through
[approval gates](../harness/human-approval-gates.md). The rule does not stop
injection. It bounds what an injected agent can achieve by removing one leg of
the attack.

The rule sits on one side of a live debate about permission prompts. Zechner
treats prompts as theatre and relies on container isolation, whereas Willison
and Meta argue for structural limits on capability combinations (see
[contain at the environment layer first](contain-environment-first.md) for the
containment view).

Agents that operate or repair systems are the uncomfortable case: they
naturally hold all three properties, reading logs and traffic (untrusted),
reaching databases, tokens and control planes (sensitive), and existing to
change state. Ways to drop a leg include keeping credentials out of the agent's
reach ([credentials stay outside the sandbox](credentials-outside-the-sandbox.md)),
splitting a read-only diagnosis tier from an approval-gated action tier
([diagnose by default, act by exception](../harness/diagnose-by-default-act-by-exception.md)),
and treating log content as data rather than instructions
([logs are untrusted input](logs-are-untrusted-input.md)). Escalating when the
combination cannot be avoided is the subject of
[autonomy bounded by the prepared envelope](../harness/envelope-bounded-autonomy.md),
and the architectural complement is
[untrusted input must not trigger actions](untrusted-input-cannot-trigger-actions.md).
