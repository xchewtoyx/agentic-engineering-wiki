---
type: concept
title: LLM Token and Cost Metrics
description: >
  Input tokens, output tokens, request rate, and cost per request are the
  units in which an agent design's cost and rate-limit exposure are paid, so
  they belong in harness and prompt decisions, not just on the invoice.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 9"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
---

For a hosted model, cost is almost entirely a function of
[token count](tokenization-fundamentals.md), billed separately for **input**
and **output** tokens. That makes a handful of quantities the real cost model
of an agent design:

- **Input vs. output tokens, counted separately.** Prefill (reading the
  prompt) and decode (generating) are computationally distinct, priced
  differently, and scale with different design choices: input grows with
  context stuffing, tool definitions, and transcript length; output grows
  with verbosity, reasoning traces, and retries. An agent loop re-sends its
  growing context on every turn, so input tokens per *task* grow roughly
  quadratically with turn count even when each turn adds little — the effect
  behind [multi-agent token inflation](orchestration/multi-agent-token-inflation.md)
  and the reason context trimming and compression pay off.
- **Cost per request (or per task), not tokens per second.** Tokenizers differ
  between models, so the same text is a different number of tokens on each;
  per-token prices and throughput figures compare only approximately across
  models. Compare candidate models and harness variants on cost per completed
  request or task, and when accuracy also differs, fold the two together with
  [successes per million tokens](evaluation/successes-per-million-tokens.md).
- **Request rate against provider limits.** Model calls take seconds, so
  requests per minute (RPM) — alongside tokens per minute — is the readable
  concurrency unit. Provider rate limits are a hard design constraint for
  fan-out patterns (parallel sub-agents, [self-consistency
  sampling](reasoning/self-consistency-decoding.md), batch evals): exceeding
  them interrupts service, so plan concurrency against them up front and give
  the [model gateway](model-gateway.md) a fallback policy rather than
  discovering the limit through failed calls.

**Length is a dual proxy.** A longer context or longer generation raises both
cost and [latency](llm-inference-latency-metrics.md), so the same length
measurement answers either question — and the same trim (tighter retrieval,
shorter output format, fewer turns) usually buys both. Raw throughput can rise
while the experience degrades, so judge any cost saving against the latency
budget, not on tokens per second alone.

**Self-hosted cost is throughput-driven.** When you pay for compute instead
of tokens, cost per token = hourly compute cost ÷ sustained tokens per hour:
at $2/h and 100 output tokens/s, roughly $5.56 per 1M output tokens; total
cost per request is prefill plus decode cost. Smaller models, better
hardware, and consistent-length workloads raise achievable throughput — see
the API vs. self-hosted cost shape in
[LLM model selection criteria](llm-model-selection-criteria.md).
