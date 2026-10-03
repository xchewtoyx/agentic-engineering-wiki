---
type: concept
title: Raw Traces over Summaries
description: >
  Optimisers and debuggers that read raw execution traces outperform those
  given only scores or LLM summaries, because summaries compress away the
  diagnostic detail needed to find causes.
evidence: weak
sources:
  - title: "Meta-Harness"
    resource: "Lee, Nair, Zhang, Lee, Khattab, Finn, arXiv 2603.28052, 30 Mar 2026, Table 3 (preprint) — https://arxiv.org/html/2603.28052v1"
---

Agent runs produce long traces, and the natural instinct is to summarise them
before handing them to whoever, or whatever, has to work out what went wrong.
Summaries are cheaper to read and fit in a context window. The question is
what they throw away.

The Meta-Harness preprint from Stanford and collaborators tested this
directly for an automated harness optimiser:

| Proposer input | Median score |
|---|---|
| Scores only | 34.6% |
| Scores plus LLM summaries of runs | 34.9% |
| Full raw execution traces | 50.0% |

The authors argue that summaries compress away exactly the diagnostic detail
an optimiser needs to find causes.

The evidence is weak. It is a single preprint, and the paper discloses that
one of its experiments used the same benchmark for search and evaluation, with
manual leakage audits, which is a contamination caveat on some headline
figures. The direction of the result is plausible and matches
[context collapse](context-collapse.md), where a summary that replaces its
source loses what made it useful, but the size should not be relied on.

There is a tension with context-management advice. Working agents need
compaction to stay effective, yet debuggers do better without it. Resolve it
by separating the two: keep raw logs in a
[session log outside the context window](../knowledge/session-log-outside-context-window.md)
for whoever diagnoses, and compact only the working agent's own context, as
[safeguarded compaction](../context/safeguarded-compaction.md) does.
[Trajectory distillation](agent-debugger-trajectory-distillation.md) is
compatible with this result because it keeps the raw traces reachable behind
its reports rather than replacing them. The same logic supports
[localising the root-cause step](../evaluation/root-cause-step-localisation.md),
which needs the raw sequence of steps.
