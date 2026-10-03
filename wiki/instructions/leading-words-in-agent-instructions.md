---
type: concept
title: Leading Words in Agent Instructions
description: >
  Words that are heavily represented in a model's training data, such as
  "refactor", steer its behaviour strongly and predictably, so instructions
  should name the task with the established term rather than novel language.
evidence: weak
sources:
  - title: "Podcast with Matt Pocock (personal listening notes)"
    resource: "notes, 2 Oct 2026"
---

A leading word is an established term that carries a large body of learned behaviour with it. "Refactor" appears in so much training data that using it pulls in a whole pattern: preserve behaviour, improve structure, move in small steps. One well-chosen word does the work of a paragraph of explanation.

Novel or invented language has the opposite effect. The model has no prior to attach it to, so it must be defined, and the definition still steers less reliably than the established term.

In practice this means choosing a design language for the task: find the frontier term practitioners actually use for the approach you want. When you are unsure what that term is, describe the approach and ask the model to name it. The name it offers is likely the one it associates most strongly with that behaviour, and is therefore the best leading word to put in the [skill](skill-as-repeated-correction.md). A project [glossary](shared-language-glossary.md) is a standing pool of such words, and a leading word placed first in a [context pointer](context-pointer.md) is what makes the pointer fire.

The claim comes from a podcast interview with Matt Pocock and is supported by his practice rather than by a controlled comparison, so the evidence is weak.

Boundary: a leading word imports its common meaning wholesale. If your intent differs from the standard sense, the strong prior will fight you; pick a different term.
