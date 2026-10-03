---
type: concept
title: Grilling the Design Tree
description: >
  A grilling skill interviews the user in rounds over a design tree, asking
  the whole frontier of currently answerable decisions with a recommended
  answer each, finding facts itself, and finishing only when the frontier is
  empty.
evidence: moderate
sources:
  - title: "mattpocock/skills, grilling skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "The Pragmatic Engineer, AI Skills with Matt Pocock"
    resource: "https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (Sep 2026)"
---

Grilling is Matt Pocock's fix for misalignment, the gap between what you meant and what the agent built. The idea of an agent interviewing its user came from Anthropic's Thariq Shihipar; Pocock wrapped it as a skill, and it is his most popular. It is a lightweight way to raise [spec fidelity](spec-fidelity.md) before any code is written: the agent pulls the missing decisions out of the human instead of guessing them.

The current `grilling` skill is short and leans on three [leading words](../instructions/leading-words-in-agent-instructions.md). The design tree maps each decision to the decisions that hang off it. The frontier is every decision whose prerequisites are settled, so it can be asked now without guessing. The agent works in rounds: it asks the whole frontier at once, numbered, each with its recommended answer, then waits and recomputes.

Responsibility is split cleanly. Facts are the agent's job: anything it can look up, it dispatches a subagent to find rather than asking. Decisions are the user's. The [completion criterion](../instructions/completion-criterion.md) is an empty frontier, with nothing silently assumed, and the agent does not act until the user confirms shared understanding.

It is a direct counterweight to [asset rush](../instructions/asset-rush.md): the skill's output is agreement, not an artefact. Several user-facing entry points reach it as [thin orchestrator skills](../instructions/thin-orchestrator-skills.md).

Boundary: grilling interrogates the subject. When the answers sit with someone else, Pocock's `to-questionnaire` inverts it and grills you only about the send (who it is for and what you need back).
