---
type: concept
title: Grounding Quality Dimensions
description: >
  Citation presence, entailment, inference legitimacy, relevance, and viewpoint
  coverage must be evaluated separately in grounded agent outputs.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

A citation-density score collapses distinct failure modes. Evaluate at least:

- whether each claim has a citation;
- whether the cited passage entails the sentence;
- whether the synthesis preserves the source's meaning;
- whether the inference legitimately connects evidence to the topic;
- whether the source is relevant; and
- whether the retrieved source set represents viewpoints neutrally.

A citation makes a claim traceable. It does not establish that the passage
entails the wording, preserves its meaning, or licenses the inference drawn
from it, and high citation density can coexist with a failure on any of these
later checks. Audit each layer on its own. Never treat automated citation
recall or entailment as a complete quality score. A system can score well on
citation precision and recall while showing no gain in human-perceived
verifiability. Combine these dimensions in
[research-agent evaluation](research-agent-eval-groundedness.md), and inspect
[inferential-link failures](inferential-link-grounding-failure.md) separately
from missing citations.
