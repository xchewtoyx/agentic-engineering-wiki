---
type: concept
title: Context Pointer
description: >
  A context pointer is an always-loaded line (a skill description, an
  AGENTS.md entry) that names out-of-context material and encodes when to
  reach it, and its wording rather than its target decides how reliably the
  agent reaches it.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
---

A context pointer is a reference that sits in the agent's context and points at material that does not. A skill's `description` is one; a line in a [steering file](steering-files-as-navigation-pointers.md) that names a doc is the same object. Matt Pocock's central claim, from his `writing-for-agents` skill, is that the pointer's wording, not the quality of what it points at, decides whether the agent goes and reads it. A must-have document behind a weakly worded pointer is a variance bug: some runs reach it and some do not.

A pointer has two jobs. It says what the material is, and it lists the branches that should trigger reading it, where a branch is a distinct case the material handles. Because the pointer is loaded on every turn, it deserves harder pruning than the body it points at. Three rules follow. Put the [leading word](leading-words-in-agent-instructions.md) first, since that is where the triggering happens. Give one trigger per branch, because synonyms for the same case are one branch written twice. Cut any identity the body already carries.

When a pointer fails to fire, the order of repair matters: sharpen the wording first, and only inline the material into always-loaded context if sharpening fails. Inlining trades a reliability problem for a [context load](context-load-versus-cognitive-load.md) problem.

Pointers are what make [progressive disclosure](progressive-disclosure.md) work: the harness preloads only the pointers, and everything else depends on them firing.

Boundary: a pointer only exists for material that is [disclosed](information-hierarchy.md). Material every branch needs belongs inline, not behind a pointer.
