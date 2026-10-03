---
type: concept
title: Model Context Protocol
description: >
  An open standard that unifies how agents securely discover, authenticate,
  and invoke external developer tools, execution environments, and data sources.
sources:
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 4"
---

Historically, agent harnesses implemented bespoke, hard-coded tool wrappers for each execution environment, database, or API. This created tight coupling between the agent's reasoning loop and specific runtime environments, leading to fragile integrations and duplicated maintenance.

The **Model Context Protocol (MCP)** provides an open, standardized client-server protocol that separates agent reasoning from external capability providers:

- **Dynamic tool discovery**: Agents query MCP servers at runtime to inspect available tools, their JSON schemas, input constraints, and descriptions, populating the [tool inventory](tool-inventory.md) on demand.
- **Contextual resources**: MCP standardizes access to external context—such as local repository files, issue trackers, documentation stores, and database schemas—via uniform URI templates.
- **Prompt templates**: MCP servers can expose server-managed prompt templates and workflows tailored to their specific underlying systems.
- **Security and authorization**: MCP establishes clear trust boundaries, allowing fine-grained permissions, sandboxing, and user approval gates before tool actions execute.

By decoupling tool implementation from the agent harness, MCP allows autonomous software engineering agents to interact with diverse developer ecosystems without requiring custom harness code for each new service.
