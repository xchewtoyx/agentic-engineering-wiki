---
type: concept
title: Closed-Loop Critique Failure Modes
description: >
  Autonomous multi-agent critique loops risk infinite oscillation, mutual error
  reinforcement, and rapid token exhaustion without deterministic termination criteria.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 13 (§13.4)"
---

While [multi-agent architecture](multi-agent-architecture.md) and peer review patterns (such as [auditor-critic inspection](auditor-critic-inspection.md)) improve initial detection of edge-case bugs, closed-loop agent critique introduces three acute failure modes when left unconstrained:

1. **Infinite oscillation loops**: Agent A critiques a solution; Agent B performs a superficial or cosmetic modification; Agent A finds a different stylistic issue or repeats its initial critique. The agents oscillate indefinitely without converging on an acceptable solution.
2. **Mutual error reinforcement**: When multiple agents share similar training distributions or flawed context prompts, they may reach uncalibrated consensus on an incorrect premise or hallucinated specification requirement, reinforcing rather than catching the bug.
3. **Runaway token inflation**: Each round of critique and rebuttal passes growing conversation transcripts back and forth, driving up inference latency and exhausting [context engineering](../context-engineering.md) limits without advancing code quality.

To prevent these failure modes, harnesses must enforce deterministic termination guards:
- Bound conversational critique to a small fixed iteration limit ($N \le 3$).
- Anchor critique progress in programmatic execution feedback (compilers, test runners, linters) rather than purely subjective text exchanges ([iterative refinement feedback channels](iterative-refinement-feedback-channels.md)).
- Escalate to human reviewers when agents reach oscillation or deadlock.
