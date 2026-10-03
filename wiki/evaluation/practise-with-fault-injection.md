---
type: concept
title: Practise with Fault Injection
description: >
  Exercise and evaluate operations agents in environments that inject faults
  under synthetic load, because response paths decay unless practised and
  each injected fault yields a labelled failure to measure against.
evidence: moderate
sources:
  - title: "AIOpsLab"
    resource: "Chen et al., MLSys 2025 (arXiv 2501.06706) — https://proceedings.mlsys.org/paper_files/paper/2025/hash/d1f9e4a9f109b6e8b75ed362736f22ec-Abstract-Conference.html"
  - title: "The Practice of Cloud System Administration"
    resource: "Limoncelli, Chalup and Hogan, Preface, ch. 2, 6 (confidence decay in unpractised safeguards, via a secondary summary)"
  - title: "When Agentic Executions Fail: AgentChaosBench"
    resource: "Zhang et al., arXiv 2608.14680, August 2026 (preprint) — https://arxiv.org/html/2608.14680"
---

An agent that only acts during real incidents is tested only during real
incidents. Its runbooks, restart caps, kill switch and escalation path sit
unused between failures while images, configurations and models change
underneath them. Operations practice describes this for any emergency-only
safeguard: confidence erodes even though its code has not changed, and the
breakage is discovered during the incident it was meant to handle. The remedy
is deliberate exercise through fire drills or game days, plus treating an
unusually high trigger rate as a sign of a masked deeper problem.

Research supplies a template for exercising agents specifically. AIOpsLab
(MLSys 2025) deploys microservice environments, injects faults, generates
workload, exports telemetry and exposes an agent-to-cloud interface, so that
detection, localisation, root-cause and mitigation agents can be evaluated
end to end. AgentChaosBench, a 2026 preprint, injects ten fault types into
agent systems, grouped in the
[agent runtime fault taxonomy](agent-runtime-fault-taxonomy.md). The evidence
is moderate: the frameworks are real, but no source reports the measured
benefit of drills for a deployed agent.

The practice is a scheduled environment: a copy of each system in which known
faults are injected (killed containers, exhausted quotas, hung tools,
corrupted configuration, full disks, broken channels) under synthetic load.
Each run produces a labelled failure, which serves three purposes:

- It tests whether the agent detects, stabilises and escalates as designed,
  including whether its
  [restart caps escalate](../orchestration/supervision-tree-escalation.md).
- It measures diagnosis accuracy for each fault class, which decides where
  autonomous action is justified, given that
  [LLM SRE agents still have low success](llm-sre-agents-low-success.md).
- It yields fault-free and faulty reference traces for
  [baseline comparison](known-good-baseline-comparison.md).

Run each drill from a clean starting state, as with any
[isolated eval environment](eval-environment-isolation.md), so one drill's
leftovers do not mask the next.
