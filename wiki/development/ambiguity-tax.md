---
type: concept
title: Ambiguity Tax
description: >
  The super-linear escalation of agent hallucination probability as specification clarity declines,
  identifying a 70% clarity threshold below which reliability collapses.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 5 (§4.7)"
---

In agentic software development, the **ambiguity tax** quantifies the exponential cost of underspecified prompts and incomplete requirements. Hallucination probability does not scale linearly with missing information; it exhibits an exponential decay curve relative to specification clarity $C \in [0, 100\%]$:

$$H(C) \approx \alpha \cdot e^{-\beta C}$$

Empirical parameterization ($H(C) = e^{-0.045 C}$) defines two distinct operational regimes:

- **Spec-Driven Safe Zone ($C \ge 70\%$)**: Specification clarity remains high enough that hallucination probability is suppressed and easily managed by deterministic test gates and linters.
- **High Hallucination Zone ($C < 70\%$)**: Hallucination probability accelerates exponentially toward unity. In this regime, models compensate for missing constraints by inventing plausible-sounding interfaces, resulting in [ambiguity amplification hazard](ambiguity-amplification-hazard.md) across multiple repository files.

For harness and orchestration design, the ambiguity tax proves that upgrading model scale or expanding context windows cannot compensate for poor input specifications. Agent harnesses must implement pre-synthesis validation gates that measure specification completeness and halt execution before entering the high-hallucination regime.
