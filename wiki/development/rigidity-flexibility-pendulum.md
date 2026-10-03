---
type: concept
title: Rigidity–Flexibility Pendulum
description: >
  Software methodology has swung between documentation fidelity and execution velocity, each pole rational
  for its era's bottleneck — and agentic synthesis swings it back toward formal specification.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 2"
---

Methodology oscillates between documentation fidelity and execution velocity; each swing was rational for the bottleneck of its time.

- **Formal rigidity (Waterfall/RUP, 1970s–1990s)** — high fidelity, low velocity. Royce actually prescribed staged phases with adjacent-phase feedback, early prototyping, and customer involvement; pedagogy flattened that into a feedback-free cascade. Strengths: traceability, reviewability, contracts that survive staff turnover. Weaknesses: feedback latency across specification freezes and late, expensive defects. Its rigorous artifacts turn out to be exactly the machine-interpretable intent agents need.
- **Iterative flexibility (Agile/Scrum, 2001–2020)** — velocity bought by trading fidelity for tacit communication. Two-week sprints gave rapid validation, but rationale lived in conversation and tribal memory. Rational while humans were the only executors; brittle for agents, which cannot reconstruct undocumented intent from context (see [tacit knowledge erosion](tacit-knowledge-erosion-under-ai-assisted-work.md)).
- **Point acceleration (Copilot era, 2021–2024)** — token-level autocomplete inside unchanged Agile structures. Short contexts and unreliable multi-file reasoning kept architecture and specification human, so methodology did not move.
- **Automated rigidity (spec-driven agentic development, 2025–2026)** — multi-million-token contexts and multi-agent orchestration make whole cross-module features synthesizable from one formal document, with documented 3–5× velocity gains — conditional on rigorous up-front specification, without which quality degrades steeply under the [ambiguity tax](ambiguity-tax.md).

Use this history when justifying agentic specification discipline to skeptics: the return to Royce-style artifacts is not nostalgia but inversion. Synthesis is fast, so durable, complete, inspectable specifications are the scarce input. The mechanism is [BDUF in agentic engineering](bduf-in-agentic-engineering.md); the economic statement is the [bottleneck inversion to intent clarity](bottleneck-inversion-to-intent-clarity.md).
