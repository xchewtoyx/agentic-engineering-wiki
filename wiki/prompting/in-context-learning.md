---
type: concept
title: In-Context Learning
description: >
  Teaching desired behaviour from examples inside the prompt alone, without
  weight updates — zero-shot through N-shot adaptation at inference time.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5–6"
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    resource: "Min et al. (2022), full paper, pp. 1–19"
---

In-context learning (Brown et al., 2020) lets a model acquire desired behaviour
from examples in the prompt without updating weights. Each example is a "shot":
zero-shot has none; N-shot has N. Feeding new documentation in context is a form
of continual learning — the model answers about material it was never trained
on. This is the implicit counterpart to
[explicit instruction design](explicit-instruction-design.md)'s stated rules:
showing the model a pattern is often more effective than describing it,
especially for things that are tedious or impossible to enumerate as rules
(tone, style, an implied output distribution). Few-shot examples are often
stronger **implicit** clarification than long rule lists — especially for
output format and tone — under
[static vs dynamic prompt content](../context/static-vs-dynamic-prompt-content.md).

Demonstrations do not teach only their literal input-to-output mappings. Their
[input distribution](demonstration-input-distribution.md),
[output space](demonstration-output-space.md), and
[paired sequence format](paired-demonstration-format.md) can each drive gains
independently, and a [mapping ablation](demonstration-mapping-ablation.md) may
show that exact label mappings contribute surprisingly little.

More examples generally help but are limited by context length and cost. Stronger
models often need fewer shots for generic instruction following, yet
domain-specific APIs and formats can still benefit greatly from in-prompt
examples. Prefer token-efficient example formats when quality is equal. Format
shots as labeled exemplars or as prior solved turns integrated into the
[advice conversation](advice-conversation-document.md) so the model continues
a successful style ([few-shot example formatting](few-shot-example-formatting.md)).

The context-length limit is sharper than it first looks when the main
question already carries rich [dynamic content](../context/static-vs-dynamic-prompt-content.md):
adding several full examples with equally rich context blows up the prompt
and creates confusable, near-identical blocks the model has trouble
attending to distinctly, since completion-side attention has to pick the
right one out of several similarly-shaped candidates — use short,
format-only shots instead when the goal is context scaling rather than
reasoning depth. Shrinking examples to fit is risky in the other direction —
overly simplistic examples can nudge the model away from the deeper reasoning
the full context should enable, and if an example carries much less
information than the main question, there's little for the model to actually
learn from it. The exception is using few-shot to clarify one narrow aspect
only (typically output format), which transports fine even via short
examples.

**Harness pitfalls to weigh against these benefits:**

1. **Context scaling** — full-fidelity few-shots that mirror rich per-user
   dynamic context explode the window and create confusable near-duplicates,
   as above.
2. **[Anchoring bias in examples](anchoring-bias-in-examples.md)** — examples
   imprint answer distributions; sample representatively from real data and
   include major edge classes without over-weighting exotics.
3. **[Spurious pattern extrapolation](spurious-pattern-extrapolation.md)** —
   accidental ascending order or "happy path then unhappy path" ordering gets
   continued by the model; shuffle/subset the examples and measure with
   [offline prompt evaluation](../evaluation/offline-prompt-evaluation.md) or
   [prompt optimization tooling](../optimization/prompt-optimization-tooling.md).

Use few-shot when you have examples illustrating something otherwise
unobvious to the model; don't reach for it by default when the problem is
already clear — it lengthens the prompt and invites all three pitfalls for no
benefit. In particular, a model meta-trained for in-context learning may show a
[simple-cue bias](meta-training-simple-cue-bias.md), so ablate example
components before concluding that it learned the intended rule.

Improvement may reflect [task location](demonstrations-as-task-location.md)
rather than acquisition of new semantics. Compare gold examples with an
[unlabelled demonstration baseline](unlabelled-demonstration-baseline.md), and
do not generalize classification results to novel mappings or open-ended
generation without task-specific evidence.

In this framing, "prompt" is the whole model input; "context" is the information
that enables the task — the material
[context engineering](../context-engineering.md) selects and places.
