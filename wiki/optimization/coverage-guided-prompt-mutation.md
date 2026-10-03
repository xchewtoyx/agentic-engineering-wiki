---
type: concept
title: Coverage-Guided Prompt Mutation
description: >
  Direct test-generation prompts toward unexercised execution paths by dynamically
  injecting coverage feedback into subsequent iteration rounds.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.4"
---

Standard LLM test generation produces repetitive test cases for common execution paths while missing edge cases and error-handling branches.

**Coverage-guided prompt mutation** (exemplified by systems like CoverUp) turns test suite creation into a closed execution-feedback loop:

1. **Test execution and measurement**: Generated test cases are executed within an instrumented environment that measures statement, branch, or condition coverage.
2. **Coverage report inspection**: The agent harness parses execution reports to identify specific unexercised branches, missing conditions, or uncovered lines.
3. **Dynamic prompt steering**: Instead of asking the model to "write more tests," the harness mutates the next generation prompt to explicitly target the uncovered branch conditions and their enclosing logic.
4. **Iterative expansion**: The agent generates targeted unit tests for those gaps, re-runs coverage analysis, and continues until branch coverage saturates or budget limits are reached.

This approach combines tool-grounded execution feedback with [prompt assembly algorithms](../context/prompt-assembly-algorithms.md), keeping the agent's [context engineering](../context-engineering.md) focused strictly on missing coverage targets rather than regenerating redundant test scaffolding.
