---
type: concept
title: Domain-Specialized Role Prompts
description: >
  Replace generic persona descriptions with explicit domain ontologies,
  deterministic checklists, and specialized toolsets in agent role prompts.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 5-6"
---

In [multi-agent architecture](../orchestration/multi-agent-architecture.md), system designers frequently assign roles using superficial persona prompts (e.g., "You are an expert security auditor" or "You are a senior software architect"). In complex technical domains, these generic personas suffer high failure rates: they offer vague, high-level advice, miss subtle domain-specific edge cases, and hallucinate compliance.

**Domain-specialized role prompts** replace stylistic persona roleplaying with deep operational grounding:

- **Domain ontologies and taxonomies**: Provide explicit definitions of domain entities, failure classes, and architectural invariants (e.g., CWE taxonomies for security agents or API lifecycle rules for integration agents).
- **Concrete evaluation checklists**: Replace open-ended instructions with deterministic evaluation rubrics and validation sequences that the agent must step through.
- **Dedicated retrieval augmentation**: Equip the agent with role-specific [context engineering](../context-engineering.md), including internal architectural decision records (ADRs), API schemas, and historical incident postmortems.
- **Narrowed tool inventories**: Limit each specialist's [tool inventory](../harness/tool-inventory.md) strictly to operations relevant to its domain responsibility, reducing action-space entropy.

Grounded role definition ensures that specialized agents act as rigorous domain validators rather than conversational approximations of human job titles.
