---
type: concept
title: Router Skill
description: >
  When user-invoked skills multiply beyond what a person can remember, a
  single user-invoked router skill that maps the others and when to use each
  cures the cognitive load, but must be kept in sync or it becomes a router
  that lies.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents SKILL-MECHANICS.md and ask-matt skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, CLAUDE.md"
    resource: "https://github.com/mattpocock/skills/blob/main/CLAUDE.md (read 2 Oct 2026)"
---

Making skills [user-invoked](model-invoked-versus-user-invoked-skills.md) removes their [context load](context-load-versus-cognitive-load.md) but piles cognitive load on the human, who becomes the index. Past a handful of skills that index fails. Matt Pocock's cure is a router skill: one user-invoked skill (`ask-matt`) that names the others and says when to reach for each, so the human remembers one name instead of twenty.

A router can only hint. User-invoked skills have no model-facing description, so the router cannot fire them; it tells the human which to type. `ask-matt` is organised as flows rather than a list: a main flow from idea to ship (grill, optional prototype detour, spec, tickets, implement, review, retro), two on-ramps, standalone skills, and context-hygiene advice about where to clear or compact.

The maintenance rule is written into the repository's `CLAUDE.md`: whenever a user-reachable skill is added, renamed, removed or changes how it fits the flows, re-read and update the router. A router that never mentions a new skill, or still routes to a stale one, lies. That makes it a [cache](single-source-of-truth-and-cache.md) of the skill set, and it goes stale like any cache.

Boundary: a router earns its place only once user-invoked skills outnumber what the human can hold; for a few skills it is pure overhead.
