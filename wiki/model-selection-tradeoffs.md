---
type: concept
title: Model Selection Tradeoffs
description: >
  Choosing a model for a task balances output quality against cost, latency
  tolerance, and whether the base model's knowledge or behavior needs changing.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
  - title: "LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities"
    resource: "Tang & Runkler (2024), sec. 4"
---

Using an LLM is not just "send prompt, get completion" — which model to send
it to is its own decision. A fuller ranked list of considerations, in
descending order of importance for most scenarios:

1. **Intelligence** — how close the output gets to an expert human's answer;
   matters most for tasks needing complex reasoning or high accuracy. Treat
   published benchmark comparisons with caution: a headline claim that one
   model beats another can rest on mismatched prompting conditions rather
   than a genuine capability gap — one widely cited launch claimed a win on a
   standard benchmark using 32-shot chain-of-thought prompting for the new
   model against a 5-shot baseline for the competitor, and the ranking
   reversed once both were evaluated under the same 5-shot setup. Re-run or
   at least re-read the fine print of any benchmark comparison that's
   driving a real model-selection decision, rather than taking a headline
   number at face value.
2. **Speed** — how long the user waits; matters most for applications that
   interact directly with a user, per
   [context gathering latency tiers](context/context-gathering-latency-tiers.md).
   Example: an early code-completion product deliberately chose a smaller,
   fast-enough model over a larger, better one, because users would rarely
   wait for a slower completion even if it were higher quality — inline
   suggestions need to appear before the user has moved on.
3. **Cost** — inference cost, whether paid to a provider or run on owned
   hardware; matters most for high-frequency-request applications.
4. **Ease of use** — how much of provisioning, deployment, crash recovery,
   routing, and caching is handled for you versus left to build.
5. **Functionality** — instruct/chat/tool-use support, logprob availability,
   image processing, and similar capability gates a task may need.
6. **Special requirements** — narrower constraints that can sharply cut the
   field: a noncommercial or open-source preference, specific training data,
   update cadence, data residency, or on/off-premises logging requirements.

These trade off against each other, not just against a fixed budget: a
high-volume simple-request app is fine with a cheap-but-not-particularly-smart
small model; a low-volume solo project can afford to splurge on a premium
tier since cost barely matters at low scale; but wanting both very cheap and
very smart for a high volume of genuinely hard requests isn't achievable —
those two properties sit at opposite ends of the spectrum, not somewhere a
better provider choice can reconcile. Operationalize the tradeoff as
Pareto filtering under
[LLM model selection criteria](llm-model-selection-criteria.md): hard
latency/cost thresholds first, then quality among survivors. Don't bake a
specific model choice too firmly into application code; a unified access
layer such as [model gateway](model-gateway.md) eases later revision as the
landscape shifts. See
[provider selection guidance](provider-selection-guidance.md) for how these
criteria narrow down to an actual provider and model size, and
[fine-tuning decision](fine-tuning-decision.md) for when adapting a chosen
model further is worth it.

This is the task-level version of the same tradeoff
[model tiering](model-router.md) makes at the routing level: match the
model's strength to what the task actually needs rather than defaulting every
call to the most capable — and most expensive — option available.

In industrial software engineering agents, model selection divides across three distinct archetypes:
- **Proprietary frontier models** offer upper-bound reasoning and instruction fidelity, but incur recurring per-token OPEX and require sending proprietary source code across third-party API endpoints.
- **Open-source local models** (e.g., LLaMA, DeepSeek-V3) guarantee on-premise data governance, eliminate source code egress, and allow custom fine-tuning to proprietary coding conventions, traded off against upfront infrastructure costs.
- **Reasoning-optimized models** (e.g., DeepSeek-R1) leverage extended test-time compute and chain-of-thought exploration, making them well-suited for complex architectural refactoring, root-cause localization, and deep debugging.
