---
type: concept
title: Harness Drift Awareness
description: >
  Prompt templates, user behaviour, and silent provider model swaps all change
  agent behaviour without code diffs — version and detect them as first-class
  maintenance risks.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

Agent systems drift even when application code is unchanged:

- **System prompt / template changes** — intentional updates or silent typos;
  catch with diffs in the [prompt catalog](../prompting/prompt-catalog.md).
- **User behaviour adaptation** — users learn phrasing that changes length and
  tool use over time.
- **Underlying model swaps** — same API name, different weights; quality can
  move without a deploy. Providers don't always disclose the swap. Chen et al.
  (2023) measured notable benchmark differences between the March and June
  2023 versions of GPT-4 and GPT-3.5, which had no visible interface change.
  Voiceflow reported a 10% performance drop when its provider moved
  `gpt-3.5-turbo-0301` traffic to `gpt-3.5-turbo-1106`. A prompt-template
  edit can at least be diffed. A vendor-side swap leaves nothing in your own
  change history to bisect against, so an unexplained shift in eval or
  production scores has to be treated as a drift hypothesis even when nothing
  you control changed.

Maintenance practice: version prompts and harness config with the
[prompt catalog](../prompting/prompt-catalog.md), pin models to a specific version rather than a floating alias where the
provider allows it (you lose automatic improvements but remove the silent-swap
failure mode), and treat provider updates as deliberate upgrades. For computer-use agents, also version
the [configurable ACI harness](../harness/configurable-aci-harness.md) YAML (templates,
command files, parsers, history processors) — those are interface changes that
shift behaviour as much as model swaps. Runtime detection and metric design for
drift belong to observability, though the
[eval/monitoring feedback loop](eval-monitoring-feedback-loop.md) is what
turns a detected shift back into an eval case; the design obligation here is to make prompts,
models, and tool inventories identifiable artifacts you can bisect when
behaviour shifts. Score those shifts at
[episode scale, not request-APM latency](episode-scale-evaluation-vs-request-apm.md).
