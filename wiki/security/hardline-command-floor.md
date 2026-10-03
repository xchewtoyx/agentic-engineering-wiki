---
type: concept
title: Hardline Command Floor
description: >
  Beneath configurable approvals, keep an un-overridable floor of blocked
  actions that protects non-negotiable targets such as volumes, state databases
  and secrets, and fail closed on anything that cannot be parsed.
evidence: moderate
sources:
  - title: "Hermes Agent docs: Security"
    resource: "Nous Research official docs as of v0.21.5 (v2026.9.24), retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/security"
  - title: "Azure SRE Agent: Execute mitigations"
    resource: "Microsoft, accessed 3 Oct 2026 — https://sre.azure.com/docs/capabilities/execute-mitigations"
  - title: "OpenClaw docs: Triage"
    resource: "OpenClaw official docs as of 2026.9.x, retrieved 3 Oct 2026 — https://docs.openclaw.ai/cli/triage"
---

Configurable approval modes exist so that operators can loosen them: an agent
that asks about everything is unusable, so harnesses offer YOLO, autonomous or
auto-approve settings. That flexibility creates a risk of its own, because a
misconfiguration, a hurried approval or a persuasive injected instruction can
then unlock an action nobody would ever want taken. A floor that no mode can
lower addresses this. Where [human approval gates](../harness/human-approval-gates.md)
decide which actions need a human, the floor lists the actions that no mode,
grant or approval can unlock.

Hermes Agent has one. As of its official v0.21.5 security docs (October 2026),
a hardline blocklist covers `rm -rf /`, fork bombs, `mkfs` on root, `dd` to
disks and piping URLs to `sh`. No override exists, YOLO mode included, and
commands that cannot be parsed fail closed. A separate non-overridable guard
stops the agent restarting its own gateway, an instance of preferring an
[external supervisor over self-repair](../orchestration/external-supervisor-over-self-diagnosis.md).
Azure SRE (site reliability engineering) Agent applies the same idea to an
operations agent: whatever its run mode, `delete` and `remove` operations and
all `az keyvault` commands are always blocked, and management locks are
respected. OpenClaw's bounded repair turn expresses a floor in its prompt
instead, forbidding credential edits, deletion of state or databases, and
service start or stop. A prompt-level rule is weaker than an enforced
blocklist, since it depends on the model complying (see
[prompt-level attack defenses](prompt-level-attack-defenses.md) for why such
rules never guarantee obedience).

A useful design rule, reasoned by analogy with reliability practice that names
baselines to protect regardless of pressure, is to define the floor by the
targets it protects rather than by a list of dangerous-sounding commands. For an
agent that operates infrastructure, candidates are volumes holding state, live
database files, `.env` files and credential directories. A
[publish-state protection guard](publish-state-protection-guard.md) is a
narrower, task-scoped relative: it protects output the agent has just verified.

The floor sits near the bottom of the
[layered agent permission stack](layered-agent-permission-stack.md). Exposing
only a [narrow action verb set](../harness/narrow-action-verb-set.md) makes it
easier to enforce, since unparseable or unknown actions can simply be refused.
Above the floor, [staged command approval](staged-command-approval.md) decides
which remaining commands need a human, and
[immutable agent guardrails](immutable-agent-guardrails.md) keep the floor's
own definition out of the agent's reach.
