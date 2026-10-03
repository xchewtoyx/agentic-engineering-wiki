---
type: concept
title: Compaction vs Context Reset
description: >
  Compaction (an in-place summary) preserves continuity but carries
  pathologies forward, while a reset (a fresh agent plus a structured handoff)
  gives a clean slate at the cost of handoff fidelity, and which is right
  depends on the model.
evidence: moderate
sources:
  - title: "Harness design for long-running application development"
    resource: "Prithvi Rajasekaran, Anthropic Engineering, 24 Mar 2026 — https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - title: "Effective context engineering for AI agents"
    resource: "Anthropic Engineering, 29 Sep 2025 — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - title: "Pi Durable"
    resource: "Earendil Engineering, 1 Oct 2026, reset(handoff) — https://earendil.com/posts/pi-durable/"
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
---

Every long-running agent eventually fills its window and has to shed something.
There are two broad ways to do it, and they fail differently.

**Compaction** summarises older turns in place and carries on in the same
conversation. Anthropic's context-engineering guidance lists it as the first of
three long-horizon techniques, alongside structured note-taking and multi-agent
designs; Claude Code compacts history and keeps the five most recently accessed
files. It is the agent-runtime form of
[memory summarization](../knowledge/memory-summarization.md). Compaction
preserves continuity, but whatever was wrong in the session (a mistaken belief,
a drifting goal, an anxious habit) is summarised along with everything else and
carried forward.

A **context reset** starts a fresh agent and gives it a structured handoff.
Rajasekaran's long-running-apps post draws this distinction explicitly. Resets
give a clean slate, but only what the handoff captures survives, so fidelity
depends on how good the handoff is; the same holds for harnesses that rebuild
every turn from a [fresh-context state summary](fresh-context-state-summary.md).
Pi Durable offers both: background summarisation from a token threshold, a
single compact-and-retry if the provider rejects a request as too long, and
`reset(handoff)` to start a fresh context from a handoff note.

**Which wins is contested, and model-dependent.** Rajasekaran reports that
resets cured the "context anxiety" Sonnet 4.5 showed as its window filled. Opus
4.5 largely lost that behaviour, so the harness dropped resets in favour of the
software development kit's (SDK's) auto-compaction, and Anthropic's Managed
Agents post later called the resets dead weight. The same choice could swing
back with a different model, which is why this decision is a standing example of
[harness assumptions going stale](../harness-assumptions-go-stale.md).

Neither option is safe without care. Compaction has its own failure modes,
addressed in [safeguarded compaction](safeguarded-compaction.md), and goal drift
under lossy compaction is one of the
[failure modes that grow with one long context](long-context-agent-failure-modes.md).
Resets depend on state held outside the window, such as the progress files in
[externalised progress artefacts](../knowledge/externalised-progress-artifacts.md).
Practitioners who reset at phase boundaries to stay in the
[smart zone](smart-zone.md) are making the same choice by workflow rather than
by harness setting.

Treat the choice as configuration to be re-tested, not a fixed design. A long
task might reset between phases (diagnose, act, verify) with a written handoff.
When an agent behaves badly after a long session, knowing which strategy it
used helps decide whether a compaction carried a bad belief forward or a fresh
session lost a constraint.
