---
type: concept
title: Navigator-Driver Pair Programming
description: >
  Structure collaborative coding agents into a navigator that explores plans
  and steers iteration and a driver that synthesizes code and tests locally.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.2"
---

The **navigator–driver** pattern (instantiated in systems like PairCoder) adapts human pair programming to [multi-agent architecture](../orchestration/multi-agent-architecture.md) by decoupling planning and steering from code synthesis and local testing:

- **Navigator agent**: Explores multiple candidate implementation plans, evaluates them against repository constraints and specifications, selects the globally optimal plan, and steers subsequent iteration rounds based on execution feedback.
- **Driver agent**: Receives the selected plan, synthesizes code patches, executes local tests, and performs immediate syntactic or functional corrections before handing control back.

This role separation prevents [compound mistake amplification](../orchestration/compound-mistake-amplification.md) by keeping the strategic planning context clean of transient syntax errors, command outputs, and intermediate test churn. It refines [plan-validate-execute](../orchestration/plan-validate-execute.md) into an ongoing conversational steering loop, allowing the navigator to maintain long-range architectural intent while the driver engages directly with the [agent-computer interface](../harness/agent-computer-interface.md) and [test-time code refinement](../optimization/test-time-code-refinement.md).
