---
type: concept
title: Model-Family Independence Rule
description: >
  Enforce that release verification agents belong to a different model family
  than the synthesis agents that authored the implementation or tests.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 8 (§8.4)"
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 21"
---

When autonomous agents generate both production implementations and their accompanying test suites, using the same underlying model family for both stages creates a dangerous blindspot: shared inductive biases, common training blindspots, and correlated hallucinations. An agent evaluating its own code—or code produced by an identical model architecture—often confirms its own flawed reasoning, as highlighted by [LLM self-assessment grading bias](llm-self-assessment-grading-bias.md).

The **model-family independence rule** requires that verification and release gates maintain architectural orthogonality:

1. **Orthogonal model families**: If code is synthesized using Model Family A (e.g., Anthropic Claude), automated code review, adversarial test synthesis, or semantic verification must be performed by Model Family B (e.g., OpenAI GPT, Google Gemini, or DeepSeek).
2. **Deterministic execution precedence**: Model-based evaluation must never replace deterministic execution oracles. Unit tests, compiler checks, linters, and property-based test suites provide ground truth that overrides model opinions.
3. **Immutable human release sign-off**: While agentic pipelines accelerate generation and intermediate verification, final release and merge authority must remain with human engineers.

Decoupling verification from the authoring model family ensures that correlated failure modes do not silently compromise pipeline integrity.

When the generator approves its own work, verification turns circular: the evidence traces back to the claim it is supposed to support. The rule therefore allows one escape hatch. A same-family verifier is acceptable only if **explicit redundancy is architected into the gate**: independent agents with genuinely different failure modes, deterministic property checks that no model can argue with, or human sign-off that cannot be delegated to a synthesis agent. Pair that sign-off with an immutable audit trail of what the agents did. The same logic applies to human review, where a co-author of a change is not an independent check on it. Automation makes the violation cheap to commit at scale, though, so the rule has to be enforced by the pipeline, not left as advice.

Independence is a spectrum, not a binary. Reviewers from outside the team or organisation are more objective, and more willing to raise problems the team has normalised ("we have always done it that way"). Outside review costs more, so reserve it for complete designs or release candidates and let cheaper internal review cover the increments in between. A model judge from another family is the automated version of the outside reviewer. Measure how far you can trust it by [cross-validating it against an independent metric](llm-judge-cross-validation-against-independent-metric.md).
