---
type: concept
title: Intention-Implementation Consistency Checking
description: >
  Deploy specialized agents to audit semantic alignment between documented developer intent
  and actual source code behavior during automated code review.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.3"
---

In software maintenance and pull request review, subtle bugs frequently arise not from overt syntax or type failures, but from semantic divergences between what the author intended and what the code actually does.

**Intention–implementation consistency checking** (instantiated in systems like ICAA) deploys specialized agents to detect this misalignment:

- **Context incubation agent**: Gathers developer intent artifacts—commit messages, issue descriptions, API docstrings, and inline comments—alongside the pull request diff and relevant dependency definitions.
- **Consistency checking agent**: Formally compares the stated intentions against the operational semantics of the code changes, identifying discrepancies such as unhandled edge cases, misleading docstrings, missing preconditions, or unexpected side effects.
- **Review report agent**: Formulates concise, actionable feedback distinguishing between implementation bugs (code deviates from intent) and specification bugs (intent itself was incomplete).

By anchoring review in the contrast between intent and implementation, this approach catches logic errors that evade automated unit tests and compiler checks.
