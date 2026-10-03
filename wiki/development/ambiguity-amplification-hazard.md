---
type: concept
title: Ambiguity Amplification Hazard
description: >
  Specification ambiguity causes non-linear increases in hallucination and error propagation
  that large context windows amplify rather than mitigate.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 6"
---

A common misconception in agentic system design is that expanding context windows compensates for incomplete or ambiguous requirements by providing more room for agent exploration.

In practice, agents exhibit **ambiguity amplification**:

- **Non-linear hallucination penalty**: When requirements contain unstated assumptions, ambiguous data contracts, or conflicting business rules, the model must guess the missing intent. Rather than halting to question underspecification, models extrapolate plausible-sounding choices.
- **Multi-file blast radius expansion**: In large repository contexts, an initial ambiguous requirement does not remain localized. It propagates conflicting implementations across multiple modules—generating mismatched schemas, broken imports, and inconsistent test assertions.
- **Failure of post-hoc correction**: Catching ambiguity-induced discrepancies via conversational review is token-expensive and prone to [compound mistake amplification](../orchestration/compound-mistake-amplification.md).

Harness engineering must enforce specification verification gates before invoking synthesis agents: require unambiguous interface definitions, typed schemas, and acceptance criteria up front to eliminate intent ambiguity before execution begins.
