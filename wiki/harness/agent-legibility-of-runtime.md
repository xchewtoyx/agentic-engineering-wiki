---
type: concept
title: Make the Runtime Legible to the Agent
description: >
  Exposing the running system's UI, logs, metrics and traces to the agent,
  for example through an ephemeral per-worktree observability stack, turns
  reliability goals into tasks the agent can verify.
evidence: moderate
sources:
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026, 'Increasing application legibility' — https://openai.com/index/harness-engineering/"
  - title: "OpenAI harness engineering (summary)"
    resource: "2ooks knowledge base — https://2ooks.github.io/knowledge-base/summaries/openai-harness-engineering.html"
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026 — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
---

An agent asked to make a service faster or more reliable is working blind if it
can only read code. It cannot reproduce the bug, see the latency, or check that
its fix changed anything, so it either guesses or declares success on the
strength of the code compiling.

OpenAI's harness-engineering team made the running application legible to the
agent. Each git worktree can boot its own copy of the app, the Chrome DevTools
Protocol is wired into the runtime, and each worktree gets an ephemeral
observability stack (logs, metrics and spans) that the agent queries with LogQL
and PromQL and that is torn down after the task. They report that this made
goals such as keeping startup under 800 milliseconds tractable for the agent,
with single runs lasting six hours or more. The agent can reproduce a bug,
apply a fix and confirm the fix in the same telemetry. Birgitta Böckeler treats
observability as a sensor in the [guides and sensors](guides-and-sensors.md)
sense, and expects tooling for tracing agent sessions and measuring sensor
effectiveness to follow.

The point is that verification needs evidence from the running system, not
from the agent's own account. That is what makes
[verify before done](verify-before-done.md) more than a prompt instruction.

The same applies to an agent that operates or repairs a live system rather than
writing code for it. It should query the system through the signals a human
operator uses (health endpoints, status commands, structured logs, telemetry),
ideally in machine-readable form so that before-and-after comparisons are
mechanical. Captured alongside each action, that telemetry is also the record
described in [full-trace remediation audit](full-trace-remediation-audit.md).
Whether to stand up an ephemeral, per-incident observability stack for such an
agent, as OpenAI does per worktree, is an open design choice rather than an
established practice.
