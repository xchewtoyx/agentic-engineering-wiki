---
type: concept
title: Error Analysis First
description: >
  Read and code real traces into a failure taxonomy before automating evals,
  and build evaluators only for failures actually observed, cheapest first.
evidence: moderate
sources:
  - title: "Evals FAQ"
    resource: "Hamel Husain and Shreya Shankar — https://hamel.dev/blog/posts/evals-faq/"
  - title: "Review of Anthropic's auto-eval plugin"
    resource: "Hamel Husain — https://hamel.dev/blog/posts/claude-auto-evals/"
---

It is tempting to start evaluating an agent by choosing metrics and wiring up
an LLM judge. The risk is measuring things that do not fail while missing the
failures that actually happen, because nobody has looked at what the agent
did.

Hamel Husain and Shreya Shankar put error analysis at the centre of
evaluation. Their procedure:

1. **Open-code** thirty or more real traces with free-form notes on what went
   wrong.
2. **Axial-code** those notes into a failure taxonomy.
3. Continue until new traces stop producing new categories, which they put at
   about a hundred traces.
4. Build evaluators only for failures that have been observed, in cost order:
   assertions first, then reference checks, then LLM judges.

Judgements should be binary pass or fail rather than Likert scales, a single
domain expert should set the standard, and generic metrics and outsourced
labelling should be avoided. Teams should expect 60–80% of evaluation effort
to go on this analysis. Husain's review of an automated eval tool makes the
same point negatively: a tool that does not put looking at data at the centre
of the workflow is not worth using.

This is practitioner guidance from two well-known evaluators, consistent with
lab advice elsewhere but not a controlled study.

Error analysis is the input step of
[eval-driven development](eval-driven-development.md): its categories decide
which cases enter the [example suite](example-suite.md). It depends on keeping
[raw traces rather than summaries](../optimization/raw-traces-over-summaries.md),
and it is where reading the
[transcript as well as the outcome](agent-eval-outcome-vs-transcript.md) earns
its keep. The resulting taxonomy is what
[failure-signature clustering](../optimization/failure-signature-clustering.md)
groups by. Published taxonomies such as
[MAST](mast-multi-agent-failure-taxonomy.md) or the
[agent runtime fault taxonomy](agent-runtime-fault-taxonomy.md) are useful
seeds but no substitute for codes drawn from your own traces.
