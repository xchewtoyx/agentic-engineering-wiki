---
type: concept
title: Full-Trace Remediation Audit
description: >
  Log every action an operational agent takes with identity, prompt, tool calls,
  trigger and verified result, keeping raw traces as well as summaries, so each
  action is reconstructable and the agent can always say what it did and why.
evidence: moderate
sources:
  - title: "Execute mitigations"
    resource: "Azure SRE Agent docs (AgentAzCliExecution events) — https://sre.azure.com/docs/capabilities/execute-mitigations"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10 (logging LLM requests and configuration)"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 June 2025, production reliability section — https://www.anthropic.com/engineering/multi-agent-research-system"
  - title: "Self-Harness"
    resource: "Zhang et al., arXiv 2606.09498, June 2026 (preprint), safety constraints — https://arxiv.org/html/2606.09498v1"
  - title: "Audit and resume agent sessions"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026), export and redaction — https://dev.meta.ai/docs/cookbook/audit-agent-sessions"
---

Automated remediation that cannot account for itself erodes trust quickly. When
a system behaves oddly the morning after an incident, the operator needs to
know whether the agent touched it, on what evidence, with which prompt and
model, through which commands, and whether the result was verified. Because LLM
behaviour is probabilistic, the same inputs may not reproduce the same decision
later, so the record has to be captured at the time.

Several sources specify what the record should hold. Azure SRE Agent logs every
action with identity, operation, timestamp, trigger and result as
`AgentAzCliExecution` events. Huyen's guidance on LLM request logging lists the
model and sampling configuration, the final assembled prompt, intermediate and
tool outputs, and lifecycle events, each tagged so its origin can be traced.
Anthropic's multi-agent research post describes full production tracing of
decision patterns without reading conversation contents. Self-Harness, a 2026
preprint on agents editing their own harness, logs every transition as one of
its safety constraints. Meta's Muse Code records proposal, review, decision,
intent and result for every action, exports sessions byte-deterministically,
and offers a redacted export for sharing outside the organisation; its
multi-agent recipe keeps every cross-role decision as a comment on a
[shared task board](../orchestration/shared-task-board-coordination.md). The
evidence is moderate: practice is consistent across vendors, but no source
evaluates audit design for remediation agents specifically.

The resulting shape is one structured record per action. It holds the trigger
and the score that woke the model, the evidence read, the full prompt and model
configuration, the proposal, the deterministic validation, the
[verb](narrow-action-verb-set.md) applied, and both the agent's claimed outcome
and the [owner's verdict](../evaluation/owner-validation-decides-success.md).
Narrow verbs and [code-applied proposals](llm-proposes-code-applies.md) are what
make such a record precise, since a raw shell session says little reliably
about what was done. Raw traces should be retained as well as any summary,
because debuggers and optimisers do markedly better on raw material
([raw traces over summaries](../optimization/raw-traces-over-summaries.md)).

Keeping full prompts and raw traces makes the audit store a place where
secrets collect: evidence an operations agent reads, such as config files,
environment dumps and tool output, often contains tokens or keys. A redacted
export protects only copies that leave the store. Scrub secrets at capture
time, before anything is persisted, replacing them with opaque references
that resolve through the secret store. Treat the audit store itself as
sensitive, with least-privilege read access and a bounded retention period.
This keeps the record consistent with
[keeping credentials outside the sandbox](../security/credentials-outside-the-sandbox.md):
the agent never sees a raw credential, so the trace of what it saw holds none
either.

The same record lets operators ask the agent what it is doing, why, and what it
will do next, which is the standard defence against people losing track of what
automation has done. Where the agent later edits its own runbooks or prompts,
the record doubles as the lineage log that
[guarded self-modification](../optimization/self-modifying-harness-controllability.md)
requires, and exposing it to the agent itself follows
[making the runtime legible](agent-legibility-of-runtime.md).
