---
type: concept
title: Progressive Disclosure
description: >
  Load only metadata up front, such as skill frontmatter and tool names, and
  pull bodies, linked files and deferred tools in when relevant; this is now
  the dominant loading pattern across agent harnesses.
evidence: strong
sources:
  - title: "Equipping agents for the real world with Agent Skills"
    resource: "Anthropic Engineering, 16 Oct 2025 — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"
  - title: "Code execution with MCP"
    resource: "Anthropic Engineering, 4 Nov 2025 — https://www.anthropic.com/engineering/code-execution-with-mcp"
  - title: "The new rules of context engineering for Claude 5 generation models"
    resource: "Thariq Shihipar, claude.dev, 24 Jul 2026 — https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/"
  - title: "Harness Engineering"
    resource: "Barbaste et al. (Wavestone AI Lab), arXiv 2609.00006, July 2026 preprint, §12 and Table 8 — https://arxiv.org/html/2609.00006v1"
  - title: "Pi 1.0"
    resource: "Earendil, 1 Oct 2026 — https://earendil.com/posts/pi-1-0/"
  - title: "Hermes Agent docs: Skills"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"
---

Every skill body, tool definition and reference document loaded at the start of a session costs context before the agent has done anything. As agents gain more skills and tools, loading everything up front crowds out the task itself and, as [context rot](../context/context-rot.md) shows, degrades performance.

Progressive disclosure answers this by loading in layers. Anthropic's Agent Skills design has three levels: a SKILL.md file's name and description frontmatter is preloaded, its body loads only when relevant, and linked files load as needed. Anthropic's post on code execution with the [Model Context Protocol](../harness/model-context-protocol.md) (MCP) names two problems with direct tool calling, tool definitions overloading the window and intermediate results consuming tokens, and lists progressive disclosure among the remedies. The claude.dev "new rules" post lists the shift from everything-upfront to progressive disclosure, including deferred tool loading, as one of six changes behind cutting most of Claude Code's system prompt. Pi 1.0 likewise added deferred tool loading, and Hermes skills follow the same agentskills.io layering.

The Wavestone study of eleven harnesses (a preprint) reports that SKILL.md skills were adopted by 9 of 11 systems and MCP by 8 of 11, and that deferred or lazy loading of skills and tools is the dominant pattern.

What makes the pattern work is the always-loaded layer: each preloaded description is a [context pointer](context-pointer.md), and its wording decides whether the agent ever pulls in the body behind it. Inside a single document the same move is the step down the [information hierarchy](information-hierarchy.md) from in-file content to a disclosed reference file. The principle also appears at other layers: a short [steering file that acts as a map](steering-files-as-navigation-pointers.md) is progressive disclosure for repository documentation, the "select" move in [write, select, compress, isolate](../context/context-write-select-compress-isolate.md) is its retrieval form, and documenting command-line tools for on-demand reading is its tool form, as argued in [minimal, general tool surface](../harness/minimal-general-tool-surface.md).

For an operations or repair agent, the implication is not to start each run with every runbook and every vendor command loaded. Short descriptions of failure-class skills can sit in context, with the full procedure loaded only once diagnosis points at that class, which keeps the window free for the logs and traces the diagnosis actually needs.
