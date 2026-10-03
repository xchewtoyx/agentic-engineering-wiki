---
type: concept
title: Minimum Sufficient Knowledge Architecture
description: >
  Adopt only the storage, retrieval, and output components justified by the
  domain, collection size, users, and model capabilities.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Why this works and Note"
---

A durable knowledge pattern should not prescribe one fixed implementation.
Directory structure, page formats, retrieval engines, image handling, and
output renderers are optional components whose value depends on the collection
and its use. A small text corpus may need only Markdown and filesystem search;
adding a vector store or media pipeline introduces maintenance without
necessarily improving retrieval.

Start with the smallest architecture that supports the
[ingest-query-maintain loop](ingest-query-maintain-loop.md). Add a component
only after observed scale or workflow pressure justifies it, then preserve the
decision in the [operating schema](knowledge-maintenance-operating-schema.md)
so future agent sessions follow the same discipline.

At moderate scale, a compact
[knowledge content inventory](knowledge-content-inventory.md) may be enough to
route retrieval. Move to lexical, vector, or hybrid search only after measured
misses show that the inventory and filesystem search no longer suffice.
