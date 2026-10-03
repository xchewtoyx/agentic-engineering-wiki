---
type: concept
title: Knowledge Content Inventory
description: >
  A compact machine-readable catalog can route an agent to relevant knowledge
  pages with progressive disclosure so they do not load the whole bundle
  before full-text or embedding retrieval becomes necessary.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Indexing and logging; Optional CLI tools; Tips and tricks"
---

For a moderate knowledge collection, maintain a compact inventory of concept
identifiers and one-line descriptions. Load or search the inventory first so
the agent can select a small set of pages for full reading. This can postpone
the operational cost of embedding infrastructure while giving retrieval a
more reliable surface than guessing filenames.

The inventory is a generated retrieval artifact, not the knowledge itself.
Rebuild or update it on ingestion, and escalate to lexical, vector, or hybrid
search only when measured discovery failures justify the added machinery under
[minimum sufficient knowledge architecture](minimum-sufficient-knowledge-architecture.md).
