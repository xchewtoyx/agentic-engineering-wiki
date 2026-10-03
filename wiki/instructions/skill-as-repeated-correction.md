---
type: concept
title: Skill as Repeated Correction
description: >
  An agent skill is worth writing when you notice yourself giving the same
  correction to an agent repeatedly, so the skill captures that correction
  once instead of re-typing it every session.
evidence: weak
sources:
  - title: "Podcast with Matt Pocock (personal listening notes)"
    resource: "notes, 2 Oct 2026"
---

A skill is a correction you got tired of making. The trigger for writing one is not a bright idea about what an agent might need, but evidence: the same nudge, fix or reminder showing up across sessions. This framing comes from a podcast interview with Matt Pocock and rests on his experience rather than a study, so the evidence is weak; it is the skill-level form of the broader rule to [fix the environment, not the output](fix-the-environment-not-the-output.md).

This makes skill creation demand-driven. Each skill starts from an observed failure, which gives it a clear purpose and a natural test: does the correction still need making after the skill exists? It also keeps the skill small, because it only has to encode what the agent kept getting wrong, not everything you know about the domain. Many such corrections push against the same underlying pull, [asset rush](asset-rush.md).

Once written, the skill competes for the agent's attention, so it should be [phrased with leading words](leading-words-in-agent-instructions.md), kept [lean and free of no-op lines](lean-skill-instructions.md), and loaded only when relevant, because [context load costs more than cognitive load](context-load-versus-cognitive-load.md).

Boundary: a one-off correction is a prompt, not a skill. Wait for the repeat.
