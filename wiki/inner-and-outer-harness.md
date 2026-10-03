---
type: concept
title: Inner and Outer Harness
description: >
  "Harness" names both the agent runtime (loop, tools, context) and the
  repository and environment the agent works in (AGENTS.md, linters, tests,
  observability), and a team running agents usually has to engineer both.
evidence: weak
sources:
  - title: "The Anatomy of an Agent Harness"
    resource: "Viv Trivedy, LangChain, 10 Mar 2026, read via secondary summary — https://businessdatasolutions.github.io/ai-wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026 — https://openai.com/index/harness-engineering/"
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026 — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
  - title: "Harness engineering: 5 companies, 5 definitions"
    resource: "kenimo49, dev.to — https://dev.to/kenimo49/harness-engineering-5-companies-5-definitions-why-everyone-disagrees-on-what-it-means-531h"
---

Conversations about "the harness" often talk past each other because the word
is used for two different things. A dev.to survey of five vendors' definitions
finds them diverging: OpenAI stresses declarative constraints, Anthropic
stresses context stability across resets, LangChain uses the
[model-plus-harness split](agent-equals-model-plus-harness.md), and Böckeler
treats the codebase itself as part of the harness.

The two meanings coexist. The **inner harness** is the agent runtime: the loop,
the tools and context management, as described by Trivedy at LangChain, by
Anthropic's Managed Agents work and by Pi. The **outer harness** is the
repository and environment the agent works inside: AGENTS.md, linters, tests and
observability, as described by Hashimoto, by OpenAI's harness-engineering post
and by Böckeler. The two are engineered differently. Inner-harness work changes
how the agent thinks and acts, while outer-harness work changes what the agent
can see and what pushes back on it, through
[guides and sensors](harness/guides-and-sensors.md) and short
[steering files that act as navigation pointers](instructions/steering-files-as-navigation-pointers.md).

This split is a synthesis across secondary summaries rather than a distinction
any single primary source draws, so the evidence is weak. It is offered as
vocabulary, not as a finding.

The vocabulary is useful whenever one agent operates on systems that are
themselves agents or agent-ready repositories. An operations agent that
maintains other services has its own inner harness (loop, tools, permissions)
and also works through an outer harness (runbooks, checks, health endpoints) of
the systems it maintains, where each failure it fixes can become a new check or
document. A fault report that does not say which side it is about is usually
ambiguous.
