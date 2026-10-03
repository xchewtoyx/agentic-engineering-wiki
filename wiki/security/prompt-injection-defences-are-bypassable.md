---
type: concept
title: Injection Defences Are Bypassable
description: >
  Adaptive attacks bypassed 12 published prompt-injection defences at over 90%
  success and human red-teams always succeeded, so model-layer defences are one
  layer of protection, never the security boundary.
evidence: weak
sources:
  - title: "New prompt injection papers: Agents Rule of Two and The Attacker Moves Second"
    resource: "Simon Willison, 2 Nov 2025, reporting 'The Attacker Moves Second' (authors from OpenAI, Anthropic and Google DeepMind) — https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/"
---

Many published defences against prompt injection work at the model layer:
classifiers that flag suspicious input, prompt wrappers that tell the model to
ignore embedded instructions, or fine-tuning for robustness. They tend to be
evaluated against fixed attack sets. The question that matters for a deployed
agent is whether they hold against an attacker who sees the defence and
adapts.

Willison reports a paper titled "The Attacker Moves Second", written by authors
from OpenAI, Anthropic and Google DeepMind, that tested exactly this. Adaptive
attacks got past 12 published defences with success rates above 90%, and human
red-teamers succeeded every time. The evidence here is weak in one specific
sense: the paper is known here only through Willison's summary, so the
experimental details and the exact defence list are unverified.

The direction of the finding is consistent with the rest of the agent-security
literature. The design-patterns and CaMeL work starts from the premise that the
model cannot be trusted once it has read hostile text (see
[untrusted input must not trigger actions](untrusted-input-cannot-trigger-actions.md)),
and Anthropic's containment guidance puts deterministic environment boundaries
first and model-layer steering second (see
[contain at the environment layer first](contain-environment-first.md)). The
prompt-side techniques in
[prompt-level attack defenses](prompt-level-attack-defenses.md) and
[defensive prompt engineering](defensive-prompt-engineering.md), and ranking
tool output low in the [instruction hierarchy](instruction-hierarchy.md), still
have a role as layers, as does scanning tool output before it reaches the model
([inspect tool output before it enters context](inspect-tool-output-before-context.md)),
but each should be expected to leak.

The consequence is that no prompt wording, system instruction or classifier in
front of an agent should be treated as what keeps it safe. Its safety has to
come from what it is structurally able to do, for example by holding at most
two of the risky capabilities named in
[the agents Rule of Two](agents-rule-of-two.md), backed by the containment
controls in [agent system-level defenses](agent-system-level-defenses.md).
