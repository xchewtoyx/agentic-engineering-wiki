---
type: concept
title: Deterministic Back-Pressure
description: >
  Type checkers, linters, tests and structural lints are the deterministic
  signals that make looping agents converge; once a rule is objective, encode
  it as a check rather than prose.
evidence: moderate
sources:
  - title: "Ralph Wiggum as a 'software engineer'"
    resource: "Geoffrey Huntley, ghuntley.com (date not captured) — https://ghuntley.com/ralph/"
  - title: "Fragments 2026-04-29"
    resource: "Martin Fowler, martinfowler.com, 29 Apr 2026 — https://martinfowler.com/fragments/2026-04-29.html"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026 — https://openai.com/index/harness-engineering/"
  - title: "Dark-factory post-mortem (Pragmatic Engineer podcast write-up)"
    resource: "Dex Horthy, via BigGo Finance news write-up, 15 Jul 2026 (secondary) — https://finance.biggo.com/news/15099f5634f5ab9a"
---

An agent running in a loop will keep producing output whether or not it is
getting closer to the goal. Without some signal that pushes back on wrong
output, a loop drifts, and instructions written as prose are interpreted
loosely or ignored once context fills up.

Practitioners converge on deterministic checks as the main source of that
signal. Geoffrey Huntley's Ralph loop, a shell loop that re-feeds a fixed
prompt to a coding agent, is viable only because type systems, linters and
tests reject bad work on every iteration; he calls it "deterministically bad in
an undeterministic world". OpenAI's harness-engineering team enforces
architecture mechanically: each domain has fixed layers checked by structural
tests, custom linters check documentation freshness and cross-links, and lint
error messages are written to inject remediation instructions into the agent's
context. Their principle is to enforce invariants rather than implementations.
Martin Fowler, quoting others, notes that agents act on every warning a human
would let slide, and argues that once a rule is objective it should move from
prose to a deterministic check. He adds that the verification loop, not
generation speed, is the advantage.

In the vocabulary of [guides and sensors](guides-and-sensors.md), back-pressure
is the computational sensor. It works best when failures are returned in a form
the agent can act on, as described in
[failures returned as actionable feedback](failures-returned-as-actionable-feedback.md),
and it underpins long-running patterns such as
[one unit of work per session](../orchestration/one-unit-of-work-per-session.md)
and [verify before done](verify-before-done.md). Moving an objective rule out of
the instruction file and into a check is the same move as
[fixing the environment rather than the output](../instructions/fix-the-environment-not-the-output.md).

There is a limit. Passing checks does not prove the work is sound where the
checks do not reach, and Dex Horthy's unattended "dark factory" degraded within
months for exactly that reason; see
[unverifiable loops rot](../development/unverifiable-loops-rot.md). OpenAI's
contrasting stance keeps blocking merge gates minimal at high throughput and
re-runs flaky checks rather than blocking.

Back-pressure is not only for coding loops. An agent that takes operational
actions needs its own: a health probe, a diagnostic command's exit code or a
smoke test that must pass after each action. Where an operational rule is
objective (for example, never copy a database file while it is being written),
it belongs in a check or a tool guard rather than in the agent's prompt.
