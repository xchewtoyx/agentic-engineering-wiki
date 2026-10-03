---
type: concept
title: Spec Fidelity
description: >
  The primary quality metric for agentic inputs, evaluating specification completeness,
  consistency, unambiguity, and verifiability.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 8 (§7.2–7.3)"
---

In autonomous code generation, the output quality of synthesis agents is bounded by the quality of the input specification. **Spec fidelity** measures the degree to which a requirement specification unambiguously captures intended system behavior, evaluated across four essential dimensions:

1. **Completeness**: All interface contracts, data models, edge cases, error-handling paths, and failure modes are explicitly documented rather than left to agent inference.
2. **Consistency**: Requirements contain zero internal contradictions, incompatible type definitions, or mutually exclusive state transitions across sections.
3. **Unambiguity**: Each requirement admits exactly one stable interpretation, eliminating vague language that triggers the [ambiguity tax](ambiguity-tax.md) and [ambiguity amplification hazard](ambiguity-amplification-hazard.md).
4. **Verifiability**: Every requirement maps directly to objective, automated tests, behavioural oracles, or deterministic acceptance criteria.

Measuring spec fidelity before dispatching synthesis agents ensures that the system operates in the safe zone where hallucinations are suppressed, enabling reliable [zero-shot repository synthesis](zero-shot-repository-synthesis.md).
