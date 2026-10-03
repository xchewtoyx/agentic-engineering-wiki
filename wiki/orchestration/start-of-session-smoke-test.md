---
type: concept
title: Start-of-Session Smoke Test
description: >
  Every session of a long-running agent should orient itself and run an init
  script plus a basic end-to-end check before starting new work, so a broken
  inherited state is caught before anything is built on it.
evidence: moderate
sources:
  - title: "Effective harnesses for long-running agents"
    resource: "Anthropic Engineering (Justin Young), 26 Nov 2025, 'Getting up to speed' — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

An agent that resumes long-running work inherits whatever the previous session
left behind, and among the failures Anthropic observed was a session leaving
the environment broken. If the next session starts building straight away, it
stacks new work on a fault it never noticed and later struggles to tell old
damage from new.

Anthropic's answer is a fixed start-of-session ritual. The agent runs `pwd`,
reads the git log and the progress file, picks the highest-priority unfinished
feature, starts the development server through `init.sh`, and runs a basic
end-to-end check before doing anything new. The point of the check is to catch
a broken state early, while it is still cheap to attribute. The same post
reports that agents often marked features done without verifying them end to
end, and that explicitly prompting them to test through browser automation, as
a user would, markedly improved results. That makes the smoke test the
entry-side counterpart of [verify before done](../harness/verify-before-done.md),
and the two together bracket [one unit of work per
session](one-unit-of-work-per-session.md).

The evidence is one lab engineering post describing its own harness, so it is a
well-motivated practice rather than a measured one.

The ritual generalises beyond coding. An agent that operates live systems
should begin every run, and every resumption after a crash, with a read-only
baseline of the systems it is responsible for before it diagnoses or acts. This
matters most after an interruption, where the agent cannot assume the world
matches its records; see [unknown state on
resurrection](../harness/unknown-state-on-resurrection.md). The orientation half
of the ritual depends on [externalised progress
artefacts](../knowledge/externalised-progress-artifacts.md) being there to read.
