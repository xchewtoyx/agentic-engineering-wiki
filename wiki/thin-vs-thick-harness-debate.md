---
type: concept
title: Thin vs Thick Harness
description: >
  Model-lab voices argue capability makes scaffolding redundant while harness
  builders show large harness-only gains, and the resolution is that harness
  thickness should track model capability and how verifiable the task is.
evidence: weak
sources:
  - title: "Is harness engineering real?"
    resource: "Latent Space (AINews), 5 Mar 2026 — https://www.latent.space/p/ainews-is-harness-engineering-real"
  - title: "Improving Deep Agents with harness engineering"
    resource: "Viv Trivedy, LangChain, 17 Feb 2026 — https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
  - title: "The Agent Harness: Past, Present, and Future"
    resource: "Polomodov, 1 Oct 2026 (secondary history) — https://polomodov.tech/en/2026-10-01-agent-harness-evolution"
  - title: "The new rules of context engineering for Claude 5 generation models"
    resource: "Thariq Shihipar, claude.dev, 24 Jul 2026 — https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/"
---

Anyone building an agent has to decide how much machinery to put around the
model. Too little and the agent loses track, loops or declares success early;
too much and the harness burns context, encodes outdated workarounds and becomes
its own maintenance burden. The field has not settled where the line sits.

**The thin side.** Latent Space reports Boris Cherny and Cat Wu (Claude Code)
and Noam Brown arguing that the value lives in the model and the harness should
stay thin. It also reports that METR and Scale's SWE-Atlas found harness
differences within noise. Anthropic's own guidance is that components encode
model weaknesses and should be removed as models improve, and a claude.dev post
confirms a cut of more than 80% of Claude Code's system prompt with no
measurable loss (see [harness assumptions go stale](harness-assumptions-go-stale.md)).
A secondary history adds that WorkOS got better results after deleting about
95% of its skill text, which is unverified.

**The thick side.** Jerry Liu is reported as saying the harness is everything,
and Latent Space cites harness-only gains across 15 models. LangChain moved an
agent from 52.8% to 66.5% on Terminal-Bench 2.0 by changing only the harness,
and preprints report ranking reversals of up to 38 points from harness choice
alone (see [harness as a performance lever](harness-as-performance-lever.md)).
swyx concludes that harness engineering is increasingly real.

The evidence is weak on both sides. The Cherny, Brown and Liu positions come
from a page that showed them truncated, with no primary source fetched, and the
95% deletion anecdote is secondary.

A workable resolution is that the right thickness depends on how capable the
model is and how verifiable the task is. Where success can be checked
mechanically, a thin harness with strong checks can work; where it cannot,
unattended loops degrade, as described in
[unverifiable loops rot](development/unverifiable-loops-rot.md). For agents that
take operational actions, the task is often partly verifiable (a health check
either passes or not) but the blast radius is large, which argues for thick
sensors and thin, auditable action paths: rich read-only diagnostics plus a
deliberately [narrow action verb set](harness/narrow-action-verb-set.md). That is
where this debate meets the
[minimal general tool surface](harness/minimal-general-tool-surface.md) argument.
