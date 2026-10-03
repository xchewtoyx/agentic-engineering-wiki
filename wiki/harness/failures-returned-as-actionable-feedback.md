---
type: concept
title: Failures Returned as Actionable Feedback
description: >
  Agents recover when tool errors, timeouts and hangs come back as specific,
  actionable feedback; silence, opaque codes, or termination without a chance
  to diagnose prevent recovery.
evidence: moderate
sources:
  - title: "Finding the Right Fit: Model–Harness Interactions"
    resource: "Li, Zhou, Teng et al. (NTU), arXiv 2610.00917, 1 Oct 2026 preprint, §5.1 and §6 — https://arxiv.org/html/2610.00917"
  - title: "Writing effective tools for agents — with agents"
    resource: "Anthropic Engineering, 11 Sep 2025 — https://www.anthropic.com/engineering/writing-tools-for-agents"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026, lint errors carry remediation — https://openai.com/index/harness-engineering/"
  - title: "How we built our multi-agent research system"
    resource: "Anthropic Engineering, 13 Jun 2025, production reliability — https://www.anthropic.com/engineering/multi-agent-research-system"
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
  - title: "Tool and function calling"
    resource: "Meta Model API cookbook, API Fundamentals, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/tool-function-calling"
---

Tools fail: commands hang, services time out, containers die, arguments are
malformed. What happens next depends less on the model than on what the
harness tells it. If a failure arrives as silence, an opaque code or an abrupt
end to the run, the model has nothing to reason about.

This is the failure-path half of the "informative but concise feedback"
principle in [ACI design principles](aci-design-principles.md). SWE-agent's
[guardrailed edit tool](guardrailed-edit-tool.md) is an early instance: a
rejected edit comes back with the error type, the proposed snippet and the
original content, not just "failed". The sources below extend the principle
from edit errors to every kind of runtime failure.

A very fresh preprint on model–harness interactions (arXiv 2610.00917, October
2026) gives a mechanism-level view. Models initiated 180 of 192 recovery
attempts, but recovery succeeded only when the harness returned the failure as
usable feedback. OpenHands' stuck-detector killed runs without letting the
model diagnose, and PI's unbounded shell turned hung commands into silence,
while openJiuwen's 300-second timeout returned an actionable signal. In one
matched case the same model on the same task failed under PI and succeeded
under openJiuwen. The authors recommend runtime support (bounded timeouts,
feedback on argument errors, turn continuation) over retraining. These figures
should be treated as provisional until the paper is reviewed.

The design guidance is primary and older. Anthropic's tool-writing post says
error messages should give specific, actionable fixes rather than opaque codes
or tracebacks. OpenAI writes custom lint messages so that they inject
remediation instructions into the agent's context, which is how
[back-pressure](back-pressure.md) becomes something the agent can act on.
Anthropic's multi-agent research system tells the agent when a tool is failing
so it can adapt, and resumes from the failure point rather than restarting. Its
Managed Agents design surfaces container death to the model as an ordinary tool
error, part of the
[brain–hands–session decoupling](brain-hands-session-decoupling.md). Meta's
tool-calling recipe gives the same advice at the API level: validate arguments
before executing and return error strings rather than raising, so the model can
recover.

In practice that means bounded timeouts on every external command, error text
that names the likely next check, and an explicit "state unknown" result when a
call's outcome cannot be confirmed (see
[unknown state on resurrection](unknown-state-on-resurrection.md)). Which
failures to expect from each tool in the first place is the subject of
[agent tool failure modes](agent-tool-failure-modes.md). A repeated failure that
the agent keeps retrying is a different problem, handled by
[doom-loop detection](doom-loop-detection.md).
