---
type: concept
title: LLM Application Loop
description: >
  An LLM application is a transformation layer converting a user's problem
  into a document the model completes, then converting the completion back.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

An LLM application is a transformation layer between the user's problem
domain and the model's text domain — and a transformation layer with a
purpose: solving problems. The model itself does only one thing, complete
documents, but this affords great flexibility: chat is completing a
transcript document, and tool execution is completing a specialized
transcript that includes function-calling syntax.

The application runs this transformation as a loop: transform the user's
problem into a document the model completes (see the
[feedforward pass](context/llm-application-feedforward-pass.md) for how), then
transform the completion back into a solution in the user's domain — prose,
parsed fields, [function calling](harness/function-calling.md), or UI/TTS events.
Loops vary in cardinality:

- **Single iteration** — e.g. converting a bulleted list into prose; the job
  is done once the model responds, with no state retained between runs.
- **Multiple iterations in a row** — e.g. a chat assistant, where each turn
  feeds into the next.
- **Iterative, stateful, and shape-shifting** — e.g. a travel-planning app
  that moves through brainstorming, then booking, then reminders and tips as
  the problem itself evolves over the interaction.

Problem difficulty scales with the medium, the level of abstraction, context
needs, and statefulness. Prompt engineering's crux at every point in the loop
is satisfying four criteria at once: train-data familiarity (the
[Little Red Riding Hood principle](prompting/little-red-riding-hood-principle.md)),
relevant information without oversaturation, a cue that leads to a *solution*
rather than mere elaboration ([prompt transition](prompting/prompt-transition.md)), and
a natural stop (chat end-of-turn or completion
[stop sequences](stop-sequences.md)). On the way back out, parsing depends on
[completion preamble types](prompting/completion-preamble-types.md) and
[completion boundary markers](prompting/completion-boundary-markers.md) so the harness
can extract the answer without paying for surrounding fluff.

This framing is the ground floor under everything else in
[agent control flow](orchestration/agent-control-flow.md) and
[conversational agent context](context/conversational-agent-context.md), both
of which describe richer shapes this same fundamental transform-complete-
transform loop can take. Complexity then grows along state,
[retrieval-augmented generation](knowledge/retrieval-augmented-generation.md),
reasoning depth, and tools — the same axes traced by
[progressive agent architecture](orchestration/progressive-agent-architecture.md) and
[prompt engineering sophistication levels](prompt-engineering-sophistication-levels.md).
