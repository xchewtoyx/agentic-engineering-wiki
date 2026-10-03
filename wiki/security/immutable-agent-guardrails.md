---
type: concept
title: Immutable Agent Guardrails
description: >
  An agent's standing rules and harness state should sit where it cannot
  rewrite them, with each attempted edit needing a fresh human approval and the
  OS sandbox mounting those directories read-only, so either layer alone blocks
  the change.
evidence: moderate
sources:
  - title: "Immutable guardrails"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/immutable-guardrails"
  - title: "Contained execution"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026), protected .git — https://dev.meta.ai/docs/cookbook/contained-execution"
  - title: "Docker"
    resource: "Hermes Agent documentation (Nous Research), read-only /opt/hermes — https://hermes-agent.nousresearch.com/docs/user-guide/docker"
---

An agent with write access to its workspace usually also has write access to
the files that govern it: its AGENTS.md, its approval policy, its hooks and its
own state. Nothing then stops it, or text injected into it, from loosening a
rule it finds inconvenient. A rule the agent can edit is advice, not a control.

Meta's Muse Code cookbook describes a harness built so that this cannot happen
silently. Standing rules live in `.agents/AGENTS.md` and harness state under
`.muse/`, both loaded when a session opens. Two independent layers protect
them. Any write to a protected path, which includes `.git`, `.muse`, `.agents`
and hook directories, stops for human review, and the review offers only
allow-this-write or reject, so no standing permission can ever be recorded.
Separately, the operating-system (OS) sandbox mounts those directories
read-only, so a shell command that bypasses the editor still fails. The
recipe's summary is that the agent "can't rewrite its own rules". Hermes
reaches a similar result by a different route: its install tree is root-owned
and read-only in Docker, confining self-improvement to data, skills and config.

This is the production counterpart of the research controls in
[guarded self-modification](../optimization/self-modifying-harness-controllability.md),
where the verifier and evaluation logic are read-only to the optimiser. It
differs from a [hardline command floor](hardline-command-floor.md) in what it
protects: the floor blocks dangerous actions on the systems, whereas this
blocks changes to the controls themselves. It also differs from a
[guardrailed edit tool](../harness/guardrailed-edit-tool.md), which checks that
an edit is well formed rather than whether the file may be edited at all. It
does not resolve the tension with
[self-authored skill drift](../instructions/self-authored-skill-drift.md), where
writing skills is a deliberate feature; there the analogous move is to keep the
rules about skill writing, not the skills, immutable.

For an agent that operates other systems, the same applies to its runbooks,
verb allow-list, approval policy and floor definitions: mount them read-only,
with changes arriving only through a reviewed path outside the agent's reach,
so that neither a mistaken action nor an injected instruction can widen the
agent's own authority.
