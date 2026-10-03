---
type: concept
title: Context Adaptation Noise Robustness
description: >
  An itemized, delta-updated context degrades gradually under weak or
  occasionally harmful reflections, falling below baseline only when every
  step is corrupted, which a harmful-reflector stress test can verify.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §4.6, App. A.4"
---

A self-adapting context is only as good as the lessons written into it, so
check how it degrades when the
[Reflector](reflector-diagnostic-prompt-contract.md) is weak or wrong.

Both experiments below are offline on FiNER with a DeepSeek-V3.1 Generator
and Curator, and have not been repeated on other benchmarks.

**Weaker reflectors.** Swapping the Reflector for a weaker model
(GPT-OSS-120B) still gave most of the gain: +5.9 over base, versus +7.6
(DeepSeek-V3.1) and +7.8 (GPT-5.1).
A strong reflector helps but is not required.

**Harmful-reflector stress test.** Instruct the Reflector to inject harmful
or conflicting bullets once every X steps, then measure accuracy as X varies.
Results (base 70.7, clean 78.3):

| Corrupt every X steps | 1 | 5 | 10 | 25 | 50/100 |
|---|---|---|---|---|---|
| Accuracy | 66.7 | 76.1 | 77.0 | 77.8 | 78.2 |

On this task degradation was gradual. Only corruption on every iteration
pushed accuracy below the unadapted base. The test *design* is cheap and can
be reused for other self-modifying harnesses, though the tolerance measured
here may not transfer. Use it to probe how much poisoned feedback (bad
labels, adversarial tool output, an
[indirect prompt injection](../security/indirect-prompt-injection.md) reaching the
Reflector) the system can absorb.

**Why itemized contexts tolerate noise.** A bad bullet is one local entry.
It is not a rewrite of the whole context. Usage metadata
([helpful/harmful counters](itemized-bullet-context.md)) lets
[grow-and-refine](grow-and-refine-context-maintenance.md) merge duplicates and
*can* filter entries flagged as potentially harmful. The authors call this a
"first line of defense" against noise; it is an explanation, not an
ablated result.

Further guards the authors suggest as compatible extensions (none
evaluated):

- contradiction detection between new and existing bullets
- prompting the Curator to admit only high-confidence updates
- periodic pruning of outdated entries
