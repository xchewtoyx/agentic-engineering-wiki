---
type: concept
title: Minimal, General Tool Surface
description: >
  A few general tools (read, write, edit, bash) plus command-line tools
  documented on demand often beat large bespoke tool sets, which spend context
  and confuse selection; MCP versus CLI remains disputed.
evidence: moderate
sources:
  - title: "What I learned building an opinionated and minimal coding agent"
    resource: "Mario Zechner, 30 Nov 2025 — https://mariozechner.at/posts/2025-11-30-pi-coding-agent/"
  - title: "How Long Contexts Fail"
    resource: "Drew Breunig, 22 Jun 2025 — https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html"
  - title: "Tools: Code Is All You Need"
    resource: "Armin Ronacher, 3 Jul 2025 — https://lucumr.pocoo.org/2025/7/3/tools/"
  - title: "Designing agentic loops"
    resource: "Simon Willison, 30 Sep 2025 — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/"
  - title: "Pi 1.0"
    resource: "Earendil, 1 Oct 2026 — https://earendil.com/posts/pi-1-0/"
  - title: "The Anatomy of an Agent Harness"
    resource: "Viv Trivedy, LangChain, 10 Mar 2026, via secondary summary — https://businessdatasolutions.github.io/ai-wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness"
  - title: "Pi coding agent pulls a 180 and adds MCP support"
    resource: "The Register, 2 Oct 2026 — https://www.theregister.com/ai-and-ml/2026/10/02/pi-coding-agent-pulls-a-180-and-adds-mcp-support/5300678"
  - title: "The Agent Harness: Past, Present, and Future"
    resource: "Polomodov, 1 Oct 2026 (secondary; Vercel figure) — https://polomodov.tech/en/2026-10-01-agent-harness-evolution"
  - title: "LLM06:2025 Excessive Agency"
    resource: "OWASP GenAI Security Project — https://genai.owasp.org/llmrisk/llm062025-excessive-agency/"
---

Sizing the [tool inventory](tool-inventory.md) is a capability versus
reliability tradeoff, and this note records where one camp of practitioners has
landed on it. Giving an agent a tool for every operation looks helpful, but
each tool definition costs context and every extra option is another chance to
pick the wrong one. Drew Breunig documents this as tool confusion: one
quantised Llama 3.1 8B model failed with 46 tools and succeeded with 19, a
direct instance of the confusion mode in
[four ways long contexts fail](../context/four-context-failure-modes.md).

The minimalist response is a small set of general tools. Mario Zechner's pi
agent has four (read, write, edit, bash), and its system prompt plus tool
definitions come to under 1,000 tokens; it was competitive on Terminal-Bench
2.0. Zechner rejected the [Model Context Protocol](model-context-protocol.md)
(MCP), noting that one browser-devtools MCP server costs about 18,000 tokens,
roughly 7–9% of the window, and preferred command-line tools with READMEs whose
cost is paid only when used, a form of
[progressive disclosure](../instructions/progressive-disclosure.md). Armin
Ronacher argues that having the model write code beats chaining MCP calls,
because code composes, uses less context and can be reviewed and re-run. Simon
Willison lists command-line tools in AGENTS.md rather than via MCP. A secondary
source reports that Vercel removed 80% of its tools, leaving bash, and got 3.5
times faster runs with 37% fewer tokens; that figure is unverified.

**The MCP counter-position.** Trivedy at LangChain treats MCP servers as a
normal harness component, and the Wavestone harness study (a preprint) found
MCP in 8 of 11 harnesses. Most tellingly, Pi itself added MCP support through
Codemode at its 1.0 release, which The Register described as a reversal. The
disagreement is live.

**The security counter-position.** A second tension matters more for agents
that act on production systems. The minimal-tools case comes from coding
agents, where a general shell is the point and the blast radius is a sandbox.
Security guidance pulls the other way: the OWASP (Open Worldwide Application
Security Project) excessive-agency risk favours narrow, single-purpose actions
with no raw shell, because a shell cannot be scoped, audited or approved
meaningfully. That case is made in
[narrow action verb set](narrow-action-verb-set.md). The two positions are not
contradictory so much as tuned to different risk profiles, and a common
resolution is to use both: broad, general, read-only tools where context
economy and flexibility help investigation, and narrow verbs for anything that
changes a live system. Whichever way the inventory is built, the right size is
an empirical question for
[tool selection ablation](../evaluation/tool-selection-ablation.md), and each
remaining tool still needs the care described in
[tool definition design](tool-definition-design.md). The broader
harness-thickness question is in
[thin vs thick harness](../thin-vs-thick-harness-debate.md).
