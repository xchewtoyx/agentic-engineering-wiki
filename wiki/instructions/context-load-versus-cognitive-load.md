---
type: concept
title: Context Load Versus Cognitive Load
description: >
  Material placed permanently in an agent's context costs attention on every
  task for as long as it stays there, so it is usually better to accept the
  one-off cognitive load of invoking a skill deliberately than to auto-invoke it.
evidence: weak
sources:
  - title: "Podcast with Matt Pocock (personal listening notes)"
    resource: "notes, 2 Oct 2026"
---

Cognitive load is the effort a person spends remembering to call a skill. Context load is the space and attention a skill consumes inside the agent's context window. They trade against each other, and they are not equal: cognitive load is paid once per use, context load is paid forever, on every task, whether the skill is relevant or not.

Auto-invoked skills feel convenient because they remove the cognitive load. But each one that loads automatically dilutes the instructions that matter for the current task and makes the agent's behaviour harder to predict. Matt Pocock's recommended default, from a podcast interview (so the evidence is one practitioner's experience, hence weak), is to turn off auto-invoke and call skills explicitly. His own skills repository later refines this into a split by who can invoke each skill, described in [model-invoked versus user-invoked skills](model-invoked-versus-user-invoked-skills.md).

This is also why skills should be [kept short](lean-skill-instructions.md): every line is a recurring cost, and longer contexts degrade attention, as [context rot](../context/context-rot.md) describes.

Boundary: a correction needed on nearly every task may justify standing context. The test is frequency of relevance, not frequency of forgetting.
