---
type: concept
title: Context Rot
description: >
  LLM performance degrades non-uniformly as input length grows, even on simple
  tasks, with focused prompts of about 300 tokens strongly outperforming full
  prompts of about 113k tokens on LongMemEval.
evidence: weak
sources:
  - title: "Context Rot"
    resource: "Hong, Troynikov, Huber, Chroma technical report, 14 Jul 2025 (not peer reviewed) — https://www.trychroma.com/research/context-rot"
  - title: "How Long Contexts Fail"
    resource: "Drew Breunig, 22 Jun 2025 — https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html"
---

Large context windows invite a simple strategy: put everything in and let the
model sort it out. If models used long inputs as well as short ones, that would
work. They do not, and the gap shows up well before the window is full.

Chroma's "Context Rot" technical report tested 18 large language models (LLMs)
and found that performance varies significantly with input length even on
simple tasks. Distractors hurt, and they hurt non-uniformly. Counter-intuitively,
shuffled haystacks produced better results than coherent ones. On the
LongMemEval benchmark, focused prompts of about 300 tokens strongly outperformed
full prompts of about 113,000 tokens containing the same answer. The report is a
vendor technical report rather than a peer-reviewed study, which is why the
evidence is rated weak, although the direction agrees with practitioner
observations such as Drew Breunig's report that agents begin repeating history
past about 100,000 tokens.

Context rot is about **length**; [lost in the middle](lost-in-the-middle.md) is
about **position**. The peer-reviewed U-curve shows that where a fact sits
matters; context rot adds that total length and distractor load degrade quality
even when position is controlled, so moving key facts to the edges is necessary
but not sufficient. The same pressure is why
[long-context binding constraints](long-context-binding-constraints.md) shift
the bottleneck from window size to retrieval policy and verification, and why
practitioners talk about a [smart zone](smart-zone.md) to stay inside.

The practical reading is that context is a budget to spend, not a container to
fill. Most context-engineering practice responds to it: the four moves in
[write, select, compress, isolate](context-write-select-compress-isolate.md),
loading only what is needed through
[progressive disclosure](../instructions/progressive-disclosure.md),
[structural context over raw dumps](structural-context-over-raw-dumps.md), and
the choice between summarising and starting fresh in
[compaction vs context reset](compaction-vs-context-reset.md). The specific ways
long contexts go wrong are catalogued in
[four ways long contexts fail](four-context-failure-modes.md).

The effect bites hardest when an agent diagnoses from large raw material:
container logs, service logs and session transcripts. Dumping them whole into
context is likely to make diagnosis worse. Filter by time window, component and
level before the model sees anything, and hand it a focused excerpt with a
pointer to the full record, which is kept outside the window as a
[session log outside the context window](../knowledge/session-log-outside-context-window.md).
