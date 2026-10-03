---
type: concept
title: The LLM Proposes, Code Applies
description: >
  The LLM proposes a diagnosis and an action from a schema of pre-approved
  actions while deterministic code computes, validates and applies the change,
  so the model never holds write authority and constrained output also cuts
  injection success.
evidence: moderate
sources:
  - title: "k8sgpt-operator"
    resource: "k8sgpt-ai on GitHub, README — https://github.com/k8sgpt-ai/k8sgpt-operator"
  - title: "Poisoning the Watchtower"
    resource: "Pandey and Bhujang, arXiv 2605.24421, 23 May 2026 (preprint) — https://arxiv.org/html/2605.24421"
  - title: "Run Claude Code programmatically"
    resource: "Claude Code docs, headless mode (--json-schema) — https://code.claude.com/docs/en/headless"
  - title: "Non-interactive mode"
    resource: "OpenAI Codex docs (--output-schema) — https://learn.chatgpt.com/docs/non-interactive-mode"
  - title: "Alert fatigue copilot"
    resource: "Meta Model API cookbook, Agent Patterns, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/alert-fatigue-copilot"
---

Giving a large language model (LLM) a shell or a write-capable API to change a
system mixes two jobs: deciding what is wrong and changing the system. The
first benefits from the model's flexibility. The second is where its errors,
and any instructions injected through the content it reads, turn into damage.

The k8sgpt operator separates the two. Its analysers find problems, and
auto-remediation is alpha, opt-in and limited to image-pull failures. Even
there, the operator re-fetches the object, computes the patch itself, validates
it against the API server and restricts changes to one approved image path. Its
README states that the LLM never receives write authority. A 2026 preprint on
log-borne prompt injection adds a security reason. Against an LLM log analyst,
constraining output cut average attack success from 26.6% to 11.8%, and the
authors recommend templated remediation output. Meta's alert-fatigue recipe
validates the model's JSON against a schema and requires every numeric claim to
trace back to the alert feed, noting that a schema guarantees shape, not facts.
The coding-agent CLIs already support this shape: Claude Code headless accepts
`--json-schema` and Codex exec accepts `--output-schema`, and the same effect
is available in an API call through
[forced tool choice](forced-tool-choice-extraction.md).

The general form: the model step emits a structured proposal, a diagnosis plus
one action chosen from a schema of pre-approved
[verbs](narrow-action-verb-set.md) with parameters, and nothing else.
Deterministic code then re-reads the live state, checks the proposal against
policy and the [hardline command floor](../security/hardline-command-floor.md),
and applies the change. This is the operational case of
[plan, validate, execute](../orchestration/plan-validate-execute.md), and an
instance of the action-selector pattern in
[untrusted input must not trigger actions](../security/untrusted-input-cannot-trigger-actions.md).
It matters most when the model reads attacker-influenceable content such as
logs ([logs are untrusted input](../security/logs-are-untrusted-input.md)). It
also fits the advice to keep control flow in ordinary code and use LLM steps
only at chosen points
([start simple and own the control flow](../orchestration/start-simple-own-control-flow.md)).

The evidence is moderate: the operator pattern is primary, while the injection
numbers come from one preprint.
