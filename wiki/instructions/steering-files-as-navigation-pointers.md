---
type: concept
title: Steering Files as Navigation Pointers
description: >
  Always-loaded steering files (AGENTS.md, CLAUDE.md) work best as a short map
  of pointers into a versioned docs system of record, with coding standards
  enforced at review and mechanical rules turned into deterministic checks.
evidence: moderate
sources:
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026 — https://openai.com/index/harness-engineering/"
  - title: "AGENTS.md"
    resource: "Open format, stewarded by the Agentic AI Foundation (Linux Foundation) — https://agents.md/"
  - title: "The new rules of context engineering for Claude 5 generation models"
    resource: "Thariq Shihipar, claude.dev, 24 Jul 2026 — https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/"
  - title: "My AI Adoption Journey"
    resource: "Mitchell Hashimoto, Feb 2026, read via Bloss0m summary — https://www.bloss0m.com/en/blog/16-mitchell-hashimoto-harness-origin/"
  - title: "Ralph Wiggum as a 'software engineer'"
    resource: "Geoffrey Huntley, ghuntley.com — https://ghuntley.com/ralph/"
  - title: "Designing agentic loops"
    resource: "Simon Willison, 30 Sep 2025 — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/"
  - title: "mattpocock/skills, retro skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/sandcastle, CLAUDE.md and .sandcastle prompts"
    resource: "https://github.com/mattpocock/sandcastle (read 2 Oct 2026)"
---

Agent instruction files tend to grow. Every surprise adds a paragraph, and before long one file tries to hold the whole system's knowledge. OpenAI's harness-engineering team reports that this "one big AGENTS.md" failed for four reasons: context is scarce, too much guidance becomes non-guidance, the file rots, and nobody can verify it.

Their replacement is a roughly 100-line AGENTS.md that acts as a map into a structured `docs/` directory, the repository's system of record. That directory holds design documents with verification status, an architecture map, quality grades, and checked-in execution plans with progress and decision logs, and linters and continuous integration check that it stays fresh and cross-linked. The core rule is that anything not in the repository does not exist for the agent. The AGENTS.md open format, which describes itself as a README for agents, supports this shape through nested files in monorepos. Anthropic's claude.dev guidance agrees from the other side: keep CLAUDE.md light, spend its tokens on gotchas, and avoid conflicting instructions spread across the system prompt, skills and user request. This is [progressive disclosure](progressive-disclosure.md) applied to repository documentation, and each line of the map is a [context pointer](context-pointer.md) whose wording decides whether the agent follows it.

Matt Pocock's `retro` skill turns the same idea into a placement policy. `CLAUDE.md` and `AGENTS.md` are pushed into every agent's context, so they hold little more than pointers. Coding standards live in a separate standards file read during review, not implementation. The reasoning is context pressure: the implementation agent explores, writes code and debugs, so its window is the most contested, while the review agent receives a diff and needs little exploration, so it is the cheaper place to impose standards. His `sandcastle` repo follows this: its review prompt points at the standards file, while its implementation prompt carries only the task, the issue and a red-green loop. Standards are further split by kind. A mechanical violation (a banned API, an import shape, a file-location rule) becomes a deterministic check such as a lint rule, a pre-commit hook or a CI job, and only judgement calls stay as written standards. A repo with no guardrail at all is treated as a finding in its own right. `sandcastle` also keeps `AGENTS.md` as a symlink to `CLAUDE.md`, so every harness reads [one source of truth](single-source-of-truth-and-cache.md).

These files have a natural growth rule. Hashimoto (via a secondary summary) reports that almost every line of Ghostty's AGENTS.md came from a past bad agent behaviour, Huntley's agents record their own learnings there, and Willison lists command-line tools there instead of loading tool servers. That makes the steering file the main channel through which [fixing the environment, not the output](fix-the-environment-not-the-output.md) reaches the next session, and it is why the file needs pruning against [sediment](sediment.md) and a scheduled check against drift, as in [entropy garbage collection](../development/entropy-garbage-collection-agents.md). No primary quantitative data was found on how much steering-file size or content affects outcomes, so the case rests on practitioner experience and the repositories that show the practice.

For an operations agent, the same shape applies: its instructions should be a short index pointing into runbooks and failure-class notes held in the repository, and facts it needs, such as which commands are safe on a live system, must be written down there, because knowledge held only by humans is invisible to it.

Boundary: some always-loaded content is legitimate, such as the one typecheck command every task needs. The test is [frequency of relevance](context-load-versus-cognitive-load.md).
