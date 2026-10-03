---
type: concept
title: Layered Agent Permission Stack
description: >
  Production harnesses layer execution policy, lifecycle hooks, LLM or human
  approval and OS sandboxing; guardrails can run optimistically in parallel, and
  a reasoning-blind classifier can replace per-action human approval.
evidence: moderate
sources:
  - title: "Harness Engineering (source-code study of agent harnesses)"
    resource: "Wavestone, arXiv 2609.00006, §10 — https://arxiv.org/html/2609.00006v1"
  - title: "A practical guide to building agents"
    resource: "OpenAI, PDF, Guardrails section — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"
  - title: "OpenAI Agents SDK"
    resource: "OpenAI developer docs — https://openai.github.io/openai-agents-python/"
  - title: "How we built Claude Code auto mode"
    resource: "Anthropic Engineering, 25 Mar 2026 — https://www.anthropic.com/engineering/claude-code-auto-mode"
  - title: "How we contain Claude across products"
    resource: "Anthropic Engineering, 25 May 2026 — https://www.anthropic.com/engineering/how-we-contain-claude"
  - title: "Staged approvals"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/staged-approvals"
---

No single permission mechanism is good enough on its own. Static policy cannot
anticipate every command, human approval does not scale to hundreds of actions
per run, and model judgement can be manipulated. Production harnesses therefore
stack several mechanisms, and the stack is one of the
[seven harness subsystems](../harness/seven-harness-subsystems.md). Where
[agent system-level defenses](agent-system-level-defenses.md) lists the kinds of
control available, this note is about how real harnesses arrange them.

The Wavestone source-code study (arXiv 2609.00006, a 2026 preprint) compares
these stacks. Aider and Mini-SWE-Agent have only cost and step budgets. Claude
Code combines execution policy, lifecycle hooks and human approval. Codex has
four layers: server-delivered Starlark policy, hooks, a large language model
(LLM) approval reviewer and a native operating-system (OS) sandbox. OpenClaw's
model is scope-based, tied to session and plugin. Only Codex and Gemini CLI
have cross-platform native OS sandboxing. Meta's Muse Code cookbook adds a
finer-grained policy layer, splitting compound shell commands into stages that
are approved one by one, with a deny always beating an allow (see
[staged command approval](staged-command-approval.md)).

Two design moves make the stack cheaper to run. OpenAI's practical guide
describes guardrails as layered defences (relevance and safety classifiers,
personal-data filtering, moderation, per-tool risk ratings, rules and output
validation), and the Agents SDK runs them optimistically: the agent proceeds
while tripwires run in parallel. The guide names two triggers for human
intervention, exceeded failure thresholds and high-risk actions. Anthropic's
auto mode goes further and replaces the human approver with a two-stage
transcript classifier, a fast single-token filter followed by chain-of-thought
only on flagged actions. The classifier is "reasoning-blind" because Claude's
messages and tool outputs are stripped from what it sees, so persuasive text
cannot talk it round, and a separate input-side probe looks for injection in
tool output (see [inspect tool output before it enters context](inspect-tool-output-before-context.md)).
Anthropic separately reports 84% fewer permission prompts once OS sandboxing
was in place.

A plausible arrangement, from the bottom up: an OS or container boundary
([contain at the environment layer first](contain-environment-first.md)), an
un-overridable floor of blocked actions
([hardline command floor](hardline-command-floor.md)), then policy and approval
tiers ([human approval gates](../harness/human-approval-gates.md)), which may
differ between a read-only diagnosis worker and one allowed to act
([diagnose by default, act by exception](../harness/diagnose-by-default-act-by-exception.md)).
