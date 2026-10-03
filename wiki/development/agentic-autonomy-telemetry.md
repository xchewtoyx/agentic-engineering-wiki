---
type: concept
title: Agentic Autonomy Telemetry
description: >
  Three delivery indicators — autonomy rate, human touchpoints, and verification latency — that keep the
  volume of agent-generated code auditable by pairing it with specification-first governance.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 11"
---

The **Agentic Autonomy Rate (AAR)** — agent-generated lines over total merged lines — measures how much of the merged codebase governed agents synthesized versus humans typed; high-autonomy regimes target above 95%. Unlike unstructured "vibe coding," AAR is meaningful only when paired with formal verification gates and human touchpoints; it is never an excuse to bypass specification-first governance.

Two companion indicators keep the ratio honest:

- **Human touchpoints** — manual post-synthesis edits per merge window, driven toward zero by applying corrections upstream: amend the spec and re-synthesize rather than hand-patching the output, which forks the single source of truth (the feedback discipline of [agentic linearism](agentic-linearism.md)).
- **Verification latency** — wall time for multi-agent audit and CI evidence to clear, targeted at minutes rather than days.

Cost per implementation completes the picture: billed tokens plus accountable [Spec Architect](spec-architect-role.md) and gatekeeper time — counting tokens alone under-budgets ownership (compare [successes per million tokens](../evaluation/successes-per-million-tokens.md) for harness-level cost normalization). When faults stem from intent drift rather than isolated bugs, weigh the **re-synthesis return**: regenerating a whole module from an updated spec versus patch-oriented repair (see [patch outcome taxonomy](patch-outcome-taxonomy.md)).

High AAR with low touchpoints and minute-scale verification signals a specification that has earned its autonomy; high AAR without those companions is ungoverned generation, and its bill arrives as [cognitive debt](cognitive-debt-in-agent-synthesized-code.md).
