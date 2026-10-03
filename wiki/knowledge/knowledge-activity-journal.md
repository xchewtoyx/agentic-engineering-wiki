---
type: concept
title: Knowledge Activity Journal
description: >
  An append-only chronological journal lets agents and humans reconstruct recent
  ingests, queries, maintenance passes, and their outcomes.
sources:
  - title: "LLM Wiki"
    resource: "LLM Wiki, Indexing and logging; Optional CLI tools; Tips and tricks"
---

Content-oriented discovery and operational history answer different questions.
A knowledge inventory says what exists; an activity journal records what
happened and when. Append one structured entry for each ingestion, consequential
query writeback, or maintenance pass so later sessions can inspect recent work
without reconstructing it from file timestamps or conversation history.

Use stable, machine-readable headings or records so simple tools can select
recent entries. Keep the journal append-only and treat it as operational
provenance for the [ingest-query-maintain loop](ingest-query-maintain-loop.md),
not as a substitute for citations from knowledge notes to original sources.
