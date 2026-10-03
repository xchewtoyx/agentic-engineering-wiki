---
type: concept
title: Shared Language Glossary
description: >
  A project glossary file gives the agent and the human one ubiquitous
  language, which cuts verbosity, keeps naming consistent, and doubles as a
  source of leading words.
evidence: moderate
sources:
  - title: "mattpocock/skills, README and GLOSSARY.md"
    resource: "https://github.com/mattpocock/skills (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, wait-what changelog entry (v1.2.0)"
    resource: "https://github.com/mattpocock/skills/blob/main/CHANGELOG.md (read 2 Oct 2026)"
---

Matt Pocock borrows the ubiquitous language from Domain-Driven Design. An agent dropped into a project has to infer its jargon, so it uses twenty words where one would do. A glossary file (his `GLOSSARY.md`, formerly `CONTEXT.md`) fixes this: each term gets a definition, the synonyms to avoid, and relationships between terms, and flagged ambiguities record how a confusion was resolved. His own example compresses a sentence about a lesson being given a place on the filesystem into "the materialization cascade".

He claims three payoffs beyond brevity: variables, functions and files get named consistently, the codebase becomes easier for the agent to navigate, and the agent spends fewer tokens thinking because it has a more concise language. These are practitioner claims shown in his repositories rather than measured.

The glossary is also a pool of [leading words](leading-words-in-agent-instructions.md). When the same term lives in prompts, docs, skills and code, a [context pointer](context-pointer.md) using it fires more reliably. `wait-what`, a three-line corrective for an over-verbose message, works by reusing that vocabulary.

The repository distinguishes passive use (reading the glossary, a one-line pointer in other skills) from active domain modelling (challenging terms, edge-case scenarios, updating the glossary and decision records inline), which is its own skill.

Boundary: a glossary that restates code identifiers adds nothing, because it becomes a [cache](single-source-of-truth-and-cache.md) of what the code already says; its value is terms and decisions the code cannot express.
