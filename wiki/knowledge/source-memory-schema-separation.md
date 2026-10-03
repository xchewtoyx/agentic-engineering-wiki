---
type: concept
title: Source-Memory-Schema Separation
description: >
  Separate immutable evidence, agent-authored knowledge, and operating
  instructions so each layer has a clear owner and mutation policy.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Architecture and Operations"
---

A durable agent knowledge system benefits from three distinct layers:

1. raw sources that the agent may read but not modify;
2. agent-authored knowledge that can be revised as evidence accumulates; and
3. an operational schema that tells future agent sessions how to ingest,
   retrieve, answer, and maintain the knowledge.

This separation preserves evidence provenance while allowing the derived wiki
to evolve. It also prevents content structure from being confused with the
[system prompt architecture](../harness/system-prompt-architecture.md) that governs the
maintainer. Give each layer explicit permissions and keep citations from
derived notes back to immutable sources.
