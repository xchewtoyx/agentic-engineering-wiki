---
type: concept
title: Specification Mutation and Selection
description: >
  Harden agent-generated specifications by applying mutation operators across boundary cases
  and filtering candidates with verifiable selection heuristics.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.1"
---

When LLMs generate formal program specifications or interface contracts from natural language or existing code, initial zero-shot or conversational completions frequently omit edge-case constraints, unstated boundary conditions, and error invariants.

The **specification mutation and selection** method (instantiated in frameworks like SpecGen) transforms specification authoring into a rigorous two-phase synthesis loop:

1. **Candidate specification generation**: An agent engages in structured prompting or dialogue conditioned on the target codebase or system architecture to propose candidate formal specifications.
2. **Mutation exploration**: The harness applies systematic mutation operators to the candidate specification (e.g., perturbing boundary values, inverting precondition/postcondition predicates, dropping assumptions, or mutating state transition rules) to generate boundary variants.
3. **Verifiable heuristic selection**: The mutated candidates are submitted to objective verification checkers (e.g., SMT solvers, symbolic execution engines, or type checkers) alongside target test suites. A selection strategy retains only candidates that are logically consistent and formally verifiable against the underlying code.

By systematically mutating candidate specifications and filtering them through verification heuristics, this process eliminates hidden ambiguity and elevates [spec fidelity](spec-fidelity.md) before downstream [zero-shot repository synthesis](zero-shot-repository-synthesis.md) or test generation occurs.
