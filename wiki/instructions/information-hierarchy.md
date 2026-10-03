---
type: concept
title: Information Hierarchy
description: >
  An agent document is built from steps and reference arranged on a ladder
  (in-file step, in-file reference, disclosed reference), and deciding where
  each piece sits, including disclosure and co-location, is the core
  structural decision.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
---

Matt Pocock's `writing-for-agents` skill splits the content of any agent document into two types. Steps are the ordered actions the agent performs; reference is the definitions, rules and facts it consults on demand. A recipe is all steps, a review checklist is all reference, and most skills mix the two. Each piece then sits on a ladder ranked by how immediately the agent needs it: in-file steps at the top, in-file reference below them, and disclosed reference (a separate file reached through a [context pointer](context-pointer.md)) at the bottom.

The tension is two-sided. Push too little down and the top of the file bloats, so the steps get buried and following them becomes a coin flip. Push too much down and the agent never sees material it actually needs. [Progressive disclosure](progressive-disclosure.md) is the move down the ladder, and Pocock frames it as protecting the hierarchy rather than as a token optimisation. The cleanest test is branching: inline what every branch needs, disclose what only some branches reach.

Co-location is the companion rule within a file. Once a concept has a rung, keep its definition, rules and caveats under one heading, so reading one part brings its neighbours. Scattering a single meaning across a file is distinct from [duplicating it](single-source-of-truth-and-cache.md), and both hurt.

The failure mode is sprawl: a document too long even when every line is live. The cure is the ladder itself, not deletion, and not [splitting into more skills](splitting-skills.md).

His repository shows the practice as short `SKILL.md` files with sibling reference files (`tdd` points at `tests.md` and `mocking.md`; `codebase-design` at `DEEPENING.md` and `DESIGN-IT-TWICE.md`).

Boundary: a flat set of peer rules on one rung (every rule of a review) is a legitimate arrangement, not a smell.
