---
type: concept
title: Dependency-Graph-Guided Planning
description: >
  Maintain a repository dependency graph to formulate coordinated multi-file
  edit plans across complex software projects.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.2"
---

When autonomous coding agents modify large repositories, planning edits strictly through conversational context or sequential tool calls leads to hallucinations of missing imports, broken cross-module call sites, and partial refactorings.

**Dependency-graph-guided planning** (exemplified by systems like CodePlan) maintains a global dependency graph—tracking abstract syntax trees, call graphs, type references, and file imports across the entire codebase—to formulate coordinated multi-file edit plans:

1. **Impact analysis**: Pinpoints which downstream files, modules, and test suites are affected by a proposed change before any file edit is executed.
2. **Topological edit scheduling**: Orders code generation and file modifications so that upstream interfaces and data contracts are updated before dependent downstream implementations.
3. **Targeted context pruning**: Extracts only the directly impacted definitions and call sites into the agent's context budget, preserving [context engineering](../context-engineering.md) limits under [lost in the middle](../context/lost-in-the-middle.md).

By grounding the agent's [plan-validate-execute](../orchestration/plan-validate-execute.md) loop in static dependency structures, this strategy enables multi-file changes without requiring full-repository context dumps or suffering from broken multi-hop dependencies.
