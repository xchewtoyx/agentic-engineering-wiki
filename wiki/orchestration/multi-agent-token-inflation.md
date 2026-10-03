---
type: concept
title: Multi-Agent Token Inflation
description: >
  Mitigate rapid token and latency growth in multi-agent workflows by enforcing
  loop early-stopping, deterministic verification gates, and structured message passing.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 5-6"
---

While [multi-agent architecture](multi-agent-architecture.md) modularizes complex workflows, it introduces **token inflation**: exponential growth in token consumption and wall-clock latency caused by multi-turn inter-agent dialogues, duplicated system prompts across specialist instances, and unconstrained trial-and-error iteration loops.

To keep multi-agent systems sustainable within production [context engineering](../context-engineering.md) limits, harnesses must apply loop minimization controls:

1. **Deterministic verification backstops**: Replace open-ended conversational debate with programmatic checks (e.g., linters, type checkers, test suites). If a patch fails compilation, return structured compiler diagnostics directly rather than invoking a multi-agent critique council.
2. **Hard iteration and budget caps**: Enforce strict per-stage turn limits and early-stopping criteria. If an agent fails to make progress after $N$ attempts, halt or escalate to human review rather than allowing conversational thrashing.
3. **Structured message passing**: Ban verbose conversational chatter between agents. Transmit minimal structured artifacts (e.g., typed diffs, diagnostic summaries, JSON schemas) rather than passing entire conversational histories across agent boundaries.
4. **Context caching and distillation**: Leverage prompt caching for shared static system prompts and distill repeated multi-agent reasoning trajectories into specialized smaller models.

These controls prevent multi-agent collaboration from devolving into unbounded conversational overhead, preserving the advantages of [role-based agent delegation](role-based-agent-delegation.md) without runaway inference costs.
