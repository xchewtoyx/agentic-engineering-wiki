---
type: concept
title: Premature Completion
description: >
  Visible steps still to come pull an agent into ending the current step
  early; the defence is to sharpen the completion criterion first, and only
  then hide later steps behind a real context boundary such as a subagent or
  hand-off.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
---

Premature completion is ending a step before it is genuinely done. Matt Pocock's `writing-for-agents` skill locates the cause in the document's shape: the post-completion steps the agent can already see supply a pull towards finishing, and the [completion criterion](completion-criterion.md)'s clarity is the only resistance. It is the step-level form of [asset rush](asset-rush.md).

The defence has an order. Sharpen the bound first, because that is local and cheap. Only if the criterion is irreducibly fuzzy, and you have actually observed the rush, hide the later steps by splitting the sequence into separate documents.

The important caveat is that hiding only works across a real context boundary: a hand-off to a fresh session or a dispatch to a subagent. An inline call to another skill leaves the later steps in context and clears nothing. The reverse also holds: merging two sequences into one document exposes the first sequence to the second's steps and invites rushing.

This is why Pocock's main flow keeps `/implement` per ticket with context cleared between tickets, and why `research` runs as a background agent: the work in front of the agent is the only work it can see.

Boundary: splitting spends [cognitive load](context-load-versus-cognitive-load.md) on the human, who must now run the second part, so split only when the rush is observed. See [splitting skills](splitting-skills.md).
