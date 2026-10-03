---
type: concept
title: Spec Fidelity
description: >
  The primary quality metric for agentic inputs, evaluating specification completeness,
  consistency, unambiguity, and verifiability.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 8 (§7.2–7.3)"
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 10"
---

In autonomous code generation, the output quality of synthesis agents is bounded by the quality of the input specification. When the consumer is an agent rather than a human engineer, the informal conversational disambiguation that used to patch weak requirements disappears — the spec must stand without unstated human context. **Spec fidelity** measures the degree to which a requirement specification unambiguously captures intended system behavior, evaluated across four essential dimensions:

1. **Completeness**: All interface contracts, data models, edge cases, error-handling paths, and failure modes are explicitly documented rather than left to agent inference.
2. **Consistency**: Requirements contain zero internal contradictions, incompatible type definitions, or mutually exclusive state transitions across sections.
3. **Unambiguity**: Each requirement admits exactly one stable interpretation, eliminating vague language that triggers the [ambiguity tax](ambiguity-tax.md) and [ambiguity amplification hazard](ambiguity-amplification-hazard.md), and closing the gaps an agent could exploit through literal-genie specification gaming.
4. **Verifiability**: Every requirement maps directly to objective, automated tests, behavioural oracles, or deterministic acceptance criteria.

Measuring spec fidelity before dispatching synthesis agents ensures that the system operates in the safe zone where hallucinations are suppressed, enabling reliable [zero-shot repository synthesis](zero-shot-repository-synthesis.md); the [spec fidelity gate](spec-fidelity-gate.md) operationalizes that check at the boundary between formalization and synthesis.

Fidelity, not velocity, is the steering metric. Scrum calibrates team capacity through cadence speed; agentic delivery instead asks how accurately the agent ingests and realizes the specification, tracked in aggregate by a synthesis-efficiency ratio and by [autonomy telemetry](agentic-autonomy-telemetry.md) rather than story points.
