---
type: concept
title: Lean Skill Instructions
description: >
  Skill files should front-load their essential instructions into the first
  100 lines, phrase them positively, and remove any line that does not change
  the agent's behaviour.
evidence: moderate
sources:
  - title: "Podcast with Matt Pocock (personal listening notes)"
    resource: "notes, 2 Oct 2026"
  - title: "Recent Claude skills-loader change (reported; not yet confirmed in public docs)"
    resource: "Russell, 2 Oct 2026"
  - title: "Claude Code docs, Extend Claude with skills"
    resource: "https://code.claude.com/docs/en/skills (read 2 Oct 2026)"
---

A skill should be short enough that every line earns its place, with the essential instructions in the first 100 lines. A recent Claude change reportedly loads skills with the equivalent of `head -100`, so anything below line 100 may never reach the agent; that report is unconfirmed. The public Claude Code docs do not yet describe that limit. They recommend keeping `SKILL.md` under 500 lines with detail moved to supporting files, and say that after auto-compaction only the first 5,000 tokens of each invoked skill are re-attached. Both point the same way: what matters must come first, and the tail of a file is the least reliable place for anything load-bearing.

This makes order a design decision, not only length. Steps and the [repeated corrections](skill-as-repeated-correction.md) that motivated the skill go at the top; reference consulted only on some branches moves into sibling files behind a pointer (see [information hierarchy](information-hierarchy.md)). Length is still not neutral: it adds [context load](context-load-versus-cognitive-load.md) and buries what matters.

Two editing passes keep it lean:

- Phrase instructions positively. State what to do rather than what to avoid; "use British spelling" steers better than "don't use American spelling", which puts the unwanted pattern in front of the model. See [negation in agent instructions](negation-in-agent-instructions.md).
- Remove no-op lines. A no-op is any instruction the agent would follow anyway: "be thorough", "write clear code". Test each line by asking whether deleting it would change the output, and settle disagreements by running the skill rather than by debate (see [sediment](sediment.md)).

What remains should be mostly the repeated corrections, named with strong [leading words](leading-words-in-agent-instructions.md).

Boundary: a positive rewrite is not always possible. A hard prohibition with real consequences (never push to main) can stay negative. The 100-line figure is harness-specific and may change; front-loading is the durable rule.
