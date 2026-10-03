---
type: concept
title: Durable Approval State
description: >
  Human approvals must be durable state: the workflow suspends on a signal
  without using compute, and the decision is persisted, so a restart neither
  loses the approval nor asks the human twice.
evidence: moderate
sources:
  - title: "pi-durable specification (spec.md)"
    resource: "Earendil, earendil-works/pi repository, §5.2 memos — https://github.com/earendil-works/pi/blob/main/packages/durable/docs/spec.md"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026, approval hook example — https://earendil.com/posts/pi-durable/"
  - title: "pi-durable README"
    resource: "Earendil, earendil-works/pi repository, §Hooks — https://github.com/earendil-works/pi/blob/main/packages/durable/README.md"
  - title: "Durable execution for crashproof AI agents"
    resource: "DBOS blog (Qian Li), 24 Feb 2025 — https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents"
  - title: "Durable execution: the key to harnessing AI agents"
    resource: "Inngest blog (Charly Poly), 19 Feb 2026 — https://www.inngest.com/blog/durable-execution-key-to-harnessing-ai-agents"
  - title: "Durable execution meets AI: why Temporal is the perfect foundation for AI"
    resource: "Temporal blog (Cornelia Davis), 10 Jul 2025 — https://temporal.io/blog/durable-execution-meets-ai-why-temporal-is-the-perfect-foundation-for-ai"
  - title: "Build an SRE agent for incident response"
    resource: "OpenAI Cookbook, 10 Sep 2026 — https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/agents_api/apps/sev_bot/README.md"
  - title: "Staged approvals"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/staged-approvals"
---

[Human approval gates](human-approval-gates.md) say which actions need a
human's go-ahead; this note is about what happens to that go-ahead while the
agent waits. An action that needs approval can wait minutes or hours. If the
waiting process holds the decision only in memory, a crash or deploy during the
wait either loses an approval already given, so the action never happens, or
forgets that the human was asked, so they are asked again. Neither is
acceptable for an agent acting on production systems.

Every durable-execution engine models the wait as durable state. Temporal
carries human input through Signals and Updates. DBOS uses `recv()` and
`send()`, so a workflow can wait indefinitely for a manager's approval.
Inngest's `waitForEvent` suspends a workflow without using compute. Pi Durable
splits the job in two. A `beforeTool` hook can block a call, for example by
returning a "Needs approval" result, or rewrite its arguments. The decision is
then stored in a memo, a small first-writer-wins value whose candidate insert
and winner read happen in one commit, so concurrent candidates see the same
durable winner and a restart reuses the decision instead of asking again.
OpenAI's SRE incident-response cookbook applies the same idea in an operations
setting: a `propose_rollback` tool has no automatic handler and pauses for
approval through a webhook and Slack buttons, deduplicating repeated
deliveries; the example records the approval but never deploys.

The evidence is a consistent set of vendor and framework documents rather than
independent evaluation. Meta's Muse Code records each approval decision in its
append-only session log before the effect runs, and persists standing
workspace grants in a policy file; how it decides *what* is approved, stage by
stage, is described in
[staged command approval](../security/staged-command-approval.md).

The practical rule is to persist any approval gate alongside the intent of the
action it guards, key it so that duplicate approvals collapse to one, and
re-read it on resume. That keeps the human boundary set by
[envelope-bounded autonomy](envelope-bounded-autonomy.md) intact across
crashes, and it composes with [the effect sandwich](../orchestration/effect-sandwich.md)
and [journal-then-replay](../orchestration/journal-then-replay-durable-execution.md).
Where workers sit in different permission tiers, the approval record is also
what lets a diagnose-only worker hand an action to one allowed to act (see
[diagnose by default, act by exception](diagnose-by-default-act-by-exception.md)).
