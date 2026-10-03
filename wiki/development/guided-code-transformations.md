---
type: concept
title: Guided Code Transformations
description: >
  Protect repository refactoring against silent semantic drift by capturing
  invariants in formal specifications and gating changes with regression suites.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 4"
---

When autonomous agents perform refactoring or code migrations across large codebases, they modify internal code structure (coupling, cohesion, code smells) while ostensibly preserving observable behavior. However, unattended agentic refactoring carries an elevated risk of **silent semantic drift**: subtle regressions in edge cases, type coercions, or side effects across interdependent modules.

The **guided transformation** framework mitigates this risk by surrounding agentic edits with formal constraints:

1. **Formal invariant specifications**: Before initiating code changes, behavioral invariants and boundary contracts are explicitly documented in testable specifications.
2. **Deterministic regression gating**: Edits must be validated against pre-existing regression test suites, compiler checks, and static analysis linters before acceptance.
3. **Prompt scaffolding**: Applying chain-of-thought (CoT) and few-shot exemplars increases test survival and structural smell reduction compared to raw zero-shot prompts.
4. **Human adjudication at boundary conditions**: Changes involving deep architectural encapsulation or unstated domain rationales are routed to human engineers, while the agent handles mechanical transformations.

By combining executable contracts with automated verification gates, guided transformations prevent [compound mistake amplification](../orchestration/compound-mistake-amplification.md) during multi-file repository maintenance.
