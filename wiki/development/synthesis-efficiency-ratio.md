---
type: concept
title: Synthesis Efficiency Ratio
description: >
  A steering metric for agentic delivery that measures how compactly a specification converts into
  working agent-generated code without regeneration loops, retries, or hallucinated scaffolding.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 10"
---

Scrum optimizes velocity (cadence speed). Agentic delivery optimizes fidelity: does the agent faithfully realize the intent it was given? The **Synthesis Efficiency Ratio (SER)** is the primary KPI for the [Spec Architect](spec-architect-role.md). It measures how compactly an intent document, such as a functional requirements document, converts into working code without wasteful agent loop-back or hallucinated scaffolding.

Read it as a diagnostic on the spec, not on the model:

- **High SER**: the specification is deterministic and high-fidelity, so synthesis is near one-shot under [agentic linearism](agentic-linearism.md).
- **Low SER**: the team is paying the [ambiguity tax](ambiguity-tax.md). Vague requirements push agents into trial-and-error, excess token spend, and guesses about latent architectural commitments. Fix it upstream at the [spec fidelity gate](spec-fidelity-gate.md), not by adding retries.

SER ties directly to synthesis economics (token cost and the repair multiplier on rework) and pairs with two observables an agent harness can log per run:

- **Ambiguity tax as a quantity**: the gap between the token spend expected under a crisp, testable spec and the actual spend when prose-heavy fragments force clarification prompts, retry loops, and repair cycles.
- **First-pass alignment rate**: the share of requirements whose first synthesis passes automated checks and human acceptance criteria without material rework. It is the per-requirement view of what SER measures in aggregate.

Together with [agentic autonomy telemetry](agentic-autonomy-telemetry.md), these replace story points as steering metrics; [successes per million tokens](../evaluation/successes-per-million-tokens.md) is the analogous cost-normalized measure at the harness level. Metrics from different eras do not convert into each other: KLOC, story points, and SER each track their era's bottleneck (coding throughput, iteration mechanics, specification fidelity). Carrying old volume proxies into agentic delivery measures output while leaving the specification, now the real constraint, uninspected.
