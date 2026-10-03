---
type: concept
title: Credentials Stay Outside the Sandbox
description: >
  Keep tokens in a vault or proxy, or bind them to resources at initialisation,
  so the agent and its sandbox never see them; where an agent must hold
  credentials, give it test-only, budget-capped ones.
evidence: moderate
sources:
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
  - title: "Build an SRE agent for incident response"
    resource: "OpenAI Cookbook, 10 Sep 2026 — https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/agents_api/apps/sev_bot/README.md"
  - title: "Designing agentic loops"
    resource: "Simon Willison, 30 Sep 2025 — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/"
  - title: "OpenClaw docs: Docker"
    resource: "OpenClaw docs, Docker networking & storage, 2026.9.x (gateway token in .env, OAuth tokens in SQLite) — https://docs.openclaw.ai/install/docker/networking-and-storage"
---

Whatever an agent can read, an injected instruction can try to exfiltrate, and
whatever an agent's sandbox holds survives as long as the sandbox does. A
credential inside the agent's reach is therefore the most direct route from a
[prompt injection](indirect-prompt-injection.md) to real damage. The sources
converge on keeping credentials where the agent cannot see them.

Anthropic's Managed Agents design makes this structural. Credentials are never
reachable from the sandbox: git tokens are wired into the remote when the
sandbox is initialised, and Model Context Protocol (MCP) OAuth tokens sit in a
vault behind a proxy, so even the harness never holds them. OpenAI's 2026 site
reliability engineering (SRE) incident-response cookbook applies the same
split to an operations agent. Each incident gets a self-hosted Docker sandbox
running `codex exec-server` with only a restricted executor key, while the
Slack, GitHub and AWS credentials stay outside. Where an agent genuinely has to
hold credentials, Willison recommends test-environment credentials with budget
caps, such as a Fly.io organisation capped at $5, so that the worst case is
bounded.

This is the cleanest way to drop the "sensitive access" leg of
[the agents Rule of Two](agents-rule-of-two.md), and it depends on the
separation described in
[decouple brain, hands and session](../harness/brain-hands-session-decoupling.md):
if the loop and the sandbox are separate, the sandbox can be given resources
rather than secrets.

The hazard is sharpest for agents that operate other agent platforms, because
those platforms often keep powerful secrets on disk. OpenClaw's Docker docs (as
of 2026.9.x), for instance, keep the gateway token in `.env` and OAuth tokens
in plaintext in SQLite under the config directory. An operating agent that
mounts such directories, or reads them through a container shell, holds the
keys to the platform. A safer shape is for the agent to call narrow,
pre-authorised operations ([narrow action verbs](../harness/narrow-action-verb-set.md))
through a broker that holds the secrets, with a diagnose tier that has none at
all ([diagnose by default, act by exception](../harness/diagnose-by-default-act-by-exception.md)).
