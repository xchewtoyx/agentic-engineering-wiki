---
type: concept
title: Agentic Linearism
description: >
  Execute agentic code synthesis as an uninterrupted linear pass against a complete,
  frozen specification rather than human-style iterative micro-sprinting.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 6"
---

Human software development thrives on incrementalism—short sprints, mid-flight course corrections, and gradual requirement discovery. However, applying this incremental posture to autonomous code generation degrades agent reliability.

**Agentic linearism** describes the empirical finding that autonomous software engineering agents achieve peak correctness, coherence, and efficiency when given an uninterrupted, single synthesis pass conditioned on a complete, unambiguous specification:

- **Context fragmentation penalty**: Mid-synthesis interventions, changing requirements, or fragmented prompts shatter the agent's working memory, causing conflicting architectural assumptions across files.
- **Technical rehabilitation of the requirements freeze**: In traditional Waterfall, upfront specification freezes failed because multi-month human implementation cycles outpaced changing business reality. Because agentic synthesis executes in hours, obsolescence risk vanishes, making a strict requirements freeze during the synthesis pass an essential technical optimization (the latest swing of the [rigidity–flexibility pendulum](rigidity-flexibility-pendulum.md)).
- **Decoupled phases**: All ambiguity resolution, requirements negotiation, and architectural debate are frontloaded into the specification authoring phase; once synthesis begins under [zero-shot repository synthesis](zero-shot-repository-synthesis.md), execution proceeds deterministically without human steering until verification gates run.
- **Feedback isolated to post-verification loops**: Humans and automated gates inspect the finished increment against [spec fidelity](spec-fidelity.md) criteria rather than steering mid-pass. A failed increment is corrected by amending the upstream specification or test harness and running a clean re-synthesis — not by patching the output in conversation, which reintroduces superseded signatures and partial refactorings into the agent's context.

This is the execution-time face of [BDUF in agentic engineering](bduf-in-agentic-engineering.md): the [Spec Architect](spec-architect-role.md) owns completeness before dispatch so the pass never needs steering. By treating specifications as executable compiler inputs, agentic linearism maximizes the benefit of [long-context binding constraints](../context/long-context-binding-constraints.md).
