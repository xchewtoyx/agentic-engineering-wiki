---
type: concept
title: Cross-Validating an LLM Judge Against an Independent Metric
description: >
  Earn trust in a model-based grader by measuring its case-by-case agreement
  with a separately computed, non-LLM metric for the same quality, and report
  that agreement rate and the judge's non-convergence rate alongside its scores.
sources:
  - title: "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"
    resource: "From Local to Global: A GraphRAG Approach to Query-Focused Summarization (Edge et al.), §5.2"
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (Shao et al.), full paper, pp. 1–27"
---

A [model-based grader](agent-grader-types.md) that picks the better of two
pipeline outputs (more comprehensive, more diverse) returns a fluent,
confident verdict. That verdict is still an unverified claim, for the same
reason any model output is: confidence is a property of the text, not
evidence that the judgment is right (see [hallucination](../hallucination.md)).
You don't earn trust in the judge by reading its verdicts more closely. You
earn it by checking them against a **structurally independent, non-LLM
metric** that measures the same quality, and reporting how often the two
agree.

A worked protocol from a pairwise RAG-pipeline comparison:

1. **Stabilise the judge.** Repeat each pairwise judgment several times (5 in
   the source) and take the majority vote. A split with no majority counts as
   a tie. This reduces noise, but it is the same judge sampled repeatedly. It
   is not a second method.
2. **Compute a metric that never asks a model to judge.** Extract atomic
   claims from each output and cluster them for redundancy. The claim count
   stands in for comprehensiveness and the cluster count for diversity.
3. **Compare only the cases the judge actually resolved.** In the source,
   33–39% of pairs got no majority. Exclude them from the agreement figure and
   report that rate separately. A high non-convergence rate is evidence about
   the judge's reliability in its own right.
4. **Report case-level agreement.** Where the judge did resolve a pair, it
   matched the independent metric 78% of the time on comprehensiveness and
   about 70% on diversity. The source calls this "moderately strong", not
   validation.

**Agreeing on direction is weak evidence.** Two instruments can both prefer
pipeline A on average while disagreeing on a large share of individual
comparisons. A judge that agrees 70% of the time per case and one that agrees
95% of the time can reach the same aggregate conclusion. Only the per-case
rate tells you how far to trust the judge when it runs alone, for example as
the sole grader in a [regression suite](capability-vs-regression-evals.md).

**Don't let an unstable analysis parameter decide the result.** The source
tried a threshold for when two claim counts count as tied, then dropped it
because the agreement figures moved with the threshold. If a cutoff or
binning rule can change the conclusion, it is doing unacknowledged work.
Disclose that sensitivity rather than quietly picking the setting that looks
best.

When no clean automatic metric exists, human review can play the same role.
In STORM's evaluation, rubric scores from an evaluator model improved on
several article qualities. Expert editors found that only organisation
improved significantly, and found no gain in verifiability. That gap is the
signal to report the model judge as one instrument, not as the construct
itself. For pooled-human validation see
[grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md),
and for the bias that comes from a judge sharing a model family with the
generator see [model-family independence](model-family-independence-rule.md).
