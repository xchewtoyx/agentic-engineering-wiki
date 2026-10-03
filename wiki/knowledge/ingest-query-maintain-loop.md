---
type: concept
title: Ingest-Query-Maintain Loop
description: >
  Durable agent knowledge compounds when ingestion, useful query results, and
  explicit maintenance all feed revisions back into the store.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Architecture and Operations"
---

Treat external memory as a continuing three-operation loop:

1. **Ingest:** read one immutable source, distil it, revise all affected
   concepts (a single source commonly touches 10–15 existing pages), and record
   provenance. Ingest one source at a time with a human in the loop to steer
   emphasis, and record the chosen workflow in the schema.
2. **Query:** retrieve relevant knowledge and synthesize an answer, filing
   valuable new connections back into memory rather than losing them in chat.
3. **Maintain** (sometimes called *lint*): periodically inspect for contradictions, stale claims, missing links,
   orphans, absent concepts, and evidence gaps, then propose repairs or new
   sources.

Maintenance is an explicit operation, not an assumed side effect of retrieval.
The loop depends on a stable
[knowledge maintenance operating schema](knowledge-maintenance-operating-schema.md)
and benefits from single-source checkpoints that keep revisions reviewable.
