---
type: concept
title: Completion Criterion
description: >
  Every step in an agent document should end on a completion criterion whose
  clarity resists premature completion and whose demand drives the depth of
  legwork; the strongest are both checkable and exhaustive.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, diagnosing-bugs skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md (read 2 Oct 2026)"
---

A completion criterion is the condition that tells the agent a step is done. Matt Pocock's `writing-for-agents` skill treats it as a lever with two independent properties.

Clarity is whether the agent can tell done from not-done. A vague bound such as "understanding reached" invites [premature completion](premature-completion.md), because the agent's attention slides towards being finished. Demand is how much the criterion requires. "Every modified model accounted for" forces thorough digging where "produce a change list" does not. Pocock calls that digging legwork: it is latent in the wording rather than written as its own step, and demand works on reference as well as on steps ("every rule applied" binds a flat checklist just as "every step done" binds a sequence).

The strongest criteria are both checkable and exhaustive. His `diagnosing-bugs` skill is the worked example: Phase 1 is only done when the agent can name one command it has already run at least once, shown with its output, that goes red on this specific bug. That turns a fuzzy gate into an observable state, which is also a [leading word](leading-words-in-agent-instructions.md) move ("red"). The same idea at harness level is to [verify before declaring done](../harness/verify-before-done.md).

This is the structural answer to [asset rush](asset-rush.md): making the check part of the definition of done means pausing to verify counts as progress.

Boundary: an irreducibly fuzzy criterion cannot be sharpened into a check; then the remaining defence is hiding later steps across a real context boundary.
