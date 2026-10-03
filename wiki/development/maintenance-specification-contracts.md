---
type: concept
title: Maintenance Specification Contracts
description: >
  Treat compatibility rules, dependency matrices, and verification commands
  as first-class specification artifacts to bound agent diff generation during repository migrations.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 5"
---

When autonomous agents execute repository-wide migrations—such as language retargeting, framework upgrades, or API deprecation cleanups—they generate thousands of mechanical edits across hundreds of files. Without explicit constraints, this volume overwhelms human review and introduces subtle regressions.

**Maintenance specification contracts** establish formal boundaries between stochastic model generation and human oversight by treating migration criteria as first-class artifacts:

- **Explicit compatibility rules**: Concrete mapping tables defining deprecated syntax, replacement APIs, and boundary semantics.
- **Dependency matrices**: Formal declarations of package versions, build graphs, and rollout sequencing.
- **Executable verification commands**: Deterministic test suites and static linters that define the machine-checkable acceptance threshold.

This structure enables an effective division of labor: the agent generates the bulk (~70–75%) of mechanical code diffs under [guided code transformations](guided-code-transformations.md), while human engineers act as directors (scoping, sequencing, and prompting) and reviewers (evaluating edge cases against business invariants) — the migration-scale instance of a [specification-governed operating model](specification-governed-operating-model.md).
