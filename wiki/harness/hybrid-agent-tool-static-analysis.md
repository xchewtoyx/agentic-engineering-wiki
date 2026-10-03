---
type: concept
title: Hybrid Agent-Tool Static Analysis
description: >
  Bridge conventional static analysis tools with LLM agents to disambiguate
  warnings and verify candidate defects across complex code paths.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.3"
---

Traditional static analysis tools (linters, AST parsers, symbolic analyzers) scale efficiently across millions of lines of code, but produce high volumes of ambiguous warnings and unresolved states on complex control flows (e.g., uninitialized variables, taint propagation). Conversely, LLMs possess deep semantic reasoning but cannot ingest entire multi-million-line codebases without context degradation and prohibitive token costs.

**Hybrid agent-tool static analysis** (exemplified by systems like LLIFT) combines the strengths of both approaches:

1. **Deterministic tool triage**: Fast static analysis tools scan the codebase globally, flagging candidate defects and pruning millions of benign lines down to a targeted subset of ambiguous or warning locations.
2. **Agentic context expansion**: For each flagged site, an agent uses [dependency-graph-guided planning](../development/dependency-graph-guided-planning.md) and repository navigation tools to trace variable definitions, function calls, and data propagation paths across related files.
3. **Semantic confirmation or refutation**: The agent reasons over the gathered slice to determine whether the warning represents an exploitable defect or a false positive, explaining its conclusion with concrete execution scenarios.

This hybrid architecture prevents [lost in the middle](../context/lost-in-the-middle.md) by grounding the agent in deterministic tool alerts rather than open-ended code reading, achieving high-precision defect triage at enterprise repository scale.
