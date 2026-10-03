---
type: concept
title: Staged Command Approval
description: >
  Split a compound shell command into stages and resolve each against policy,
  so only complete, known-safe stages clear automatically, one rejected stage
  denies the whole command, interpreters never get prefix grants, and a deny
  always beats an allow.
evidence: moderate
sources:
  - title: "Staged approvals"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/staged-approvals"
  - title: "Hermes Agent docs: Security"
    resource: "Nous Research official docs as of v0.21.5, fail-closed parsing — https://hermes-agent.nousresearch.com/docs/user-guide/security"
---

Approval systems that judge a command by its first word are easy to fool. A
pipeline that starts with a harmless `grep` can end with a deletion, and a
standing grant for `python` approves whatever script follows it. Approving
whole command strings, on the other hand, prompts the human for every
read-only probe and trains them to click through. This note is about how a
[human approval gate](../harness/human-approval-gates.md) should read a shell
command when the agent has one.

Meta's Muse Code cookbook describes a middle path. The harness parses a
compound command into ordered stages, each with its own argument vector and a
flag for whether it could be fully parsed. Each stage resolves against policy
as known-safe, such as `ls`, `cat` or `grep`, which clears automatically;
dangerous, such as `rm -rf` even when wrapped in `sudo`; or unresolved, which
is held for review. The first unresolved stage blocks, one rejected stage
denies the whole command, and the command runs as a single unit only once every
stage has cleared. Stages containing variables, command substitution or writing
redirects can never count as known-safe. Trust comes in three scopes: allow
once, a workspace rule stored in a policy file, or reject. Prefix rules are
refused for interpreter wrappers such as `bash`, `python`, `env` and `sudo`,
because whatever follows them is arbitrary code. Precedence is fixed: deny
beats prompt, and prompt beats allow.

The evidence is one vendor recipe, but its fail-closed parsing matches Hermes's
rule that unparseable commands are refused. It sits in the policy layer of the
[layered agent permission stack](layered-agent-permission-stack.md), above an
un-overridable [hardline command floor](hardline-command-floor.md), and the
decisions it records still need to survive restarts as
[durable approval state](../harness/durable-approval-state.md).

How much it matters depends on tool design. An agent that exposes only a
[narrow action verb set](../harness/narrow-action-verb-set.md) has little to
stage, since each verb is approved by name. One that keeps a general shell, as
the [minimal, general tool surface](../harness/minimal-general-tool-surface.md)
camp recommends, or keeps a shell only for read-only investigation, can use
staged approval to let probes run unattended while any write, restart or
interpreter call in the same pipeline waits for a human.
