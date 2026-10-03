---
type: concept
title: Externalised Progress Artefacts
description: >
  Long-running agents keep continuity across context windows through artefacts
  outside the transcript (a pass/fail feature list, a progress file, an init
  script, git commits and checked-in plans), not through transcript memory.
evidence: strong
sources:
  - title: "Effective harnesses for long-running agents"
    resource: "Anthropic Engineering (Justin Young), 26 Nov 2025 — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - title: "Using PLANS.md for multi-hour problem solving"
    resource: "OpenAI Cookbook, 7 Oct 2025 — https://raw.githubusercontent.com/openai/openai-cookbook/main/articles/codex_exec_plans.md"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "OpenAI (Ryan Lopopolo), Feb 2026, repository knowledge as system of record — https://openai.com/index/harness-engineering/"
  - title: "Ralph Wiggum as a 'software engineer'"
    resource: "Geoffrey Huntley, undated — https://ghuntley.com/ralph/"
  - title: "Multi-turn context management"
    resource: "Meta Model API cookbook, Agent Patterns, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/multi-turn-context-management"
---

A long task outlives any single context window. Anthropic describes two
failures it hit when an agent worked across many sessions: the agent tried to
finish everything in one go and ran out of context half way, or a later session
saw partial progress and declared the job done (see
[agent failure modes that grow with one long context](../context/long-context-agent-failure-modes.md)).
Compaction alone fixed neither, because a summarised transcript is a poor record
of what is actually finished.

The remedy that recurs across providers is to put the state of the work into the
environment. In Anthropic's pattern an initializer agent writes an `init.sh`, a
`claude-progress.txt` log and a first git commit, plus a JSON (JavaScript Object
Notation) feature list of more than 200 items that all start as failing. Later
agents may only flip each item's `passes` field; JSON was chosen because the
model is less likely to rewrite it wrongly than Markdown. OpenAI's cookbook takes
the same idea further with "ExecPlans": self-contained living design documents,
written for a reader with no prior context, carrying milestones and decision
logs, which it credits with letting Codex work for more than seven hours from one
prompt. OpenAI's harness post keeps these plans checked into the repository, and
Huntley's Ralph loop has the agent record learnings in `AGENT.md` and bugs in
`fix_plan.md`. Meta's multi-turn recipe keeps a running `STATE.md` holding the
objective, decisions, a task graph with status and a file map, and has the agent
consult it before each task.

This is continuity by artefact rather than by runtime journal, a different
mechanism from [journal-then-replay durable execution](../orchestration/journal-then-replay-durable-execution.md),
and different from long-term [agent memory tiers](agent-memory-tiers.md): the
artefacts record the state of one piece of work, not facts to recall later. It
is the "write" move in [write, select, compress, isolate](../context/context-write-select-compress-isolate.md),
and the state a [context reset](../context/compaction-vs-context-reset.md)
depends on.

The evidence is a strong convergence of lab and practitioner reports rather than
a controlled study, so the effect size is unknown.

In practice, an agent's durable record of a task (what was observed, what was
tried, what is still open) should live in files or a store it re-reads, not in
its own context. Each new session can then reorient through a
[start-of-session smoke test](../orchestration/start-of-session-smoke-test.md),
take [one unit of work per session](../orchestration/one-unit-of-work-per-session.md),
and leave the raw event history in a
[session log outside the context window](session-log-outside-context-window.md).
