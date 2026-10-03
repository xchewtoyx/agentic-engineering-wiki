---
type: concept
title: Eval Observation Anti-Leakage
description: >
  Censor environment observations that overlap the question or reference answer
  so agents cannot solve the eval by copying leaked gold text.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), Appendix A"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 1–15 (§5)"
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Open-book agent evals are invalid if the environment surfaces the answer.
WebGPT **censors** fetched pages with high *n*-gram overlap (e.g. 10-gram)
against the question — and against a reference answer when one is provided —
so the agent cannot cheat by retrieving near-duplicate text. Domain filters
(e.g. dropping answer-forum mirrors) are a coarser sibling of the same idea.

Build this into the ACI used for
[offline prompt evaluation](offline-prompt-evaluation.md) and harness
regression, not only into training data filters. This guards against leakage
*within* a single observation; see
[eval environment isolation](eval-environment-isolation.md) for the sibling
problem of state leaking *across* trials that are supposed to be independent. Leakage is an
[agent-computer interface](../harness/agent-computer-interface.md) bug: the observation
surface must match the intended task difficulty. Combine with
[lm-oriented web observations](../harness/lm-oriented-web-observations.md) so cleaning
and anti-leakage run in the same fetch pipeline.

**Temporal holdout as a training-data leakage check.** When eval tasks are
mined from a live corpus a model may have been pretrained on (GitHub issues,
public Q&A), a within-context observation filter doesn't rule out the model
simply having memorized the answer from pretraining rather than solving the
task from the given context. Partition instances by date around the model's
training cutoff and compare resolve rate before vs. after: little difference
is evidence against memorization-driven "cheating" (the model isn't scoring
better on pre-cutoff instances it could have seen verbatim); a sharp drop
after the cutoff is a genuine capability difference, not necessarily leakage.
This is a coarser, corpus-level complement to the per-observation n-gram
censor above — use it for benchmark *construction* (is this eval measuring
what it claims to) even when no single observation can be shown to leak the
answer directly.

For continuously edited public corpora, construct a moving temporal benchmark
from artifacts created or heavily revised after the training cutoff, and
refresh it as newer models shift that cutoff. This reduces rather than
eliminates memorization risk: post-cutoff facts may still enter later training
sets, and a mature reference artifact may encode far more editing effort than
the evaluated one-pass workflow. How much protection you get depends on how
accurately the model's cutoff is known and on what its training data actually
contained. State the temporal boundary, meaning the model and the cutoff it
was checked against, as part of any claim made from the eval. Treat it as a
scoped control rather than proof that the task measures from-scratch
capability, and rebuild the boundary whenever the evaluated model changes.
