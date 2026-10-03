---
type: concept
title: One Unit of Work per Session
description: >
  Limiting each session or loop iteration of a long-running agent to one
  feature or item prevents one-shot attempts and premature "done" claims.
evidence: moderate
sources:
  - title: "Effective harnesses for long-running agents"
    resource: "Anthropic Engineering (Justin Young), 26 Nov 2025 — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - title: "Ralph Wiggum as a 'software engineer'"
    resource: "Geoffrey Huntley, undated — https://ghuntley.com/ralph/"
---

Given a large goal and an open-ended session, agents tend to attempt everything
at once, exhaust their context half way through, and leave partial work that a
later session mistakes for completion. Anthropic names both of these,
one-shotting and [premature
completion](../instructions/premature-completion.md), as the failure modes its
long-running harness was built to stop.

Its fix is to scope each session to a single feature. The coding agent picks
one unfinished item, implements it, commits with a descriptive message, updates
the progress file and leaves the code in a clean state fit to merge. Geoffrey
Huntley's Ralph loop reaches the same rule from the other direction. It is a
plain shell loop that pipes the same prompt file into a coding agent over and
over, loading the same specs and plan each time and taking one item per
iteration. What makes such a crude loop converge is
[back-pressure](../harness/back-pressure.md): type checkers, linters and tests
give a correctness signal on every pass. Huntley also allows many sub-agents
for search but only one for build and test, the rule of [single-threaded
writes](single-threaded-writes.md), and tunes the loop by adding constraining
prompt lines where a failure is predictable.

The evidence is two practitioner-level accounts, one from a lab and one from an
individual, with no comparative numbers.

The rule fits the failures that grow with time in one context, such as stopping
early and losing constraints to compaction; see [long-context agent failure
modes](../context/long-context-agent-failure-modes.md). Each session pairs it
with a [start-of-session smoke test](start-of-session-smoke-test.md) on entry,
[verification before done](../harness/verify-before-done.md) on exit, and
[externalised progress
artefacts](../knowledge/externalised-progress-artifacts.md) to carry the outcome
to the next session. Outside coding, the unit is whatever the agent can finish
and verify in one context: one incident, one ticket, one document section.
