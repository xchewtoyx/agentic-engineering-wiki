---
type: concept
title: LLM Inference Latency Metrics (TTFT, TPOT)
description: >
  LLM latency splits into time to first token (driven by prompt length) and
  time per output token (paid on every generated token), so prompt and harness
  choices move the two halves independently.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 9"
---

Because of [autoregressive generation](autoregressive-generation.md), one
model call has two phases with different cost profiles: **prefill** reads the
whole prompt in parallel, and **decode** emits output one token at a time. Its
latency is therefore not one number:

- **TTFT (time to first token)** — time from request to the first output
  token; essentially prefill time, so it grows with input length.
- **TPOT (time per output token)** — average time for each subsequent token.
  Per-gap variants are called **TBT** (time between tokens) or **ITL**
  (inter-token latency) when you need the distribution rather than the mean.

**Total latency ≈ TTFT + TPOT × output tokens.** For harness design this says
where each lever acts:

- Stuffing more context into the prompt raises TTFT — modestly per token,
  since reading is parallel — while every extra *generated* token adds a full
  TPOT. Verbose output formats, long [chain-of-thought](reasoning/chain-of-thought-prompting.md),
  and chatty tool-call arguments usually cost more wall-clock time than the
  same number of extra prompt tokens. Cap output with concise instructions
  and [stop sequences](stop-sequences.md).
- An agent loop pays TTFT + decode on every turn, so latency scales with the
  number of model calls; [ReAct-style loops](orchestration/react-loop.md) and
  [self-consistency](reasoning/self-consistency-decoding.md) multiply it, and
  a long, growing transcript makes each turn's TTFT larger than the last.
  Reusing a stable prompt prefix (system prompt and tool definitions first,
  per [static vs dynamic prompt content](context/static-vs-dynamic-prompt-content.md))
  is what lets provider prefix caching cut prefill work.
- Equal totals can feel very different: an instant first token followed by a
  slow stream versus a delayed but fast stream. In streaming UIs TPOT only
  needs to beat human reading speed (~120 ms/token for a fast reader); beyond
  that, TTFT dominates perceived responsiveness. Which split is preferable is
  an empirical UX question tied to the request's
  [latency tier](context/context-gathering-latency-tiers.md).

**Time to publish vs. model first token.** In agentic or chain-of-thought
flows the model emits hidden tokens — plans, reasoning, tool-call scaffolding,
whole intermediate calls — before anything the user sees. The user-visible
metric, sometimes named **time to publish**, can be far larger than the
model's TTFT. Design budgets and evaluation around time to publish, and keep
intermediate steps logged so the step that owns a delay is identifiable.

When stating latency requirements for
[model selection](llm-model-selection-criteria.md), use percentiles (e.g. TTFT
p90) rather than averages: a few multi-second outliers, often from unusually
long prompts, drag a mean far from typical experience. Latency and
[token cost](llm-token-and-cost-metrics.md) share a driver — length — so the
same prompt trim usually improves both.
