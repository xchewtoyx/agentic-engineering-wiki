---
type: concept
title: Model-Family Independence Rule
description: >
  Enforce that release verification agents belong to a different model family
  than the synthesis agents that authored the implementation or tests.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 8 (§8.4)"
---

When autonomous agents generate both production implementations and their accompanying test suites, using the same underlying model family for both stages creates a dangerous blindspot: shared inductive biases, common training blindspots, and correlated hallucinations. An agent evaluating its own code—or code produced by an identical model architecture—often confirms its own flawed reasoning, as highlighted by [LLM self-assessment grading bias](llm-self-assessment-grading-bias.md).

The **model-family independence rule** requires that verification and release gates maintain architectural orthogonality:

1. **Orthogonal model families**: If code is synthesized using Model Family A (e.g., Anthropic Claude), automated code review, adversarial test synthesis, or semantic verification must be performed by Model Family B (e.g., OpenAI GPT, Google Gemini, or DeepSeek).
2. **Deterministic execution precedence**: Model-based evaluation must never replace deterministic execution oracles. Unit tests, compiler checks, linters, and property-based test suites provide ground truth that overrides model opinions.
3. **Immutable human release sign-off**: While agentic pipelines accelerate generation and intermediate verification, final release and merge authority must remain with human engineers.

Decoupling verification from the authoring model family ensures that correlated failure modes do not silently compromise pipeline integrity.
