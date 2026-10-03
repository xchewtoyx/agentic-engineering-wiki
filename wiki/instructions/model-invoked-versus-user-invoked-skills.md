---
type: concept
title: Model-Invoked Versus User-Invoked Skills
description: >
  Every skill can be split on one axis, who can invoke it, trading
  always-loaded context load (model-invoked) against human cognitive load
  (user-invoked), with the rule that a user-invoked skill may call
  model-invoked skills but never another user-invoked one.
evidence: moderate
sources:
  - title: "mattpocock/skills, .agents/invocation.md and writing-for-agents SKILL-MECHANICS.md"
    resource: "https://github.com/mattpocock/skills/blob/main/.agents/invocation.md (read 2 Oct 2026, v1.2.3)"
  - title: "AI Hero, skills v1 announcement"
    resource: "https://www.aihero.dev/skills/skills-changelog-v1-announcement (18 Jun 2026)"
---

A model-invoked skill keeps a model-facing `description` full of trigger branches, so the agent can fire it on its own and other skills can reach it. The human can still type its name: model invocation only ever adds the agent's reach. The price is that the description is a [context pointer](context-pointer.md) loaded on every turn.

A user-invoked skill sets `disable-model-invocation: true` (and the Codex equivalent, `policy.allow_implicit_invocation: false`). Its description becomes a one-line summary for a human browsing slash commands, with trigger lists stripped. It costs no context, but the human becomes the index who must remember it exists.

Matt Pocock's test for model invocation, written into his skills repository, is whether the agent could usefully reach for the skill autonomously, or another skill must reach it. Reuse alone is a reason to extract a skill, not a reason to make it model-invoked. In his v1 release, moving orchestration skills to user-invoked was reported as cutting skill-description token cost by 63%.

This produces a deliberate architecture: user-invoked skills orchestrate, model-invoked skills hold reusable discipline (`tdd`, `diagnosing-bugs`, `grilling`, `codebase-design`). A user-invoked skill may call model-invoked ones but never another user-invoked one, because nothing but the human can fire a skill with no description. Shared reference needed by two user-invoked skills therefore has to live in a plain file outside the skill system. The orchestrators can then be [a line or two long](thin-orchestrator-skills.md), and once they multiply past what a person can remember, a [router skill](router-skill.md) restores the index.

This refines [context load versus cognitive load](context-load-versus-cognitive-load.md): the repository does not default everything to explicit invocation. It reserves model invocation for discipline the agent should reach mid-task (for example `wizard`, made model-invoked so the agent fires it the moment it hits a step only a human can perform).

Boundary: harness behaviour varies. A Codex flag once hid `writing-for-agents` from the model entirely and had to be removed (v1.2.2), and one changelog entry notes a desktop and web surface dropping user-invoked skills from its listing.
