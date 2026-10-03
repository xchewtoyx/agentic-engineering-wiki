---
type: concept
title: Structural Context Over Raw Dumps
description: >
  Conditioning agents on extracted semantic schemas and structured interfaces consistently
  outperforms dumping raw repository files or flat documents into the context window.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 9 (§8.4.3–8.4.4)"
---

With the expansion of model context windows into hundreds of thousands of tokens, a tempting antipattern is to dump raw codebase files, unstructured documentation, or full HTML trees directly into the prompt.

Empirical evaluations across code synthesis, UI generation, and test generation demonstrate that **structural context engineering strictly dominates raw dumps**:

- **Semantic schema extraction**: Providing tightly scoped, structured representations (e.g., interface contracts, type signatures, API schemas, and AST dependency graphs) enables higher synthesis accuracy and test pass rates than dumping complete file contents.
- **Attention dispersion and noise**: Raw files and large markup dumps introduce irrelevant tokens, syntax noise, and distractor implementations that trigger [lost in the middle](lost-in-the-middle.md) and degrade instruction following.
- **Mutation and coverage sensitivity**: In test generation, structured context framing exposes branch conditions and state invariants explicitly, yielding significantly higher branch coverage and mutation kill rates than raw source ingestion.

Rather than maximizing token volume, effective [context engineering](../context-engineering.md) relies on the harness to parse, filter, and extract compact structural abstractions before prompting the model.
