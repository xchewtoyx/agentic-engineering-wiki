---
type: concept
title: Negation in Agent Instructions
description: >
  Steering by prohibition activates the forbidden behaviour and makes it more
  available, so instructions should state the positive target, keeping a
  prohibition only as a hard guardrail and even then pairing it with the
  positive.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, CLAUDE.md"
    resource: "https://github.com/mattpocock/skills/blob/main/CLAUDE.md (read 2 Oct 2026)"
---

Stating positives instead of negatives is a standing rule of [explicit instruction design](../prompting/explicit-instruction-design.md). Matt Pocock's `writing-for-agents` skill explains why it works with the "don't think of an elephant" mechanism. Naming the forbidden behaviour puts a strongly activated concept into context, and the negation is a weak modifier that the concept overruns, so a ban half-reads as an instruction to do the thing. The fix is to state the target behaviour ("write one-line comments") so the unwanted one is never spoken. This matters more in standing instructions than in a single prompt, because a [skill or steering file](lean-skill-instructions.md) repeats the activated concept on every task it loads into.

A prohibition keeps its place only as a hard guardrail that cannot be phrased positively, and even then it should be paired with the positive target so attention lands on what to do.

His own repository shows the pairing in practice. The `CLAUDE.md` bans em-dashes in all prose, but the same sentence tells the agent what to use instead (a comma, colon, period, parentheses or a conjunction, chosen by what the sentence needs) and forbids blind character substitution.

Boundary: this is a claim about steering a model's generation. It does not argue against prohibitions enforced mechanically by tooling, such as hooks that block destructive git commands; turning a mechanical rule into such a check is usually better than writing it down at all, as in [steering files as navigation pointers](steering-files-as-navigation-pointers.md).
