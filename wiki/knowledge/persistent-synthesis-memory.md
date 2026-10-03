---
type: concept
title: Persistent Synthesis Memory
description: >
  Persisting cross-source synthesis lets agent knowledge compound instead of
  reconstructing the same relationships at every retrieval.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, The core idea"
---

Conventional retrieval brings raw fragments into each query and asks the model
to reconstruct their relationships anew. A persistent synthesis memory instead
stores agent-authored concepts, cross-references, contradictions, and revised
conclusions between sessions. New sources update the existing synthesis, so
earlier integration work becomes durable input to later questions.

This is more than indexing and more mutable than the raw evidence. Preserve the
distinction with [source-memory-schema separation](source-memory-schema-separation.md),
carry provenance into derived notes, and run an explicit
[ingest-query-maintain loop](ingest-query-maintain-loop.md) so accumulated
synthesis does not become accumulated staleness.
