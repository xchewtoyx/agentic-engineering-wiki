---
type: concept
title: Phase Latency Compression
description: >
  Agents keep the sequential phases and governance gates of the software lifecycle intact while collapsing
  elapsed time inside each phase, making it cheap to rerun upstream specification work.
sources:
  - title: "SDAD: Spec-Driven Agentic Development for the AI-Native SDLC"
    resource: "Nguyen & Nguyen (2026), ch. 3"
---

The Waterfall cascade — requirements specification, high- and low-level design, coding, testing — existed for governance, auditability, and accountability. Its failure was latency: months per phase pushed teams to bypass stale documents and smuggle change in at the code layer.

Agent assistance does not abandon the phase sequence or its gates. It achieves **phase latency compression**: elapsed time collapses *inside* each phase.

- **Requirements** — agents ingest interview transcripts, summarize stakeholder goals, detect contradictions, and draft structured requirement sections; a human architect still signs off.
- **Design** — agents propose architectural options, component interfaces, API contracts, and trade-off notes traced to upstream requirement IDs.
- **Construction and testing** — agents generate multi-file code and aligned test oracles bound by the design documents, as in [zero-shot repository synthesis](zero-shot-repository-synthesis.md).

The economic consequence is an inversion: once synthesis is cheaper than clarification, teams rerun upstream specification refinement earlier and in smaller batches instead of patching downstream. Keep strict phase gates (for example "requirements signed", "all P1 design risks mitigated", the [spec fidelity gate](spec-fidelity-gate.md)) and bidirectional requirement-to-artifact traceability — they are the deterministic context bounds that keep long-context agents aligned, and they make [BDUF in agentic engineering](bduf-in-agentic-engineering.md) affordable without losing delivery velocity.
