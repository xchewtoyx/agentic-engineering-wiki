---
type: concept
title: Inter-Agent Coordination Protocols
description: >
  Structure multi-agent interaction through formal task bidding, contract awards,
  and standardized messaging layers rather than free-form conversational chatter.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 4"
---

When scaling [multi-agent architecture](multi-agent-architecture.md), allowing agents to interact purely through unstructured conversational chat leads to [multi-agent token inflation](multi-agent-token-inflation.md), ambiguous task handoffs, and cascading coordination failures.

**Inter-agent coordination protocols** establish formal interaction contracts across multi-agent networks:

- **Contract Net Protocol (CNP)**: Decomposes task allocation into a structured three-phase market:
  1. *Task announcement*: A manager agent advertises an engineering task (e.g., "generate unit tests for module X") along with constraints and budget.
  2. *Bidding*: Contractor agents evaluate their capabilities, availability, and tool access to submit formal bids.
  3. *Awarding and execution*: The manager awards the contract to the best-suited agent, which executes the work and returns structured deliverables.
- **Agent-to-Agent (A2A) and Agent Network Protocols (ANP)**: Standardized network and messaging envelopes that support agent identity verification, service discovery, typed payload routing, and asynchronous status notifications.

Replacing open-ended chat with explicit delegation protocols provides inspectable lifecycle flow, bounds token overhead, and enables dynamic agent discovery in complex enterprise environments.
