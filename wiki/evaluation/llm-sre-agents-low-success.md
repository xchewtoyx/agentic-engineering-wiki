---
type: concept
title: LLM SRE Agents Still Have Low Success
description: >
  Current agents resolve only a small fraction of realistic production
  incidents, so an operations agent should propose evidenced diagnoses and act
  alone only on fault classes it diagnoses reliably.
evidence: moderate
sources:
  - title: "ITBench"
    resource: "Jha, Puri et al., arXiv 2502.05352, February 2025 — https://arxiv.org/abs/2502.05352"
  - title: "OpenRCA"
    resource: "Xu, Zhang, Zhong, He et al., ICLR 2025 — https://mlanthology.org/iclr/2025/xu2025iclr-openrca/"
  - title: "When Agentic Executions Fail: AgentChaosBench"
    resource: "Zhang et al., arXiv 2608.14680, August 2026 (preprint), Tables 3–5 — https://arxiv.org/html/2608.14680"
  - title: "AWS DevOps Agent GA"
    resource: "InfoQ, April 2026 (reporting the vendor's MTTR claim) — https://www.infoq.com/news/2026/04/aws-devops-agent-ga/"
---

It is tempting to assume that an LLM which writes good code will also
diagnose production incidents well. Benchmarks of site reliability
engineering (SRE) and AIOps agents say otherwise, and the gap matters for how
much an operations agent should be allowed to do alone.

| Benchmark | What it measures | Best reported result |
|---|---|---|
| ITBench | Resolving SRE scenarios | 13.8% |
| OpenRCA (ICLR 2025) | Root-cause identification over 335 failure cases, 68 GB+ of telemetry | 11.34% |
| AgentChaosBench (2026 preprint) | Diagnosing faults inside agent systems from one trace | 24.8% fault type, 22% type and location |

The AgentChaosBench result also splits sharply by class: tool failures were
always diagnosed, guardrail bypass once in 25 attempts.

The position is contested by vendor claims. AWS's preview of its DevOps Agent
claimed "up to 75% lower MTTR" (mean time to resolution), reported by InfoQ as
a vendor figure, and other products market investigation speed. These claims
and the benchmarks measure different things in different settings, and no
primary data was found on the accuracy of coding agents used as on-call
responders. The benchmark figures are the more conservative basis for design.

The implication is that an operations agent's default output should be a
diagnosis with the evidence attached, for a human, another agent or a
deterministic verifier to confirm, which is the
[diagnose-by-default posture](../harness/diagnose-by-default-act-by-exception.md).
Autonomous action should be limited to fault classes where diagnosis is
reliable, such as tool unavailability, timeouts and resource kills. That sets
the width of the [prepared envelope](../harness/envelope-bounded-autonomy.md).
The [fault taxonomy](agent-runtime-fault-taxonomy.md) suggests where to draw
the line, and [practising with fault injection](practise-with-fault-injection.md)
measures your own per-class accuracy rather than relying on published
averages.
