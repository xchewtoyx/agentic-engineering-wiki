---
type: concept
title: Thin Orchestrator Skills
description: >
  User-invoked entry-point skills can be a line or two long, delegating to a
  model-invoked primitive by explicitly instructing the agent to call the Skill
  tool, so behaviour lives in one place and is composed rather than copied.
evidence: moderate
sources:
  - title: "mattpocock/skills, grill-me, grill-with-docs, grilling and implement skills"
    resource: "https://github.com/mattpocock/skills/tree/main/skills (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, .agents/invocation.md"
    resource: "https://github.com/mattpocock/skills/blob/main/.agents/invocation.md (read 2 Oct 2026)"
---

Matt Pocock's most popular skill, `grill-me`, has a body of one sentence: call the Skill tool with "grilling". `grill-with-docs` is the same, calling the Skill tool twice, for "grilling" and "domain-modeling". The user-invoked skill is a named entry point; the behaviour lives in a model-invoked primitive that several entry points share (`grilling`, described in [grilling the design tree](../development/grilling-the-design-tree.md), sits behind `grill-me`, `grill-with-docs`, `triage`, `wayfinder` and `improve-codebase-architecture`).

The wiring convention is specific. Dependencies are written as an operative instruction to call the Skill tool with a bare skill name, not as a `/skill` mention left for the model to interpret and not as a cross-folder file link. Naming the tool is reported to fire more reliably, and dropping the slash keeps the instruction harness-neutral. One skill per call: a step needing two skills says "call the Skill tool twice", because "call it with X and Y" reads as one call. A user-invoked precondition (such as running setup) is phrased as an instruction to tell the human, since no skill can fire it.

The payoff is a [single source of truth](single-source-of-truth-and-cache.md) for each discipline and very small skills: across the promoted set, entry points run 7 to 16 lines while the primitives carry the weight.

Boundary: this only works when the target is model-invoked, as described in [model-invoked versus user-invoked skills](model-invoked-versus-user-invoked-skills.md).
