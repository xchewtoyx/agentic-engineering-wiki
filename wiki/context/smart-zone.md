---
type: concept
title: Smart Zone
description: >
  The smart zone is the portion of a context window (Pocock cites roughly 150k
  tokens on current frontier models) within which a model still reasons
  sharply, so workflows should clear or compact at phase boundaries rather than
  push on degraded.
evidence: moderate
sources:
  - title: "mattpocock/skills, ask-matt skill (context hygiene)"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "The Pragmatic Engineer, AI Skills with Matt Pocock"
    resource: "https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (Sep 2026)"
---

Matt Pocock treats context capacity as a budget with a quality cliff. Inside the
smart zone the model reasons well; beyond it, in what he calls the dumb zone,
quality degrades. His router skill puts the boundary at about 150k tokens on
state-of-the-art models. That figure is one practitioner's working estimate, not
a measurement; the measured basis for a cliff of this kind is
[context rot](context-rot.md), which finds degradation with length well before
the window is full.

The working rules follow from where context is valuable. Keep the alignment
phases (grilling, spec, tickets) in one unbroken window so each builds on the
same thinking. Then start each implementation ticket fresh, because a
self-contained ticket makes the previous context disposable. If a session nears
the zone's edge mid-phase, compact at the nearest phase boundary rather than
continuing; the trade-off between the two ways of shedding context is in
[compaction vs context reset](compaction-vs-context-reset.md). The interview
also mentions a "day shift" and "night shift" way of working tied to splitting
context, but the published summary does not define it, so treat any reading of
it as unverified.

This is the runtime twin of
[context load versus cognitive load](../instructions/context-load-versus-cognitive-load.md):
standing context spends the smart zone on every task, and splitting work to
avoid [premature completion](../instructions/premature-completion.md) only works
across the same boundaries that reset it.

The 150k figure is model-dependent and will move. The durable idea is a budget
with a cliff, managed at phase boundaries.
