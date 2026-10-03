---
type: concept
title: Harness as a Performance Lever
description: >
  Holding the base model fixed, harness design alone materially shifts task
  completion — and the best harness is model-specific, so it must be
  re-adapted every time the base model changes.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §1–2"
  - title: "Finding the Right Fit: Model–Harness Interactions"
    resource: "Li, Zhou, Teng et al. (NTU), arXiv 2610.00917, 1 Oct 2026 preprint, §4.1–4.3 — https://arxiv.org/html/2610.00917"
  - title: "Stop Comparing LLM Agents Without Disclosing the Harness"
    resource: "Zhang, Wang, Ge et al., arXiv 2605.23950, 7 May 2026 preprint, Tables 1–2 — https://arxiv.org/html/2605.23950v1"
  - title: "Holistic Agent Leaderboard (HAL)"
    resource: "Kapoor, Stroebl et al. (Princeton), arXiv 2510.11977, Oct 2025 — https://arxiv.org/html/2510.11977v1"
  - title: "Improving Deep Agents with harness engineering"
    resource: "Viv Trivedy, LangChain, 17 Feb 2026 — https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
  - title: "Is harness engineering real?"
    resource: "Latent Space (AINews), 5 Mar 2026 — https://www.latent.space/p/ainews-is-harness-engineering-real"
---

A harness — the system prompt shaping work style, the tools exposing file
system and shell, the middleware controlling context and recovery — is not
inert scaffolding around a fixed model. On long-horizon coding benchmarks,
swapping harnesses while holding the base model exactly fixed produces large
swings in task completion, which makes harness engineering "a first-class
lever, not an afterthought" for agent performance rather than a secondary
concern once the model is chosen. That follows from treating the
[agent as model plus harness](agent-equals-model-plus-harness.md): the harness
is a separate artefact with its own effect on outcomes.

Other comparisons put numbers on the swing, and suggest harness choice can even
**reverse model rankings**. A 2026 model–harness interaction preprint
(arXiv 2610.00917) ran 5 models across 6 harnesses (66 pairs, 6,204
trajectories). On one benchmark, Claude led GPT by 7.94 points under OpenHands
but trailed it by 30.16 under PI, a swing of about 38 percentage points. Four
of five models had a different best harness on different task collections,
OpenAI's Codex harness never gave GPT its top score, and cost decoupled from
score (GPT scored 60.32% under PI at $4.66 per task against 52.38% under another
harness at $19.94). A harness-disclosure position paper (arXiv 2605.23950,
also a preprint) compiles further swings, such as Sonnet 4.5 ranging from 68%
to 34% across scaffolds, and reports a controlled 3×3 factorial in which
harness-induced variance was 7.80 times model-induced variance. The Holistic
Agent Leaderboard (HAL) found task-specific scaffolds beating generalist ones in
most runs while generalist scaffolds were 25–80% cheaper, and LangChain reports
that harness-only changes moved one agent from 52.8% to 66.5% on
Terminal-Bench 2.0. The caveats are real: both headline papers are preprints,
some swings in 2605.23950 are compiled from other sources, and Latent Space
reports that METR and Scale found harness differences within noise, so the size
of the effect is contested (see [thin vs thick harness](thin-vs-thick-harness-debate.md)
and [infrastructure failure as eval failure](evaluation/infra-failure-as-eval-failure.md)).
The practical upshot is to choose model and harness together by testing on your
own tasks rather than assuming a vendor-native pairing is best, and to treat
leaderboard results as comparable only when the harness is disclosed
([harness card disclosure](evaluation/harness-card-disclosure.md)).

The complication: the **optimal harness is model-specific**. A harness tuned
for one base model can underperform on another and needs re-adaptation as the
underlying model changes, because each component encodes an assumption about
what the model cannot do ([harness assumptions go stale](harness-assumptions-go-stale.md)) — the same tool descriptions, prompt phrasing, and
recovery hints that compensate for one model's blind spots may be redundant or
actively counterproductive for a model that doesn't share them. Manual
adaptation (a developer inspecting trajectories, spotting failure patterns,
hand-crafting fixes) cannot keep pace with how often base models ship,
"creating a widening gap between model capability and the harness needed to
realize it" — the harness a team shipped six months ago is quietly leaving
capability on the table against whatever model is deployed today.

The claim that makes this tractable to automate: harness evolution is
"bottlenecked by observability, not by agent capability" — once an editing
agent has structured evidence over a clear action space, it reliably converges
on better designs without needing new capability itself. That evidence comes
from three matched pieces: which components are editable at all
([component observability](optimization/component-observability.md)), what the
trajectories actually show
([Agent Debugger trajectory distillation](optimization/agent-debugger-trajectory-distillation.md)),
and whether a given edit's predicted effect held up
([evidence-driven change manifest](optimization/evidence-driven-change-manifest.md)).
Together these support an automated
[harness evolution outer loop](optimization/harness-evolution-outer-loop.md) that
re-adapts the harness at the pace base models actually ship, instead of at the
pace a team can hand-inspect trajectories.

A harness evolved this way is not automatically overfit to the benchmark it
was tuned on — see
[harness evolution transfer and generalization](optimization/harness-evolution-transfer-generalization.md)
for what does and doesn't carry over to unseen tasks and models.
