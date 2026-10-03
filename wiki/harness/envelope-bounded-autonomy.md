---
type: concept
title: Autonomy Bounded by the Prepared Envelope
description: >
  An agent that takes operational actions should act alone only on situations
  matching a known runbook signature, and leaving that prepared envelope
  (unknown diagnosis, exceeded retry or failure thresholds, a high-risk action)
  should trigger escalation as a planned step.
evidence: moderate
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Cuvelier and Falzon, ch. 3 (envelope trespass as the escalation trigger)"
  - title: "Incident Management for Operations"
    resource: "Schnepp, Vidal and Hawley, ch. 4 (escalation as a resource request)"
  - title: "A practical guide to building agents"
    resource: "OpenAI, business guide PDF, section 'Plan for human intervention' — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"
  - title: "Build an SRE agent for incident response"
    resource: "OpenAI Cookbook, 10 September 2026 — https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/agents_api/apps/sev_bot/README.md"
---

An autonomous agent that acts on live systems will meet situations nobody
anticipated. If it treats every situation as solvable, it improvises under
incident conditions with a model whose diagnostic accuracy is uneven and often low
(see [LLM SRE agent success varies by benchmark and fault class](../evaluation/llm-sre-agents-low-success.md)).
If it escalates everything, it adds nothing. The design question is where the
boundary of autonomous action sits and what crossing it means.
[Human approval gates](human-approval-gates.md) answer this per action ("this
tool needs approval"); the envelope answers it per situation ("this incident is
one we prepared for").

Resilience engineering supplies a frame, by analogy from work on human
operators rather than software. Cuvelier and Falzon distinguish situations that
were foreseen and have prepared responses from those that were not. Deciding
that the situation has left the prepared envelope is itself the escalation
trigger, and calling for help is a deliberate, pivotal step rather than a
defeat. Incident-management practice makes the same point from the other side:
escalation is a request for more or different resources as conditions change,
not an admission of failure. The split mirrors the operational distinction
between known failure modes handled by runbooks and novel ones that need
open-ended investigation.

The idea also has direct support from agent builders. OpenAI's practical guide
names two triggers for human intervention: exceeding failure thresholds such as
retry or action limits, and high-risk actions. Its SRE-agent cookbook gives
`propose_rollback` no automatic handler; the agent pauses for approval through
a webhook and Slack buttons. Combining these with the analogy, the evidence is
rated moderate.

In practice the agent carries an explicit catalogue of failure signatures with
pre-approved responses, and acts autonomously only when a diagnosis matches
one. Three conditions route the incident to a human or a more capable worker
as a named runbook step: an unmatched diagnosis, an exceeded retry or failure
threshold, or an action above a risk line. Low agent success rates argue for
keeping the envelope narrow. Inside it, the
[diagnose-by-default posture](diagnose-by-default-act-by-exception.md) and the
[degradation ladder](../orchestration/degradation-ladder.md) apply, and the
pre-approved responses are easiest to define as
[narrow action verbs](narrow-action-verb-set.md). Any approval obtained at the
boundary should survive restarts
([durable approval state](durable-approval-state.md)), and the envelope should
never let one actor hold untrusted input, sensitive access and state change
together ([the agents Rule of Two](../security/agents-rule-of-two.md)).
