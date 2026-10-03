---
type: concept
title: Logs Are Untrusted Input
description: >
  Logs and alert payloads are attacker-influenceable, so an agent that reads
  them must keep them out of its instruction channel, preserve field provenance
  and constrain its outputs, because naive defences let persona hijack and
  context manipulation through.
evidence: weak
sources:
  - title: "Poisoning the Watchtower"
    resource: "Pandey & Bhujang, arXiv 2605.24421, 23 May 2026 (preprint) — https://arxiv.org/html/2605.24421"
  - title: "Emerging threats to your logging system"
    resource: "Nutrient Security Team, 15 Sep 2026 — https://www.nutrient.io/blog/emerging-threats-your-logging-system/"
  - title: "Cursor docs: Automations"
    resource: "Cursor, accessed 3 Oct 2026 — https://cursor.com/docs/cloud-agent/automations"
  - title: "OpenClaw docs: Triage"
    resource: "OpenClaw official docs as of 2026.9.x, retrieved 3 Oct 2026 — https://docs.openclaw.ai/cli/triage"
  - title: "OpenClaw docs: General troubleshooting"
    resource: "OpenClaw official docs, retrieved 3 Oct 2026 — https://docs.openclaw.ai/help/troubleshooting"
---

Operators tend to treat logs as the system talking about itself, and therefore
as trustworthy. That assumption breaks once a large language model (LLM) reads
them. A log line records whatever a request contained, so an unauthenticated
outsider can choose part of what a diagnosing agent reads simply by sending a
crafted URI, user agent or DNS query. Logs are thus a delivery channel for
[indirect prompt injection](indirect-prompt-injection.md), and one that
operations agents read by design.

A 2026 preprint, "Poisoning the Watchtower" (Pandey and Bhujang), tested this
against an LLM analyst reading logs. Blunt "ignore previous instructions"
overrides and obfuscated payloads got nowhere (0% success). Subtler attacks
did: persona hijack reached up to 68% and context manipulation up to 96%
against naive defences. Summarisation tasks were more vulnerable than
classification, and constraining the output format cut average attack success
from 26.6% to 11.8%. The authors recommend separating attacker bytes from the
instruction channel, preserving field provenance, using templated remediation
output, and requiring human review before an escalation is suppressed.

A field case points the same way, though from a single vendor source. The
Nutrient Security Team describes a June 2026 campaign of forged Sentry alerts
that told readers to run a typosquatted npm package, which exfiltrated
environment variables and credentials and specifically detected AI coding
environments including Claude Code and Cursor; the alerts carried injection
metadata such as `allowed_bash_commands: npx`. Their mitigations are trust
boundaries, validating commands against policy rather than event text, keeping
secrets out of agent runtimes, short-lived credentials and egress controls.
Cursor's own Automations docs advise caution when an automation handles
untrusted input. The evidence is rated weak because the study is a preprint and
the campaign details come from one vendor blog.

Any agent that reads logs, health payloads or alerts should therefore treat
them as data in a separate channel, inspect them before use
([inspect tool output before it enters context](inspect-tool-output-before-context.md)),
and emit only constrained, schema-shaped proposals that deterministic code then
validates ([the LLM proposes, code applies](../harness/llm-proposes-code-applies.md)).
The tier that consumes logs should not also hold write power
([diagnose by default, act by exception](../harness/diagnose-by-default-act-by-exception.md),
[untrusted input must not trigger actions](untrusted-input-cannot-trigger-actions.md)).

**Handing diagnostics to a second agent.** The same caution applies when one
agent packages a fault for another to fix. OpenClaw's `openclaw triage` (as of
2026.9.x) is a first-party example of doing it carefully. It collects
diagnostics into an archive that excludes secrets, tokens, raw chat payloads
and raw logs, builds a prompt holding the version, the platform, prioritised
diagnostic findings with fix hints and the archive path, and opens an external
coding agent to diagnose, repair and verify, or, in non-interactive mode, only
prints the handoff command. It adds no permission overrides, so the receiving
agent runs under its own native execution policy. The general lessons are to
hand over sanitised, structured findings and a pinned path rather than raw
logs, and to leave the receiving agent's permissions to its own tier rather
than widening them for the handoff. Using a separate agent at all follows the
case for an
[external supervisor over self-diagnosis](../orchestration/external-supervisor-over-self-diagnosis.md).
