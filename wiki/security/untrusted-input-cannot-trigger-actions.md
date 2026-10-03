---
type: concept
title: Untrusted Input Must Not Trigger Actions
description: >
  Once untrusted content enters an agent's context, the architecture rather than
  model robustness must stop it from causing consequential actions, through
  injection-resistant design patterns or CaMeL-style control/data-flow
  separation.
evidence: moderate
sources:
  - title: "Design Patterns for Securing LLM Agents against Prompt Injections"
    resource: "Beurer-Kellner, Tramèr et al., arXiv 2506.08837, June 2025, via Simon Willison's summary — https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/"
  - title: "CaMeL: Defeating Prompt Injections by Design"
    resource: "Debenedetti et al., arXiv 2503.18813 (SaTML 2026), via Pith review https://pith.science/paper/2503.18813 and MIT reading-list PDF https://css.csail.mit.edu/6.5660/2026/readings/camel.pdf"
---

An agent that reads anything it did not write (a web page, a tool return, a log
line) is exposed to [indirect prompt injection](indirect-prompt-injection.md):
instructions planted in that content can be followed as if they came from the
operator, turning the agent into a [confused deputy](confused-deputy.md).
Attempts to make the model itself resist this keep failing (see
[injection defences are bypassable](prompt-injection-defences-are-bypassable.md)),
and ranking tool output low in the [instruction hierarchy](instruction-hierarchy.md)
only lowers the odds. So the research literature has shifted the question from
"will the model obey the attacker?" to "can the attacker's text reach anything
that matters?".

The design-patterns paper by Beurer-Kellner and colleagues states the principle
directly: once an agent has ingested untrusted input, that input must be unable
to trigger consequential actions. It offers six patterns for achieving this.
Action-selector and plan-then-execute fix the set of actions before untrusted
data is seen; large language model (LLM) map-reduce and the dual-LLM pattern
quarantine untrusted text in a model that cannot act; code-then-execute and
context-minimisation limit what the untrusted text can influence. The paper is
known here mainly through Willison's summary. Plan-then-execute is the security
reading of [plan, validate, execute](../orchestration/plan-validate-execute.md).

CaMeL (Debenedetti et al., published at SaTML 2026) is the strongest form of
the idea. It extracts control and data flow from the trusted user query before
any untrusted data is read, then enforces capability-based policies at every
tool call. On AgentDojo it solved 77% of tasks with provable security, against
84% for an undefended agent. Reviewers note an important limit: the guarantee
holds only when flow extraction succeeds, so it is a strong but conditional
boundary rather than a universal one.

Agents that operate systems read exactly the kind of content these papers worry
about ([logs are untrusted input](logs-are-untrusted-input.md)). Such an agent
should either be unable to take consequential actions while reading that
content, or should hand findings to a separate privileged actor as structured,
symbolic references. That maps onto the action-selector pattern in
[the LLM proposes, code applies](../harness/llm-proposes-code-applies.md), and
onto limiting capability combinations under
[the agents Rule of Two](agents-rule-of-two.md).
