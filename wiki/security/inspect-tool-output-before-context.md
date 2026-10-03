---
type: concept
title: Inspect Tool Output Before It Enters Context
description: >
  Tool output is an attack surface even from trusted tools, and remote MCP
  servers can change after approval, so inspect returns and context files with
  a small classifier or pattern scanner before they reach the model.
evidence: moderate
sources:
  - title: "How we contain Claude across products"
    resource: "Anthropic Engineering, 25 May 2026 — https://www.anthropic.com/engineering/how-we-contain-claude"
  - title: "How we built Claude Code auto mode"
    resource: "Anthropic Engineering, 25 Mar 2026 — https://www.anthropic.com/engineering/claude-code-auto-mode"
  - title: "Hermes Agent docs: Security"
    resource: "Nous Research, official docs as of Hermes Agent v0.21.5 (v2026.9.24), retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/security"
---

Most thinking about agent permissions concerns what goes out: which commands
the agent may run. The reverse direction matters as much. Everything a tool
returns becomes part of the model's context, and a tool can faithfully return
attacker-written text, for example a web page or a log line, which is the
delivery channel of [indirect prompt injection](indirect-prompt-injection.md).
Approving a tool once does not settle the matter either.

Anthropic's containment post makes three points about this. Tool output is an
attack surface even when the tool itself is trusted. Remote
[Model Context Protocol](../harness/model-context-protocol.md) (MCP) servers can
change after they have been approved, so Anthropic tests them against fake data
first. And its proxies inspect tool returns before they enter context, using a
classifier that can be a small model. The auto-mode post adds an input-side
prompt-injection probe on tool outputs, separate from the classifier that
judges the agent's actions (see
[layered agent permission stack](layered-agent-permission-stack.md)).

Hermes Agent applies the same idea to context files. As of the official Hermes
v0.21.5 security docs (October 2026), it scans AGENTS.md, `.cursorrules` and
SOUL.md for injection patterns such as ignore-instructions phrasing, hidden
comments, secret reads, curl-based exfiltration and invisible Unicode, and
blocks project files that match. A user's own `HERMES_HOME/SOUL.md` only
produces a warning. That pattern list is a reasonable starting set for any
agent that loads instruction files from repositories it does not control.

Inspection is a filter, not a boundary: it is an instance of the
[input guardrails](input-output-guardrails.md) applied to tool returns, and it
leaks like them. Adaptive attacks get past model-layer defences most of the
time (see [injection defences are bypassable](prompt-injection-defences-are-bypassable.md)),
so a scanner reduces exposure without making untrusted text safe to act on
(see [untrusted input must not trigger actions](untrusted-input-cannot-trigger-actions.md)).
For agents that read operational data, this is the input-side half of treating
[logs as untrusted input](logs-are-untrusted-input.md).
