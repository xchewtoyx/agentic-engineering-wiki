---
type: concept
title: Iterative Refinement Feedback Channels
description: >
  Classify agent refinement feedback across model-based reflection,
  tool-grounded environment diagnostics, and human clarification.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.2"
---

Iterative refinement loops in software engineering agents rely on three complementary feedback channels to detect defects and guide repair:

1. **Model-based peer reflection and self-refinement**:
   - Conversational critique and debate between specialized roles (e.g., AutoGen, CAMEL) or self-reflective introspection on previous trajectory traces ([Reflexion](reflexion.md)).
   - While flexible, purely model-generated critiques risk hallucinated bugs or ungrounded suggestions when divorced from execution feedback.
2. **Tool-grounded environmental feedback**:
   - Compiler diagnostics, linter errors, type checker output, and runtime stack traces (e.g., InterCode).
   - External information retrieval: tool-driven queries to documentation or library signatures (e.g., ToolCoder).
   - Hybrid diagnostic interpretation: combining raw tool outputs with an LLM explainer to translate cryptic compiler error codes into actionable repair instructions.
3. **Human-in-the-loop clarification**:
   - Interactive dialogue targeting underspecified or ambiguous requirements before and during code synthesis (e.g., ClarifyGPT, MINT benchmarks).
   - Prevents catastrophic divergence when the agent lacks domain intent that cannot be inferred from repository context alone.

Effective harness design chains these channels hierarchically: fast tool feedback (linters, compilers) catches syntactic and type errors first, model reflection evaluates architectural logic, and human clarification intervenes when specification ambiguity cannot be resolved programmatically.
