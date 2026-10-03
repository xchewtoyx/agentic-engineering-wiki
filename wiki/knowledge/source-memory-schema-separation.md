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

The layers differ in mutability as much as in content. Sources are the stable
truth and stay read-only. The knowledge layer is a flat set of agent-owned
concept and summary pages: the agent holds write authority, revises pages as
evidence arrives, and is responsible for consistency and de-duplication, while
humans mostly read it (see
[human-agent knowledge roles](human-agent-knowledge-roles.md)). The schema, typically
a repository instruction file such as `AGENTS.md` or `CLAUDE.md`, co-evolves
with the system as conventions and workflows are refined, keeping maintainer
behaviour consistent across sessions.

This separation preserves evidence provenance while allowing the derived wiki
to evolve. It also prevents content structure from being confused with the
[system prompt architecture](../harness/system-prompt-architecture.md) that governs the
maintainer. Give each layer explicit permissions and keep citations from
derived notes back to immutable sources.
