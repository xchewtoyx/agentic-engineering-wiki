---
type: concept
title: Knowledge Maintenance Operating Schema
description: >
  A versioned instruction artifact makes knowledge-ingestion and maintenance
  conventions repeatable across otherwise stateless agent sessions.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Architecture and Operations"
---

Store the rules for a durable knowledge system in an explicit operational
instruction document. It should define structure, source-ingestion steps,
answering conventions, citation expectations, mutation permissions, and health
checks. Recording the workflow turns a generic model invocation into a
repeatable maintainer even when each session begins without conversational
history.

The schema is part of the harness, not part of the knowledge corpus. Evolve it
when recurring use exposes better domain-specific practices, and regression
test changes as part of [harness drift awareness](../evaluation/harness-drift-awareness.md).
Keep its mutation policy distinct through
[source-memory-schema separation](source-memory-schema-separation.md).
