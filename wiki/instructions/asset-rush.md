---
type: concept
title: Asset Rush
description: >
  Models are trained to finish by producing a result, so they tend to push
  ahead on untested hypotheses and state guesses with confidence, and many of
  the corrections that become skills are counterweights to this pull.
evidence: weak
sources:
  - title: "Podcast with Matt Pocock (personal listening notes)"
    resource: "notes, 2 Oct 2026"
---

Asset rush is a model's built-in drive to produce a deliverable (code, a document, an answer) rather than stop, check or admit uncertainty. Training rewards finishing with something to show, so finishing becomes what the model wants by default. The framing comes from a podcast interview with Matt Pocock and rests on his practitioner experience rather than measurement, which is why the evidence is weak.

Two failures come from it. First, the model acts on an untested hypothesis: it picks a plausible cause or design and builds on it without checking, because checking delays the output. Second, it [hallucinates](../hallucination.md) with confidence: a polished, certain-sounding claim does more to look like a finished result than "I don't know".

This is why many of the [corrections worth turning into skills](skill-as-repeated-correction.md) say the same thing: verify before proceeding, test the hypothesis, say what is unknown. A skill pushing against asset rush should name the step it wants with a strong [leading word](leading-words-in-agent-instructions.md) ("reproduce", "verify", "spike") and make checking part of the [completion criterion](completion-criterion.md), so that pausing to check counts as progress rather than delay. At the level of a single step inside a document, the same pull shows up as [premature completion](premature-completion.md).

Boundary: not every confident output is asset rush. Treat it as the likely cause when the model skips a check it could have run cheaply.
