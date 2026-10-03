---
type: concept
title: Unverifiable Loops Rot
description: >
  Unattended agent loops degrade a codebase when success cannot be verified,
  because passing tests does not prove sound architecture; humans belong at
  leverage points, though high-throughput teams argue for minimal gates.
evidence: weak
sources:
  - title: "Dark-factory post-mortem (news write-up of a Pragmatic Engineer podcast appearance by Dex Horthy)"
    resource: "BigGo Finance, reporting a 15 Jul 2026 podcast (secondary) — https://finance.biggo.com/news/15099f5634f5ab9a"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "OpenAI (Ryan Lopopolo), Feb 2026 — https://openai.com/index/harness-engineering/"
---

How much human oversight an agent loop needs is a live disagreement, and both sides have run the experiment.

On one side is Dex Horthy of HumanLayer. According to a news write-up of his podcast appearance, he ran a fully unattended, "lights-off" agent software factory from July to November 2025. The codebase degraded within about three months, and one bug took weeks of manual debugging because no human had read the layers involved, the failure described as [cognitive debt](cognitive-debt-in-agent-synthesized-code.md). His diagnosis is that loops are unsafe when the task is not verifiable, because passing tests does not show the architecture is sound. He now argues for front-loading human planning at "leverage points" such as plans and specs, with real-time steering.

On the other side is OpenAI's harness-engineering team, which built about a million lines of code with no hand-written code, often in single runs of six hours or more. It keeps blocking merge gates minimal and re-runs flaky tests rather than blocking on them, on the grounds that corrections are cheap and waiting is expensive. The post itself says this is right only at high agent throughput, and the team escalates to a human only when judgement is required. It also leans on scheduled clean-up agents, described in [entropy garbage collection](entropy-garbage-collection-agents.md), to stop drift accumulating between human looks.

The evidence is weak: Horthy's account arrives second-hand through a news article about a podcast, and OpenAI's is a single team's report. The two reconcile if the right amount of oversight depends on how verifiable the task is.

That reconciliation gives a working rule. Where the outcome is only partly verifiable, as with infrastructure changes where a health check can pass while the system is still wrong (see [owner validation decides success](../evaluation/owner-validation-decides-success.md)), or where the blast radius is large, invest in strong sensors and [back-pressure](../harness/back-pressure.md), [verification before done](../harness/verify-before-done.md), and humans placed at the edge of an explicit [autonomy envelope](../harness/envelope-bounded-autonomy.md), rather than either a fully unattended loop or approval of every action. Where the task is checkable end to end, minimal gates are defensible. The broader argument about harness thickness is in [thin vs thick harness](../thin-vs-thick-harness-debate.md).
