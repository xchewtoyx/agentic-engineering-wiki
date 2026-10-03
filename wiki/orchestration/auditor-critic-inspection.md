---
type: concept
title: Auditor-Critic Inspection
description: >
  Separate vulnerability and defect detection into an auditor that generates candidate
  flaws and a critic that rigorously scores and filters false positives.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 3.3"
---

When a single LLM inspects source code for security vulnerabilities and code smells, it faces an acute tension: prompt configurations tuned to maximize recall produce high false-positive rates, overwhelming developers with spurious warnings, while conservative prompts miss subtle bugs.

The **auditor–critic** pattern (instantiated in systems like GPTLENS) resolves this by decomposing inspection across two specialized roles in a [multi-agent architecture](multi-agent-architecture.md):

1. **Auditor agent**: Focuses on high recall. It scans source code, generates diverse vulnerability hypotheses, and provides detailed causal reasoning paths explaining how the flaw could be triggered.
2. **Critic agent**: Focuses on precision. It independently evaluates the auditor's findings against formal vulnerability criteria, threat models, and code constraints, assigning confidence scores and discarding ungrounded claims.

Decoupling hypothesis generation from rigorous verification keeps the auditor uninhibited in exploring complex edge cases while ensuring that only high-confidence, actionable defects pass through to human developers or automated blocking gates. It extends [critique-optimizer-separation](../optimization/critique-optimizer-separation.md) from code generation to static quality assurance.
