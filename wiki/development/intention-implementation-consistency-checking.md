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

In software maintenance and pull request review, subtle bugs frequently arise not from overt syntax or type failures, but from semantic divergences between what the author intended and what the code actually does. Code can be internally consistent and still be wrong: it faithfully implements something nobody intended.

**Intention–implementation consistency checking** (instantiated in systems like ICAA) deploys specialized agents to detect this misalignment:

- **Context incubation agent**: Gathers developer intent artifacts—commit messages, issue descriptions, API docstrings, and inline comments—alongside the pull request diff and relevant dependency definitions.
- **Consistency checking agent**: Formally compares the stated intentions against the operational semantics of the code changes, identifying discrepancies such as unhandled edge cases, misleading docstrings, missing preconditions, or unexpected side effects.
- **Review report agent**: Formulates concise, actionable feedback distinguishing between implementation bugs (code deviates from intent) and specification bugs (intent itself was incomplete).

By anchoring review in the contrast between intent and implementation, this approach catches logic errors that evade automated unit tests and compiler checks.

Read its findings with two caveats:

- **It is a correspondence check, not a correctness proof.** It compares two artifacts (words about the code and the code itself) and proves neither one correct. Either side can be at fault: the code may betray correct intent, or the intent record may misdescribe correct code. A finding should name which side is likely wrong so the fix lands on the right artifact: patch the code, or amend the docstring, commit message, or spec.
- **Misleading comments are defects in their own right.** The next reader, human or agent, will trust them, so a comment that contradicts working code is a bug to fix, not noise to ignore.
